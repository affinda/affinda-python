<a name="models._models"></a>

# models.\_models

<a name="models._models.Error"></a>

## Error Objects

```python
class Error(msrest.serialization.Model)
```

Error.

:keyword error_code:
:paramtype error_code: str
:keyword error_detail:
:paramtype error_detail: str

<a name="models._models.Get200ApplicationJsonPropertiesItemsItem"></a>

## Get200ApplicationJsonPropertiesItemsItem Objects

```python
class Get200ApplicationJsonPropertiesItemsItem(msrest.serialization.Model)
```

Get200ApplicationJsonPropertiesItemsItem.

All required parameters must be populated in order to send to Azure.

:keyword identifier: Required. Unique identifier for the resume. If creating a document and
left blank, one will be automatically generated.
:paramtype identifier: str
:keyword format_file: Required. The template to apply.
:paramtype format_file: str

<a name="models._models.GetAllDocumentsResults"></a>

## GetAllDocumentsResults Objects

```python
class GetAllDocumentsResults(msrest.serialization.Model)
```

GetAllDocumentsResults.

:keyword count:
:paramtype count: int
:keyword next:
:paramtype next: str
:keyword previous:
:paramtype previous: str
:keyword results:
:paramtype results: list[~affinda.models.Meta]

<a name="models._models.Location"></a>

## Location Objects

```python
class Location(msrest.serialization.Model)
```

Location.

All required parameters must be populated in order to send to Azure.

:keyword formatted:
:paramtype formatted: str
:keyword postal_code:
:paramtype postal_code: str
:keyword state:
:paramtype state: str
:keyword country:
:paramtype country: str
:keyword raw_input: Required.
:paramtype raw_input: str
:keyword street_number:
:paramtype street_number: str
:keyword street:
:paramtype street: str
:keyword apartment_number:
:paramtype apartment_number: str
:keyword city:
:paramtype city: str

<a name="models._models.Meta"></a>

## Meta Objects

```python
class Meta(msrest.serialization.Model)
```

Meta.

All required parameters must be populated in order to send to Azure.

:keyword identifier: Required. Unique identifier for the resume. If creating a document and
left blank, one will be automatically generated.
:paramtype identifier: str
:keyword file_name: Optional filename of the file.
:paramtype file_name: str
:keyword ready: Required. If true, the document has finished processing. Particularly useful if
an endpoint request specified wait=False, when polling use this variable to determine when to
stop polling.
:paramtype ready: bool
:keyword ready_dt: The datetime when the document was ready.
:paramtype ready_dt: ~datetime.datetime
:keyword failed: Required. If true, some exception was raised during processing. Check the
'error' field of the main return object.
:paramtype failed: bool
:keyword expiry_time: The date/time in ISO-8601 format when the resume will be automatically
deleted.  Defaults to no expiry.
:paramtype expiry_time: str

<a name="models._models.Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema"></a>

## Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema.

:keyword count:
:paramtype count: int
:keyword next:
:paramtype next: str
:keyword previous:
:paramtype previous: str
:keyword results:
:paramtype results: list[~affinda.models.Get200ApplicationJsonPropertiesItemsItem]

<a name="models._models.Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema"></a>

## Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema Objects

```python
class Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model)
```

Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema.

:keyword file: File as binary data blob.
:paramtype file: IO
:keyword identifier: Unique identifier for the resume. If creating a document and left blank,
one will be automatically generated.
:paramtype identifier: str
:keyword file_name: Optional filename of the file.
:paramtype file_name: str
:keyword url: URL to file to download and process.
:paramtype url: str
:keyword wait: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
:paramtype wait: bool
:keyword resume_language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for
Chinese.
:paramtype resume_language: str
:keyword expiry_time: The date/time in ISO-8601 format when the resume will be automatically
deleted.  Defaults to no expiry.
:paramtype expiry_time: str

<a name="models._models.Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema"></a>

## Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema Objects

```python
class Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model)
```

Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema.

:keyword file: File as binary data blob.
:paramtype file: IO
:keyword identifier: Unique identifier for the resume. If creating a document and left blank,
one will be automatically generated.
:paramtype identifier: str
:keyword file_name: Optional filename of the file.
:paramtype file_name: str
:keyword url: URL to file to download and process.
:paramtype url: str
:keyword resume_language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for
Chinese.
:paramtype resume_language: str
:keyword wait: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
:paramtype wait: bool
:keyword redact_headshot: Whether to redact headshot.
:paramtype redact_headshot: str
:keyword redact_personal_details: Whether to redact personal details (e.g. name, address).
:paramtype redact_personal_details: str
:keyword redact_work_details: Whether to redact work details (e.g. company names).
:paramtype redact_work_details: str
:keyword redact_education_details: Whether to redact education details (e.g. university names).
:paramtype redact_education_details: str
:keyword redact_referees: Whether to redact referee details.
:paramtype redact_referees: str
:keyword redact_locations: Whether to redact location names.
:paramtype redact_locations: str
:keyword redact_dates: Whether to redact dates.
:paramtype redact_dates: str
:keyword expiry_time: The date/time in ISO-8601 format when the resume will be automatically
deleted.  Defaults to no expiry.
:paramtype expiry_time: str

