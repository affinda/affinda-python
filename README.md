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

Before using the API, you need to create an account, setup a workspace, and obtain an API key. Follow the steps in our [documentation](https://docs.affinda.com/docs/getting-started-with-affinda).

```python
from pathlib import Path
from affinda import AffindaAPI, TokenCredential

API_KEY = "YOUR_API_KEY"                      # replace with your actual key
WORKSPACE_ID = "YOUR_WORKSPACE_IDENTIFIER"    # e.g. "vBAdDBer"
FILE_PATH = Path("resume.pdf")                # path to the résumé you want to parse

# Set up the client
credential = TokenCredential(token=API_KEY)
client = AffindaAPI(credential=credential)

# Upload the document and wait until processing finishes
with FILE_PATH.open("rb") as f:
    doc = client.create_document(
        file=f,
        workspace=WORKSPACE_ID,
    )

# Access parsed data
print(doc.data)
```

## Samples

Samples for all operations using the client can be [found here.](./docs/samples_python.md)

## API reference

-   [API operations can be found here](./docs/sync_operations.md)
-   [API models and objects](./docs/models.md)
-   [Exceptions](./docs/exceptions.md)
