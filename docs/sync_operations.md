<a id="_affinda_api"></a>

# \_affinda\_api

<a id="_affinda_api.AffindaAPI"></a>

## AffindaAPI Objects

```python
class AffindaAPI(AffindaAPIOperationsMixin)
```

Affinda API client for Python.

**Arguments**:

- `credential` (`~azure.core.credentials.TokenCredential`): Credential needed for the client to connect to Azure.
- `base_url` (`str`): Service URL. Default value is 'https://api.affinda.com/v2'.

<a id="operations._affinda_api_operations"></a>

# operations.\_affinda\_api\_operations

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin"></a>

## AffindaAPIOperationsMixin Objects

```python
class AffindaAPIOperationsMixin(object)
```

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_resumes"></a>

#### get\_all\_resumes

```python
def get_all_resumes(offset=None, limit=300, **kwargs)
```

Get list of all resumes.

Returns all the resume summaries for that user, limited to 300 per page.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return.

**Returns**:

`~affinda.models.GetAllDocumentsResults or ~affinda.models.RequestError`: GetAllDocumentsResults or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume"></a>

#### create\_resume

```python
def create_resume(file=None, identifier=None, file_name=None, url=None, wait=True, language=None, expiry_time=None, **kwargs)
```

Upload a resume for parsing.

Uploads a resume for parsing.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/resumes/{identifier} <#operation/getResume>`_ endpoint to check processing status and
retrieve results.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `file` (`IO`): 
- `identifier` (`str`): 
- `file_name` (`str`): 
- `url` (`str`): 
- `wait` (`bool`): 
- `language` (`str`): 
- `expiry_time` (`str`): 

**Returns**:

`~affinda.models.Resume or ~affinda.models.RequestError`: Resume or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume"></a>

#### get\_resume

```python
def get_resume(identifier, **kwargs)
```

Get parse results for a specific resume.

Returns all the parse results for that resume if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the resume via the `/resumes
<#operation/createResume>`_ endpoint.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.Resume or ~affinda.models.RequestError`: Resume or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_resume"></a>

#### delete\_resume

```python
def delete_resume(identifier, **kwargs)
```

Delete a resume.

Deletes the specified resume from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Resume identifier.

**Returns**:

`~affinda.models.RequestError or None`: RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_redacted_resumes"></a>

#### get\_all\_redacted\_resumes

```python
def get_all_redacted_resumes(offset=None, limit=300, **kwargs)
```

Get list of all redacted resumes.

Returns all the redacted resume information for that resume.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return.

**Returns**:

`~affinda.models.GetAllDocumentsResults or ~affinda.models.RequestError`: GetAllDocumentsResults or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_redacted_resume"></a>

#### create\_redacted\_resume

```python
def create_redacted_resume(file=None, identifier=None, file_name=None, url=None, language=None, wait=True, redact_headshot=True, redact_personal_details=True, redact_work_details=True, redact_education_details=True, redact_referees=True, redact_locations=True, redact_dates=True, redact_gender=True, expiry_time=None, **kwargs)
```

Upload a resume for redacting.

Uploads a resume for redacting.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `file` (`IO`): 
- `identifier` (`str`): 
- `file_name` (`str`): 
- `url` (`str`): 
- `language` (`str`): 
- `wait` (`bool`): 
- `redact_headshot` (`bool`): Whether to redact headshot.
- `redact_personal_details` (`bool`): Whether to redact personal details (e.g. name, address).
- `redact_work_details` (`bool`): Whether to redact work details (e.g. company names).
- `redact_education_details` (`bool`): Whether to redact education details (e.g. university names).
- `redact_referees` (`bool`): Whether to redact referee details.
- `redact_locations` (`bool`): Whether to redact location names.
- `redact_dates` (`bool`): Whether to redact dates.
- `redact_gender` (`bool`): Whether to redact gender.
- `expiry_time` (`str`): 

**Returns**:

`~affinda.models.RedactedResume or ~affinda.models.RequestError`: RedactedResume or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_redacted_resume"></a>

#### get\_redacted\_resume

```python
def get_redacted_resume(identifier, **kwargs)
```

Get redaction results for a specific resume.

Returns all the redaction results for that resume if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the resume via the
`/redacted_resumes <#operation/createRedactedResume>`_ endpoint.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.RedactedResume or ~affinda.models.RequestError`: RedactedResume or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_redacted_resume"></a>

