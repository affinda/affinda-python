![affinda logo](affinda_logo.png)

This is the python client for the **Affinda API**

## Installation

```shell
git clone git@github.com:affinda/affinda-python.git
cd affinda
pip install -e . 
```

Or to use in code:
```shell
git clone git@github.com:affinda/affinda-python.git
cd affinda
pip install -r requirements.txt
```

## Quickstart

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

## API reference
- [API operations can be found here](./docs/sync_operations.md)
- [API models and objects](./docs/models.md)
- [Exceptions](./docs/exceptions.md)

## Parser
### Gets summary information for all resumes of a user
```python
from pathlib import Path
from affinda.public.openapi.generated.python.affinda_python import AffindaAPI, TokenCredential

TOKEN = "YOUR_API_TOKEN"

file_pth = Path("path_to_file")
credential = TokenCredential(token=TOKEN)

client = AffindaAPI(credential=credential)
with open(file_pth, "rb") as f:
    resume = client.get_all_resumes()

print(resume.as_dict())
```
### Uploads a resume for parsing
```python
from pathlib import Path
from affinda.public.openapi.generated.python.affinda_python import AffindaAPI, TokenCredential

TOKEN = "YOUR_API_TOKEN"

file_pth = Path("path_to_file")
credential = TokenCredential(token=TOKEN)

client = AffindaAPI(credential=credential)
with open(file_pth, "rb") as f:
    resume = client.create_resume(file=f, file_name="test.pdf", wait=False)

print(resume.as_dict())
```
### Gets parse results for a specific resume
```python
from pathlib import Path
from affinda.public.openapi.generated.python.affinda_python import AffindaAPI, TokenCredential

TOKEN = "YOUR_API_TOKEN"

file_pth = Path("path_to_file")
credential = TokenCredential(token=TOKEN)

client = AffindaAPI(credential=credential)
with open(file_pth, "rb") as f:
    resume = client.get_resume(identifier="DUglqBoT")

print(resume.as_dict())
```
### Deletes a resume
```python
from pathlib import Path
from affinda.public.openapi.generated.python.affinda_python import AffindaAPI, TokenCredential

TOKEN = "YOUR_API_TOKEN"

file_pth = Path("path_to_file")
credential = TokenCredential(token=TOKEN)

client = AffindaAPI(credential=credential)
with open(file_pth, "rb") as f:
    confirmation = client.delete_resume(identifier="DUglqBoT")

print(confirmation.as_dict())
```
## Redactor
### Gets summary information for all redacted resumes of a user
```python
import requests

token = "REPLACE_TOKEN"

url = "https://api.affinda.com/v1/redacted_resumes"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)

print(response.json())

### THIS TEXT WILL NOT BE INCLUDED IN THE REDOCS, BUT WILL HELP DEFINE THE OUTPUT IN README.MD
### HEADING = "Get a resume
```
### Uploads a resume for redacting
```python
import requests
from pathlib import Path

FILE_TO_UPLOAD_PATH = Path("path/to/file")

url = "https://api.affinda.com/v1/redacted_resumes/"

token = "REPLACE_TOKEN"

headers = {"Authorization": f"Bearer {token}"}

with open(FILE_TO_UPLOAD_PATH, "rb") as doc_file:
    response = requests.post(
        url,
        data={"fileName": FILE_TO_UPLOAD_PATH.name},
        files={"file": doc_file},
        headers=headers,
    )

print(response.json())
```
### Gets redaction results for a specific resume
```python
import requests

identifier = "REPLACE_IDENTIFIER"

token = "REPLACE_TOKEN"

url = f"https://api.affinda.com/v1/redacted_resumes/{identifier}"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)

print(response.json())
```
### Deletes a redacted resume
```python
import requests

identifier = "REPLACE_IDENTIFIER"

token = "REPLACE_TOKEN"

url = f"https://api.affinda.com/v1/redacted_resumes/{identifier}"

headers = {"Authorization": f"Bearer {token}"}

response = requests.delete(url, headers=headers)
```
## Reformatter
### Gets summary information for all resume formats of a user
```python
import requests

token = "REPLACE_TOKEN"

url = "https://api.affinda.com/v1/resume_formats"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)

print(response.json())
```
### Gets summary information for all reformatted resumes of a user
```python
import requests

token = "REPLACE_TOKEN"

url = "https://api.affinda.com/v1/reformatted_resumes"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)

print(response.json())
```
### Uploads a resume for reformatting
```python
import requests
from pathlib import Path

FILE_TO_UPLOAD_PATH = Path("path/to/file")

url = "https://api.affinda.com/v1/reformatted_resumes/"

token = "REPLACE_TOKEN"
resumeFormat = "REPLACE_FORMAT_IDENTIFIER"

headers = {"Authorization": f"Bearer {token}"}

with open(FILE_TO_UPLOAD_PATH, "rb") as doc_file:
    response = requests.post(
        url,
        data={"fileName": FILE_TO_UPLOAD_PATH.name, "resumeFormat": resumeFormat},
        files={"file": doc_file},
        headers=headers,
    )

print(response.json())
```
### Gets reformatting results for a specific resume
```python
import requests

identifier = "REPLACE_IDENTIFIER"

token = "REPLACE_TOKEN"

url = f"https://api.affinda.com/v1/redacted_resumes/{identifier}"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)

print(response.json())
```
### Deletes a reformatted resume
```python
import requests

identifier = "REPLACE_IDENTIFIER"

token = "REPLACE_TOKEN"

url = f"https://api.affinda.com/v1/reformatted_resumes/{identifier}"

headers = {"Authorization": f"Bearer {token}"}

response = requests.delete(url, headers=headers)
```