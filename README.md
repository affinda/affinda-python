Affinda API - Python Client Library
===================================

![affinda logo](https://raw.githubusercontent.com/affinda/affinda-python/main/affinda_logo.png)

[![pypi ver](https://img.shields.io/pypi/v/affinda)](https://pypi.org/project/affinda/)
[![pypi pyver](https://img.shields.io/pypi/pyversions/affinda)](https://pypi.org/affinda/)
[![pypi dlm](https://img.shields.io/pypi/dm/affinda)](https://pypi.org/project/affinda/)
[![license](https://img.shields.io/github/license/affinda/affinda-python)](https://choosealicense.com/licenses/mit/)

[![codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/affinda/affinda-python)

- [Installation](#installation)
- [Quickstart](#quickstart)
- [API reference](#api-reference)
- [Parser](#parser)
- [Redactor](#redactor)
- [Reformatter](#reformatter)

Generated using [autorest](https://github.com/Azure/autorest)
and [autorest.python](https://github.com/Azure/autorest.python).

Installation
------------

```shell
pip install affinda
```

Or latest dev from github

```shell
git clone git@github.com:affinda/affinda-python.git
cd affinda-python
pip install -e .
```

Quickstart
----------

```python
from pathlib import Path
from affinda import AffindaAPI, TokenCredential

TOKEN = "YOUR_API_TOKEN"

file_pth = Path("path_to_file")
credential = TokenCredential(token=TOKEN)

client = AffindaAPI(credential=credential)
with open(file_pth, "rb") as f:
    resp = client.create_resume(file=f, file_name="test.pdf", wait=False)
```

Samples
-------

Samples for all operations using the client can be [found here.](./docs/samples_python.md)


API reference
-------------

- [API operations can be found here](./docs/sync_operations.md)
- [API models and objects](./docs/models.md)
- [Exceptions](./docs/exceptions.md)

