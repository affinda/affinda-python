<a name="models._models"></a>

# models.\_models

<a name="models._models.Components10Bc157ResponsesConversionerrorContentApplicationJsonSchema"></a>

## Components10Bc157ResponsesConversionerrorContentApplicationJsonSchema Objects

```python
class Components10Bc157ResponsesConversionerrorContentApplicationJsonSchema(msrest.serialization.Model)
```

Components10Bc157ResponsesConversionerrorContentApplicationJsonSchema.

**Arguments**:

- `file_for_conversion` (`str`): 

<a name="models._models.ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema"></a>

## ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema Objects

```python
class ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema(msrest.serialization.Model)
```

ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema.

**Arguments**:

- `detail` (`str`): 
- `status_code` (`int`): 

<a name="models._models.ComponentsP4H6CrResponses404ErrorContentApplicationJsonSchema"></a>

## ComponentsP4H6CrResponses404ErrorContentApplicationJsonSchema Objects

```python
class ComponentsP4H6CrResponses404ErrorContentApplicationJsonSchema(msrest.serialization.Model)
```

ComponentsP4H6CrResponses404ErrorContentApplicationJsonSchema.

**Arguments**:

- `detail` (`str`): 
- `status_code` (`int`): 

<a name="models._models.Error"></a>

## Error Objects

```python
class Error(msrest.serialization.Model)
```

Error.

All required parameters must be populated in order to send to Azure.

**Arguments**:

- `error_code` (`int`): Required.
- `error_detail` (`str`): Required.

<a name="models._models.Get200ApplicationJsonPropertiesItemsItem"></a>

## Get200ApplicationJsonPropertiesItemsItem Objects

```python
class Get200ApplicationJsonPropertiesItemsItem(msrest.serialization.Model)
```

Get200ApplicationJsonPropertiesItemsItem.

All required parameters must be populated in order to send to Azure.

**Arguments**:

- `identifier` (`str`): Required.
- `format_file` (`str`): Required.

<a name="models._models.Location"></a>

## Location Objects

```python
class Location(msrest.serialization.Model)
```

Location.

All required parameters must be populated in order to send to Azure.

**Arguments**:

- `formatted` (`str`): 
- `postal_code` (`str`): 
- `state` (`str`): 
- `country` (`str`): 
- `raw_input` (`str`): Required.
- `street_number` (`str`): 
- `street` (`str`): 
- `apartment_number` (`str`): 
- `city` (`str`): 

<a name="models._models.Meta"></a>

## Meta Objects

```python
class Meta(msrest.serialization.Model)
```

Meta.

All required parameters must be populated in order to send to Azure.

**Arguments**:

blank, one will be automatically generated.
an endpoint request specified wait=False, when polling use this variable to determine when to
stop polling.
'error' field of the main return object.
automatically deleted.  Defaults to no expiry.
- `identifier` (`str`): Required. Unique identifier for the resume. If creating a document and left
- `file_name` (`str`): Optional filename of the file.
- `ready` (`bool`): Required. If true, the document has finished processing. Particularly useful if
- `ready_dt` (`~datetime.datetime`): Required. The datetime when the document was ready.
- `failed` (`bool`): Required. If true, some exception was raised during processing. Check the
- `user` (`~affinda_python.models.User`): Required.
- `expiry_time` (`str`): Required. The date/time in ISO-8601 format when the resume will be

<a name="models._models.Paths1My65ZdRedactedResumesGetResponses200ContentApplicationJsonSchema"></a>

## Paths1My65ZdRedactedResumesGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths1My65ZdRedactedResumesGetResponses200ContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths1My65ZdRedactedResumesGetResponses200ContentApplicationJsonSchema.

**Arguments**:

- `count` (`int`): 
- `next` (`str`): 
- `previous` (`str`): 
- `results` (`list[~affinda_python.models.Meta]`): 

<a name="models._models.Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema"></a>

## Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema.

**Arguments**:

- `count` (`int`): 
- `next` (`str`): 
- `previous` (`str`): 
- `results` (`list[~affinda_python.models.Get200ApplicationJsonPropertiesItemsItem]`): 

<a name="models._models.Paths1VouiekRedactedResumesPostResponses201ContentApplicationJsonSchema"></a>

## Paths1VouiekRedactedResumesPostResponses201ContentApplicationJsonSchema Objects

