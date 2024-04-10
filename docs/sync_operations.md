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
- `region` (`str or ~affinda.models.Region`): region - server parameter. Default value is "api".

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
def get_all_resumes(offset=None, limit=None, custom_identifier=None, **kwargs)
```

Get list of all resumes.

Returns all the resume summaries for that user, limited to 300 per page.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `custom_identifier` (`str`): Filter for documents with this custom identifier. Default value is
None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths14VxierV2ResumesGetResponses200ContentApplicationJsonSchema`: Paths14VxierV2ResumesGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume"></a>

#### create\_resume

```python
def create_resume(file=None,
                  url=None,
                  data=None,
                  identifier=None,
                  custom_identifier=None,
                  file_name=None,
                  wait=True,
                  reject_duplicates=None,
                  language=None,
                  expiry_time=None,
                  region_bias=None,
                  low_priority=None,
                  **kwargs)
```

Upload a resume for parsing.

Uploads a resume for parsing. When successful, returns an ``identifier`` in the response for
subsequent use with the `/resumes/{identifier} <#get-/resumes/-identifier->`_ endpoint to check
processing status and retrieve results.:code:`<br/>`
Resumes can be uploaded as a file or a URL. In addition, data can be added directly if users
want to upload directly without parsing any resume file. For uploading resume data, the
``data`` argument provided must be a JSON-encoded string. Data uploads will not impact upon
parsing credits.

**Arguments**:

