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
def get_all_resumes(offset=None, limit=300, **kwargs)
```

Get list of all resumes.

Returns all the resume summaries for that user, limited to 300 per page.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.GetAllDocumentsResultsV2`: GetAllDocumentsResultsV2, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume"></a>

#### create\_resume

```python
def create_resume(file=None, url=None, data=None, identifier=None, file_name=None, wait=True, reject_duplicates=False, language=None, expiry_time=None, **kwargs)
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
- `url` (`str`): Default value is None.
- `data` (`~affinda.models.ResumeData`): Default value is None.
- `identifier` (`str`): Default value is None.
- `file_name` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `reject_duplicates` (`bool`): Default value is False.
- `language` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.
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
- `format` (`str`): Set this to "hr-xml" to get the response in HR-XML format. Currently the only
supported value for this parameter is "hr-xml". Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

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
def get_all_redacted_resumes(offset=None, limit=300, **kwargs)
```

Get list of all redacted resumes.

Returns all the redacted resume information for that resume.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.GetAllDocumentsResultsV2`: GetAllDocumentsResultsV2, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_redacted_resume"></a>

#### create\_redacted\_resume

```python
def create_redacted_resume(file=None, identifier=None, file_name=None, url=None, language=None, wait=True, redact_headshot="true", redact_personal_details="true", redact_work_details="true", redact_education_details="true", redact_referees="true", redact_locations="true", redact_dates="true", redact_gender="true", expiry_time=None, **kwargs)
```

Upload a resume for redacting.

Uploads a resume for redacting.

**Arguments**:

- `file` (`IO`): Default value is None.
- `identifier` (`str`): Default value is None.
- `file_name` (`str`): Default value is None.
- `url` (`str`): Default value is None.
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
def get_all_invoices(offset=None, limit=300, **kwargs)
```

Get list of all invoices.

Returns all the invoice summaries for that user, limited to 300 per page.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.GetAllInvoicesResults`: GetAllInvoicesResults, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_invoice"></a>

#### create\_invoice

```python
def create_invoice(file=None, url=None, identifier=None, file_name=None, wait=True, reject_duplicates=False, language=None, expiry_time=None, **kwargs)
```

Upload an invoice for parsing.

Uploads an invoice for parsing.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/invoices/{identifier} <#get-/invoices/-identifier->`_ endpoint to check processing status and
retrieve results.

**Arguments**:

- `file` (`IO`): Default value is None.
- `url` (`str`): Default value is None.
- `identifier` (`str`): Default value is None.
- `file_name` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `reject_duplicates` (`bool`): Default value is False.
- `language` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.
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
def get_all_job_descriptions(offset=None, limit=300, **kwargs)
```

Get list of all job descriptions.

Returns all the job descriptions for that user, limited to 300 per page.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.GetAllJobDescriptionsResults`: GetAllJobDescriptionsResults, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_job_description"></a>

#### create\_job\_description

```python
def create_job_description(file=None, url=None, identifier=None, file_name=None, wait=True, reject_duplicates=False, language=None, expiry_time=None, **kwargs)
```

Upload a job description for parsing.

Uploads a job description for parsing.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/job_descriptions/{identifier} <#get-/job_descriptions/-identifier->`_ endpoint to check
processing status and retrieve results.
Job Descriptions can be uploaded as a file or a URL.

**Arguments**:

- `file` (`IO`): Default value is None.
- `url` (`str`): Default value is None.
- `identifier` (`str`): Default value is None.
- `file_name` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `reject_duplicates` (`bool`): Default value is False.
- `language` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.
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
def create_job_description_search(body, offset=None, limit=300, **kwargs)
```

Search through parsed job descriptions.

Searches through parsed job descriptions. You can search with custom criterias or a resume.

**Arguments**:

- `body` (`~affinda.models.JobDescriptionSearchParameters`): Search parameters.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
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
def create_resume_search(body, offset=None, limit=300, **kwargs)
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
- `limit` (`int`): The numbers of results to return. Default value is 300.
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
def get_resume_search_match(resume, job_description, index=None, search_expression=None, job_titles_weight=None, years_experience_weight=None, locations_weight=None, languages_weight=None, skills_weight=None, education_weight=None, search_expression_weight=None, soc_codes_weight=None, management_level_weight=None, **kwargs)
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

- `body` (`~affinda.models.Paths1Czpnk1V3ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema`): Default value is None.
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
def get_all_indexes(offset=None, limit=300, document_type=None, **kwargs)
```

