

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
credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Create resume with file
file_pth = Path("path_to_file.pdf")

with open(file_pth, "rb") as f:
    resume = client.create_resume(file=f)

print(resume.as_dict())

# Create resume with url
url = "REPLACE_URL"
resume = client.create_resume(url=url)
print(resume.as_dict())

# Create resume with data (for direct import of resume data, no parsing is performed)
import json
from affinda.models import ResumeData

data = ResumeData(date_of_birth="1999-11-01")
data = json.dumps(data.as_dict())
res = client.create_resume(data=data, file_name="test_resume.pdf")
print(res.as_dict())
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

### updateResumeData - Update a resume's data

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Update resume
from affinda.models import ResumeDataResumeDataSkillsItem

resume = client.get_resume(identifier=identifier)
updated_data = resume.data
updated_data.date_of_birth = "1980-08-15"  # Update some attributes

# For lists, you can update, create new, or delete objects
updated_data.skills[0].last_used = "2022-06-01"  # Update the first skill
updated_data.skills.pop(-1)  # Delete the last skill
updated_data.skills.append(ResumeDataResumeDataSkillsItem(name="git", number_of_months=24))  # Create a new skill

resp = client.update_resume_data(identifier=identifier, body=updated_data)
print(resp.as_dict())
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

Search & Match - Searching
--------------------------

### createResumeSearch - Search through parsed resumes

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResumeSearchParameters

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Search with custom criterias
parameters = ResumeSearchParameters(
    indices=["Resume-Search-Demo"],
    job_titles=["Senior Java Software Developer"],
    institutions=["Boston University"],
    # Many more criterias are available, refer to ResumeSearchParameters
)
resp = client.create_resume_search(parameters)
print(resp.as_dict())

# Search with a job description
job_description_identifier = "REPLACE_JOB_DESCRIPTION_IDENTIFIER"
parameters = ResumeSearchParameters(
    indices=["Resume-Search-Demo"],
    job_description=job_description_identifier,
)
resp = client.create_resume_search(parameters)
print(resp.as_dict())

# Search with a resume
resume_identifier = "REPLACE_RESUME_IDENTIFIER"
parameters = ResumeSearchParameters(
    indices=["Resume-Search-Demo"],
    resume=resume_identifier,
)
resp = client.create_resume_search(parameters)
print(resp.as_dict())
```

### getResumeSearchDetail - Get search result of specific resume

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResumeSearchParameters

token = "REPLACE_TOKEN"
resume_identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Search with custom criterias
parameters = ResumeSearchParameters(
    indices=["Resume-Search-Demo"],
    job_titles=["Senior Java Software Developer"],
    institutions=["Boston University"],
    # Many more criterias are available, refer to ResumeSearchParameters
)
resp = client.get_resume_search_detail(body=parameters, identifier=resume_identifier)
print(resp.as_dict())
```

### getResumeSearchMatch - Match a single resume and job description

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

resume = "REPLACE_RESUME_IDENTIFIER"
job_description = "REPLACE_JOB_DESCRIPTION_IDENTIFIER"
index = "REPLACE_INDEX_NAME"  # Optional

result = client.get_resume_search_match(resume, job_description, index=index)
print(result.score)
```

### getResumeSearchSuggestionJobTitle - Get job title suggestions based on provided job title(s)

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

suggested_job_titles = client.get_resume_search_suggestion_job_title(["Software Developer", "Team Lead"])
print(suggested_job_titles)
```

### getResumeSearchSuggestionSkill - Get skill suggestions based on provided skill(s)

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

suggested_skills = client.get_resume_search_suggestion_skill(["Javascript", "Python"])
print(suggested_skills)
```

### createJobDescriptionSearch - Search through parsed job descriptions

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import JobDescriptionSearchParameters

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Search with custom criterias
parameters = JobDescriptionSearchParameters(
    indices=["Job-Description-Search-Demo"],
    job_titles=["Senior Java Software Developer"],
    skills=["Java Programming"],
    # Many more criterias are available, refer to JobDescriptionSearchParameters
)
resp = client.create_job_description_search(parameters)
print(resp.as_dict())

# Search with a resume
resume_identifier = "REPLACE_RESUME_IDENTIFIER"
parameters = JobDescriptionSearchParameters(
    indices=["Job-Description-Search-Demo"],
    resume=resume_identifier,
)
resp = client.create_job_description_search(parameters)
print(resp.as_dict())
```

### getJobDescriptionSearchDetail - Get search result of specific job description

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import JobDescriptionSearchParameters

token = "REPLACE_TOKEN"
job_description_identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Search with custom criterias
parameters = JobDescriptionSearchParameters(
    indices=["Job-Description-Search-Demo"],
    job_titles=["Senior Java Software Developer"],
    degrees=["Bachelors"],
    # Many more criterias are available, refer to JobDescriptionSearchParameters
)
resp = client.get_job_description_search_detail(body=parameters, identifier=job_description_identifier)
print(resp.as_dict())
```

Search & Match - Embedding
--------------------------

### getResumeSearchConfig - Get the config for the logged in user's embeddable resume search tool

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

result = client.get_resume_search_config()
print(result.as_dict())
```

### updateResumeSearchConfig - Update the config for the logged in user's embeddable resume search tool

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResumeSearchConfig

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

config = ResumeSearchConfig(
    indices=["my-index"],
    max_results=10,
    display_job_title=False,
    weight_location=0.8,
    # etc.
)

result = client.update_resume_search_config(config)
print(result.as_dict())
```

### createResumeSearchEmbedUrl - Create a signed URL for the embeddable resume search tool

```python
from affinda import AffindaAPI, TokenCredential
from affinda.models import ResumeSearchConfig

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

# Config override is optional
request_body = {
    "config_override": ResumeSearchConfig(
        indices=["my-index"],
        max_results=10,
        display_job_title=False,
        weight_location=0.8,
        # etc.
    )
}

result = client.create_resume_search_embed_url(body=request_body)
print(result.url)
```

Job Description Parser
----------------------

### getAllJobDescriptions - Get list of all job descriptions

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
all_job_descriptions = client.get_all_job_descriptions()

print(all_job_descriptions.as_dict())
```

### createJobDescription - Upload a job description for parsing

```python
from pathlib import Path

from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
file_pth = Path("path_to_file.pdf")

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

with open(file_pth, "rb") as f:
    job_description = client.create_job_description(file=f)

print(job_description.as_dict())
```

### getJobDescription - Get job description results for a specific job description file

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
job_description = client.get_job_description(identifier=identifier)

print(job_description.as_dict())
```

### deleteJobDescription - Delete a job description

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"
identifier = "REPLACE_IDENTIFIER"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)
response = client.delete_job_description(identifier=identifier)

print(response.as_dict())
```

Search & Match - Indexing
-------------------------

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

Invoice Extractor
-----------------

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
invoice = client.get_invoice(identifier=identifier)

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

Users
-----

### createUser - Create a new user

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

response = client.create_user(email="myuser@gmail.com")

print(response.as_dict())
```

### createOrganization - Create a new organization

```python
from affinda import AffindaAPI, TokenCredential

token = "REPLACE_TOKEN"

credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

response = client.create_organization(name="Grove Street King")

print(response.as_dict())
```

Documents API
-------------