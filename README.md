Python Client Library for Affinda Resume Parser API
===================================================

![affinda logo](https://raw.githubusercontent.com/affinda/affinda-python/main/affinda_logo.png)

[![pypi ver](https://img.shields.io/pypi/v/affinda)](https://pypi.org/project/affinda/)
[![pypi pyver](https://img.shields.io/pypi/pyversions/affinda)](https://pypi.org/affinda/)
[![pypi dlm](https://img.shields.io/pypi/dm/affinda)](https://pypi.org/project/affinda/)
[![license](https://img.shields.io/github/license/affinda/affinda-python)](https://choosealicense.com/licenses/mit/)

[![codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/affinda/affinda-python)

This is a python client for the Affinda document parsing API which wraps all available endpoints
and handles authentication and signing.  You may also want to refer to the full
[API documentation](https://api.affinda.com/docs) for additional information.

Installation
------------

```shell
pip install affinda
```


Quickstart
----------
If you don't have an API token, obtain one from [affinda.com](https://affinda.com/resume-parser/free-api-key/).

```python
from affinda import AffindaAPI, TokenCredential

credential = TokenCredential(token="YOUR_API_TOKEN")
client = AffindaAPI(credential=credential)

with open("PATH_TO_FILE", "rb") as f:
    resume = client.create_resume(file=f)
```

Samples
-------

Samples for all operations using the client can be [found here.](./docs/samples_python.md)


API reference
-------------

- [API operations can be found here](./docs/sync_operations.md)
- [API models and objects](./docs/models.md)
- [Exceptions](./docs/exceptions.md)