```python
class Paths1VouiekRedactedResumesPostResponses201ContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths1VouiekRedactedResumesPostResponses201ContentApplicationJsonSchema.

**Arguments**:

- `file_name` (`str`): 
- `identifier` (`str`): 
- `redact_headshot` (`bool`): 
- `redact_personal_details` (`bool`): 
- `redact_work_details` (`bool`): 
- `redact_education_details` (`bool`): 
- `redact_referees` (`bool`): 
- `redact_locations` (`bool`): 
- `redact_dates` (`bool`): 

<a name="models._models.Paths1Vwy7YkResumesGetResponses200ContentApplicationJsonSchema"></a>

## Paths1Vwy7YkResumesGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths1Vwy7YkResumesGetResponses200ContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths1Vwy7YkResumesGetResponses200ContentApplicationJsonSchema.

**Arguments**:

- `count` (`int`): 
- `next` (`str`): 
- `previous` (`str`): 
- `results` (`list[~affinda_python.models.Meta]`): 

<a name="models._models.Paths1Wyf6PlReformattedResumesPostResponses201ContentApplicationJsonSchema"></a>

## Paths1Wyf6PlReformattedResumesPostResponses201ContentApplicationJsonSchema Objects

```python
class Paths1Wyf6PlReformattedResumesPostResponses201ContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths1Wyf6PlReformattedResumesPostResponses201ContentApplicationJsonSchema.

**Arguments**:

will be automatically generated.
- `file_name` (`str`): Optional filename of the file.
- `identifier` (`str`): Unique identifier for the resume. If creating a document and left blank, one
- `resume_format` (`str`): Identifier of the format used.

<a name="models._models.Paths4Fg3YrReformattedResumesGetResponses200ContentApplicationJsonSchema"></a>

## Paths4Fg3YrReformattedResumesGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths4Fg3YrReformattedResumesGetResponses200ContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths4Fg3YrReformattedResumesGetResponses200ContentApplicationJsonSchema.

**Arguments**:

- `count` (`int`): 
- `next` (`str`): 
- `previous` (`str`): 
- `results` (`list[~affinda_python.models.Meta]`): 

<a name="models._models.Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema"></a>

## Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema Objects

```python
class Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model)
```

Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema.

**Arguments**:

will be automatically generated.
completed. If False, will return an identifier, which can be polled at the GET endpoint until
processing is complete.
Chinese.
deleted.  Defaults to no expiry.
- `file` (`IO`): File as binary data blob.
- `identifier` (`str`): Unique identifier for the resume. If creating a document and left blank, one
- `file_name` (`str`): Optional filename of the file.
- `url` (`str`): URL to file to download and process.
- `wait` (`bool`): If true (default), will return a response only after resume processing has
- `resume_language` (`str`): Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for
- `expiry_time` (`str`): The date/time in ISO-8601 format when the resume will be automatically

<a name="models._models.Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema"></a>

## Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema Objects

```python
class Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model)
```

Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema.

**Arguments**:

will be automatically generated.
Chinese.
deleted.  Defaults to no expiry.
- `file` (`IO`): File as binary data blob.
- `identifier` (`str`): Unique identifier for the resume. If creating a document and left blank, one
- `file_name` (`str`): Optional filename of the file.
- `url` (`str`): URL to file to download and process.
- `resume_language` (`str`): Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for
- `redact_headshot` (`bool`): Whether to redact headshot.
- `redact_personal_details` (`bool`): Whether to redact personal details (e.g. name, address).
- `redact_work_details` (`bool`): Whether to redact work details (e.g. company names).
- `redact_education_details` (`bool`): Whether to redact education details (e.g. university names).
- `redact_referees` (`bool`): Whether to redact referee details.
- `redact_locations` (`bool`): Whether to redact location names.
- `redact_dates` (`bool`): Whether to redact dates.
- `expiry_time` (`str`): The date/time in ISO-8601 format when the resume will be automatically

<a name="models._models.PathsWt95EfResumesPostResponses201ContentApplicationJsonSchema"></a>

## PathsWt95EfResumesPostResponses201ContentApplicationJsonSchema Objects

```python
class PathsWt95EfResumesPostResponses201ContentApplicationJsonSchema(msrest.serialization.Model)
```

PathsWt95EfResumesPostResponses201ContentApplicationJsonSchema.

**Arguments**:

