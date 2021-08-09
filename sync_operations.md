<a name="_affinda_api"></a>

# \_affinda\_api

<a name="_affinda_api.AffindaAPI"></a>

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

<a name="operations._affinda_api_operations"></a>

# operations.\_affinda\_api\_operations

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin"></a>

## AffindaAPIOperationsMixin Objects

```python
class AffindaAPIOperationsMixin(object)
```

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_resumes"></a>

#### get\_all\_resumes

```python
 | get_all_resumes(**kwargs)
```

Gets summary information for all resumes of a user.

Returns all the resume summaries for that user, limited to 300 per page.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

`~affinda_python.models.Paths1Vwy7YkResumesGetResponses200ContentApplicationJsonSchema`: Paths1Vwy7YkResumesGetResponses200ContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_resume"></a>

#### create\_resume

```python
 | create_resume(file=None, identifier=None, file_name=None, url=None, wait=None, resume_language=None, expiry_time=None, **kwargs)
```

Uploads a resume for parsing.

Uploads a resume for parsing.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/resumes/{identifier} <#operation/getResume>`_ endpoint to check processing status and
retrieve results.

**Arguments**:

completed. If False, will return an identifier, which can be polled at the GET endpoint until
processing is complete.
:keyword callable cls: A custom type or function that will be passed the direct response
- `file` (`IO`): File as binary data blob.
- `identifier` (`str`): 
- `file_name` (`str`): 
- `url` (`str`): 
- `wait` (`bool`): If true (default), will return a response only after resume processing has
- `resume_language` (`str`): 
- `expiry_time` (`str`): 

**Returns**:

`~affinda_python.models.PathsWt95EfResumesPostResponses201ContentApplicationJsonSchema`: PathsWt95EfResumesPostResponses201ContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_resume"></a>

#### get\_resume

```python
 | get_resume(identifier, **kwargs)
```

Gets parse results for a specific resume.

Returns all the parse results for that resume if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the resume via the `/resumes
<#operation/createResume>`_ endpoint.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda_python.models.Resume or`: Resume or ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_resume"></a>

#### delete\_resume

```python
 | delete_resume(identifier, **kwargs)
```

Deletes a resume.

Deletes the specified resume from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Resume identifier.

**Returns**:

`~affinda_python.models.ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema or`: ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_redacted_resumes"></a>

#### get\_all\_redacted\_resumes

```python
 | get_all_redacted_resumes(**kwargs)
```

Gets summary information for all redacted resumes of a user.

Returns all the redacted resume information for that resume.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

Paths1My65ZdRedactedResumesGetResponses200ContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_redacted_resume"></a>

#### create\_redacted\_resume

```python
 | create_redacted_resume(file=None, identifier=None, file_name=None, url=None, resume_language=None, redact_headshot=True, redact_personal_details=True, redact_work_details=True, redact_education_details=True, redact_referees=True, redact_locations=True, redact_dates=True, expiry_time=None, **kwargs)
```

Uploads a resume for redacting.

Uploads a resume for redacting.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/redacted_resumes/{identifier} <#operation/getRedactedResume>`_ endpoint to check processing
status and retrieve results.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `file` (`IO`): File as binary data blob.
- `identifier` (`str`): 
- `file_name` (`str`): 
- `url` (`str`): 
- `resume_language` (`str`): 
- `redact_headshot` (`bool`): Whether to redact headshot.
- `redact_personal_details` (`bool`): Whether to redact personal details (e.g. name, address).
- `redact_work_details` (`bool`): Whether to redact work details (e.g. company names).
- `redact_education_details` (`bool`): Whether to redact education details (e.g. university names).
- `redact_referees` (`bool`): Whether to redact referee details.
- `redact_locations` (`bool`): Whether to redact location names.
- `redact_dates` (`bool`): Whether to redact dates.
- `expiry_time` (`str`): 

**Returns**:

Paths1VouiekRedactedResumesPostResponses201ContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_redacted_resume"></a>

#### get\_redacted\_resume

```python
 | get_redacted_resume(identifier, **kwargs)
```

Gets redaction results for a specific resume.

Returns all the redaction results for that resume if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the resume via the
`/redacted_resumes <#operation/createRedactedResume>`_ endpoint.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda_python.models.RedactedDocument or`: RedactedDocument or ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_redacted_resume"></a>

#### delete\_redacted\_resume

```python
 | delete_redacted_resume(identifier, **kwargs)
```

Deletes a redacted resume.

Deletes the specified resume from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda_python.models.ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema or`: ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_resume_formats"></a>

#### get\_all\_resume\_formats

```python
 | get_all_resume_formats(**kwargs)
```

Gets summary information for all resume formats of a user.

Returns all the resume formats.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_reformatted_resumes"></a>

#### get\_all\_reformatted\_resumes

```python
 | get_all_reformatted_resumes(**kwargs)
```

Gets summary information for all reformatted resumes of a user.

Returns all the reformatted resume information for that resume.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

Paths4Fg3YrReformattedResumesGetResponses200ContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_reformatted_resume"></a>

#### create\_reformatted\_resume

```python
 | create_reformatted_resume(resume_format, file=None, identifier=None, file_name=None, url=None, resume_language=None, **kwargs)
```

Uploads a resume for reformatting.

Uploads a resume for reformatting.
When successful, returns an ``identifier`` in the response for subsequent use with the
`/reformatted_resumes/{identifier} <#operation/getReformattedResume>`_ endpoint to check
processing status and retrieve results.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `resume_format` (`str`): 
- `file` (`IO`): File as binary data blob.
- `identifier` (`str`): 
- `file_name` (`str`): 
- `url` (`str`): URL to file to download and process.
- `resume_language` (`str`): 

**Returns**:

Paths1Wyf6PlReformattedResumesPostResponses201ContentApplicationJsonSchema or

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_reformatted_resume"></a>

#### get\_reformatted\_resume

```python
 | get_reformatted_resume(identifier, **kwargs)
```

Gets reformatting results for a specific resume.

Returns all the reformatting results for that resume if processing is completed.
The ``identifier`` is the unique ID returned after POST-ing the resume via the
`/reformatted_resumes <#operation/createReformattedResume>`_ endpoint.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda_python.models.ReformattedDocument or`: ReformattedDocument or ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema

<a name="operations._affinda_api_operations.AffindaAPIOperationsMixin.delete_reformatted_resume"></a>

#### delete\_reformatted\_resume

```python
 | delete_reformatted_resume(identifier, **kwargs)
```

Deletes a reformatted resume.

Deletes the specified resume from the database.

**Arguments**:

:keyword callable cls: A custom type or function that will be passed the direct response
- `identifier` (`str`): Document identifier.

**Returns**:

`~affinda_python.models.ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema or`: ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema or