<a name="models._models.PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema"></a>

## PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema Objects

```python
class PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model)
```

PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema.

All required parameters must be populated in order to send to Azure.

:keyword file: File as binary data blob.
:paramtype file: IO
:keyword identifier: Unique identifier for the resume. If creating a document and left blank,
one will be automatically generated.
:paramtype identifier: str
:keyword file_name: Optional filename of the file.
:paramtype file_name: str
:keyword url: URL to file to download and process.
:paramtype url: str
:keyword resume_language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for
Chinese.
:paramtype resume_language: str
:keyword resume_format: Required. Identifier of the format used.
:paramtype resume_format: str
:keyword wait: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
:paramtype wait: bool

<a name="models._models.RedactedResume"></a>

## RedactedResume Objects

```python
class RedactedResume(msrest.serialization.Model)
```

RedactedResume.

All required parameters must be populated in order to send to Azure.

:keyword data: Required.
:paramtype data: ~affinda.models.RedactedResumeData
:keyword meta: Required.
:paramtype meta: ~affinda.models.Meta
:keyword error: Required.
:paramtype error: ~affinda.models.Error

<a name="models._models.RedactedResumeData"></a>

## RedactedResumeData Objects

```python
class RedactedResumeData(msrest.serialization.Model)
```

RedactedResumeData.

:keyword redacted_pdf:
:paramtype redacted_pdf: str

<a name="models._models.ReformattedResume"></a>

## ReformattedResume Objects

```python
class ReformattedResume(msrest.serialization.Model)
```

ReformattedResume.

All required parameters must be populated in order to send to Azure.

:keyword data: Required.
:paramtype data: ~affinda.models.ReformattedResumeData
:keyword meta: Required.
:paramtype meta: ~affinda.models.Meta
:keyword error: Required.
:paramtype error: ~affinda.models.Error

<a name="models._models.ReformattedResumeData"></a>

## ReformattedResumeData Objects

```python
class ReformattedResumeData(msrest.serialization.Model)
```

ReformattedResumeData.

:keyword reformatted_file:
:paramtype reformatted_file: str

<a name="models._models.RequestError"></a>

## RequestError Objects

```python
class RequestError(msrest.serialization.Model)
```

RequestError.

All required parameters must be populated in order to send to Azure.

:keyword detail: Required.
:paramtype detail: str
:keyword status_code: Required.
:paramtype status_code: int

<a name="models._models.Resume"></a>

## Resume Objects

```python
class Resume(msrest.serialization.Model)
```

Resume.

All required parameters must be populated in order to send to Azure.

:keyword data: Required.
:paramtype data: ~affinda.models.ResumeData
:keyword meta: Required.
:paramtype meta: ~affinda.models.Meta
:keyword error: Required.
:paramtype error: ~affinda.models.Error

<a name="models._models.ResumeData"></a>

## ResumeData Objects

```python
class ResumeData(msrest.serialization.Model)
```

ResumeData.

:keyword name:
:paramtype name: ~affinda.models.ResumeDataName
:keyword phone_numbers:
:paramtype phone_numbers: list[str]
:keyword websites:
:paramtype websites: list[str]
:keyword emails:
:paramtype emails: list[str]
:keyword date_of_birth:
:paramtype date_of_birth: str
:keyword location:
:paramtype location: ~affinda.models.Location
:keyword objective:
:paramtype objective: str
:keyword languages:
:paramtype languages: list[str]
:keyword summary:
:paramtype summary: str
:keyword total_years_experience:
:paramtype total_years_experience: int
:keyword head_shot: base64 encoded string.
:paramtype head_shot: bytearray
:keyword education:
:paramtype education: list[~affinda.models.ResumeDataEducationItem]
:keyword profession: Prediction of the candidate's profession based on recent work experience.
:paramtype profession: str
:keyword linkedin: Linkedin account associated with the candidate.
:paramtype linkedin: str
:keyword work_experience:
:paramtype work_experience: list[~affinda.models.ResumeDataWorkExperienceItem]
:keyword skills:
:paramtype skills: list[~affinda.models.ResumeDataSkillsItem]
:keyword certifications:
:paramtype certifications: list[str]
:keyword publications:
:paramtype publications: list[str]
:keyword referees:
:paramtype referees: list[~affinda.models.ResumeDataRefereesItem]
:keyword sections:
:paramtype sections: list[~affinda.models.ResumeDataSectionsItem]
:keyword is_resume_probability: Probability that the given document is a resume. Values below
30 suggest that the resume is not a resume.
:paramtype is_resume_probability: int
:keyword raw_text: All of the raw text of the parsed resume, example is shortened for
readiblity.
:paramtype raw_text: str

<a name="models._models.ResumeDataEducationItem"></a>