will be automatically generated.
- `identifier` (`str`): Unique identifier for the resume. If creating a document and left blank, one
- `file_name` (`str`): Optional filename of the file.

<a name="models._models.PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema"></a>

## PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema Objects

```python
class PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model)
```

PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema.

All required parameters must be populated in order to send to Azure.

**Arguments**:

will be automatically generated.
Chinese.
- `file` (`IO`): File as binary data blob.
- `identifier` (`str`): Unique identifier for the resume. If creating a document and left blank, one
- `file_name` (`str`): Optional filename of the file.
- `url` (`str`): URL to file to download and process.
- `resume_language` (`str`): Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for
- `resume_format` (`str`): Required. Identifier of the format used.

<a name="models._models.RedactedDocument"></a>

## RedactedDocument Objects

```python
class RedactedDocument(msrest.serialization.Model)
```

RedactedDocument.

**Arguments**:

- `data` (`~affinda_python.models.RedactedDocumentData`): 
- `meta` (`~affinda_python.models.Meta`): 
- `error` (`~affinda_python.models.Error`): 

<a name="models._models.RedactedDocumentData"></a>

## RedactedDocumentData Objects

```python
class RedactedDocumentData(msrest.serialization.Model)
```

RedactedDocumentData.

**Arguments**:

- `redacted_pdf` (`str`): 

<a name="models._models.ReformattedDocument"></a>

## ReformattedDocument Objects

```python
class ReformattedDocument(msrest.serialization.Model)
```

ReformattedDocument.

**Arguments**:

- `data` (`~affinda_python.models.ReformattedDocumentData`): 
- `meta` (`~affinda_python.models.Meta`): 
- `error` (`~affinda_python.models.Error`): 

<a name="models._models.ReformattedDocumentData"></a>

## ReformattedDocumentData Objects

```python
class ReformattedDocumentData(msrest.serialization.Model)
```

ReformattedDocumentData.

**Arguments**:

- `reformatted_file` (`str`): 

<a name="models._models.Resume"></a>

## Resume Objects

```python
class Resume(msrest.serialization.Model)
```

Resume.

**Arguments**:

- `data` (`~affinda_python.models.ResumeData`): 
- `meta` (`~affinda_python.models.Meta`): 
- `error` (`~affinda_python.models.Error`): 

<a name="models._models.ResumeData"></a>

## ResumeData Objects

```python
class ResumeData(msrest.serialization.Model)
```

ResumeData.

**Arguments**:

suggest that the resume is not a resume.
- `name` (`~affinda_python.models.ResumeDataName`): 
- `phone_numbers` (`list[str]`): 
- `websites` (`list[str]`): 
- `emails` (`list[str]`): 
- `date_of_birth` (`str`): 
- `location` (`~affinda_python.models.Location`): 
- `objective` (`str`): 
- `languages` (`list[str]`): 
- `summary` (`str`): 
- `total_years_experience` (`int`): 
- `head_shot` (`IO`): base64 encoded string.
- `education` (`list[~affinda_python.models.ResumeDataEducationItem]`): 
- `work_experience` (`list[~affinda_python.models.ResumeDataWorkExperienceItem]`): 
- `skills` (`list[str]`): 
- `skills_details` (`list[~affinda_python.models.ResumeDataSkillsDetailsItem]`): 
- `certifications` (`list[str]`): 
- `publications` (`list[str]`): 
- `referees` (`list[~affinda_python.models.ResumeDataRefereesItem]`): 
- `sections` (`list[~affinda_python.models.ResumeDataSectionsItem]`): 
- `is_resume_probability` (`int`): Probability that the given document is a resume. Values below 30

<a name="models._models.ResumeDataEducationItem"></a>

## ResumeDataEducationItem Objects

```python
class ResumeDataEducationItem(msrest.serialization.Model)
```

ResumeDataEducationItem.

**Arguments**:

- `organization` (`str`): 
- `accreditation` (`~affinda_python.models.ResumeDataEducationItemAccreditation`): 
- `grade` (`~affinda_python.models.ResumeDataEducationItemGrade`): 
- `location` (`~affinda_python.models.Location`): 
- `dates` (`~affinda_python.models.ResumeDataEducationItemDates`): 

<a name="models._models.ResumeDataEducationItemAccreditation"></a>

## ResumeDataEducationItemAccreditation Objects