- `file` (`IO`): Default value is None.
- `url` (`str`): URL to download the resume. Default value is None.
- `data` (`~affinda.models.ResumeData`): Default value is None.
- `identifier` (`str`): Deprecated in favor of ``customIdentifier``. Default value is None.
- `custom_identifier` (`str`): Specify a custom identifier for the document if you need one, not
required to be unique. Default value is None.
- `file_name` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `reject_duplicates` (`bool`): Default value is None.
- `language` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.
- `region_bias` (`str`): Default value is None.
- `low_priority` (`bool`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Resume`: Resume, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume"></a>

#### get\_resume

```python
def get_resume(identifier, format=None, **kwargs)
```

Get parse results for a specific resume.

Returns all the parse results for that resume if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the resume via the `/resumes
<#post-/resumes>`_ endpoint.

**Arguments**:

- `identifier` (`str`): Document identifier.
- `format` (`str or ~affinda.models.Enum2`): Set this to "hr-xml" to get the response in HR-XML format. Currently the only
supported value for this parameter is "hr-xml". Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Resume`: Resume, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_resume_data"></a>

#### update\_resume\_data

```python
def update_resume_data(identifier, body, **kwargs)
```

Update a resume's data.

Update data of a parsed resume.
The ``identifier`` is the unique ID returned after POST-ing the resume via the `/resumes
<#post-/resumes>`_ endpoint.

**Arguments**:

- `identifier` (`str`): Resume identifier.
- `body` (`~affinda.models.ResumeData`): Resume data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeData or None`: ResumeData or None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_resume"></a>

#### delete\_resume

```python
def delete_resume(identifier, **kwargs)
```

Delete a resume.

Deletes the specified resume from the database.

**Arguments**:

- `identifier` (`str`): Resume identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_redacted_resumes"></a>

#### get\_all\_redacted\_resumes

```python
def get_all_redacted_resumes(offset=None,
                             limit=None,
                             custom_identifier=None,
                             **kwargs)
```

Get list of all redacted resumes.

Returns all the redacted resume information for that resume.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `custom_identifier` (`str`): Filter for documents with this custom identifier. Default value is
None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths1D957B5V2RedactedResumesGetResponses200ContentApplicationJsonSchema`: Paths1D957B5V2RedactedResumesGetResponses200ContentApplicationJsonSchema, or the
result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_redacted_resume"></a>

#### create\_redacted\_resume

```python
def create_redacted_resume(file=None,
                           identifier=None,
                           custom_identifier=None,
                           file_name=None,
                           url=None,
                           language=None,
                           wait=True,
                           redact_headshot="true",
                           redact_personal_details="true",
                           redact_work_details="true",
                           redact_education_details="true",
                           redact_referees="true",
                           redact_locations="true",
                           redact_dates="true",
                           redact_gender="true",
                           redact_pdf_metadata="true",
                           expiry_time=None,
                           **kwargs)
```

Upload a resume for redacting.

Uploads a resume for redacting.

**Arguments**:

- `file` (`IO`): Default value is None.
- `identifier` (`str`): Deprecated in favor of ``customIdentifier``. Default value is None.
- `custom_identifier` (`str`): Specify a custom identifier for the document if you need one, not
required to be unique. Default value is None.
- `file_name` (`str`): Default value is None.
- `url` (`str`): URL to download the resume. Default value is None.
- `language` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `redact_headshot` (`str`): Whether to redact headshot. Default value is "true".
- `redact_personal_details` (`str`): Whether to redact personal details (e.g. name, address).
Default value is "true".
- `redact_work_details` (`str`): Whether to redact work details (e.g. company names). Default value
is "true".
- `redact_education_details` (`str`): Whether to redact education details (e.g. university names).
Default value is "true".
- `redact_referees` (`str`): Whether to redact referee details. Default value is "true".
- `redact_locations` (`str`): Whether to redact location names. Default value is "true".
- `redact_dates` (`str`): Whether to redact dates. Default value is "true".
- `redact_gender` (`str`): Whether to redact gender. Default value is "true".
- `redact_pdf_metadata` (`str`): Whether to redact PDF metadata. Default value is "true".
- `expiry_time` (`~datetime.datetime`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.RedactedResume`: RedactedResume, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_redacted_resume"></a>

#### get\_redacted\_resume

```python
def get_redacted_resume(identifier, **kwargs)
```

Get redaction results for a specific resume.

Returns all the redaction results for that resume if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the resume via the
`/redacted_resumes <#post-/redacted_resumes>`_ endpoint.

**Arguments**:

- `identifier` (`str`): Document identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.RedactedResume`: RedactedResume, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_redacted_resume"></a>

#### delete\_redacted\_resume

```python
def delete_redacted_resume(identifier, **kwargs)
```

Delete a redacted resume.

Deletes the specified resume from the database.

**Arguments**:

- `identifier` (`str`): Document identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_invoices"></a>

#### get\_all\_invoices

```python
def get_all_invoices(offset=None,
                     limit=None,
                     custom_identifier=None,
                     **kwargs)
```

Get list of all invoices.

Returns all the invoice summaries for that user, limited to 300 per page.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `custom_identifier` (`str`): Filter for documents with this custom identifier. Default value is
None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsGfm23QV2InvoicesGetResponses200ContentApplicationJsonSchema`: PathsGfm23QV2InvoicesGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_invoice"></a>

#### create\_invoice

```python
def create_invoice(file=None,
                   url=None,
                   identifier=None,
                   custom_identifier=None,
                   file_name=None,
                   wait=True,
                   reject_duplicates=None,
                   language=None,
                   expiry_time=None,
                   region_bias=None,
                   low_priority=None,
                   **kwargs)
```

Upload an invoice for parsing.

Uploads an invoice for parsing.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/invoices/{identifier} <#get-/invoices/-identifier->`_ endpoint to check processing status and
retrieve results.

**Arguments**:

- `file` (`IO`): Default value is None.
- `url` (`str`): URL to download the invoice. Default value is None.
- `identifier` (`str`): Deprecated in favor of ``customIdentifier``. Default value is None.
- `custom_identifier` (`str`): Specify a custom identifier for the document if you need one, not
required to be unique. Default value is None.
- `file_name` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `reject_duplicates` (`bool`): Default value is None.
- `language` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.
- `region_bias` (`str`): Default value is None.
- `low_priority` (`bool`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invoice`: Invoice, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_invoice"></a>

#### get\_invoice

```python
def get_invoice(identifier, **kwargs)
```

Get parse results for a specific invoice.

Returns all the parse results for that invoice if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the invoice via the `/invoices
<#post-/invoices>`_ endpoint.

**Arguments**:

- `identifier` (`str`): Document identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invoice`: Invoice, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_invoice"></a>

#### delete\_invoice

```python
def delete_invoice(identifier, **kwargs)
```

Delete an invoice.

Delete the specified invoice from the database. Note, any invoices deleted from the database
will no longer be used in any tailored customer models.

**Arguments**:

- `identifier` (`str`): Invoice identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_job_descriptions"></a>

#### get\_all\_job\_descriptions

```python
def get_all_job_descriptions(offset=None,
                             limit=None,
                             custom_identifier=None,
                             **kwargs)
```

Get list of all job descriptions.

Returns all the job descriptions for that user, limited to 300 per page.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `custom_identifier` (`str`): Filter for documents with this custom identifier. Default value is
None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsChbpqfV2JobDescriptionsGetResponses200ContentApplicationJsonSchema`: PathsChbpqfV2JobDescriptionsGetResponses200ContentApplicationJsonSchema, or the result
of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_job_description"></a>

#### create\_job\_description

```python
def create_job_description(file=None,
                           url=None,
                           data=None,
                           identifier=None,
                           custom_identifier=None,
                           file_name=None,
                           wait=True,
                           reject_duplicates=None,
                           language=None,
                           expiry_time=None,
                           region_bias=None,
                           low_priority=None,
                           **kwargs)
```

Upload a job description for parsing.

Uploads a job description for parsing.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/job_descriptions/{identifier} <#get-/job_descriptions/-identifier->`_ endpoint to check
processing status and retrieve results.
Job Descriptions can be uploaded as a file or a URL. In addition, data can be added directly if
users want to upload directly without parsing any resume file. For uploading resume data, the
``data`` argument provided must be a JSON-encoded string. Data uploads will not impact upon
parsing credits.

**Arguments**:

- `file` (`IO`): Default value is None.
- `url` (`str`): URL to download the job description. Default value is None.
- `data` (`~affinda.models.JobDescriptionDataUpdate`): Default value is None.
- `identifier` (`str`): Deprecated in favor of ``customIdentifier``. Default value is None.
- `custom_identifier` (`str`): Specify a custom identifier for the document if you need one, not
required to be unique. Default value is None.
- `file_name` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `reject_duplicates` (`bool`): Default value is None.
- `language` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.
- `region_bias` (`str`): Default value is None.
- `low_priority` (`bool`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescription`: JobDescription, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_job_description"></a>

#### get\_job\_description

```python
def get_job_description(identifier, **kwargs)
```

Get job description results for a specific job description file.

Returns all the results for that job description if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the resume via the
`/job_descriptions <#post-/job_descriptions>`_ endpoint.

**Arguments**:

- `identifier` (`str`): Document identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescription`: JobDescription, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_job_description_data"></a>

#### update\_job\_description\_data

```python
def update_job_description_data(identifier, body, **kwargs)
```

Update a job description's data.

Update data of a job description.
The ``identifier`` is the unique ID returned after POST-ing the job description via the
`/job_descriptions <#post-/job_descriptions>`_ endpoint.

**Arguments**:

- `identifier` (`str`): Job description identifier.
- `body` (`~affinda.models.JobDescriptionDataUpdate`): Job description data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionData or None`: JobDescriptionData or None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_job_description"></a>

#### delete\_job\_description

```python
def delete_job_description(identifier, **kwargs)
```

Delete a job description.

Deletes the specified job description from the database.

**Arguments**:

- `identifier` (`str`): Document identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_job_description_search"></a>

#### create\_job\_description\_search

```python
def create_job_description_search(body, offset=None, limit=None, **kwargs)
```

Search through parsed job descriptions.

Searches through parsed job descriptions. You can search with custom criterias or a resume.

**Arguments**:

- `body` (`~affinda.models.JobDescriptionSearchParameters`): Search parameters.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionSearch`: JobDescriptionSearch, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_job_description_search_detail"></a>

#### get\_job\_description\_search\_detail

```python
def get_job_description_search_detail(identifier, body, **kwargs)
```

Get search result of specific job description.

This contains more detailed information about the matching score of the search criteria, or
which search criteria is missing in this job description.
The ``identifier`` is the unique ID returned via the `/job_description_search
<#post-/job_description_search>`_ endpoint.

**Arguments**:

- `identifier` (`str`): Job Description identifier.
- `body` (`~affinda.models.JobDescriptionSearchParameters`): Search parameters.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionSearchDetail`: JobDescriptionSearchDetail, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_job_description_search_config"></a>

#### get\_job\_description\_search\_config

```python
def get_job_description_search_config(**kwargs)
```

Get the config for the logged in user's embeddable job description search tool.

Return configurations such as which fields can be displayed in the logged in user's embeddable
job description search tool, what are their weights, what is the maximum number of results that
can be returned, etc.

**Arguments**:

- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionSearchConfig`: JobDescriptionSearchConfig, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_job_description_search_config"></a>

#### update\_job\_description\_search\_config

```python
def update_job_description_search_config(body, **kwargs)
```

Update the config for the logged in user's embeddable job description search tool.

Update configurations such as which fields can be displayed in the logged in user's embeddable
job description search tool, what are their weights, what is the maximum number of results that
can be returned, etc.

**Arguments**:

- `body` (`~affinda.models.JobDescriptionSearchConfig`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionSearchConfig`: JobDescriptionSearchConfig, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_job_description_search_embed_url"></a>

#### create\_job\_description\_search\_embed\_url

```python
def create_job_description_search_embed_url(body=None, **kwargs)
```

Create a signed URL for the embeddable job description search tool.

Create and return a signed URL of the job description search tool which then can be embedded on
a web page. An optional parameter ``config_override`` can be passed to override the user-level
configurations of the embeddable search tool.

**Arguments**:

- `body` (`~affinda.models.Paths15O3Zn5V2JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.JobDescriptionSearchEmbed`: JobDescriptionSearchEmbed, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume_search"></a>

#### create\_resume\_search

```python
def create_resume_search(body, offset=None, limit=None, **kwargs)
```

Search through parsed resumes.

Searches through parsed resumes. Users have 3 options to create a search::code:`<br
/>`:code:`<br />` 1.    Match to a job description - a parsed job description is used to find
candidates that suit it:code:`<br />` 2.  Match to a resume - a parsed resume is used to find
other candidates that have similar attributes:code:`<br />` 3.  Search using custom
criteria:code:`<br />`:code:`<br />` Users should only populate 1 of jobDescription, resume or
the custom criteria.

**Arguments**:

- `body` (`~affinda.models.ResumeSearchParameters`): Search parameters.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearch`: ResumeSearch, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_detail"></a>

#### get\_resume\_search\_detail

```python
def get_resume_search_detail(identifier, body, **kwargs)
```

Get search result of specific resume.

This contains more detailed information about the matching score of the search criteria, or
which search criteria is missing in this resume.
The ``identifier`` is the unique ID returned via the `/resume_search <#post-/resume_search>`_
endpoint.

**Arguments**:

- `identifier` (`str`): Resume identifier.
- `body` (`~affinda.models.ResumeSearchParameters`): Search parameters.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearchDetail`: ResumeSearchDetail, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_match"></a>

#### get\_resume\_search\_match

```python
def get_resume_search_match(resume,
                            job_description,
                            index=None,
                            search_expression=None,
                            job_titles_weight=None,
                            years_experience_weight=None,
                            locations_weight=None,
                            languages_weight=None,
                            skills_weight=None,
                            education_weight=None,
                            search_expression_weight=None,
                            soc_codes_weight=None,
                            management_level_weight=None,
                            **kwargs)
```

Match a single resume and job description.

Get the matching score between a resume and a job description. The score ranges between 0 and
1, with 0 being not a match at all, and 1 being perfect match.:code:`<br/>` Note, this score
will not directly match the score returned from POST `/resume_search/details/{identifier}
<#post-/resume_search/details/-identifier->`_.

**Arguments**:

- `resume` (`str`): Identify the resume to match.
- `job_description` (`str`): Identify the job description to match.
- `index` (`str`): Optionally, specify an index to search in. If not specified, will search in all
indexes. Default value is None.
- `search_expression` (`str`): Add keywords to the search criteria. Default value is None.
- `job_titles_weight` (`float`): How important is this criteria to the matching score, range from 0 to
1. Default value is None.
- `years_experience_weight` (`float`): How important is this criteria to the matching score, range
from 0 to 1. Default value is None.
- `locations_weight` (`float`): How important is this criteria to the matching score, range from 0 to
1. Default value is None.
- `languages_weight` (`float`): How important is this criteria to the matching score, range from 0 to
1. Default value is None.
- `skills_weight` (`float`): How important is this criteria to the matching score, range from 0 to 1.
Default value is None.
- `education_weight` (`float`): How important is this criteria to the matching score, range from 0 to
1. Default value is None.
- `search_expression_weight` (`float`): How important is this criteria to the matching score, range
from 0 to 1. Default value is None.
- `soc_codes_weight` (`float`): How important is this criteria to the matching score, range from 0 to
1. Default value is None.
- `management_level_weight` (`float`): How important is this criteria to the matching score, range
from 0 to 1. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearchMatch`: ResumeSearchMatch, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_config"></a>

#### get\_resume\_search\_config

```python
def get_resume_search_config(**kwargs)
```

Get the config for the logged in user's embeddable resume search tool.

Return configurations such as which fields can be displayed in the logged in user's embeddable
resume search tool, what are their weights, what is the maximum number of results that can be
returned, etc.

**Arguments**:

- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearchConfig`: ResumeSearchConfig, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_resume_search_config"></a>

#### update\_resume\_search\_config

```python
def update_resume_search_config(body, **kwargs)
```

Update the config for the logged in user's embeddable resume search tool.

Update configurations such as which fields can be displayed in the logged in user's embeddable
resume search tool, what are their weights, what is the maximum number of results that can be
returned, etc.

**Arguments**:

- `body` (`~affinda.models.ResumeSearchConfig`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearchConfig`: ResumeSearchConfig, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume_search_embed_url"></a>

#### create\_resume\_search\_embed\_url

```python
def create_resume_search_embed_url(body=None, **kwargs)
```

Create a signed URL for the embeddable resume search tool.

Create and return a signed URL of the resume search tool which then can be embedded on a web
page. An optional parameter ``config_override`` can be passed to override the user-level
configurations of the embeddable resume search tool.

**Arguments**:

- `body` (`~affinda.models.Paths23Ubd8V2ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResumeSearchEmbed`: ResumeSearchEmbed, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_suggestion_job_title"></a>

#### get\_resume\_search\_suggestion\_job\_title

```python
def get_resume_search_suggestion_job_title(job_titles, **kwargs)
```

Get job title suggestions based on provided job title(s).

Provided one or more job titles, get related suggestions for your search.

**Arguments**:

- `job_titles` (`list[str]`): Job title to query suggestions for.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[str]`: list of str, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume_search_suggestion_skill"></a>

#### get\_resume\_search\_suggestion\_skill

```python
def get_resume_search_suggestion_skill(skills, **kwargs)
```

Get skill suggestions based on provided skill(s).

Provided one or more skills, get related suggestions for your search.

**Arguments**:

- `skills` (`list[str]`): Skill to query suggestions for.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[str]`: list of str, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_indexes"></a>

#### get\_all\_indexes

```python
def get_all_indexes(offset=None, limit=None, document_type=None, **kwargs)
```

Get list of all indexes.

Returns all the indexes.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `document_type` (`str or ~affinda.models.Enum7`): Filter indices by a document type. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths18Iqsr4V2IndexGetResponses200ContentApplicationJsonSchema`: Paths18Iqsr4V2IndexGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_index"></a>

#### create\_index

```python
def create_index(body, **kwargs)
```

Create a new index.

Create an index for the search tool.

**Arguments**:

- `body` (`~affinda.models.IndexCreate`): Index to create.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Index`: Index, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_index"></a>

#### update\_index

```python
def update_index(name, body, **kwargs)
```

Update an index.

Updates the specified index.

**Arguments**:

- `name` (`str`): Index name.
- `body` (`~affinda.models.IndexUpdate`): Index data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Index`: Index, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_index"></a>

#### delete\_index

```python
def delete_index(name, **kwargs)
```

Delete an index.

Deletes the specified index from the database.

**Arguments**:

- `name` (`str`): Index name.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_index_documents"></a>

#### get\_all\_index\_documents

```python
def get_all_index_documents(name, **kwargs)
```

Get indexed documents for a specific index.

Returns all the indexed documents for that index.

**Arguments**:

- `name` (`str`): Index name.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsAf7Nd4V2IndexNameDocumentsGetResponses200ContentApplicationJsonSchema`: PathsAf7Nd4V2IndexNameDocumentsGetResponses200ContentApplicationJsonSchema, or the
result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_index_document"></a>

#### create\_index\_document

```python
def create_index_document(name, body, **kwargs)
```

Index a new document.

Create an indexed document for the search tool.

**Arguments**:

- `name` (`str`): Index name.
- `body` (`~affinda.models.PathsYg099PV2IndexNameDocumentsPostRequestbodyContentApplicationJsonSchema`): Document to index.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths14R8PdgV2IndexNameDocumentsPostResponses201ContentApplicationJsonSchema`: Paths14R8PdgV2IndexNameDocumentsPostResponses201ContentApplicationJsonSchema, or the
result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_index_document"></a>

#### delete\_index\_document

```python
def delete_index_document(name, identifier, **kwargs)
```

Delete an indexed document.

Delete the specified indexed document from the database.

**Arguments**:

- `name` (`str`): Index name.
- `identifier` (`str`): Document identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.list_occupation_groups"></a>

#### list\_occupation\_groups

```python
def list_occupation_groups(**kwargs)
```

List occupation groups.

Returns the list of searchable occupation groups.

**Arguments**:

- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.OccupationGroup]`: list of OccupationGroup, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_resthook_subscriptions"></a>

#### get\_all\_resthook\_subscriptions

```python
def get_all_resthook_subscriptions(offset=None, limit=None, **kwargs)
```

Get list of all resthook subscriptions.

Returns your resthook subscriptions.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsMda0LlV2ResthookSubscriptionsGetResponses200ContentApplicationJsonSchema`: PathsMda0LlV2ResthookSubscriptionsGetResponses200ContentApplicationJsonSchema, or the
result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resthook_subscription"></a>

#### create\_resthook\_subscription

```python
def create_resthook_subscription(body, **kwargs)
```

Create a resthook subscription.

After a subscription is successfully created, we'll send a POST request to your target URL with
a ``X-Hook-Secret`` header. :code:`<br />`
You need to response to this request with a 200 status code to confirm your subscribe
intention. :code:`<br />`
Then, you need to use the ``X-Hook-Secret`` to activate the subscription using the
`/resthook_subscriptions/activate <#post-/v3/resthook_subscriptions/activate>`_ endpoint.

**Arguments**:

- `body` (`~affinda.models.ResthookSubscriptionCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResthookSubscription`: ResthookSubscription, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resthook_subscription"></a>

#### get\_resthook\_subscription

```python
def get_resthook_subscription(id, **kwargs)
```

Get specific resthook subscription.

Return a specific resthook subscription.

**Arguments**:

- `id` (`int`): Resthook subscription's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResthookSubscription`: ResthookSubscription, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_resthook_subscription"></a>

#### update\_resthook\_subscription

```python
def update_resthook_subscription(id, body, **kwargs)
```

Update a resthook subscription.

Update data of a resthook subscription.

**Arguments**:

- `id` (`int`): ResthookSubscription's ID.
- `body` (`~affinda.models.ResthookSubscriptionUpdate`): ResthookSubscription data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResthookSubscription`: ResthookSubscription, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_resthook_subscription"></a>

#### delete\_resthook\_subscription

```python
def delete_resthook_subscription(id, **kwargs)
```

Delete a resthook subscription.

Deletes the specified resthook subscription from the database.

**Arguments**:

- `id` (`int`): ResthookSubscription's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.activate_resthook_subscription"></a>

#### activate\_resthook\_subscription

```python
def activate_resthook_subscription(x_hook_secret, **kwargs)
```

Activate a resthook subscription.

After creating a subscription, we'll send a POST request to your target URL with a
``X-Hook-Secret`` header.
You should response to this with a 200 status code, and use the value of the ``X-Hook-Secret``
header that you received to activate the subscription using this endpoint.

**Arguments**:

- `x_hook_secret` (`str`): The secret received when creating a subscription.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.ResthookSubscription`: ResthookSubscription, or the result of cls(response)

