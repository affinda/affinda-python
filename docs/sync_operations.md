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
- `limit` (`int`): The numbers of documents to return, defaults to 300.
- `offset` (`int`): The number of documents to skip before starting to collect the result set.
- `base_url` (`str`): Service URL

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
def get_all_resumes(**kwargs)
```

Gets list of all resumes.

Returns all the resume summaries for that user, limited to 300 per page.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

`~affinda.models.GetAllDocumentsResults or ~affinda.models.RequestError`: GetAllDocumentsResults or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume"></a>

#### create\_resume

```python
def create_resume(file=None, identifier=None, file_name=None, url=None, wait=True, resume_language=None, expiry_time=None, **kwargs)
```

Uploads a resume for parsing.

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
- `resume_language` (`str`): 
- `expiry_time` (`str`): 

**Returns**:

`~affinda.models.Resume or ~affinda.models.RequestError`: Resume or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume"></a>

#### get\_resume

```python
def get_resume(identifier, **kwargs)
```

Gets parse results for a specific resume.

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

Deletes a resume.

Deletes the specified resume from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Resume identifier.

**Returns**:

`~affinda.models.RequestError or None`: RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_redacted_resumes"></a>

#### get\_all\_redacted\_resumes

```python
def get_all_redacted_resumes(**kwargs)
```

Gets list of all redacted resumes.

Returns all the redacted resume information for that resume.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

`~affinda.models.GetAllDocumentsResults or ~affinda.models.RequestError`: GetAllDocumentsResults or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_redacted_resume"></a>

#### create\_redacted\_resume

```python
def create_redacted_resume(file=None, identifier=None, file_name=None, url=None, resume_language=None, wait=True, redact_headshot="true", redact_personal_details="true", redact_work_details="true", redact_education_details="true", redact_referees="true", redact_locations="true", redact_dates="true", expiry_time=None, **kwargs)
```

Uploads a resume for redacting.

Uploads a resume for redacting.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `file` (`IO`): 
- `identifier` (`str`): 
- `file_name` (`str`): 
- `url` (`str`): 
- `resume_language` (`str`): 
- `wait` (`bool`): 
- `redact_headshot` (`str`): Whether to redact headshot.
- `redact_personal_details` (`str`): Whether to redact personal details (e.g. name, address).
- `redact_work_details` (`str`): Whether to redact work details (e.g. company names).
- `redact_education_details` (`str`): Whether to redact education details (e.g. university names).
- `redact_referees` (`str`): Whether to redact referee details.
- `redact_locations` (`str`): Whether to redact location names.
- `redact_dates` (`str`): Whether to redact dates.
- `expiry_time` (`str`): 

**Returns**:

`~affinda.models.RedactedResume or ~affinda.models.RequestError`: RedactedResume or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_redacted_resume"></a>

#### get\_redacted\_resume

```python
def get_redacted_resume(identifier, **kwargs)
```

Gets redaction results for a specific resume.

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

Deletes a redacted resume.

Deletes the specified resume from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.RequestError or None`: RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_resume_formats"></a>

#### get\_all\_resume\_formats

```python
def get_all_resume_formats(**kwargs)
```

Gets list of all resume formats.

Returns all the resume formats.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

`~affinda.models.Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema or`: Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema or RequestError,

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_reformatted_resumes"></a>

#### get\_all\_reformatted\_resumes

```python
def get_all_reformatted_resumes(**kwargs)
```

Gets list of all reformatted resumes.

Returns all the reformatted resume information for that resume.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

`~affinda.models.GetAllDocumentsResults or ~affinda.models.RequestError`: GetAllDocumentsResults or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_reformatted_resume"></a>

#### create\_reformatted\_resume

```python
def create_reformatted_resume(resume_format, file=None, identifier=None, file_name=None, url=None, resume_language=None, wait=True, **kwargs)
```

Uploads a resume for reformatting.

Uploads a resume for reformatting.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `resume_format` (`str`): 
- `file` (`IO`): 
- `identifier` (`str`): 
- `file_name` (`str`): 
- `url` (`str`): 
- `resume_language` (`str`): 
- `wait` (`bool`): 

**Returns**:

`~affinda.models.ReformattedResume or ~affinda.models.RequestError`: ReformattedResume or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_reformatted_resume"></a>

#### get\_reformatted\_resume

```python
def get_reformatted_resume(identifier, **kwargs)
```

Gets reformatting results for a specific resume.

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

Deletes a reformatted resume.

Deletes the specified resume from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda.models.RequestError or None`: RequestError, or the result of cls(response)