Get list of all indexes.

Returns all the indexes.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `document_type` (`str or ~affinda.models.Enum3`): Filter indices by a document type. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsDvrcp3V3IndexGetResponses200ContentApplicationJsonSchema`: PathsDvrcp3V3IndexGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_index"></a>

#### create\_index

```python
def create_index(name=None, document_type=None, **kwargs)
```

Create a new index.

Create an index for the search tool.

**Arguments**:

- `name` (`str`): Default value is None.
- `document_type` (`str or ~affinda.models.PostContentSchemaDocumentType`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths1TvfqeiV3IndexPostResponses201ContentApplicationJsonSchema`: Paths1TvfqeiV3IndexPostResponses201ContentApplicationJsonSchema, or the result of
cls(response)

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

`~affinda.models.PathsO7SnenV3IndexNameDocumentsGetResponses200ContentApplicationJsonSchema`: PathsO7SnenV3IndexNameDocumentsGetResponses200ContentApplicationJsonSchema, or the
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
- `body` (`~affinda.models.PathsCl024WV3IndexNameDocumentsPostRequestbodyContentApplicationJsonSchema`): Document to index.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsFte27NV3IndexNameDocumentsPostResponses201ContentApplicationJsonSchema`: PathsFte27NV3IndexNameDocumentsPostResponses201ContentApplicationJsonSchema, or the
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

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_organizations"></a>

#### get\_all\_organizations

```python
def get_all_organizations(**kwargs)
```

Get list of all organizations.

Returns all the organizations.

**Arguments**:

- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Organization]`: list of Organization, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_organization"></a>

#### create\_organization

```python
def create_organization(name, avatar=None, resthook_signature_key=None, **kwargs)
```

Create a new organization.

Create a new organization.

**Arguments**:

