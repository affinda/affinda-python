

Resume Parser
-------------

### getAllResumes - Get list of all resumes

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_resumes = client.get_all_resumes()

print(all_resumes.as_dict())
```

### createResume - Upload a resume for parsing

```python
from pathlib import Path

from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
file_pth = Path("path_to_file.pdf")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    resume = client.create_resume(file=f)

print(resume.as_dict())
```

### getResume - Get parse results for a specific resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
resume = client.get_resume(identifier=identifier)

print(resume.as_dict())
```

### deleteResume - Delete a resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
response = client.delete_resume(identifier=identifier)

print(response.as_dict())
```

Resume Redactor
---------------

### getAllRedactedResumes - Get list of all redacted resumes

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_redacted_resumes = client.get_all_redacted_resumes()

print(all_redacted_resumes.as_dict())
```

### createRedactedResume - Upload a resume for redacting

```python
from pathlib import Path

from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
file_pth = Path("path_to_file.pdf")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    redacted_resume = client.create_redacted_resume(file=f)

print(redacted_resume.as_dict())
```

### getRedactedResume - Get redaction results for a specific resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
redacted_resume = client.get_redacted_resume(identifier=identifier)

print(redacted_resume.as_dict())
```

### deleteRedactedResume - Delete a redacted resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
response = client.delete_redacted_resume(identifier=identifier)

print(response.as_dict())
```

Resume Reformatter
------------------

### getAllResumeFormats - Get list of all resume formats

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
resume_formats = client.get_all_resume_formats()

print(resume_formats.as_dict())
```

### getAllReformattedResumes - Get list of all reformatted resumes

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_reformatted_resumes = client.get_all_reformatted_resumes()

print(all_reformatted_resumes.as_dict())
```

### createReformattedResume - Upload a resume for reformatting

```python
from pathlib import Path

from affinda import TokenCredential, AffindaAPI

token = "REPLACE_TOKEN"
resume_format = "REPLACE_FORMAT_IDENTIFIER"
file_pth = Path("path_to_file.pdf")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    reformatted_resume = client.create_reformatted_resume(file=f, file_name=file_pth.name, resume_format=resume_format)

print(reformatted_resume.as_dict())
```

### getReformattedResume - Get reformatting results for a specific resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
reformatted_resume = client.get_reformatted_resume(identifier=identifier)

print(reformatted_resume.as_dict())
```

### deleteReformattedResume - Delete a reformatted resume

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
response = client.delete_reformatted_resume(identifier=identifier)

print(response.as_dict())
```

Resume Search
-------------

### createResumeSearch - Search through parsed resumes

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

request_body = {
    "indices": ["MyIndex"],
    "job_titles": ["Senior Java Software Developer"],
    "institutions": ["Boston University"],
}


resp = client.create_resume_search(body=request_body)

print(resp[0].as_dict())
```

### getAllIndexes - Get list of all indexes

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

all_indexes = client.get_all_indexes()

print(all_indexes.as_dict())
```

### createIndex - Create a new index

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
index_name = "REPLACE_INDEX_NAME"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

response = client.create_index(name=index_name)

print(response.as_dict())
```

### deleteIndex - Delete an index

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
index_name = "REPLACE_INDEX_NAME"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_index(name=index_name)
```

### createIndexDocument - Index a new document

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
index_name = "REPLACE_INDEX_NAME"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

request_body = {
    "document": identifier,
}

resp = client.create_index_document(name=index_name, body=request_body)

print(resp.as_dict())
```

### deleteIndexDocument - Delete an indexed document

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
index_name = "REPLACE_INDEX_NAME"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

client.delete_index_document(name=index_name, identifier=identifier)
```

Invoice Parser
--------------

### getAllInvoices - Get list of all invoices

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_invoices = client.get_all_invoices()

print(all_invoices.as_dict())
```

### createInvoice - Upload an invoice for parsing

```python
from pathlib import Path

from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
file_pth = Path("path_to_file.pdf")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    invoice = client.create_invoice(file=f)

print(invoice.as_dict())
```

### getInvoice - Get parse results for a specific invoice

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
invoice = client.get_invoices(identifier=identifier)

print(invoice.as_dict())
```

### deleteInvoice - Delete an invoice

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
response = client.delete_invoice(identifier=identifier)

print(response.as_dict())
```