```python
class ResumeDataEducationItemAccreditation(msrest.serialization.Model)
```

ResumeDataEducationItemAccreditation.

**Arguments**:

- `education` (`str`): 
- `input_str` (`str`): 
- `match_str` (`str`): 
- `education_level` (`str`): 

<a name="models._models.ResumeDataEducationItemDates"></a>

## ResumeDataEducationItemDates Objects

```python
class ResumeDataEducationItemDates(msrest.serialization.Model)
```

ResumeDataEducationItemDates.

**Arguments**:

- `completion_date` (`~datetime.date`): 
- `is_current` (`bool`): 
- `start_date` (`~datetime.date`): 

<a name="models._models.ResumeDataEducationItemGrade"></a>

## ResumeDataEducationItemGrade Objects

```python
class ResumeDataEducationItemGrade(msrest.serialization.Model)
```

ResumeDataEducationItemGrade.

**Arguments**:

- `raw` (`str`): 
- `metric` (`str`): 
- `value` (`str`): 

<a name="models._models.ResumeDataName"></a>

## ResumeDataName Objects

```python
class ResumeDataName(msrest.serialization.Model)
```

ResumeDataName.

**Arguments**:

- `raw` (`str`): 
- `first` (`str`): 
- `last` (`str`): 
- `middle` (`str`): 
- `title` (`str`): 

<a name="models._models.ResumeDataRefereesItem"></a>

## ResumeDataRefereesItem Objects

```python
class ResumeDataRefereesItem(msrest.serialization.Model)
```

ResumeDataRefereesItem.

**Arguments**:

- `name` (`str`): 
- `text` (`str`): 
- `email` (`str`): 
- `number` (`str`): 

<a name="models._models.ResumeDataSectionsItem"></a>

## ResumeDataSectionsItem Objects

```python
class ResumeDataSectionsItem(msrest.serialization.Model)
```

ResumeDataSectionsItem.

**Arguments**:

- `section_type` (`str`): 
- `bbox` (`list[float]`): 
- `page_index` (`int`): 
- `text` (`str`): 

<a name="models._models.ResumeDataSkillsDetailsItem"></a>

## ResumeDataSkillsDetailsItem Objects

```python
class ResumeDataSkillsDetailsItem(msrest.serialization.Model)
```

ResumeDataSkillsDetailsItem.

**Arguments**:

- `name` (`str`): 
- `last_used` (`str`): 
- `number_of_months` (`int`): 
- `type` (`str`): 
- `sources` (`list[~affinda_python.models.ResumeDataSkillsDetailsPropertiesItemsItem]`): 

<a name="models._models.ResumeDataSkillsDetailsPropertiesItemsItem"></a>

## ResumeDataSkillsDetailsPropertiesItemsItem Objects

```python
class ResumeDataSkillsDetailsPropertiesItemsItem(msrest.serialization.Model)
```

ResumeDataSkillsDetailsPropertiesItemsItem.

**Arguments**:

- `section` (`str`): 
- `position` (`int`): 

<a name="models._models.ResumeDataWorkExperienceItem"></a>

## ResumeDataWorkExperienceItem Objects

```python
class ResumeDataWorkExperienceItem(msrest.serialization.Model)
```

ResumeDataWorkExperienceItem.

**Arguments**:

- `job_title` (`str`): 
- `organization` (`str`): 
- `location` (`~affinda_python.models.Location`): 
- `job_description` (`str`): 
- `dates` (`~affinda_python.models.ResumeDataWorkExperienceItemDates`): 

<a name="models._models.ResumeDataWorkExperienceItemDates"></a>

## ResumeDataWorkExperienceItemDates Objects

```python
class ResumeDataWorkExperienceItemDates(msrest.serialization.Model)
```

ResumeDataWorkExperienceItemDates.

**Arguments**:

- `start_date` (`~datetime.date`): 
- `end_date` (`~datetime.date`): 
- `months_in_position` (`int`): 
- `is_current` (`bool`): 

<a name="models._models.User"></a>

## User Objects

```python
class User(msrest.serialization.Model)
```

User.

**Arguments**:

- `document_count` (`int`): 
- `redacted_document_count` (`int`): 
- `reformatted_resume_count` (`int`): 
- `parsing_credits` (`int`): 
- `redaction_credits` (`int`): 
- `reformatting_credits` (`int`): 

