from __future__ import annotations

import click

from .generate_models import main as _generate_models_command


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:
    """Affinda command-line utilities."""


cli.add_command(_generate_models_command, name="generate_models")


if __name__ == "__main__":  # pragma: no cover
    cli()
