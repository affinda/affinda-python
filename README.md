# Python Client Library for Affinda Document Parser API

![affinda logo](https://api.affinda.com/static/documentation/affinda_logo_light.png)

[![pypi ver](https://img.shields.io/pypi/v/affinda)](https://pypi.org/project/affinda/)
[![pypi pyver](https://img.shields.io/pypi/pyversions/affinda)](https://pypi.org/affinda/)
[![pypi dlm](https://img.shields.io/pypi/dm/affinda)](https://pypi.org/project/affinda/)
[![license](https://img.shields.io/github/license/affinda/affinda-python)](https://choosealicense.com/licenses/mit/)

[![codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/affinda/affinda-python)

This is a python client for the Affinda document parsing API which wraps all available endpoints
and handles authentication and signing. You may also want to refer to the full
[API documentation](https://api.affinda.com/docs) for additional information.

## Installation

```shell
pip install affinda
```

## API Version Compatibility

The Affinda API is currently on `v3`, with breaking changes meant the release of new versions of the client library.
Please see below for which versions are compatible with which API version.

| Affinda API version | `affinda-python` versions |
| ------------------- | ------------------------- |
| v2                  | 0.1.0 - 3.x.x             |
| v3                  | \>= 4.x.x                 |

## Quickstart

If you don't have an API token, obtain one from [affinda.com](https://affinda.com/resume-parser/free-api-key/).

```python
from pathlib import Path
from pprint import pprint

from affinda import AffindaAPI, TokenCredential
from affinda.models import WorkspaceCreate, CollectionCreate

token = "REPLACE_API_TOKEN"
file_pth = Path("PATH_TO_DOCUMENT.pdf")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# First get the organisation, by default your first one will have free credits
my_organisation = client.get_all_organizations()[0]

# And within that organisation, create a workspace, for example for Recruitment:
workspace_body = WorkspaceCreate(
    organization=my_organisation.identifier,
    name="My Workspace",
)
recruitment_workspace = client.create_workspace(body=workspace_body)

# Finally, create a collection that will contain our uploaded documents, for example resumes, by selecting the
# appropriate extractor
collection_body = CollectionCreate(
    name="Resumes", workspace=recruitment_workspace.identifier, extractor="resume"
)
resume_collection = client.create_collection(collection_body)

# Now we can upload a resume for parsing
with open(file_pth, "rb") as f:
    resume = client.create_document(file=f, file_name=file_pth.name, collection=resume_collection.identifier)

pprint(resume.as_dict())
```

## Samples

Samples for all operations using the client can be [found here.](./docs/samples_python.md)

## API reference

-   [API operations can be found here](./docs/sync_operations.md)
-   [API models and objects](./docs/models.md)
-   [Exceptions](./docs/exceptions.md)