#### delete\_redacted\_resume

```python
def delete_redacted_resume(identifier, **kwargs)
```

Delete a redacted resume.

Deletes the specified resume from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.RequestError or None`: RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_resume_formats"></a>

#### get\_all\_resume\_formats

```python
def get_all_resume_formats(offset=None, limit=300, **kwargs)
```

Get list of all resume formats.

Returns all the resume formats.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return.

**Returns**:

`~affinda.models.Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema or`: Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema or RequestError,

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_reformatted_resumes"></a>

#### get\_all\_reformatted\_resumes

```python
def get_all_reformatted_resumes(offset=None, limit=300, **kwargs)
```

Get list of all reformatted resumes.

Returns all the reformatted resume information for that resume.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return.

**Returns**:

`~affinda.models.GetAllDocumentsResults or ~affinda.models.RequestError`: GetAllDocumentsResults or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_reformatted_resume"></a>

#### create\_reformatted\_resume

```python
def create_reformatted_resume(resume_format, file=None, identifier=None, file_name=None, url=None, language=None, wait=True, **kwargs)
```

Upload a resume for reformatting.

Upload a resume for reformatting.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `resume_format` (`str`): 
- `file` (`IO`): 
- `identifier` (`str`): 
- `file_name` (`str`): 
- `url` (`str`): 
- `language` (`str`): 
- `wait` (`bool`): 

**Returns**:

`~affinda.models.ReformattedResume or ~affinda.models.RequestError`: ReformattedResume or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_reformatted_resume"></a>

#### get\_reformatted\_resume

```python
def get_reformatted_resume(identifier, **kwargs)
```

Get reformatting results for a specific resume.

Returns all the reformatting results for that resume if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the resume via the
`/reformatted_resumes <#operation/createReformattedResume>`_ endpoint.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.ReformattedResume or ~affinda.models.RequestError`: ReformattedResume or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_reformatted_resume"></a>

#### delete\_reformatted\_resume

```python
def delete_reformatted_resume(identifier, **kwargs)
```

Delete a reformatted resume.

Delete the specified resume from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.RequestError or None`: RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume_search"></a>

#### create\_resume\_search

```python
def create_resume_search(body, offset=None, limit=20, **kwargs)
```

Search through parsed resumes.

Searches through parsed resumes.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `body` (`~affinda.models.ResumeSearchParameters`): Search parameters.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return.

**Returns**:

`~affinda.models.ResumeSearch or ~affinda.models.RequestError`: ResumeSearch or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_job_descriptions"></a>

#### get\_all\_job\_descriptions

```python
def get_all_job_descriptions(offset=None, limit=300, **kwargs)
```

Get list of all job descriptions.

Returns all the job descriptions for that user, limited to 300 per page.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return.

**Returns**:

`~affinda.models.GetAllJobDescriptionsResults or ~affinda.models.RequestError`: GetAllJobDescriptionsResults or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_job_description"></a>

#### create\_job\_description

```python
def create_job_description(file=None, identifier=None, file_name=None, url=None, wait=True, language=None, expiry_time=None, **kwargs)
```

Upload a job description for parsing.

Uploads a job description for parsing.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/job_descriptions/{identifier} <#operation/getResume>`_ endpoint to check processing status
and retrieve results.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `file` (`IO`): 
- `identifier` (`str`): 
- `file_name` (`str`): 
- `url` (`str`): 
- `wait` (`bool`): 
- `language` (`str`): 
- `expiry_time` (`str`): 

**Returns**:

`~affinda.models.JobDescription or ~affinda.models.RequestError`: JobDescription or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_job_description"></a>

#### get\_job\_description

```python
def get_job_description(identifier, **kwargs)
```

Get job description results for a specific job description file.

Returns all the results for that job description if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the resume via the
`/job_descriptions <#operation/createJobDescription>`_ endpoint.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.JobDescription or ~affinda.models.RequestError`: JobDescription or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_job_description"></a>

#### delete\_job\_description

```python
def delete_job_description(identifier, **kwargs)
```

Delete a job description.

Deletes the specified job description from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.RequestError or None`: RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_indexes"></a>