## ResumeDataEducationItem Objects

```python
class ResumeDataEducationItem(msrest.serialization.Model)
```

ResumeDataEducationItem.

:keyword organization:
:paramtype organization: str
:keyword accreditation:
:paramtype accreditation: ~affinda.models.ResumeDataEducationItemAccreditation
:keyword grade:
:paramtype grade: ~affinda.models.ResumeDataEducationItemGrade
:keyword location:
:paramtype location: ~affinda.models.Location
:keyword dates:
:paramtype dates: ~affinda.models.ResumeDataEducationItemDates

<a name="models._models.ResumeDataEducationItemAccreditation"></a>

## ResumeDataEducationItemAccreditation Objects

```python
class ResumeDataEducationItemAccreditation(msrest.serialization.Model)
```

ResumeDataEducationItemAccreditation.

:keyword education:
:paramtype education: str
:keyword input_str:
:paramtype input_str: str
:keyword match_str:
:paramtype match_str: str
:keyword education_level:
:paramtype education_level: str

<a name="models._models.ResumeDataEducationItemDates"></a>

## ResumeDataEducationItemDates Objects

```python
class ResumeDataEducationItemDates(msrest.serialization.Model)
```

ResumeDataEducationItemDates.

:keyword completion_date:
:paramtype completion_date: ~datetime.date
:keyword is_current:
:paramtype is_current: bool
:keyword start_date:
:paramtype start_date: ~datetime.date

<a name="models._models.ResumeDataEducationItemGrade"></a>

## ResumeDataEducationItemGrade Objects

```python
class ResumeDataEducationItemGrade(msrest.serialization.Model)
```

ResumeDataEducationItemGrade.

:keyword raw:
:paramtype raw: str
:keyword metric:
:paramtype metric: str
:keyword value:
:paramtype value: str

<a name="models._models.ResumeDataName"></a>

## ResumeDataName Objects

```python
class ResumeDataName(msrest.serialization.Model)
```

ResumeDataName.

:keyword raw:
:paramtype raw: str
:keyword first:
:paramtype first: str
:keyword last:
:paramtype last: str
:keyword middle:
:paramtype middle: str
:keyword title:
:paramtype title: str

<a name="models._models.ResumeDataRefereesItem"></a>

## ResumeDataRefereesItem Objects

```python
class ResumeDataRefereesItem(msrest.serialization.Model)
```

ResumeDataRefereesItem.

:keyword name:
:paramtype name: str
:keyword text:
:paramtype text: str
:keyword email:
:paramtype email: str
:keyword number:
:paramtype number: str

<a name="models._models.ResumeDataSectionsItem"></a>

## ResumeDataSectionsItem Objects

```python
class ResumeDataSectionsItem(msrest.serialization.Model)
```

ResumeDataSectionsItem.

:keyword section_type:
:paramtype section_type: str
:keyword bbox:
:paramtype bbox: list[float]
:keyword page_index:
:paramtype page_index: int
:keyword text:
:paramtype text: str

<a name="models._models.ResumeDataSkillsItem"></a>

## ResumeDataSkillsItem Objects

```python
class ResumeDataSkillsItem(msrest.serialization.Model)
```

ResumeDataSkillsItem.

:keyword name:
:paramtype name: str
:keyword last_used:
:paramtype last_used: str
:keyword number_of_months:
:paramtype number_of_months: int
:keyword type:
:paramtype type: str
:keyword sources:
:paramtype sources: list[~affinda.models.ResumeDataSkillsPropertiesItemsItem]

<a name="models._models.ResumeDataSkillsPropertiesItemsItem"></a>

## ResumeDataSkillsPropertiesItemsItem Objects

```python
class ResumeDataSkillsPropertiesItemsItem(msrest.serialization.Model)
```

ResumeDataSkillsPropertiesItemsItem.

:keyword section:
:paramtype section: str
:keyword position:
:paramtype position: int

<a name="models._models.ResumeDataWorkExperienceItem"></a>

## ResumeDataWorkExperienceItem Objects

```python
class ResumeDataWorkExperienceItem(msrest.serialization.Model)
```

ResumeDataWorkExperienceItem.

:keyword job_title:
:paramtype job_title: str
:keyword organization:
:paramtype organization: str
:keyword location:
:paramtype location: ~affinda.models.Location
:keyword job_description:
:paramtype job_description: str
:keyword dates:
:paramtype dates: ~affinda.models.ResumeDataWorkExperienceItemDates

<a name="models._models.ResumeDataWorkExperienceItemDates"></a>

## ResumeDataWorkExperienceItemDates Objects

```python
class ResumeDataWorkExperienceItemDates(msrest.serialization.Model)
```

ResumeDataWorkExperienceItemDates.

:keyword start_date:
:paramtype start_date: ~datetime.date
:keyword end_date:
:paramtype end_date: ~datetime.date
:keyword months_in_position:
:paramtype months_in_position: int
:keyword is_current:
:paramtype is_current: bool

