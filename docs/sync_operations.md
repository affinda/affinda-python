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
- `base_url` (`str`): Service URL. Default value is "https://api.affinda.com/v2".

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

Default value is None.
:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return. Default value is 300.

**Returns**:

`~affinda.models.GetAllDocumentsResults or ~affinda.models.RequestError`: GetAllDocumentsResults or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume"></a>

#### create\_resume

```python
def create_resume(file=None, url=None, data=None, identifier=None, file_name=None, wait=True, language=None, expiry_time=None, **kwargs)
```

Upload a resume for parsing.

Uploads a resume for parsing.
Provide ``file`` for uploading a resume file, or ``url`` for getting resume file from an url,
or ``data`` if you want to upload resume data directly without parsing any resume file.
For uploading resume data, the ``data`` argument provided must be a JSON-encoded string.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/resumes/{identifier} <#operation/getResume>`_ endpoint to check processing status and
retrieve results.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `file` (`IO`): Default value is None.
- `url` (`str`): Default value is None.
- `data` (`~affinda.models.ResumeData`): A JSON-encoded string of the ``ResumeData`` object. Default value is None.
- `identifier` (`str`): Default value is None.
- `file_name` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `language` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.

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

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_resume_data"></a>

#### update\_resume\_data

```python
def update_resume_data(identifier, body, **kwargs)
```

Update a resume's data.

Update data of a parsed resume.
The ``identifier`` is the unique ID returned after POST-ing the resume via the `/resumes
<#operation/createResume>`_ endpoint.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Resume identifier.
- `body` (`~affinda.models.ResumeData`): Resume data to update.

**Returns**:

`~affinda.models.ResumeData or None or ~affinda.models.RequestError`: ResumeData or None or RequestError, or the result of cls(response)

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

Default value is None.
:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return. Default value is 300.

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

Default value is True.
is True.
Default value is True.
:keyword callable cls: A custom type or function that will be passed the direct response
- `file` (`IO`): Default value is None.
- `identifier` (`str`): Default value is None.
- `file_name` (`str`): Default value is None.
- `url` (`str`): Default value is None.
- `language` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `redact_headshot` (`bool`): Whether to redact headshot. Default value is True.
- `redact_personal_details` (`bool`): Whether to redact personal details (e.g. name, address).
- `redact_work_details` (`bool`): Whether to redact work details (e.g. company names). Default value
- `redact_education_details` (`bool`): Whether to redact education details (e.g. university names).
- `redact_referees` (`bool`): Whether to redact referee details. Default value is True.
- `redact_locations` (`bool`): Whether to redact location names. Default value is True.
- `redact_dates` (`bool`): Whether to redact dates. Default value is True.
- `redact_gender` (`bool`): Whether to redact gender. Default value is True.
- `expiry_time` (`~datetime.datetime`): Default value is None.

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

Default value is None.
:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return. Default value is 300.

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

Default value is None.
:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return. Default value is 300.

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
- `file` (`IO`): Default value is None.
- `identifier` (`str`): Default value is None.
- `file_name` (`str`): Default value is None.
- `url` (`str`): Default value is None.
- `language` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.

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
def create_resume_search(body, offset=None, limit=300, **kwargs)
```

Search through parsed resumes.

Searches through parsed resumes. You can search with custom criterias, a job description, or a
resume.
When searching with a job description, a parsed job description is used to find candidates that
suit it.
When searching with a resume, a parsed resume is used to find other candidates that have
similar attributes.

**Arguments**:

Default value is None.
:keyword callable cls: A custom type or function that will be passed the direct response
- `body` (`~affinda.models.ResumeSearchParameters`): Search parameters.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return. Default value is 300.

**Returns**:

`~affinda.models.ResumeSearch or ~affinda.models.RequestError`: ResumeSearch or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_detail"></a>

#### get\_resume\_search\_detail

```python
def get_resume_search_detail(identifier, body, **kwargs)
```

Get search result of specific resume.

This contains more detailed information about the matching score of the search criteria, or
which search criteria is missing in this resume.
The ``identifier`` is the unique ID returned via the `/resume_search
<#operation/createResumeSearch>`_ endpoint.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Resume identifier.
- `body` (`~affinda.models.ResumeSearchParameters`): Search parameters.

**Returns**:

`~affinda.models.ResumeSearchDetail or ~affinda.models.RequestError`: ResumeSearchDetail or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_match"></a>

#### get\_resume\_search\_match

```python
def get_resume_search_match(resume, job_description, index=None, search_expression=None, job_titles_weight=None, years_experience_weight=None, locations_weight=None, languages_weight=None, skills_weight=None, education_weight=None, search_expression_weight=None, soc_codes_weight=None, management_level_weight=None, **kwargs)
```

Resume and job description 1:1 match.

Get the matching score between a resume and a job description. The score ranges between 0 and
1, with 0 being not a match at all, and 1 being perfect match.

**Arguments**:

indexes. Default value is None.
1. Default value is None.
from 0 to 1. Default value is None.
1. Default value is None.
1. Default value is None.
Default value is None.
1. Default value is None.
from 0 to 1. Default value is None.
1. Default value is None.
from 0 to 1. Default value is None.
:keyword callable cls: A custom type or function that will be passed the direct response
- `resume` (`str`): Identify the resume to match.
- `job_description` (`str`): Identify the job description to match.
- `index` (`str`): Optionally, specify an index to search in. If not specified, will search in all
- `search_expression` (`str`): Add keywords to the search criteria. Default value is None.
- `job_titles_weight` (`float`): How important is this criteria to the matching score, range from 0 to
- `years_experience_weight` (`float`): How important is this criteria to the matching score, range
- `locations_weight` (`float`): How important is this criteria to the matching score, range from 0 to
- `languages_weight` (`float`): How important is this criteria to the matching score, range from 0 to
- `skills_weight` (`float`): How important is this criteria to the matching score, range from 0 to 1.
- `education_weight` (`float`): How important is this criteria to the matching score, range from 0 to
- `search_expression_weight` (`float`): How important is this criteria to the matching score, range
- `soc_codes_weight` (`float`): How important is this criteria to the matching score, range from 0 to
- `management_level_weight` (`float`): How important is this criteria to the matching score, range

**Returns**:

`~affinda.models.ResumeSearchMatch or ~affinda.models.RequestError`: ResumeSearchMatch or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_config"></a>

#### get\_resume\_search\_config

```python
def get_resume_search_config(**kwargs)
```

Get the config for the logged in user's embedable search tool.

Return configurations such as which fields can be displayed in the logged in user's embedable
search tool, what are their weights, what is the maximum number of results that can be
returned, etc.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

`~affinda.models.ResumeSearchConfig or ~affinda.models.RequestError`: ResumeSearchConfig or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_resume_search_config"></a>

#### update\_resume\_search\_config

```python
def update_resume_search_config(body, **kwargs)
```

Update the config for the logged in user's embedable search tool.

Update configurations such as which fields can be displayed in the logged in user's embedable
search tool, what are their weights, what is the maximum number of results that can be
returned, etc.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `body` (`~affinda.models.ResumeSearchConfig`): 

**Returns**:

`~affinda.models.ResumeSearchConfig or ~affinda.models.RequestError`: ResumeSearchConfig or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume_search_embed_url"></a>

#### create\_resume\_search\_embed\_url

```python
def create_resume_search_embed_url(body=None, **kwargs)
```

Create a signed URL for the embedable search tool.

Create and return a signed URL of the resume search tool which then can be embedded on a web
page. An optional parameter ``config_override`` can be passed to override the user-level
configurations of the embedable search tool.

**Arguments**:

~affinda.models.Paths2T1Oc0ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema
:keyword callable cls: A custom type or function that will be passed the direct response
- `body`: Default value is None.

**Returns**:

`~affinda.models.ResumeSearchEmbed or ~affinda.models.RequestError`: ResumeSearchEmbed or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_job_descriptions"></a>

#### get\_all\_job\_descriptions

```python
def get_all_job_descriptions(offset=None, limit=300, **kwargs)
```

Get list of all job descriptions.

Returns all the job descriptions for that user, limited to 300 per page.

**Arguments**:

Default value is None.
:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return. Default value is 300.

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
- `file` (`IO`): Default value is None.
- `identifier` (`str`): Default value is None.
- `file_name` (`str`): Default value is None.
- `url` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `language` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.

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

Default value is None.
:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return. Default value is 300.

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
- `name` (`bool`): Default value is True.

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

Default value is None.
:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return. Default value is 300.

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
- `file` (`IO`): Default value is None.
- `identifier` (`str`): Default value is None.
- `file_name` (`str`): Default value is None.
- `url` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `language` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.

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

`list[~affinda.models.OccupationGroup] or ~affinda.models.RequestError`: list of OccupationGroup or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_users"></a>

#### get\_all\_users

```python
def get_all_users(offset=None, limit=300, **kwargs)
```

Get list of all users.

Returns all the users.

**Arguments**:

Default value is None.
:keyword callable cls: A custom type or function that will be passed the direct response
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `limit` (`int`): The numbers of results to return. Default value is 300.

**Returns**:

`~affinda.models.PathsWjaaeuUsersGetResponses200ContentApplicationJsonSchema or`: PathsWjaaeuUsersGetResponses200ContentApplicationJsonSchema or RequestError, or the

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_user"></a>

#### create\_user

```python
def create_user(username, id=None, name=None, email=None, api_key=None, **kwargs)
```

Create a new user.

Create an user as part of your account.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `username` (`str`): 
- `id` (`int`): Default value is None.
- `name` (`str`): Default value is None.
- `email` (`str`): Default value is None.
- `api_key` (`str`): Default value is None.

**Returns**:

`~affinda.models.PathsTop5ZkUsersPostResponses201ContentApplicationJsonSchema or`: PathsTop5ZkUsersPostResponses201ContentApplicationJsonSchema or RequestError, or the

