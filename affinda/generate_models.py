#!/usr/bin/env python3

from __future__ import annotations

import ast
import os
import re
import sys
from pathlib import Path

import click

from affinda import AffindaAPI, TokenCredential


def _get_pydantic_models(
    api_key: str,
    base_url: str,
    doc_type_id: str,
    model_name: str | None = None,
) -> str:
    creds = TokenCredential(api_key)
    client = AffindaAPI(creds, base_url=base_url)
    response = client.pydantic_models_from_document_type(doc_type_id, model_name=model_name)
    code = response.code
    return code


def _camel_to_snake(camel: str) -> str:
    if camel.isalpha() and camel.isupper():
        # Boundary case - handle text that is entirely uppercase like AUD, VAT
        return camel.lower()

    # Wrap abbreviations around underscores and make lowercase, e.g. myVATAmount -> my_vat_amount
    text = re.sub(r"([A-Z]+)(?![a-z])", lambda m: f"_{m.group(1).lower()}_", camel)
    text = text.removeprefix("_").removesuffix("_")

    # Wrap digits around underscores, e.g. amount123 -> amount_123
    text = re.sub(r"(\d+)", lambda m: f"_{m.group(1)}_", text)
    text = text.removeprefix("_").removesuffix("_")

    # Add a underscore in front of every uppercase letter except beginning of line
    text = re.sub(r"(?<!^)([A-Z])", r"_\1", text)

    # Collapse multiple underscores into one
    text = re.sub(r"(_+)", "_", text)

    # Make lowercase
    text = text.lower()

    return text


def _is_basemodel(base: ast.expr) -> bool:
    """Return True if the AST *base* node represents ``BaseModel``."""
    return (isinstance(base, ast.Name) and base.id == "BaseModel") or (
        isinstance(base, ast.Attribute) and base.attr == "BaseModel"
    )


def _extract_pydantic_class_names(code: str) -> list[str]:
    """Return ordered names of top-level classes inheriting from BaseModel.

    Falls back to *all* top-level classes when none inherit from BaseModel.
    """
    tree = ast.parse(code)
    pydantic_classes: list[str] = []
    all_classes: list[str] = []

    for node in tree.body:  # keeps original order
        if not isinstance(node, ast.ClassDef):
            continue

        all_classes.append(node.name)
        if any(_is_basemodel(base) for base in node.bases):
            pydantic_classes.append(node.name)

    return pydantic_classes or all_classes


def _write_models(code: str, models_dir: Path) -> Path:
    """Write *code* to its own file within *models_dir*, overwriting if needed.

    Returns the path to the written file.
    """

    models_dir.mkdir(parents=True, exist_ok=True)

    class_names = _extract_pydantic_class_names(code)
    if not class_names:
        raise ValueError("No class definitions found in code.")

    file_stem = _camel_to_snake(class_names[-1])  # use last model name
    model_path = models_dir / f"{file_stem}.py"

    # Code must end with a single newline
    _code = code.rstrip("\n") + "\n"

    model_path_exists = model_path.exists()
    model_path.write_text(_code, encoding="utf-8")
    print(
        f"Overwrote existing model at {model_path}."
        if model_path_exists
        else f"Created model file {model_path}."
    )

    return model_path


def _get_document_type_ids(
    api_key: str,
    base_url: str,
    organization_id: str | None = None,
    workspace_id: str | None = None,
) -> list[str]:
    creds = TokenCredential(api_key)
    client = AffindaAPI(creds, base_url=base_url)

    kwargs = {}
    if organization_id:
        kwargs["organization"] = organization_id
    elif workspace_id:
        kwargs["workspace"] = workspace_id
    else:
        raise ValueError("Either organization_id or workspace_id must be provided.")

    response = client.get_document_types(**kwargs)
    doc_types_ids = [doc_type.identifier for doc_type in response]

    # Fallback for portal v2 users whose collections are not yet migrated to be compatible with v3
    if workspace_id and not doc_types_ids:
        collection_response = client.get_all_collections(workspace=workspace_id)
        doc_types_ids = [collection.identifier for collection in collection_response]

    return doc_types_ids


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "--base-url",
    "base_url",
    default="https://api.affinda.com",
    show_default=True,
    help="Affinda API base URL.",
)
@click.option(
    "--organization-id",
    "organization_id",
    help="Generate models for all document types in the organization.",
)
@click.option(
    "--workspace-id",
    "workspace_id",
    help="Generate models for all document types (collections) in the workspace.",
)
@click.option(
    "--document-type-id",
    "document_type_id",
    help="Generate models for a specific document type.",
)
@click.option(
    "--collection-id",
    "collection_id",
    help="Alias for --document-type-id.",
)
@click.option(
    "--model-name",
    "model_name",
    help="Specify model name to generate. Only valid when --document-type-id is provided.",
)
@click.option(
    "--output-dir",
    "output_dir",
    default="./affinda_models",
    show_default=True,
    type=click.Path(file_okay=False, dir_okay=True, writable=True, path_type=Path),
    help="Directory in which to output the generated models.",
)
def main(
    base_url: str | None,
    organization_id: str | None,
    workspace_id: str | None,
    document_type_id: str | None,
    collection_id: str | None,
    model_name: str | None,
    output_dir: Path,
) -> None:
    """Fetch Pydantic model(s) for the given Affinda document type(s).

    The generated models are written to *OUTPUT_DIR*.
    """
    document_type_id = document_type_id or collection_id

    # Validate inputs
    if bool(organization_id) + bool(workspace_id) + bool(document_type_id) != 1:
        click.echo(
            "Please provide exactly one of --organization-id, --workspace-id, or --document-type-id.",
            err=True,
        )
        sys.exit(1)

    if model_name and not document_type_id:
        click.echo(
            "--model-name can only be used when --document-type-id is provided.",
            err=True,
        )
        sys.exit(1)

    # Prompt for API key
    api_key = os.getenv("AFFINDA_API_KEY")
    if not api_key:
        api_key = click.prompt(
            "Enter your API key (required when AFFINDA_API_KEY is not set)",
            hide_input=True,
            type=click.STRING,
        )
        if not isinstance(api_key, str) or not api_key.strip():
            click.echo("API key is required.", err=True)
            sys.exit(1)
        api_key = api_key.strip()

    models_dir = Path(output_dir).expanduser().resolve()

    # Determine document type IDs to process
    if document_type_id:
        doc_type_ids = [document_type_id]
    else:
        doc_type_ids = _get_document_type_ids(
            api_key,
            base_url,
            organization_id=organization_id,
            workspace_id=workspace_id,
        )

    if not doc_type_ids:
        click.echo("No document types found to generate models for.", err=True)
        sys.exit(1)

    # Fetch and write models
    any_written = False

    for dt_id in doc_type_ids:
        code = _get_pydantic_models(api_key, base_url, dt_id, model_name=model_name)
        written_path = _write_models(code, models_dir)
        any_written = any_written or written_path is not None

    if any_written:
        click.echo("\nAll requested Pydantic models processed.")