- `name` (`str`): 
- `avatar` (`IO`): Upload avatar for the organization. Default value is None.
- `resthook_signature_key` (`str`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Organization`: Organization, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_organization"></a>

#### get\_organization

```python
def get_organization(identifier, **kwargs)
```

Get detail of an organization.

Get detail of an organization.

**Arguments**:

- `identifier` (`str`): Organization identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Organization`: Organization, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_organization"></a>

#### update\_organization

```python
def update_organization(identifier, name=None, avatar=None, resthook_signature_key=None, **kwargs)
```

Update an organization.

Update the detail of an organization.

**Arguments**:

- `identifier` (`str`): Organization identifier.
- `name` (`str`): Default value is None.
- `avatar` (`IO`): Default value is None.
- `resthook_signature_key` (`str`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Organization`: Organization, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_organization"></a>

#### delete\_organization

```python
def delete_organization(identifier, **kwargs)
```

Delete an organization.

Delete the specified organization from the database.

**Arguments**:

- `identifier` (`str`): Organization identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_organization_memberships"></a>

#### get\_all\_organization\_memberships

```python
def get_all_organization_memberships(offset=None, limit=300, organization=None, role=None, **kwargs)
```

Get list of all organization memberships.

Returns all the organization memberships.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `organization` (`str`): Filter by organization. Default value is None.
- `role` (`str or ~affinda.models.OrganizationRole`): Filter by role. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsQ5Os5RV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchema`: PathsQ5Os5RV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchema, or
the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_organization_membership"></a>

#### get\_organization\_membership

```python
def get_organization_membership(identifier, **kwargs)
```

Get detail of an organization membership.

Get detail of an organization membership.

**Arguments**:

- `identifier` (`str`): Membership identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.OrganizationMembership`: OrganizationMembership, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_organization_membership"></a>

#### update\_organization\_membership

```python
def update_organization_membership(identifier, body, **kwargs)
```

Update an organization membership.

The admin users can use this endpoint to update the role of the members within their
organization.

**Arguments**:

- `identifier` (`str`): Membership identifier.
- `body` (`~affinda.models.OrganizationMembershipUpdate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.OrganizationMembership`: OrganizationMembership, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_organization_membership"></a>

#### delete\_organization\_membership

```python
def delete_organization_membership(identifier, **kwargs)
```

Delete an organization membership.

The admin users can use this endpoint to remove member from their organization. Other users can
also use this to leave their organization.

**Arguments**:

- `identifier` (`str`): Membership identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_invitations"></a>

#### get\_all\_invitations

```python
def get_all_invitations(offset=None, limit=300, organization=None, status=None, role=None, **kwargs)
```

Get list of all invitations.

Get list of all invitations you created or sent to you.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `organization` (`str`): Filter by organization. Default value is None.
- `status` (`str or ~affinda.models.InvitationStatus`): Filter by status. Default value is None.
- `role` (`str or ~affinda.models.OrganizationRole`): Filter by role. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Paths18Wh2VcV3InvitationsGetResponses200ContentApplicationJsonSchema`: Paths18Wh2VcV3InvitationsGetResponses200ContentApplicationJsonSchema, or the result of
cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_invitation"></a>

#### create\_invitation

```python
def create_invitation(body, **kwargs)
```

Create a new invitation.

Create a new invitation.

**Arguments**:

- `body` (`~affinda.models.InvitationCreate`): Invitation to create.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invitation`: Invitation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_invitation"></a>

#### get\_invitation

```python
def get_invitation(identifier, **kwargs)
```

Get detail of an invitation.

Get detail of an invitation.

**Arguments**:

- `identifier` (`str`): Invitation identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invitation`: Invitation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_invitation"></a>

#### update\_invitation

```python
def update_invitation(identifier, body, **kwargs)
```

Update an invitation.

Update the detail of an invitation.

**Arguments**:

- `identifier` (`str`): Invitation identifier.
- `body` (`~affinda.models.InvitationUpdate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invitation`: Invitation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_invitation"></a>

#### delete\_invitation

```python
def delete_invitation(identifier, **kwargs)
```

Delete an invitation.

Delete the specified invitation from the database.

**Arguments**:

- `identifier` (`str`): Invitation identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_invitation_by_token"></a>

#### get\_invitation\_by\_token

```python
def get_invitation_by_token(token, **kwargs)
```

Get detail of an invitation by token.

Get detail of an invitation using a secret token. This allows users who have not
registered/logged in to view the invitation.

**Arguments**:

- `token` (`str`): Invitation token.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invitation`: Invitation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.respond_to_invitation"></a>

#### respond\_to\_invitation

```python
def respond_to_invitation(token, body, **kwargs)
```

Respond to an invitation.

Choose to accept or decline an invitation.

**Arguments**:

- `token` (`str`): Invitation token.
- `body` (`~affinda.models.PathsCtl5TcV3InvitationsTokenPatchRequestbodyContentApplicationJsonSchema`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Invitation`: Invitation, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_extractors"></a>

#### get\_all\_extractors

```python
def get_all_extractors(organization, include_public_extractors=None, name=None, validatable=None, **kwargs)
```

Get list of all extractors.

Returns your custom extractors as well as Affinda's off-the-shelf extractors.

**Arguments**:

- `organization` (`str`): Filter by organization.
- `include_public_extractors` (`bool`): Whether to include Affinda's off-the-shelf extractors.
Default value is None.
- `name` (`str`): Filter by name. Default value is None.
- `validatable` (`bool`): Filter by validatable. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Extractor]`: list of Extractor, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_extractor"></a>

#### create\_extractor

```python
def create_extractor(body=None, **kwargs)
```

Create an extractor.

Create a custom extractor.

**Arguments**:

- `body` (`~affinda.models.ExtractorCreate`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Extractor`: Extractor, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_extractor"></a>

#### get\_extractor

```python
def get_extractor(id, **kwargs)
```

Get specific extractor.

Return a specific extractor.

**Arguments**:

- `id` (`int`): Extractor's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Extractor`: Extractor, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_extractor_data"></a>

#### update\_extractor\_data

```python
def update_extractor_data(id, body, **kwargs)
```

Update an extractor's data.

Update data of an extractor.

**Arguments**:

- `id` (`int`): Extractor's ID.
- `body` (`~affinda.models.ExtractorUpdate`): Extractor data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Extractor`: Extractor, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_extractor"></a>

#### delete\_extractor

```python
def delete_extractor(id, **kwargs)
```

Delete an extractor.

Deletes the specified extractor from the database.

**Arguments**:

- `id` (`int`): Extractor's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_data_points"></a>

#### get\_all\_data\_points

```python
def get_all_data_points(offset=None, limit=300, organization=None, extractor=None, slug=None, description=None, annotation_content_type=None, **kwargs)
```

Get list of all data points.

Returns your custom data points as well as Affinda's off-the-shelf data points.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `organization` (`str`): Filter by organization. Default value is None.
- `extractor` (`int`): Filter by extractor. Default value is None.
- `slug` (`str`): Filter by slug. Default value is None.
- `description` (`str`): Filter by description. Default value is None.
- `annotation_content_type` (`str`): Filter by annotation content type, e.g. text, integer, float,
date, etc. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.DataPoint]`: list of DataPoint, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_data_point"></a>

#### create\_data\_point

```python
def create_data_point(body=None, **kwargs)
```

Create a data point.

Create a custom data point.

**Arguments**:

- `body` (`~affinda.models.DataPointCreate`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataPoint`: DataPoint, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_data_point"></a>

#### get\_data\_point

```python
def get_data_point(identifier, **kwargs)
```

Get specific data point.

Return a specific data point.

**Arguments**:

- `identifier` (`str`): Data point's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataPoint`: DataPoint, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_data_point_data"></a>

#### update\_data\_point\_data

```python
def update_data_point_data(identifier, body, **kwargs)
```

Update a data point's data.

Update data of a data point.

**Arguments**:

- `identifier` (`str`): DataPoint's identifier.
- `body` (`~affinda.models.DataPointUpdate`): Data point to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.DataPoint`: DataPoint, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_data_point"></a>

#### delete\_data\_point

```python
def delete_data_point(identifier, **kwargs)
```

Delete a data point.

Deletes the specified data point from the database.

**Arguments**:

- `identifier` (`str`): DataPoint's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_data_point_choices"></a>

#### get\_data\_point\_choices

```python
def get_data_point_choices(data_point, offset=None, limit=300, search=None, **kwargs)
```

Get list of data point choices.

Returns available choices for a specific enum data point.

**Arguments**:

- `data_point` (`str`): The data point to get choices for.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `search` (`str`): Filter choices by searching for a substring. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsMnwxgV3DataPointChoicesGetResponses200ContentApplicationJsonSchema`: PathsMnwxgV3DataPointChoicesGetResponses200ContentApplicationJsonSchema, or the result
of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_workspaces"></a>

#### get\_all\_workspaces

```python
def get_all_workspaces(organization, name=None, **kwargs)
```

Get list of all workspaces.

Returns your workspaces.

**Arguments**:

- `organization` (`str`): Filter by organization.
- `name` (`str`): Filter by name. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Workspace]`: list of Workspace, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_workspace"></a>

#### create\_workspace

```python
def create_workspace(body, **kwargs)
```

Create a workspace.

Create a workspace.

**Arguments**:

- `body` (`~affinda.models.WorkspaceCreate`): Workspace to create.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Workspace`: Workspace, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_workspace"></a>

#### get\_workspace

```python
def get_workspace(identifier, **kwargs)
```

Get specific workspace.

Return a specific workspace.

**Arguments**:

- `identifier` (`str`): Workspace's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Workspace`: Workspace, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_workspace"></a>

#### update\_workspace

```python
def update_workspace(identifier, body, **kwargs)
```

Update a workspace.

Update a workspace.

**Arguments**:

- `identifier` (`str`): Workspace's identifier.
- `body` (`~affinda.models.WorkspaceUpdate`): Workspace data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Workspace`: Workspace, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_workspace"></a>

#### delete\_workspace

```python
def delete_workspace(identifier, **kwargs)
```

Delete a workspace.

Deletes the specified workspace from the database.

**Arguments**:

- `identifier` (`str`): Workspace's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_workspace_memberships"></a>

#### get\_all\_workspace\_memberships

```python
def get_all_workspace_memberships(offset=None, limit=300, workspace=None, user=None, **kwargs)
```

Get list of all workspace memberships.

Returns the memberships of your workspaces.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `workspace` (`str`): Filter by workspace. Default value is None.
- `user` (`str`): Partial text match on user's email, case-insensitive. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.PathsZ1JuagV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchema`: PathsZ1JuagV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchema, or the
result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_workspace_membership"></a>

#### create\_workspace\_membership

```python
def create_workspace_membership(body, **kwargs)
```

Create a workspace membership.

Create a workspace membership.

**Arguments**:

- `body` (`~affinda.models.WorkspaceMembershipCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.WorkspaceMembership`: WorkspaceMembership, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_workspace_membership"></a>

#### get\_workspace\_membership

```python
def get_workspace_membership(identifier, **kwargs)
```

Get specific workspace membership.

Return a specific workspace membership.

**Arguments**:

- `identifier` (`str`): Workspace membership's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.WorkspaceMembership`: WorkspaceMembership, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_workspace_membership"></a>

#### delete\_workspace\_membership

```python
def delete_workspace_membership(identifier, **kwargs)
```

Delete a workspace membership.

Remove an user from a workspace.

**Arguments**:

- `identifier` (`str`): Workspace membership's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_collections"></a>

#### get\_all\_collections

```python
def get_all_collections(workspace, **kwargs)
```

Get list of all collections.

Returns your collections.

**Arguments**:

- `workspace` (`str`): Filter by workspace.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Collection]`: list of Collection, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_collection"></a>

#### create\_collection

```python
def create_collection(body, **kwargs)
```

Create a collection.

Create a collection.

**Arguments**:

- `body` (`~affinda.models.CollectionCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Collection`: Collection, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_collection"></a>

#### get\_collection

```python
def get_collection(identifier, **kwargs)
```

Get specific collection.

Return a specific collection.

**Arguments**:

- `identifier` (`str`): Collection's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Collection`: Collection, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_collection_data"></a>

#### update\_collection\_data

```python
def update_collection_data(identifier, body, **kwargs)
```

Update a collection's data.

Update data of a collection.

**Arguments**:

- `identifier` (`str`): Collection's identifier.
- `body` (`~affinda.models.CollectionUpdate`): Collection data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Collection`: Collection, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_collection"></a>

#### delete\_collection

```python
def delete_collection(identifier, **kwargs)
```

Delete a collection.

Deletes the specified collection from the database.

**Arguments**:

- `identifier` (`str`): Collection's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_documents"></a>

#### get\_all\_documents

```python
def get_all_documents(offset=None, limit=300, workspace=None, collection=None, state=None, tags=None, created_dt=None, search=None, ordering=None, include_data=None, exclude=None, **kwargs)
```

Get list of all documents.

Returns all the document summaries for that user, limited to 300 per page.

**Arguments**:

- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `limit` (`int`): The numbers of results to return. Default value is 300.
- `workspace` (`str`): Filter by workspace. Default value is None.
- `collection` (`str`): Filter by collection. Default value is None.
- `state` (`str or ~affinda.models.DocumentState`): Filter by the document's state. Default value is None.
- `tags` (`list[int]`): Filter by tags. Default value is None.
- `created_dt` (`str or ~affinda.models.DateRange`): Filter by created datetime. Default value is None.
- `search` (`str`): Partial, case-insensitive match with file name or tag name. Default value is
None.
- `ordering` (`list[str or ~affinda.models.Get8ItemsItem]`): Sort the result set. A "-" at the beginning denotes DESC sort, e.g.
-created_dt. Sort by multiple fields is supported. Default value is None.
- `include_data` (`bool`): By default, this endpoint returns only the meta data of the documents. Set
this to ``true`` will return the detailed data that was parsed, at a performance cost. Default
value is None.
- `exclude` (`list[str]`): Exclude some documents from the result. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.GetAllDocumentsResults`: GetAllDocumentsResults, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_document"></a>

#### create\_document

```python
def create_document(file=None, url=None, collection=None, workspace=None, wait=True, identifier=None, file_name=None, expiry_time=None, language=None, **kwargs)
```

Upload a document for parsing.

Uploads a document for parsing. When successful, returns an ``identifier`` in the response for
subsequent use with the `/documents/{identifier} <#get-/documents/-identifier->`_ endpoint to
check processing status and retrieve results.:code:`<br/>`.

**Arguments**:

- `file` (`IO`): Default value is None.
- `url` (`str`): Default value is None.
- `collection` (`str`): Default value is None.
- `workspace` (`str`): Default value is None.
- `wait` (`bool`): Default value is True.
- `identifier` (`str`): Specify a custom identifier for the document. Default value is None.
- `file_name` (`str`): Default value is None.
- `expiry_time` (`~datetime.datetime`): Default value is None.
- `language` (`str`): Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Document`: Document, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_document"></a>

#### get\_document

```python
def get_document(identifier, **kwargs)
```

Get specific document.

Return a specific document.

**Arguments**:

- `identifier` (`str`): Document's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Document`: Document, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_document_data"></a>

#### update\_document\_data

```python
def update_document_data(identifier, body, **kwargs)
```

Update a document's data.

Update file name, expiry time, or move to another collection, etc.

**Arguments**:

- `identifier` (`str`): Document's identifier.
- `body` (`~affinda.models.DocumentUpdate`): Document data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Document`: Document, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_document"></a>

#### delete\_document

```python
def delete_document(identifier, **kwargs)
```

Delete a document.

Deletes the specified document from the database.

**Arguments**:

- `identifier` (`str`): Document's identifier.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_tags"></a>

#### get\_all\_tags

```python
def get_all_tags(limit=300, offset=None, workspace=None, **kwargs)
```

Get list of all tags.

Returns your tags.

**Arguments**:

- `limit` (`int`): The numbers of results to return. Default value is 300.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
Default value is None.
- `workspace` (`str`): Filter by workspace. Default value is None.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`list[~affinda.models.Tag]`: list of Tag, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_tag"></a>

#### create\_tag

```python
def create_tag(body, **kwargs)
```

Create a tag.

Create a tag.

**Arguments**:

- `body` (`~affinda.models.TagCreate`): 
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Tag`: Tag, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_tag"></a>

#### get\_tag

```python
def get_tag(id, **kwargs)
```

Get specific tag.

Return a specific tag.

**Arguments**:

- `id` (`int`): Tag's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Tag`: Tag, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.update_tag_data"></a>

#### update\_tag\_data

```python
def update_tag_data(id, body, **kwargs)
```

Update an tag's data.

Update data of an tag.

**Arguments**:

- `id` (`int`): Tag's ID.
- `body` (`~affinda.models.TagUpdate`): Tag data to update.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`~affinda.models.Tag`: Tag, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_tag"></a>

#### delete\_tag

```python
def delete_tag(id, **kwargs)
```

Delete an tag.

Deletes the specified tag from the database.

**Arguments**:

- `id` (`int`): Tag's ID.
- `cls` (`callable`): A custom type or function that will be passed the direct response

**Raises**:

- `None`: ~azure.core.exceptions.HttpResponseError

**Returns**:

`None`: None, or the result of cls(response)

