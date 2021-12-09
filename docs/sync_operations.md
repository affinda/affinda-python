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
- `base_url` (`str`): Service URL. Default value is 'https://api.affinda.com/v1'.

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

Get list of all resumes.

Returns all the resume summaries for that user, limited to 300 per page.

:keyword callable cls: A custom type or function that will be passed the direct response

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
def get_all_redacted_resumes(**kwargs)
```

Get list of all redacted resumes.

Returns all the redacted resume information for that resume.

:keyword callable cls: A custom type or function that will be passed the direct response

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
def get_all_resume_formats(**kwargs)
```

Get list of all resume formats.

Returns all the resume formats.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

`~affinda.models.Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema or`: Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema or RequestError,

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_reformatted_resumes"></a>

#### get\_all\_reformatted\_resumes

```python
def get_all_reformatted_resumes(**kwargs)
```

Get list of all reformatted resumes.

Returns all the reformatted resume information for that resume.

:keyword callable cls: A custom type or function that will be passed the direct response

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

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.get_all_invoices"></a>

#### get\_all\_invoices

```python
def get_all_invoices(**kwargs)
```

Get list of all invoices.

Returns all the invoice summaries for that user, limited to 300 per page.

:keyword callable cls: A custom type or function that will be passed the direct response

**Returns**:

`~affinda.models.GetAllInvoicesResults or ~affinda.models.RequestError`: GetAllInvoicesResults or RequestError, or the result of cls(response)

<a id="operations._affinda_api_operations.AffindaAPIOperationsMixin.create_invoice"></a>

#### create\_invoice

```python
def create_invoice(file=None, identifier=None, file_name=None, url=True, wait=True, language=None, expiry_time=None, **kwargs)
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
- `url` (`bool`): URL to file to download and process.
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