#### get\_all\_indexes

```python
def get_all_indexes(offset=None, limit=300, **kwargs)
```

Get list of all indexes.

Returns all the indexes.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return.

**Returns**:

`~affinda.models.Paths6Pypg5IndexGetResponses200ContentApplicationJsonSchema or`: Paths6Pypg5IndexGetResponses200ContentApplicationJsonSchema or RequestError, or the

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_index"></a>

#### create\_index

```python
def create_index(name=True, **kwargs)
```

Create a new index.

Create an index for the search tool.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `name` (`bool`): 

**Returns**:

`~affinda.models.Paths1Mc0Je6IndexPostResponses201ContentApplicationJsonSchema or`: Paths1Mc0Je6IndexPostResponses201ContentApplicationJsonSchema or RequestError, or the

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_index"></a>

#### delete\_index

```python
def delete_index(name, **kwargs)
```

Delete an index.

Deletes the specified index from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `name` (`str`): Index name.

**Returns**:

`~affinda.models.RequestError or None`: RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_index_documents"></a>

#### get\_all\_index\_documents

```python
def get_all_index_documents(name, **kwargs)
```

Get indexed documents for a specific index.

Returns all the indexed documents for that index.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `name` (`str`): Index name.

**Returns**:

PathsRvverlIndexNameDocumentsGetResponses200ContentApplicationJsonSchema or

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_index_document"></a>

#### create\_index\_document

```python
def create_index_document(name, body, **kwargs)
```

Index a new document.

Create an indexed document for the search tool.

**Arguments**:

~affinda.models.PathsGpptmIndexNameDocumentsPostRequestbodyContentApplicationJsonSchema
:keyword callable cls: A custom type or function that will be passed the direct response
- `name` (`str`): Index name.
- `body`: Document to index.

**Returns**:

PathsCoo0XpIndexNameDocumentsPostResponses201ContentApplicationJsonSchema or

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_index_document"></a>

#### delete\_index\_document

```python
def delete_index_document(name, identifier, **kwargs)
```

Delete an indexed document.

Delete the specified indexed document from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `name` (`str`): Index name.
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.RequestError or None`: RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_invoices"></a>

#### get\_all\_invoices

```python
def get_all_invoices(offset=None, limit=300, **kwargs)
```

Get list of all invoices.

Returns all the invoice summaries for that user, limited to 300 per page.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return.

**Returns**:

`~affinda.models.GetAllInvoicesResults or ~affinda.models.RequestError`: GetAllInvoicesResults or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_invoice"></a>

#### create\_invoice

```python
def create_invoice(file=None, identifier=None, file_name=None, url=None, wait=True, language=None, expiry_time=None, **kwargs)
```

Upload an invoice for parsing.

Uploads an invoice for parsing.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/invoices/{identifier} <#operation/getInvoice>`_ endpoint to check processing status and
retrieve results.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `file` (`IO`): 
- `identifier` (`str`): 
- `file_name` (`str`): 
- `url` (`str`): 
- `wait` (`bool`): 
- `language` (`str`): 
- `expiry_time` (`str`): 

**Returns**:

`~affinda.models.Invoice or ~affinda.models.RequestError`: Invoice or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_invoice"></a>

#### get\_invoice

```python
def get_invoice(identifier, **kwargs)
```

Get parse results for a specific invoice.

Returns all the parse results for that invoice if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the invoice via the `/invoices
<#operation/createInvoice>`_ endpoint.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.Invoice or ~affinda.models.RequestError`: Invoice or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_invoice"></a>

#### delete\_invoice

```python
def delete_invoice(identifier, **kwargs)
```

Delete an invoice.

Delete the specified invoice from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Invoice identifier.

**Returns**:

`~affinda.models.RequestError or None`: RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.list_occupation_groups"></a>

#### list\_occupation\_groups

```python
def list_occupation_groups(**kwargs)
```

List occupation groups.

TODO TODO TODO.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

`~affinda.models.OccupationGroup or ~affinda.models.RequestError`: OccupationGroup or RequestError, or the result of cls(response)

