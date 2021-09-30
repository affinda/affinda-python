

Parser
------

### getAllResumes - Gets list of all resumes

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_resumes = client.get_all_resumes()

print(all_resumes.as_dict())
```

### createResume - Uploads a resume for parsing

```python
from pathlib import Path

from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
file_pth = Path("path_to_file")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    resume = client.create_resume(file=f)

print(resume.as_dict())
```

### getResume - Gets parse results for a specific resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
resume = client.get_resume(identifier=identifier)

print(resume.as_dict())
```

### deleteResume - Deletes a resume

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

### getAllRedactedResumes - Gets list of all redacted resumes

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_redacted_resumes = client.get_all_redacted_resumes()

print(all_redacted_resumes.as_dict())
```

### createRedactedResume - Uploads a resume for redacting

```python
from pathlib import Path

from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
file_pth = Path("path_to_file")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    redacted_resume = client.create_redacted_resume(file=f)

print(redacted_resume.as_dict())
```

### getRedactedResume - Gets redaction results for a specific resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
redacted_resume = client.get_redacted_resume(identifier=identifier)

print(redacted_resume.as_dict())
```

### deleteRedactedResume - Deletes a redacted resume

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

### getAllResumeFormats - Gets list of all resume formats

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
resume_formats = client.get_all_resume_formats()

print(resume_formats.as_dict())
```

### getAllReformattedResumes - Gets list of all reformatted resumes

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_reformatted_resumes = client.get_all_reformatted_resumes()

print(all_reformatted_resumes.as_dict())
```

### createReformattedResume - Uploads a resume for reformatting

```python
from pathlib import Path

from affinda import TokenCredential, AffindaAPI

token = "REPLACE_TOKEN"
resume_format = "REPLACE_FORMAT_IDENTIFIER"
file_pth = Path("path_to_file")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    reformatted_resume = client.create_reformatted_resume(file=f, file_name=file_pth.name, resume_format=resume_format)

print(reformatted_resume.as_dict())
```

### getReformattedResume - Gets reformatting results for a specific resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
reformatted_resume = client.get_reformatted_resume(identifier=identifier)

print(reformatted_resume.as_dict())
```

### deleteReformattedResume - Deletes a reformatted resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
response = client.delete_reformatted_resume(identifier=identifier)

print(response.as_dict())
```