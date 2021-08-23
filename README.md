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

Generated using [autorest](https://github.com/Azure/autorest) and [autorest.python](https://github.com/Azure/autorest.python).

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

API reference
-------------

- [API operations can be found here](./docs/sync_operations.md)
- [API models and objects](./docs/models.md)
- [Exceptions](./docs/exceptions.md)

Parser
------

### Gets summary information for all resumes of a user

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_resumes = client.get_all_resumes()

print(all_resumes.as_dict())
```

### Uploads a resume for parsing

```python
from pathlib import Path

from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"
file_pth = Path("path_to_file")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    resume = client.create_resume(file=f, file_name=file_pth.name, wait=True)

print(resume.as_dict())
```

### Gets parse results for a specific resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
resume = client.get_resume(identifier=identifier)

print(resume.as_dict())
```

### Deletes a resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
response = client.delete_resume(identifier=identifier)

print(response.as_dict())
```

Redactor
--------

### Gets summary information for all redacted resumes of a user

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_redacted_resumes = client.get_all_redacted_resumes()

print(all_redacted_resumes.as_dict())
```

### Uploads a resume for redacting

```python
from pathlib import Path

from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"
file_pth = Path("path_to_file")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    redacted_resume = client.create_redacted_resume(file=f, file_name=file_pth.name)

print(redacted_resume.as_dict())
```

### Gets redaction results for a specific resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
redacted_resume = client.get_redacted_resume(identifier=identifier)

print(redacted_resume.as_dict())
```

### Deletes a redacted resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
response = client.delete_redacted_resume(identifier=identifier)

print(response.as_dict())
```

Reformatter
-----------

### Gets summary information for all resume formats of a user

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
resume_formats = client.get_all_resume_formats()

print(resume_formats.as_dict())
```

### Gets summary information for all reformatted resumes of a user

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_reformatted_resumes = client.get_all_reformatted_resumes()

print(all_reformatted_resumes.as_dict())
```

### Uploads a resume for reformatting

```python
from pathlib import PathAdding basic test suite

from affinda import TokenCredential, AffindaAPI

token = "REPLACE_TOKEN"
resume_format = "REPLACE_FORMAT_IDENTIFIER"
file_pth = Path("path_to_file")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    reformatted_resume = client.create_reformatted_resume(file=f,
                                                          file_name=file_pth.name,
                                                          resume_format=resume_format)

print(reformatted_resume.as_dict())
```

### Gets reformatting results for a specific resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
reformatted_resume = client.get_reformatted_resume(identifier=identifier)

print(reformatted_resume.as_dict())
```

### Deletes a reformatted resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
response = client.delete_reformatted_resume(identifier=identifier)

print(response.as_dict())
```
