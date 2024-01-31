<a id="models._models"></a>

# models.\_models

<a id="models._models.Accreditation"></a>

## Accreditation Objects

```python
class Accreditation(msrest.serialization.Model)
```

Accreditation.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar education:
:vartype education: str
:ivar input_str:
:vartype input_str: str
:ivar match_str:
:vartype match_str: str
:ivar education_level:
:vartype education_level: str

<a id="models._models.Accreditation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `education`: 

<a id="models._models.Annotation"></a>

## Annotation Objects

```python
class Annotation(msrest.serialization.Model)
```

Annotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int

<a id="models._models.Annotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.

<a id="models._models.AnnotationBase"></a>

## AnnotationBase Objects

```python
class AnnotationBase(msrest.serialization.Model)
```

AnnotationBase.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle:
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles:
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar page_index:
:vartype page_index: int
:ivar raw:
:vartype raw: str
:ivar confidence: The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: The model's confidence that the text has been classified
 correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: If the document was submitted as an image, this is the
 confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified:
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar data_point:
:vartype data_point: str
:ivar content_type:
:vartype content_type: str

<a id="models._models.AnnotationBase.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: 
- `page_index`: 
- `raw`: 
- `confidence`: The overall confidence that the model's prediction is correct.
- `classification_confidence`: The model's confidence that the text has been classified
correctly.
- `text_extraction_confidence`: If the document was submitted as an image, this is the
confidence that the text in the image has been correctly read by the model.
- `is_verified`: 
- `is_client_verified`: 
- `is_auto_verified`: 
- `data_point`: 
- `content_type`: 

<a id="models._models.AnnotationUpdate"></a>

## AnnotationUpdate Objects

```python
class AnnotationUpdate(msrest.serialization.Model)
```

AnnotationUpdate.

:ivar rectangles: x/y coordinates for the rectangles containing the data. An annotation can be
 contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Unique identifier for the document.
:vartype document: str
:ivar page_index: The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar parsed: Anything.
:vartype parsed: any
:ivar is_client_verified: Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar data_point: Data point's identifier.
:vartype data_point: str
:ivar parent: The parent annotation's ID.
:vartype parent: int

<a id="models._models.AnnotationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `rectangles`: x/y coordinates for the rectangles containing the data. An annotation can
be contained within multiple rectangles.
- `document`: Unique identifier for the document.
- `page_index`: The page number within the document, starting from 0.
- `raw`: Raw data extracted from the before any post-processing.
- `parsed`: Anything.
- `is_client_verified`: Indicates whether the data has been validated by a human.
- `data_point`: Data point's identifier.
- `parent`: The parent annotation's ID.

<a id="models._models.AnnotationBatchUpdate"></a>

## AnnotationBatchUpdate Objects

```python
class AnnotationBatchUpdate(AnnotationUpdate)
```

AnnotationBatchUpdate.

All required parameters must be populated in order to send to Azure.

:ivar rectangles: x/y coordinates for the rectangles containing the data. An annotation can be
 contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Unique identifier for the document.
:vartype document: str
:ivar page_index: The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar parsed: Anything.
:vartype parsed: any
:ivar is_client_verified: Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar data_point: Data point's identifier.
:vartype data_point: str
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar id: Required. Annotation's ID.
:vartype id: int

<a id="models._models.AnnotationBatchUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `rectangles`: x/y coordinates for the rectangles containing the data. An annotation can
be contained within multiple rectangles.
- `document`: Unique identifier for the document.
- `page_index`: The page number within the document, starting from 0.
- `raw`: Raw data extracted from the before any post-processing.
- `parsed`: Anything.
- `is_client_verified`: Indicates whether the data has been validated by a human.
- `data_point`: Data point's identifier.
- `parent`: The parent annotation's ID.
- `id`: Required. Annotation's ID.

<a id="models._models.AnnotationCreate"></a>

## AnnotationCreate Objects

```python
class AnnotationCreate(msrest.serialization.Model)
```

AnnotationCreate.

All required parameters must be populated in order to send to Azure.

:ivar rectangles: x/y coordinates for the rectangles containing the data. An annotation can be
 contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar raw: Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar parsed: Anything.
:vartype parsed: any
:ivar is_client_verified: Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar parent: The parent annotation's ID.
:vartype parent: int

<a id="models._models.AnnotationCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `rectangles`: x/y coordinates for the rectangles containing the data. An annotation can
be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `data_point`: Required. Data point's identifier.
- `raw`: Raw data extracted from the before any post-processing.
- `parsed`: Anything.
- `is_client_verified`: Indicates whether the data has been validated by a human.
- `parent`: The parent annotation's ID.

<a id="models._models.ApiUserCreate"></a>

## ApiUserCreate Objects

```python
class ApiUserCreate(msrest.serialization.Model)
```

ApiUserCreate.

All required parameters must be populated in order to send to Azure.

:ivar name:
:vartype name: str
:ivar username:
:vartype username: str
:ivar email:
:vartype email: str
:ivar avatar: URL of the user's avatar.
:vartype avatar: str
:ivar organization: Required. Uniquely identify an organization.
:vartype organization: str

<a id="models._models.ApiUserCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `username`: 
- `email`: 
- `avatar`: URL of the user's avatar.
- `organization`: Required. Uniquely identify an organization.

<a id="models._models.ApiUserUpdate"></a>

## ApiUserUpdate Objects

```python
class ApiUserUpdate(msrest.serialization.Model)
```

ApiUserUpdate.

:ivar name:
:vartype name: str
:ivar username:
:vartype username: str
:ivar email:
:vartype email: str
:ivar avatar: URL of the user's avatar.
:vartype avatar: str

<a id="models._models.ApiUserUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `username`: 
- `email`: 
- `avatar`: URL of the user's avatar.

<a id="models._models.ApiUserWithKey"></a>

## ApiUserWithKey Objects

```python
class ApiUserWithKey(msrest.serialization.Model)
```

ApiUserWithKey.

All required parameters must be populated in order to send to Azure.

:ivar id: Required. Uniquely identify a user.
:vartype id: int
:ivar name: Required.
:vartype name: str
:ivar username: Required.
:vartype username: str
:ivar email: Required.
:vartype email: str
:ivar avatar: Required. URL of the user's avatar.
:vartype avatar: str
:ivar organizations: Required.
:vartype organizations: list[~affinda.models.ApiUserWithKeyOrganizationsItem]
:ivar api_key: Required. Use this key to authenticate with the API.
:vartype api_key: str
:ivar api_key_last_chars: The last 4 characters of the API key.
:vartype api_key_last_chars: str

<a id="models._models.ApiUserWithKey.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Required. Uniquely identify a user.
- `name`: Required.
- `username`: Required.
- `email`: Required.
- `avatar`: Required. URL of the user's avatar.
- `organizations`: Required.
- `api_key`: Required. Use this key to authenticate with the API.
- `api_key_last_chars`: The last 4 characters of the API key.

<a id="models._models.ApiUserWithKeyOrganizationsItem"></a>

## ApiUserWithKeyOrganizationsItem Objects

```python
class ApiUserWithKeyOrganizationsItem(msrest.serialization.Model)
```

ApiUserWithKeyOrganizationsItem.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify an organization.
:vartype identifier: str
:ivar name: Required.
:vartype name: str

<a id="models._models.ApiUserWithKeyOrganizationsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify an organization.
- `name`: Required.

<a id="models._models.ApiUserWithoutKey"></a>

## ApiUserWithoutKey Objects

```python
class ApiUserWithoutKey(msrest.serialization.Model)
```

ApiUserWithoutKey.

All required parameters must be populated in order to send to Azure.

:ivar id: Required. Uniquely identify a user.
:vartype id: int
:ivar name: Required.
:vartype name: str
:ivar username: Required.
:vartype username: str
:ivar email: Required.
:vartype email: str
:ivar avatar: Required. URL of the user's avatar.
:vartype avatar: str
:ivar organizations: Required.
:vartype organizations: list[~affinda.models.ApiUserWithoutKeyOrganizationsItem]
:ivar api_key_last_chars: The last 4 characters of the API key.
:vartype api_key_last_chars: str

<a id="models._models.ApiUserWithoutKey.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Required. Uniquely identify a user.
- `name`: Required.
- `username`: Required.
- `email`: Required.
- `avatar`: Required. URL of the user's avatar.
- `organizations`: Required.
- `api_key_last_chars`: The last 4 characters of the API key.

<a id="models._models.ApiUserWithoutKeyOrganizationsItem"></a>

## ApiUserWithoutKeyOrganizationsItem Objects

```python
class ApiUserWithoutKeyOrganizationsItem(msrest.serialization.Model)
```

ApiUserWithoutKeyOrganizationsItem.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify an organization.
:vartype identifier: str
:ivar name: Required.
:vartype name: str

<a id="models._models.ApiUserWithoutKeyOrganizationsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify an organization.
- `name`: Required.

<a id="models._models.BaseExtractor"></a>

## BaseExtractor Objects

```python
class BaseExtractor(msrest.serialization.Model)
```

BaseExtractor.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify an extractor.
:vartype identifier: str
:ivar name: Required.
:vartype name: str
:ivar name_plural: Required.
:vartype name_plural: str
:ivar validatable: Required.
:vartype validatable: bool
:ivar is_custom:
:vartype is_custom: bool
:ivar created_dt:
:vartype created_dt: ~datetime.datetime

<a id="models._models.BaseExtractor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify an extractor.
- `name`: Required.
- `name_plural`: Required.
- `validatable`: Required.
- `is_custom`: 
- `created_dt`: 

<a id="models._models.BatchAddTagRequest"></a>

## BatchAddTagRequest Objects

```python
class BatchAddTagRequest(msrest.serialization.Model)
```

BatchAddTagRequest.

:ivar identifiers: List of documents to tag.
:vartype identifiers: list[str]
:ivar tag: The tag's ID.
:vartype tag: int

<a id="models._models.BatchAddTagRequest.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifiers`: List of documents to tag.
- `tag`: The tag's ID.

<a id="models._models.BatchRemoveTagRequest"></a>

## BatchRemoveTagRequest Objects

```python
class BatchRemoveTagRequest(msrest.serialization.Model)
```

BatchRemoveTagRequest.

:ivar identifiers: List of documents to remove tag from.
:vartype identifiers: list[str]
:ivar tag: The tag's ID.
:vartype tag: int

<a id="models._models.BatchRemoveTagRequest.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifiers`: List of documents to remove tag from.
- `tag`: The tag's ID.

<a id="models._models.Collection"></a>

## Collection Objects

```python
class Collection(msrest.serialization.Model)
```

Collection.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify a collection.
:vartype identifier: str
:ivar name:
:vartype name: str
:ivar workspace:
:vartype workspace: ~affinda.models.CollectionWorkspace
:ivar extractor:
:vartype extractor: ~affinda.models.Extractor
:ivar auto_validation_threshold:
:vartype auto_validation_threshold: float
:ivar fields:
:vartype fields: list[~affinda.models.FieldGroup]
:ivar fields_layout:
:vartype fields_layout: ~affinda.models.FieldsLayout
:ivar fields_configured:
:vartype fields_configured: bool
:ivar date_format_preference: Known values are: "DMY", "MDY", "YMD".
:vartype date_format_preference: str or ~affinda.models.CollectionDateFormatPreference
:ivar date_format_from_document: Predict the date format from any dates in the document that is
 not ambiguous.
:vartype date_format_from_document: bool
:ivar extractor_config: Extra configurations specific to an extractor.
:vartype extractor_config: ~affinda.models.ExtractorConfig
:ivar unvalidated_docs_count: Number of unvalidated documents in the collection.
:vartype unvalidated_docs_count: int
:ivar confirmed_docs_count: Number of validated documents in the collection.
:vartype confirmed_docs_count: int
:ivar ingest_email: When you send email to this address, any document attached in the body will
 be uploaded to this collection.
:vartype ingest_email: str
:ivar tailored_extractor_requested: Whether a tailored extractor has been requested for this
 collection.
:vartype tailored_extractor_requested: bool
:ivar allow_openai: Whether to allow OpenAI API to be used to assist in creating a model for
 this collection.
:vartype allow_openai: bool
:ivar trains_extractor: Whether this collection feeds documents into the extractor's training
 queue. This setting can only be toggled for custom extractors.
:vartype trains_extractor: bool

<a id="models._models.Collection.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify a collection.
- `name`: 
- `workspace`: 
- `extractor`: 
- `auto_validation_threshold`: 
- `fields`: 
- `fields_layout`: 
- `fields_configured`: 
- `date_format_preference`: Known values are: "DMY", "MDY", "YMD".
- `date_format_from_document`: Predict the date format from any dates in the document that
is not ambiguous.
- `extractor_config`: Extra configurations specific to an extractor.
- `unvalidated_docs_count`: Number of unvalidated documents in the collection.
- `confirmed_docs_count`: Number of validated documents in the collection.
- `ingest_email`: When you send email to this address, any document attached in the body
will be uploaded to this collection.
- `tailored_extractor_requested`: Whether a tailored extractor has been requested for this
collection.
- `allow_openai`: Whether to allow OpenAI API to be used to assist in creating a model for
this collection.
- `trains_extractor`: Whether this collection feeds documents into the extractor's
training queue. This setting can only be toggled for custom extractors.

<a id="models._models.CollectionCreate"></a>

## CollectionCreate Objects

```python
class CollectionCreate(msrest.serialization.Model)
```

CollectionCreate.

All required parameters must be populated in order to send to Azure.

:ivar name: Required.
:vartype name: str
:ivar workspace: Required. Uniquely identify a workspace.
:vartype workspace: str
:ivar extractor: Uniquely identify an extractor. Required if you are not a super user.
:vartype extractor: str
:ivar base_extractor: Not applicable, please leave empty. This feature is reserved for super
 user.
:vartype base_extractor: str
:ivar auto_validation_threshold:
:vartype auto_validation_threshold: float
:ivar fields:
:vartype fields: list[~affinda.models.FieldGroup]
:ivar fields_layout:
:vartype fields_layout: ~affinda.models.FieldsLayout
:ivar date_format_preference: Known values are: "DMY", "MDY", "YMD".
:vartype date_format_preference: str or ~affinda.models.DateFormatPreference
:ivar date_format_from_document: Predict the date format from any dates in the document that is
 not ambiguous.
:vartype date_format_from_document: bool
:ivar extractor_config: Extra configurations specific to an extractor.
:vartype extractor_config: ~affinda.models.ExtractorConfig
:ivar allow_openai: Whether to allow OpenAI API to be used to assist in creating a model for
 this collection.
:vartype allow_openai: bool
:ivar trains_extractor: Whether this collection feeds documents into the extractor's training
 queue. This setting can only be toggled for custom extractors.
:vartype trains_extractor: bool

<a id="models._models.CollectionCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Required.
- `workspace`: Required. Uniquely identify a workspace.
- `extractor`: Uniquely identify an extractor. Required if you are not a super user.
- `base_extractor`: Not applicable, please leave empty. This feature is reserved for super
user.
- `auto_validation_threshold`: 
- `fields`: 
- `fields_layout`: 
- `date_format_preference`: Known values are: "DMY", "MDY", "YMD".
- `date_format_from_document`: Predict the date format from any dates in the document that
is not ambiguous.
- `extractor_config`: Extra configurations specific to an extractor.
- `allow_openai`: Whether to allow OpenAI API to be used to assist in creating a model for
this collection.
- `trains_extractor`: Whether this collection feeds documents into the extractor's
training queue. This setting can only be toggled for custom extractors.

<a id="models._models.CollectionField"></a>

## CollectionField Objects

```python
class CollectionField(msrest.serialization.Model)
```

CollectionField.

:ivar label:
:vartype label: str
:ivar mandatory:
:vartype mandatory: bool
:ivar show_dropdown:
:vartype show_dropdown: bool
:ivar display_enum_value: If true, both the value and the label for the enums will appear in
 the dropdown in the validation tool.
:vartype display_enum_value: bool
:ivar auto_validation_threshold:
:vartype auto_validation_threshold: float
:ivar data_source: Data source mapping identifier.
:vartype data_source: str
:ivar mapping: Defines how the data point is mapped to the data source.
:vartype mapping: str

<a id="models._models.CollectionField.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `label`: 
- `mandatory`: 
- `show_dropdown`: 
- `display_enum_value`: If true, both the value and the label for the enums will appear in
the dropdown in the validation tool.
- `auto_validation_threshold`: 
- `data_source`: Data source mapping identifier.
- `mapping`: Defines how the data point is mapped to the data source.

<a id="models._models.CollectionUpdate"></a>

## CollectionUpdate Objects

```python
class CollectionUpdate(msrest.serialization.Model)
```

CollectionUpdate.

:ivar name:
:vartype name: str
:ivar auto_validation_threshold:
:vartype auto_validation_threshold: float
:ivar fields:
:vartype fields: list[~affinda.models.FieldGroup]
:ivar fields_layout:
:vartype fields_layout: ~affinda.models.FieldsLayout
:ivar date_format_preference: Known values are: "DMY", "MDY", "YMD".
:vartype date_format_preference: str or ~affinda.models.DateFormatPreference
:ivar date_format_from_document: Predict the date format from any dates in the document that is
 not ambiguous.
:vartype date_format_from_document: bool
:ivar extractor_config: Extra configurations specific to an extractor.
:vartype extractor_config: ~affinda.models.ExtractorConfig
:ivar allow_openai: Whether to allow OpenAI API to be used to assist in creating a model for
 this collection.
:vartype allow_openai: bool
:ivar trains_extractor: Whether this collection feeds documents into the extractor's training
 queue. This setting can only be toggled for custom extractors.
:vartype trains_extractor: bool

<a id="models._models.CollectionUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `auto_validation_threshold`: 
- `fields`: 
- `fields_layout`: 
- `date_format_preference`: Known values are: "DMY", "MDY", "YMD".
- `date_format_from_document`: Predict the date format from any dates in the document that
is not ambiguous.
- `extractor_config`: Extra configurations specific to an extractor.
- `allow_openai`: Whether to allow OpenAI API to be used to assist in creating a model for
this collection.
- `trains_extractor`: Whether this collection feeds documents into the extractor's
training queue. This setting can only be toggled for custom extractors.

<a id="models._models.CollectionWorkspace"></a>

## CollectionWorkspace Objects

```python
class CollectionWorkspace(msrest.serialization.Model)
```

CollectionWorkspace.

:ivar identifier: Uniquely identify a workspace.
:vartype identifier: str
:ivar organization:
:vartype organization: ~affinda.models.Organization
:ivar name:
:vartype name: str

<a id="models._models.CollectionWorkspace.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Uniquely identify a workspace.
- `organization`: 
- `name`: 

<a id="models._models.Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1"></a>

## Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1 Objects

```python
class Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1(
        msrest.serialization.Model)
```

Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1"></a>

## Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1 Objects

```python
class Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1(
        msrest.serialization.Model)
```

Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1"></a>

## Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1 Objects

```python
class Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1(
        msrest.serialization.Model)
```

Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1"></a>

## Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1 Objects

```python
class Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1(
        msrest.serialization.Model)
```

Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1"></a>

## Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1 Objects

```python
class Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1(
        msrest.serialization.Model)
```

Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1.

:ivar match:
:vartype match: bool

<a id="models._models.Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 

<a id="models._models.Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1"></a>

## Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1 Objects

```python
class Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1(
        msrest.serialization.Model)
```

Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1"></a>

## Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1 Objects

```python
class Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1(
        msrest.serialization.Model)
```

Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1"></a>

## Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1 Objects

```python
class Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1(
        msrest.serialization.Model)
```

Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1"></a>

## Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1 Objects

```python
class Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1(
        msrest.serialization.Model)
```

Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1"></a>

## Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1 Objects

```python
class Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1(
        msrest.serialization.Model)
```

Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1"></a>

## Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1 Objects

```python
class Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1(
        msrest.serialization.Model)
```

Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1"></a>

## Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1 Objects

```python
class Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1(
        msrest.serialization.Model)
```

Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1"></a>

## Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1 Objects

```python
class Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1(
        msrest.serialization.Model)
```

Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1"></a>

## Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1 Objects

```python
class Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1(
        msrest.serialization.Model)
```

Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1.

:ivar match:
:vartype match: bool

<a id="models._models.Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 

<a id="models._models.Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification"></a>

## Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification Objects

```python
class Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification(
        msrest.serialization.Model)
```

Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification.

:ivar title: SOC2020 classification for this job title.
:vartype title: str
:ivar minor_group: SOC2020 minor group.
:vartype minor_group: str
:ivar sub_major_group: SOC2020 sub major group.
:vartype sub_major_group: str
:ivar major_group: SOC2020 major group.
:vartype major_group: str
:ivar soc_code: The 4 digit code representing the SOC2020 classification for this job title.
:vartype soc_code: int
:ivar minor_group_code: The 4 digit code representing the SOC2020 classification for this job
 title.
:vartype minor_group_code: int
:ivar sub_major_group_code: The 4 digit code representing the SOC2020 classification for this
 job title.
:vartype sub_major_group_code: int
:ivar major_group_code: The 4 digit code representing the SOC2020 classification for this job
 title.
:vartype major_group_code: int

<a id="models._models.Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `title`: SOC2020 classification for this job title.
- `minor_group`: SOC2020 minor group.
- `sub_major_group`: SOC2020 sub major group.
- `major_group`: SOC2020 major group.
- `soc_code`: The 4 digit code representing the SOC2020 classification for this job title.
- `minor_group_code`: The 4 digit code representing the SOC2020 classification for this
job title.
- `sub_major_group_code`: The 4 digit code representing the SOC2020 classification for
this job title.
- `major_group_code`: The 4 digit code representing the SOC2020 classification for this
job title.

<a id="models._models.Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1"></a>

## Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1 Objects

```python
class Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1(
        msrest.serialization.Model)
```

Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1"></a>

## Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1 Objects

```python
class Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1(
        msrest.serialization.Model)
```

Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1"></a>

## Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1 Objects

```python
class Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1(
        msrest.serialization.Model)
```

Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1"></a>

## Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1 Objects

```python
class Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1(
        msrest.serialization.Model)
```

Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1"></a>

## Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1 Objects

```python
class Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1(
        msrest.serialization.Model)
```

Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1"></a>

## Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1 Objects

```python
class Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1(
        msrest.serialization.Model)
```

Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1"></a>

## Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1 Objects

```python
class Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1(
        msrest.serialization.Model)
```

Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1"></a>

## Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1 Objects

```python
class Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1(
        msrest.serialization.Model)
```

Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1"></a>

## Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1 Objects

```python
class Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1(
        msrest.serialization.Model)
```

Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1"></a>

## Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1 Objects

```python
class Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1(
        msrest.serialization.Model)
```

Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1"></a>

## ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1 Objects

```python
class ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1(
        msrest.serialization.Model)
```

ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1"></a>

## ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1 Objects

```python
class ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1(
        msrest.serialization.Model)
```

ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1"></a>

## ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1 Objects

```python
class ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1(
        msrest.serialization.Model)
```

ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1"></a>

## ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1 Objects

```python
class ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1(
        msrest.serialization.Model)
```

ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1"></a>

## ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1 Objects

```python
class ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1(
        msrest.serialization.Model)
```

ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1"></a>

## ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1 Objects

```python
class ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1(
        msrest.serialization.Model)
```

ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1.

:ivar match:
:vartype match: bool

<a id="models._models.ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 

<a id="models._models.ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1"></a>

## ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1 Objects

```python
class ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1(
        msrest.serialization.Model)
```

ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1.

:ivar match:
:vartype match: bool

<a id="models._models.ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 

<a id="models._models.ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties"></a>

## ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties Objects

```python
class ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties(
        msrest.serialization.Model)
```

ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties.

All required parameters must be populated in order to send to Azure.

:ivar value:
:vartype value: str
:ivar label: Required.
:vartype label: str
:ivar score:
:vartype score: float

<a id="models._models.ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `value`: 
- `label`: Required.
- `score`: 

<a id="models._models.ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1"></a>

## ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1 Objects

```python
class ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1(
        msrest.serialization.Model)
```

ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1.

:ivar match:
:vartype match: bool

<a id="models._models.ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 

<a id="models._models.ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1"></a>

## ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1 Objects

```python
class ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1(
        msrest.serialization.Model)
```

ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1"></a>

## ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1 Objects

```python
class ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1(
        msrest.serialization.Model)
```

ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1.

:ivar raw:
:vartype raw: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `parsed`: 

<a id="models._models.CurrencyCodeAnnotation"></a>

## CurrencyCodeAnnotation Objects

```python
class CurrencyCodeAnnotation(Annotation)
```

CurrencyCodeAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~affinda.models.DataPointChoice

<a id="models._models.CurrencyCodeAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.CustomFieldConfig"></a>

## CustomFieldConfig Objects

```python
class CustomFieldConfig(msrest.serialization.Model)
```

CustomFieldConfig.

All required parameters must be populated in order to send to Azure.

:ivar data_point: Required. Data point identifier.
:vartype data_point: str
:ivar weight: Required.
:vartype weight: float

<a id="models._models.CustomFieldConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `data_point`: Required. Data point identifier.
- `weight`: Required.

<a id="models._models.DataField"></a>

## DataField Objects

```python
class DataField(msrest.serialization.Model)
```

DataField.

All required parameters must be populated in order to send to Azure.

:ivar category_label: The label of the category that this field will be put into. If not
 provided, the field will be put into the default category. If no category exists with the
 specified label, a new category will be created.
:vartype category_label: str
:ivar field: Required. The field to be created.
:vartype field: ~affinda.models.DataFieldField
:ivar data_point: Required. The data point to be created for this field. If a data point with
 the same slug and collection already exists, it will be reused.
:vartype data_point: ~affinda.models.DataFieldDataPoint

<a id="models._models.DataField.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `category_label`: The label of the category that this field will be put into. If not
provided, the field will be put into the default category. If no category exists with the
specified label, a new category will be created.
- `field`: Required. The field to be created.
- `data_point`: Required. The data point to be created for this field. If a data point
with the same slug and collection already exists, it will be reused.

<a id="models._models.DataFieldCreate"></a>

## DataFieldCreate Objects

```python
class DataFieldCreate(msrest.serialization.Model)
```

DataFieldCreate.

All required parameters must be populated in order to send to Azure.

:ivar category_label: The label of the category that this field will be put into. If not
 provided, the field will be put into the default category. If no category exists with the
 specified label, a new category will be created.
:vartype category_label: str
:ivar field: Required. The field to be created.
:vartype field: ~affinda.models.DataFieldCreateField
:ivar data_point: Required. The data point to be created for this field. If a data point with
 the same slug and collection already exists, it will be reused.
:vartype data_point: ~affinda.models.DataFieldCreateDataPoint

<a id="models._models.DataFieldCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `category_label`: The label of the category that this field will be put into. If not
provided, the field will be put into the default category. If no category exists with the
specified label, a new category will be created.
- `field`: Required. The field to be created.
- `data_point`: Required. The data point to be created for this field. If a data point
with the same slug and collection already exists, it will be reused.

<a id="models._models.DataFieldCreateDataPoint"></a>

## DataFieldCreateDataPoint Objects

```python
class DataFieldCreateDataPoint(msrest.serialization.Model)
```

The data point to be created for this field. If a data point with the same slug and collection already exists, it will be reused.

All required parameters must be populated in order to send to Azure.

:ivar name: Required. Name of the data point.
:vartype name: str
:ivar slug: Required. A camelCase string that will be used as the key in the API response.
:vartype slug: str
:ivar description:
:vartype description: str
:ivar type: Required. The different data types of annotations. Known values are: "text",
 "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum", "location",
 "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language", "skill",
 "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype type: str or ~affinda.models.AnnotationContentType
:ivar multiple:
:vartype multiple: bool
:ivar no_rect:
:vartype no_rect: bool
:ivar parent: The identifier of the parent data point if applicable.
:vartype parent: str
:ivar manual_entry: If true, the model will not be used to predict this data point. Instead,
 the user will be able to manually enter the value in the validation tool.
:vartype manual_entry: bool

<a id="models._models.DataFieldCreateDataPoint.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Required. Name of the data point.
- `slug`: Required. A camelCase string that will be used as the key in the API response.
- `description`: 
- `type`: Required. The different data types of annotations. Known values are: "text",
"integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum", "location",
"phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language", "skill",
"yearsexperience", "group", "table_deprecated", "url", "image".
- `multiple`: 
- `no_rect`: 
- `parent`: The identifier of the parent data point if applicable.
- `manual_entry`: If true, the model will not be used to predict this data point. Instead,
the user will be able to manually enter the value in the validation tool.

<a id="models._models.DataFieldCreateField"></a>

## DataFieldCreateField Objects

```python
class DataFieldCreateField(msrest.serialization.Model)
```

The field to be created.

All required parameters must be populated in order to send to Azure.

:ivar label: Required.
:vartype label: str
:ivar field_type: The different data types of annotations. Known values are: "text", "integer",
 "float", "decimal", "date", "datetime", "daterange", "boolean", "enum", "location",
 "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language", "skill",
 "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype field_type: str or ~affinda.models.AnnotationContentType
:ivar mandatory:
:vartype mandatory: bool
:ivar show_dropdown:
:vartype show_dropdown: bool
:ivar display_enum_value: If true, both the value and the label for the enums will appear in
 the dropdown in the validation tool.
:vartype display_enum_value: bool
:ivar auto_validation_threshold:
:vartype auto_validation_threshold: float
:ivar data_source: Data source mapping identifier.
:vartype data_source: str
:ivar mapping: Defines how the data point is mapped to the data source.
:vartype mapping: str

<a id="models._models.DataFieldCreateField.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `label`: Required.
- `field_type`: The different data types of annotations. Known values are: "text",
"integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum", "location",
"phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language", "skill",
"yearsexperience", "group", "table_deprecated", "url", "image".
- `mandatory`: 
- `show_dropdown`: 
- `display_enum_value`: If true, both the value and the label for the enums will appear in
the dropdown in the validation tool.
- `auto_validation_threshold`: 
- `data_source`: Data source mapping identifier.
- `mapping`: Defines how the data point is mapped to the data source.

<a id="models._models.DataFieldDataPoint"></a>

## DataFieldDataPoint Objects

```python
class DataFieldDataPoint(msrest.serialization.Model)
```

The data point to be created for this field. If a data point with the same slug and collection already exists, it will be reused.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify a data point.
:vartype identifier: str
:ivar name: Required. Name of the data point.
:vartype name: str
:ivar slug: Required. A camelCase string that will be used as the key in the API response.
:vartype slug: str
:ivar description: Required.
:vartype description: str
:ivar type: Required. The different data types of annotations. Known values are: "text",
 "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum", "location",
 "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language", "skill",
 "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype type: str or ~affinda.models.AnnotationContentType
:ivar multiple: Required.
:vartype multiple: bool
:ivar no_rect: Required.
:vartype no_rect: bool
:ivar parent: Required. The identifier of the parent data point if applicable.
:vartype parent: str
:ivar children: Required.
:vartype children: list[~affinda.models.DataPoint]
:ivar manual_entry: If true, the model will not be used to predict this data point. Instead,
 the user will be able to manually enter the value in the validation tool.
:vartype manual_entry: bool
:ivar available_data_sources:
:vartype available_data_sources: list[~affinda.models.MappingDataSource]

<a id="models._models.DataFieldDataPoint.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify a data point.
- `name`: Required. Name of the data point.
- `slug`: Required. A camelCase string that will be used as the key in the API response.
- `description`: Required.
- `type`: Required. The different data types of annotations. Known values are: "text",
"integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum", "location",
"phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language", "skill",
"yearsexperience", "group", "table_deprecated", "url", "image".
- `multiple`: Required.
- `no_rect`: Required.
- `parent`: Required. The identifier of the parent data point if applicable.
- `children`: Required.
- `manual_entry`: If true, the model will not be used to predict this data point. Instead,
the user will be able to manually enter the value in the validation tool.
- `available_data_sources`: 

<a id="models._models.DataFieldField"></a>

## DataFieldField Objects

```python
class DataFieldField(msrest.serialization.Model)
```

The field to be created.

All required parameters must be populated in order to send to Azure.

:ivar label: Required.
:vartype label: str
:ivar field_type: The different data types of annotations. Known values are: "text", "integer",
 "float", "decimal", "date", "datetime", "daterange", "boolean", "enum", "location",
 "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language", "skill",
 "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype field_type: str or ~affinda.models.AnnotationContentType
:ivar mandatory: Required.
:vartype mandatory: bool
:ivar show_dropdown: Required.
:vartype show_dropdown: bool
:ivar display_enum_value: Required. If true, both the value and the label for the enums will
 appear in the dropdown in the validation tool.
:vartype display_enum_value: bool
:ivar auto_validation_threshold: Required.
:vartype auto_validation_threshold: float
:ivar enabled_child_fields: Required.
:vartype enabled_child_fields: list[~affinda.models.Field]
:ivar disabled_child_fields: Required.
:vartype disabled_child_fields: list[~affinda.models.Field]
:ivar data_source: Data source mapping identifier.
:vartype data_source: str
:ivar mapping: Defines how the data point is mapped to the data source.
:vartype mapping: str

<a id="models._models.DataFieldField.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `label`: Required.
- `field_type`: The different data types of annotations. Known values are: "text",
"integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum", "location",
"phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language", "skill",
"yearsexperience", "group", "table_deprecated", "url", "image".
- `mandatory`: Required.
- `show_dropdown`: Required.
- `display_enum_value`: Required. If true, both the value and the label for the enums will
appear in the dropdown in the validation tool.
- `auto_validation_threshold`: Required.
- `enabled_child_fields`: Required.
- `disabled_child_fields`: Required.
- `data_source`: Data source mapping identifier.
- `mapping`: Defines how the data point is mapped to the data source.

<a id="models._models.DataPoint"></a>

## DataPoint Objects

```python
class DataPoint(msrest.serialization.Model)
```

DataPoint.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify a data point.
:vartype identifier: str
:ivar name: Required. Name of the data point.
:vartype name: str
:ivar slug: Required. A camelCase string that will be used as the key in the API response.
:vartype slug: str
:ivar description:
:vartype description: str
:ivar annotation_content_type: Required. The different data types of annotations. Known values
 are: "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype annotation_content_type: str or ~affinda.models.AnnotationContentType
:ivar organization: Required.
:vartype organization: ~affinda.models.Organization
:ivar extractor: Required. Uniquely identify an extractor.
:vartype extractor: str
:ivar multiple:
:vartype multiple: bool
:ivar no_rect:
:vartype no_rect: bool
:ivar parent: The identifier of the parent data point if applicable.
:vartype parent: str
:ivar children:
:vartype children: list[~affinda.models.DataPoint]
:ivar available_data_sources:
:vartype available_data_sources: list[~affinda.models.MappingDataSource]
:ivar manual_entry: If true, the model will not be used to predict this data point. Instead,
 the user will be able to manually enter the value in the validation tool.
:vartype manual_entry: bool

<a id="models._models.DataPoint.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify a data point.
- `name`: Required. Name of the data point.
- `slug`: Required. A camelCase string that will be used as the key in the API response.
- `description`: 
- `annotation_content_type`: Required. The different data types of annotations. Known
values are: "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean",
"enum", "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle",
"language", "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `organization`: Required.
- `extractor`: Required. Uniquely identify an extractor.
- `multiple`: 
- `no_rect`: 
- `parent`: The identifier of the parent data point if applicable.
- `children`: 
- `available_data_sources`: 
- `manual_entry`: If true, the model will not be used to predict this data point. Instead,
the user will be able to manually enter the value in the validation tool.

<a id="models._models.DataPointChoice"></a>

## DataPointChoice Objects

```python
class DataPointChoice(msrest.serialization.Model)
```

DataPointChoice.

All required parameters must be populated in order to send to Azure.

:ivar id: Required. Data point choice's ID.
:vartype id: int
:ivar label: Required.
:vartype label: str
:ivar value: Required.
:vartype value: str
:ivar synonyms:
:vartype synonyms: list[str]
:ivar description:
:vartype description: str

<a id="models._models.DataPointChoice.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Required. Data point choice's ID.
- `label`: Required.
- `value`: Required.
- `synonyms`: 
- `description`: 

<a id="models._models.DataPointChoiceCreate"></a>

## DataPointChoiceCreate Objects

```python
class DataPointChoiceCreate(msrest.serialization.Model)
```

DataPointChoiceCreate.

All required parameters must be populated in order to send to Azure.

:ivar data_point: Required. Uniquely identify a data point.
:vartype data_point: str
:ivar organization: Uniquely identify an organization.
:vartype organization: str
:ivar collection: Uniquely identify a collection.
:vartype collection: str
:ivar label: Required.
:vartype label: str
:ivar value: Required.
:vartype value: str
:ivar synonyms:
:vartype synonyms: list[str]
:ivar description:
:vartype description: str

<a id="models._models.DataPointChoiceCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `data_point`: Required. Uniquely identify a data point.
- `organization`: Uniquely identify an organization.
- `collection`: Uniquely identify a collection.
- `label`: Required.
- `value`: Required.
- `synonyms`: 
- `description`: 

<a id="models._models.DataPointChoiceForReplace"></a>

## DataPointChoiceForReplace Objects

```python
class DataPointChoiceForReplace(msrest.serialization.Model)
```

DataPointChoiceForReplace.

All required parameters must be populated in order to send to Azure.

:ivar value: Required.
:vartype value: str
:ivar label:
:vartype label: str
:ivar synonyms:
:vartype synonyms: list[str]
:ivar description:
:vartype description: str

<a id="models._models.DataPointChoiceForReplace.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `value`: Required.
- `label`: 
- `synonyms`: 
- `description`: 

<a id="models._models.DataPointChoiceReplaceRequest"></a>

## DataPointChoiceReplaceRequest Objects

```python
class DataPointChoiceReplaceRequest(msrest.serialization.Model)
```

Request body for replacing choices of a data point. Either ``collection`` or ``organization`` is required.

All required parameters must be populated in order to send to Azure.

:ivar data_point: Required. Uniquely identify a data point.
:vartype data_point: str
:ivar collection: Uniquely identify a collection.
:vartype collection: str
:ivar organization: Uniquely identify an organization.
:vartype organization: str
:ivar choices: Required. Incoming choices to replace existing choices of a data point. Existing
 choices and incoming choices are matched base on their ``value``. New ``value`` will be
 created, existing ``value`` will be updated, and ``value`` not in incoming choices will be
 deleted.
:vartype choices: list[~affinda.models.DataPointChoiceForReplace]

<a id="models._models.DataPointChoiceReplaceRequest.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `data_point`: Required. Uniquely identify a data point.
- `collection`: Uniquely identify a collection.
- `organization`: Uniquely identify an organization.
- `choices`: Required. Incoming choices to replace existing choices of a data point.
Existing choices and incoming choices are matched base on their ``value``. New ``value`` will
be created, existing ``value`` will be updated, and ``value`` not in incoming choices will be
deleted.

<a id="models._models.DataPointChoiceReplaceResponse"></a>

## DataPointChoiceReplaceResponse Objects

```python
class DataPointChoiceReplaceResponse(msrest.serialization.Model)
```

DataPointChoiceReplaceResponse.

All required parameters must be populated in order to send to Azure.

:ivar data_point: Required. Uniquely identify a data point.
:vartype data_point: str
:ivar collection: Required. Uniquely identify a collection.
:vartype collection: str
:ivar organization: Required. Uniquely identify an organization.
:vartype organization: str
:ivar choices: Required.
:vartype choices: list[~affinda.models.DataPointChoiceReplaceResponseChoicesItem]

<a id="models._models.DataPointChoiceReplaceResponse.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `data_point`: Required. Uniquely identify a data point.
- `collection`: Required. Uniquely identify a collection.
- `organization`: Required. Uniquely identify an organization.
- `choices`: Required.

<a id="models._models.DataPointChoiceReplaceResponseChoicesItem"></a>

## DataPointChoiceReplaceResponseChoicesItem Objects

```python
class DataPointChoiceReplaceResponseChoicesItem(msrest.serialization.Model)
```

DataPointChoiceReplaceResponseChoicesItem.

All required parameters must be populated in order to send to Azure.

:ivar id: Required. Data point choice's ID.
:vartype id: int
:ivar value: Required.
:vartype value: str
:ivar label: Required.
:vartype label: str
:ivar synonyms: Required.
:vartype synonyms: list[str]
:ivar description: Required.
:vartype description: str

<a id="models._models.DataPointChoiceReplaceResponseChoicesItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Required. Data point choice's ID.
- `value`: Required.
- `label`: Required.
- `synonyms`: Required.
- `description`: Required.

<a id="models._models.DataPointChoiceUpdate"></a>

## DataPointChoiceUpdate Objects

```python
class DataPointChoiceUpdate(msrest.serialization.Model)
```

DataPointChoiceUpdate.

:ivar data_point: Uniquely identify a data point.
:vartype data_point: str
:ivar organization: Uniquely identify an organization.
:vartype organization: str
:ivar collection: Uniquely identify a collection.
:vartype collection: str
:ivar label:
:vartype label: str
:ivar value:
:vartype value: str
:ivar synonyms:
:vartype synonyms: list[str]
:ivar description:
:vartype description: str

<a id="models._models.DataPointChoiceUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `data_point`: Uniquely identify a data point.
- `organization`: Uniquely identify an organization.
- `collection`: Uniquely identify a collection.
- `label`: 
- `value`: 
- `synonyms`: 
- `description`: 

<a id="models._models.DataPointCreate"></a>

## DataPointCreate Objects

```python
class DataPointCreate(msrest.serialization.Model)
```

DataPointCreate.

All required parameters must be populated in order to send to Azure.

:ivar name: Required. Name of the data point.
:vartype name: str
:ivar slug: Required. A camelCase string that will be used as the key in the API response.
:vartype slug: str
:ivar description:
:vartype description: str
:ivar annotation_content_type: Required. The different data types of annotations. Known values
 are: "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype annotation_content_type: str or ~affinda.models.AnnotationContentType
:ivar organization: Required. Uniquely identify an organization.
:vartype organization: str
:ivar extractor: Required. Uniquely identify an extractor.
:vartype extractor: str
:ivar multiple:
:vartype multiple: bool
:ivar no_rect:
:vartype no_rect: bool
:ivar parent: The identifier of the parent data point if applicable.
:vartype parent: str
:ivar manual_entry: If true, the model will not be used to predict this data point. Instead,
 the user will be able to manually enter the value in the validation tool.
:vartype manual_entry: bool

<a id="models._models.DataPointCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Required. Name of the data point.
- `slug`: Required. A camelCase string that will be used as the key in the API response.
- `description`: 
- `annotation_content_type`: Required. The different data types of annotations. Known
values are: "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean",
"enum", "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle",
"language", "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `organization`: Required. Uniquely identify an organization.
- `extractor`: Required. Uniquely identify an extractor.
- `multiple`: 
- `no_rect`: 
- `parent`: The identifier of the parent data point if applicable.
- `manual_entry`: If true, the model will not be used to predict this data point. Instead,
the user will be able to manually enter the value in the validation tool.

<a id="models._models.DataPointUpdate"></a>

## DataPointUpdate Objects

```python
class DataPointUpdate(msrest.serialization.Model)
```

DataPointUpdate.

:ivar name: Name of the data point.
:vartype name: str
:ivar slug: A camelCase string that will be used as the key in the API response.
:vartype slug: str
:ivar description:
:vartype description: str
:ivar parent: The identifier of the parent data point if applicable.
:vartype parent: str

<a id="models._models.DataPointUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Name of the data point.
- `slug`: A camelCase string that will be used as the key in the API response.
- `description`: 
- `parent`: The identifier of the parent data point if applicable.

<a id="models._models.DateAnnotation"></a>

## DateAnnotation Objects

```python
class DateAnnotation(Annotation)
```

DateAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~datetime.date

<a id="models._models.DateAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.DateAnnotationUpdate"></a>

## DateAnnotationUpdate Objects

```python
class DateAnnotationUpdate(AnnotationBase)
```

DateAnnotationUpdate.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle:
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles:
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar page_index:
:vartype page_index: int
:ivar raw:
:vartype raw: str
:ivar confidence: The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: The model's confidence that the text has been classified
 correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: If the document was submitted as an image, this is the
 confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified:
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar data_point:
:vartype data_point: str
:ivar content_type:
:vartype content_type: str
:ivar parsed:
:vartype parsed: ~datetime.date

<a id="models._models.DateAnnotationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: 
- `page_index`: 
- `raw`: 
- `confidence`: The overall confidence that the model's prediction is correct.
- `classification_confidence`: The model's confidence that the text has been classified
correctly.
- `text_extraction_confidence`: If the document was submitted as an image, this is the
confidence that the text in the image has been correctly read by the model.
- `is_verified`: 
- `is_client_verified`: 
- `is_auto_verified`: 
- `data_point`: 
- `content_type`: 
- `parsed`: 

<a id="models._models.DateRangeAnnotation"></a>

## DateRangeAnnotation Objects

```python
class DateRangeAnnotation(Annotation)
```

DateRangeAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~affinda.models.DateRangeAnnotationParsed

<a id="models._models.DateRangeAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.DateRangeAnnotationParsed"></a>

## DateRangeAnnotationParsed Objects

```python
class DateRangeAnnotationParsed(msrest.serialization.Model)
```

DateRangeAnnotationParsed.

:ivar start:
:vartype start: ~affinda.models.DateRangeValue
:ivar end:
:vartype end: ~affinda.models.DateRangeValue

<a id="models._models.DateRangeAnnotationParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `start`: 
- `end`: 

<a id="models._models.DateRangeValue"></a>

## DateRangeValue Objects

```python
class DateRangeValue(msrest.serialization.Model)
```

DateRangeValue.

:ivar date:
:vartype date: ~datetime.date
:ivar is_current:
:vartype is_current: bool
:ivar day:
:vartype day: int
:ivar month:
:vartype month: int
:ivar year:
:vartype year: int

<a id="models._models.DateRangeValue.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `date`: 
- `is_current`: 
- `day`: 
- `month`: 
- `year`: 

<a id="models._models.Document"></a>

## Document Objects

```python
class Document(msrest.serialization.Model)
```

Document.

You probably want to use the sub-classes and not this class directly. Known
sub-classes are: Invoice, JobDescription, Resume, ResumeRedact.

All required parameters must be populated in order to send to Azure.

:ivar data: Any object.
:vartype data: any
:ivar extractor: Required. Constant filled by server.
:vartype extractor: str
:ivar meta: Required.
:vartype meta: ~affinda.models.DocumentMeta
:ivar error:
:vartype error: ~affinda.models.DocumentError
:ivar warnings:
:vartype warnings: list[~affinda.models.DocumentWarning]

<a id="models._models.Document.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `data`: Any object.
- `meta`: Required.
- `error`: 
- `warnings`: 

<a id="models._models.DocumentCreate"></a>

## DocumentCreate Objects

```python
class DocumentCreate(msrest.serialization.Model)
```

DocumentCreate.

:ivar file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML, PNG,
 JPG.
:vartype file: IO
:ivar url: URL to download the document.
:vartype url: str
:ivar data: Create resume or job description directly from data.
:vartype data: any
:ivar collection: Uniquely identify a collection.
:vartype collection: str
:ivar workspace: Uniquely identify a workspace.
:vartype workspace: str
:ivar wait: If "true" (default), will return a response only after processing has completed. If
 "false", will return an empty data object which can be polled at the GET endpoint until
 processing is complete.
:vartype wait: bool
:ivar identifier: Deprecated in favor of ``customIdentifier``.
:vartype identifier: str
:ivar custom_identifier: Specify a custom identifier for the document if you need one, not
 required to be unique.
:vartype custom_identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: ~datetime.datetime
:ivar language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:vartype language: str
:ivar reject_duplicates: If "true", parsing will fail when the uploaded document is duplicate
 of an existing document, no credits will be consumed. If "false", will parse the document
 normally whether its a duplicate or not. If not provided, will fallback to the workspace
 settings.
:vartype reject_duplicates: bool
:ivar region_bias: A JSON representation of the RegionBias object.
:vartype region_bias: str
:ivar low_priority: Explicitly mark this document as low priority.
:vartype low_priority: bool

<a id="models._models.DocumentCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `file`: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML,
PNG, JPG.
- `url`: URL to download the document.
- `data`: Create resume or job description directly from data.
- `collection`: Uniquely identify a collection.
- `workspace`: Uniquely identify a workspace.
- `wait`: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
- `identifier`: Deprecated in favor of ``customIdentifier``.
- `custom_identifier`: Specify a custom identifier for the document if you need one, not
required to be unique.
- `file_name`: Optional filename of the file.
- `expiry_time`: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.
- `language`: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
- `reject_duplicates`: If "true", parsing will fail when the uploaded document is
duplicate of an existing document, no credits will be consumed. If "false", will parse the
document normally whether its a duplicate or not. If not provided, will fallback to the
workspace settings.
- `region_bias`: A JSON representation of the RegionBias object.
- `low_priority`: Explicitly mark this document as low priority.

<a id="models._models.DocumentEditRequest"></a>

## DocumentEditRequest Objects

```python
class DocumentEditRequest(msrest.serialization.Model)
```

DocumentEditRequest.

All required parameters must be populated in order to send to Azure.

:ivar splits: Required.
:vartype splits: list[~affinda.models.DocumentSplit]

<a id="models._models.DocumentEditRequest.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `splits`: Required.

<a id="models._models.DocumentError"></a>

## DocumentError Objects

```python
class DocumentError(msrest.serialization.Model)
```

DocumentError.

:ivar error_code:
:vartype error_code: str
:ivar error_detail:
:vartype error_detail: str

<a id="models._models.DocumentError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `error_code`: 
- `error_detail`: 

<a id="models._models.DocumentMeta"></a>

## DocumentMeta Objects

```python
class DocumentMeta(msrest.serialization.Model)
```

DocumentMeta.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Unique identifier for the document.
:vartype identifier: str
:ivar custom_identifier: Optional identifier for the document that you can set to track the
 document in the Affinda system.  Is not required to be unique.
:vartype custom_identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar ready: If true, the document has finished processing. Particularly useful if an endpoint
 request specified wait=False, when polling use this variable to determine when to stop polling.
:vartype ready: bool
:ivar ready_dt: The datetime when the document was ready.
:vartype ready_dt: ~datetime.datetime
:ivar failed: If true, some exception was raised during processing. Check the 'error' field of
 the main return object.
:vartype failed: bool
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: ~datetime.datetime
:ivar language: The document's language.
:vartype language: str
:ivar pdf: The URL to the document's pdf (if the uploaded document is not already pdf, it's
 converted to pdf as part of the parsing process).
:vartype pdf: str
:ivar parent_document: If this document is part of a splitted document, this attribute points
 to the original document that this document is splitted from.
:vartype parent_document: ~affinda.models.DocumentMetaParentDocument
:ivar child_documents: If this document has been splitted into a number of child documents,
 this attribute points to those child documents.
:vartype child_documents: list[~affinda.models.DocumentMetaChildDocumentsItem]
:ivar pages: Required. The document's pages.
:vartype pages: list[~affinda.models.PageMeta]
:ivar is_ocrd:
:vartype is_ocrd: bool
:ivar ocr_confidence:
:vartype ocr_confidence: float
:ivar review_url:
:vartype review_url: str
:ivar collection:
:vartype collection: ~affinda.models.DocumentMetaCollection
:ivar workspace: Required.
:vartype workspace: ~affinda.models.DocumentMetaWorkspace
:ivar archived_dt:
:vartype archived_dt: ~datetime.datetime
:ivar is_archived:
:vartype is_archived: bool
:ivar confirmed_dt:
:vartype confirmed_dt: ~datetime.datetime
:ivar is_confirmed:
:vartype is_confirmed: bool
:ivar rejected_dt:
:vartype rejected_dt: ~datetime.datetime
:ivar is_rejected:
:vartype is_rejected: bool
:ivar created_dt:
:vartype created_dt: ~datetime.datetime
:ivar error_code:
:vartype error_code: str
:ivar error_detail:
:vartype error_detail: str
:ivar file: URL to view the file.
:vartype file: str
:ivar tags: A set of tags.
:vartype tags: list[~affinda.models.Tag]
:ivar confirmed_by:
:vartype confirmed_by: ~affinda.models.UserNullable
:ivar created_by:
:vartype created_by: ~affinda.models.User
:ivar source_email: If the document is created via email ingestion, this field stores the email
 file's URL.
:vartype source_email: str
:ivar source_email_address: If the document is created via email ingestion, this field stores
 the email's From address.
:vartype source_email_address: str
:ivar region_bias:
:vartype region_bias: ~affinda.models.RegionBias

<a id="models._models.DocumentMeta.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Unique identifier for the document.
- `custom_identifier`: Optional identifier for the document that you can set to track the
document in the Affinda system.  Is not required to be unique.
- `file_name`: Optional filename of the file.
- `ready`: If true, the document has finished processing. Particularly useful if an
endpoint request specified wait=False, when polling use this variable to determine when to stop
polling.
- `ready_dt`: The datetime when the document was ready.
- `failed`: If true, some exception was raised during processing. Check the 'error' field
of the main return object.
- `expiry_time`: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.
- `language`: The document's language.
- `pdf`: The URL to the document's pdf (if the uploaded document is not already pdf, it's
converted to pdf as part of the parsing process).
- `parent_document`: If this document is part of a splitted document, this attribute
points to the original document that this document is splitted from.
- `child_documents`: If this document has been splitted into a number of child documents,
this attribute points to those child documents.
- `pages`: Required. The document's pages.
- `is_ocrd`: 
- `ocr_confidence`: 
- `review_url`: 
- `collection`: 
- `workspace`: Required.
- `archived_dt`: 
- `is_archived`: 
- `confirmed_dt`: 
- `is_confirmed`: 
- `rejected_dt`: 
- `is_rejected`: 
- `created_dt`: 
- `error_code`: 
- `error_detail`: 
- `file`: URL to view the file.
- `tags`: A set of tags.
- `confirmed_by`: 
- `created_by`: 
- `source_email`: If the document is created via email ingestion, this field stores the
email file's URL.
- `source_email_address`: If the document is created via email ingestion, this field
stores the email's From address.
- `region_bias`: 

<a id="models._models.DocumentMetaChildDocumentsItem"></a>

## DocumentMetaChildDocumentsItem Objects

```python
class DocumentMetaChildDocumentsItem(msrest.serialization.Model)
```

DocumentMetaChildDocumentsItem.

:ivar identifier: Unique identifier for the document.
:vartype identifier: str

<a id="models._models.DocumentMetaChildDocumentsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Unique identifier for the document.

<a id="models._models.DocumentMetaCollection"></a>

## DocumentMetaCollection Objects

```python
class DocumentMetaCollection(msrest.serialization.Model)
```

DocumentMetaCollection.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify a collection.
:vartype identifier: str
:ivar name:
:vartype name: str
:ivar extractor:
:vartype extractor: ~affinda.models.DocumentMetaCollectionExtractor

<a id="models._models.DocumentMetaCollection.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify a collection.
- `name`: 
- `extractor`: 

<a id="models._models.DocumentMetaCollectionExtractor"></a>

## DocumentMetaCollectionExtractor Objects

```python
class DocumentMetaCollectionExtractor(msrest.serialization.Model)
```

DocumentMetaCollectionExtractor.

:ivar identifier: Uniquely identify an extractor.
:vartype identifier: str
:ivar name:
:vartype name: str
:ivar base_extractor: Base extractor's identifier.
:vartype base_extractor: str
:ivar validatable:
:vartype validatable: bool

<a id="models._models.DocumentMetaCollectionExtractor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Uniquely identify an extractor.
- `name`: 
- `base_extractor`: Base extractor's identifier.
- `validatable`: 

<a id="models._models.DocumentMetaParentDocument"></a>

## DocumentMetaParentDocument Objects

```python
class DocumentMetaParentDocument(msrest.serialization.Model)
```

If this document is part of a splitted document, this attribute points to the original document that this document is splitted from.

:ivar identifier: Unique identifier for the document.
:vartype identifier: str

<a id="models._models.DocumentMetaParentDocument.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Unique identifier for the document.

<a id="models._models.DocumentMetaWorkspace"></a>

## DocumentMetaWorkspace Objects

```python
class DocumentMetaWorkspace(msrest.serialization.Model)
```

DocumentMetaWorkspace.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify a workspace.
:vartype identifier: str
:ivar name:
:vartype name: str

<a id="models._models.DocumentMetaWorkspace.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify a workspace.
- `name`: 

<a id="models._models.DocumentSplit"></a>

## DocumentSplit Objects

```python
class DocumentSplit(msrest.serialization.Model)
```

Describe a split of a document.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Anything.
:vartype identifier: any
:ivar pages: Required.
:vartype pages: list[~affinda.models.DocumentSplitPage]

<a id="models._models.DocumentSplit.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Anything.
- `pages`: Required.

<a id="models._models.DocumentSplitPage"></a>

## DocumentSplitPage Objects

```python
class DocumentSplitPage(msrest.serialization.Model)
```

List the pages within this split. Not including a page here will signal that the page should be deleted.

All required parameters must be populated in order to send to Azure.

:ivar id: Required. Page's ID.
:vartype id: int
:ivar rotation: Specify a degree of rotation if you want to rotate a page. Possitive number for
 clockwise rotation, and negative number for counter-clockwise rotation.
:vartype rotation: int

<a id="models._models.DocumentSplitPage.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Required. Page's ID.
- `rotation`: Specify a degree of rotation if you want to rotate a page. Possitive number
for clockwise rotation, and negative number for counter-clockwise rotation.

<a id="models._models.DocumentUpdate"></a>

## DocumentUpdate Objects

```python
class DocumentUpdate(msrest.serialization.Model)
```

DocumentUpdate.

:ivar collection: Uniquely identify a collection.
:vartype collection: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: ~datetime.datetime
:ivar is_confirmed:
:vartype is_confirmed: bool
:ivar is_rejected:
:vartype is_rejected: bool
:ivar is_archived:
:vartype is_archived: bool
:ivar language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:vartype language: str
:ivar identifier: Deprecated in favor of ``customIdentifier``.
:vartype identifier: str
:ivar custom_identifier: Specify a custom identifier for the document if you need one, not
 required to be unique.
:vartype custom_identifier: str

<a id="models._models.DocumentUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `collection`: Uniquely identify a collection.
- `file_name`: Optional filename of the file.
- `expiry_time`: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.
- `is_confirmed`: 
- `is_rejected`: 
- `is_archived`: 
- `language`: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
- `identifier`: Deprecated in favor of ``customIdentifier``.
- `custom_identifier`: Specify a custom identifier for the document if you need one, not
required to be unique.

<a id="models._models.DocumentWarning"></a>

## DocumentWarning Objects

```python
class DocumentWarning(msrest.serialization.Model)
```

DocumentWarning.

:ivar warning_code:
:vartype warning_code: str
:ivar warning_detail:
:vartype warning_detail: str

<a id="models._models.DocumentWarning.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `warning_code`: 
- `warning_detail`: 

<a id="models._models.Education"></a>

## Education Objects

```python
class Education(msrest.serialization.Model)
```

Education.

:ivar id:
:vartype id: int
:ivar organization:
:vartype organization: str
:ivar accreditation:
:vartype accreditation: ~affinda.models.Accreditation
:ivar grade:
:vartype grade: ~affinda.models.EducationGrade
:ivar location:
:vartype location: ~affinda.models.Location
:ivar dates:
:vartype dates: ~affinda.models.EducationDates

<a id="models._models.Education.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: 
- `organization`: 
- `accreditation`: 
- `grade`: 
- `location`: 
- `dates`: 

<a id="models._models.EducationDates"></a>

## EducationDates Objects

```python
class EducationDates(msrest.serialization.Model)
```

EducationDates.

:ivar completion_date:
:vartype completion_date: ~datetime.date
:ivar is_current:
:vartype is_current: bool
:ivar start_date:
:vartype start_date: ~datetime.date
:ivar raw_text:
:vartype raw_text: str

<a id="models._models.EducationDates.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `completion_date`: 
- `is_current`: 
- `start_date`: 
- `raw_text`: 

<a id="models._models.EducationGrade"></a>

## EducationGrade Objects

```python
class EducationGrade(msrest.serialization.Model)
```

EducationGrade.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar raw:
:vartype raw: str
:ivar metric:
:vartype metric: str
:ivar value:
:vartype value: str

<a id="models._models.EducationGrade.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `raw`: 
- `metric`: 
- `value`: 

<a id="models._models.EducationSearchScoreComponent"></a>

## EducationSearchScoreComponent Objects

```python
class EducationSearchScoreComponent(msrest.serialization.Model)
```

EducationSearchScoreComponent.

All required parameters must be populated in order to send to Azure.

:ivar value:
:vartype value: str
:ivar label: Required.
:vartype label: str
:ivar score:
:vartype score: float

<a id="models._models.EducationSearchScoreComponent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `value`: 
- `label`: Required.
- `score`: 

<a id="models._models.ExpectedRemunerationAnnotation"></a>

## ExpectedRemunerationAnnotation Objects

```python
class ExpectedRemunerationAnnotation(Annotation)
```

ExpectedRemunerationAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~affinda.models.ExpectedRemunerationAnnotationParsed

<a id="models._models.ExpectedRemunerationAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.ExpectedRemunerationAnnotationParsed"></a>

## ExpectedRemunerationAnnotationParsed Objects

```python
class ExpectedRemunerationAnnotationParsed(msrest.serialization.Model)
```

ExpectedRemunerationAnnotationParsed.

:ivar minimum:
:vartype minimum: float
:ivar maximum:
:vartype maximum: float
:ivar currency:
:vartype currency: str
:ivar unit:
:vartype unit: str

<a id="models._models.ExpectedRemunerationAnnotationParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `minimum`: 
- `maximum`: 
- `currency`: 
- `unit`: 

<a id="models._models.ExpectedRemunerationAnnotationUpdate"></a>

## ExpectedRemunerationAnnotationUpdate Objects

```python
class ExpectedRemunerationAnnotationUpdate(AnnotationBase)
```

ExpectedRemunerationAnnotationUpdate.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle:
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles:
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar page_index:
:vartype page_index: int
:ivar raw:
:vartype raw: str
:ivar confidence: The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: The model's confidence that the text has been classified
 correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: If the document was submitted as an image, this is the
 confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified:
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar data_point:
:vartype data_point: str
:ivar content_type:
:vartype content_type: str
:ivar parsed:
:vartype parsed: ~affinda.models.ExpectedRemunerationAnnotationUpdateParsed

<a id="models._models.ExpectedRemunerationAnnotationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: 
- `page_index`: 
- `raw`: 
- `confidence`: The overall confidence that the model's prediction is correct.
- `classification_confidence`: The model's confidence that the text has been classified
correctly.
- `text_extraction_confidence`: If the document was submitted as an image, this is the
confidence that the text in the image has been correctly read by the model.
- `is_verified`: 
- `is_client_verified`: 
- `is_auto_verified`: 
- `data_point`: 
- `content_type`: 
- `parsed`: 

<a id="models._models.ExpectedRemunerationAnnotationUpdateParsed"></a>

## ExpectedRemunerationAnnotationUpdateParsed Objects

```python
class ExpectedRemunerationAnnotationUpdateParsed(msrest.serialization.Model)
```

ExpectedRemunerationAnnotationUpdateParsed.

:ivar minimum:
:vartype minimum: float
:ivar maximum:
:vartype maximum: float
:ivar currency:
:vartype currency: str
:ivar unit:
:vartype unit: str

<a id="models._models.ExpectedRemunerationAnnotationUpdateParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `minimum`: 
- `maximum`: 
- `currency`: 
- `unit`: 

<a id="models._models.ExperienceSearchScoreComponent"></a>

## ExperienceSearchScoreComponent Objects

```python
class ExperienceSearchScoreComponent(msrest.serialization.Model)
```

ExperienceSearchScoreComponent.

All required parameters must be populated in order to send to Azure.

:ivar value:
:vartype value: str
:ivar label: Required.
:vartype label: str
:ivar score:
:vartype score: float

<a id="models._models.ExperienceSearchScoreComponent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `value`: 
- `label`: Required.
- `score`: 

<a id="models._models.Extractor"></a>

## Extractor Objects

```python
class Extractor(msrest.serialization.Model)
```

Extractor.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify an extractor.
:vartype identifier: str
:ivar name: Required.
:vartype name: str
:ivar name_plural: Required.
:vartype name_plural: str
:ivar base_extractor:
:vartype base_extractor: ~affinda.models.ExtractorBaseExtractor
:ivar organization:
:vartype organization: ~affinda.models.Organization
:ivar category:
:vartype category: str
:ivar validatable: Required.
:vartype validatable: bool
:ivar is_custom:
:vartype is_custom: bool
:ivar field_groups:
:vartype field_groups: list[~affinda.models.FieldGroup]
:ivar created_dt:
:vartype created_dt: ~datetime.datetime
:ivar last_trained_dt:
:vartype last_trained_dt: ~datetime.datetime

<a id="models._models.Extractor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify an extractor.
- `name`: Required.
- `name_plural`: Required.
- `base_extractor`: 
- `organization`: 
- `category`: 
- `validatable`: Required.
- `is_custom`: 
- `field_groups`: 
- `created_dt`: 
- `last_trained_dt`: 

<a id="models._models.ExtractorBaseExtractor"></a>

## ExtractorBaseExtractor Objects

```python
class ExtractorBaseExtractor(msrest.serialization.Model)
```

ExtractorBaseExtractor.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify an extractor.
:vartype identifier: str
:ivar name: Required.
:vartype name: str
:ivar name_plural: Required.
:vartype name_plural: str
:ivar validatable: Required.
:vartype validatable: bool
:ivar is_custom:
:vartype is_custom: bool
:ivar created_dt:
:vartype created_dt: ~datetime.datetime

<a id="models._models.ExtractorBaseExtractor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify an extractor.
- `name`: Required.
- `name_plural`: Required.
- `validatable`: Required.
- `is_custom`: 
- `created_dt`: 

<a id="models._models.ExtractorConfig"></a>

## ExtractorConfig Objects

```python
class ExtractorConfig(msrest.serialization.Model)
```

Extra configurations specific to an extractor.

:ivar resume_redact:
:vartype resume_redact: ~affinda.models.RedactConfig

<a id="models._models.ExtractorConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `resume_redact`: 

<a id="models._models.ExtractorCreate"></a>

## ExtractorCreate Objects

```python
class ExtractorCreate(msrest.serialization.Model)
```

ExtractorCreate.

All required parameters must be populated in order to send to Azure.

:ivar name: Required.
:vartype name: str
:ivar name_plural:
:vartype name_plural: str
:ivar base_extractor: Uniquely identify an extractor.
:vartype base_extractor: str
:ivar organization: Required. Uniquely identify an organization.
:vartype organization: str
:ivar category:
:vartype category: str
:ivar validatable:
:vartype validatable: bool
:ivar field_groups:
:vartype field_groups: list[~affinda.models.FieldGroup]

<a id="models._models.ExtractorCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Required.
- `name_plural`: 
- `base_extractor`: Uniquely identify an extractor.
- `organization`: Required. Uniquely identify an organization.
- `category`: 
- `validatable`: 
- `field_groups`: 

<a id="models._models.ExtractorUpdate"></a>

## ExtractorUpdate Objects

```python
class ExtractorUpdate(msrest.serialization.Model)
```

ExtractorUpdate.

:ivar name:
:vartype name: str
:ivar name_plural:
:vartype name_plural: str
:ivar base_extractor: Uniquely identify an extractor.
:vartype base_extractor: str
:ivar category:
:vartype category: str
:ivar validatable:
:vartype validatable: bool
:ivar field_groups:
:vartype field_groups: list[~affinda.models.FieldGroup]

<a id="models._models.ExtractorUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `name_plural`: 
- `base_extractor`: Uniquely identify an extractor.
- `category`: 
- `validatable`: 
- `field_groups`: 

<a id="models._models.Field"></a>

## Field Objects

```python
class Field(msrest.serialization.Model)
```

Field.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar label: Required.
:vartype label: str
:ivar data_point: Required. Data point identifier.
:vartype data_point: str
:ivar field_type: Required. The different data types of annotations. Known values are: "text",
 "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum", "location",
 "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language", "skill",
 "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype field_type: str or ~affinda.models.AnnotationContentType
:ivar data_source: Data source mapping identifier.
:vartype data_source: str
:ivar mapping: Defines how the data point is mapped to the data source.
:vartype mapping: str
:ivar mandatory:
:vartype mandatory: bool
:ivar auto_validation_threshold:
:vartype auto_validation_threshold: float
:ivar show_dropdown:
:vartype show_dropdown: bool
:ivar display_enum_value: If true, both the value and the label for the enums will appear in
 the dropdown in the validation tool.
:vartype display_enum_value: bool
:ivar drop_null: If True, any dropdown annotations that fail to parse to a value will be
 discarded.
:vartype drop_null: bool
:ivar enabled_child_fields:
:vartype enabled_child_fields: list[~affinda.models.Field]
:ivar disabled_child_fields:
:vartype disabled_child_fields: list[~affinda.models.Field]
:ivar slug:
:vartype slug: str
:ivar fields:
:vartype fields: list[any]

<a id="models._models.Field.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `label`: Required.
- `data_point`: Required. Data point identifier.
- `field_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `data_source`: Data source mapping identifier.
- `mapping`: Defines how the data point is mapped to the data source.
- `mandatory`: 
- `auto_validation_threshold`: 
- `show_dropdown`: 
- `display_enum_value`: If true, both the value and the label for the enums will appear in
the dropdown in the validation tool.
- `drop_null`: If True, any dropdown annotations that fail to parse to a value will be
discarded.
- `enabled_child_fields`: 
- `disabled_child_fields`: 
- `slug`: 
- `fields`: 

<a id="models._models.FieldCategory"></a>

## FieldCategory Objects

```python
class FieldCategory(msrest.serialization.Model)
```

FieldCategory.

All required parameters must be populated in order to send to Azure.

:ivar label: Required.
:vartype label: str
:ivar enabled_fields: Required.
:vartype enabled_fields: list[~affinda.models.Field]
:ivar disabled_fields: Required.
:vartype disabled_fields: list[~affinda.models.Field]

<a id="models._models.FieldCategory.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `label`: Required.
- `enabled_fields`: Required.
- `disabled_fields`: Required.

<a id="models._models.FieldDeprecated"></a>

## FieldDeprecated Objects

```python
class FieldDeprecated(msrest.serialization.Model)
```

FieldDeprecated.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar label: Required.
:vartype label: str
:ivar slug:
:vartype slug: str
:ivar field_type: Required. The different data types of annotations. Known values are: "text",
 "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum", "location",
 "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language", "skill",
 "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype field_type: str or ~affinda.models.AnnotationContentType
:ivar data_source: Data source mapping identifier.
:vartype data_source: str
:ivar mapping: Defines how the data point is mapped to the data source.
:vartype mapping: str
:ivar data_point: Required.
:vartype data_point: str
:ivar mandatory:
:vartype mandatory: bool
:ivar disabled:
:vartype disabled: bool
:ivar auto_validation_threshold:
:vartype auto_validation_threshold: float
:ivar show_dropdown:
:vartype show_dropdown: bool
:ivar drop_null: If True, any dropdown annotations that fail to parse to a value will be
 discarded.
:vartype drop_null: bool
:ivar display_enum_value:
:vartype display_enum_value: bool
:ivar fields:
:vartype fields: list[~affinda.models.FieldDeprecated]

<a id="models._models.FieldDeprecated.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `label`: Required.
- `slug`: 
- `field_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `data_source`: Data source mapping identifier.
- `mapping`: Defines how the data point is mapped to the data source.
- `data_point`: Required.
- `mandatory`: 
- `disabled`: 
- `auto_validation_threshold`: 
- `show_dropdown`: 
- `drop_null`: If True, any dropdown annotations that fail to parse to a value will be
discarded.
- `display_enum_value`: 
- `fields`: 

<a id="models._models.FieldGroup"></a>

## FieldGroup Objects

```python
class FieldGroup(msrest.serialization.Model)
```

FieldGroup.

All required parameters must be populated in order to send to Azure.

:ivar label: Required.
:vartype label: str
:ivar fields: Required.
:vartype fields: list[~affinda.models.FieldDeprecated]

<a id="models._models.FieldGroup.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `label`: Required.
- `fields`: Required.

<a id="models._models.FieldsLayout"></a>

## FieldsLayout Objects

```python
class FieldsLayout(msrest.serialization.Model)
```

FieldsLayout.

All required parameters must be populated in order to send to Azure.

:ivar default_category: Required.
:vartype default_category: ~affinda.models.FieldCategory
:ivar categories: Required.
:vartype categories: list[~affinda.models.FieldCategory]

<a id="models._models.FieldsLayout.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `default_category`: Required.
- `categories`: Required.

<a id="models._models.FloatAnnotation"></a>

## FloatAnnotation Objects

```python
class FloatAnnotation(Annotation)
```

FloatAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: float

<a id="models._models.FloatAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.Get200ApplicationJsonPropertiesItemsItem"></a>

## Get200ApplicationJsonPropertiesItemsItem Objects

```python
class Get200ApplicationJsonPropertiesItemsItem(msrest.serialization.Model)
```

Get200ApplicationJsonPropertiesItemsItem.

:ivar document:
:vartype document: str

<a id="models._models.Get200ApplicationJsonPropertiesItemsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `document`: 

<a id="models._models.Index"></a>

## Index Objects

```python
class Index(msrest.serialization.Model)
```

Index.

Variables are only populated by the server, and will be ignored when sending a request.

All required parameters must be populated in order to send to Azure.

:ivar name: Required. Unique index name.
:vartype name: str
:ivar document_type: Required. Known values are: "resumes", "job_descriptions".
:vartype document_type: str or ~affinda.models.IndexDocumentType
:ivar user: Required. The user who created this index.
:vartype user: ~affinda.models.IndexUser

<a id="models._models.Index.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Required. Unique index name.
- `document_type`: Required. Known values are: "resumes", "job_descriptions".

<a id="models._models.IndexCreate"></a>

## IndexCreate Objects

```python
class IndexCreate(msrest.serialization.Model)
```

IndexRequestBody.

All required parameters must be populated in order to send to Azure.

:ivar name: Required. Unique index name.
:vartype name: str
:ivar document_type: Known values are: "resumes", "job_descriptions".
:vartype document_type: str or ~affinda.models.DocumentType

<a id="models._models.IndexCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Required. Unique index name.
- `document_type`: Known values are: "resumes", "job_descriptions".

<a id="models._models.IndexUpdate"></a>

## IndexUpdate Objects

```python
class IndexUpdate(msrest.serialization.Model)
```

IndexUpdate.

:ivar name: Unique index name.
:vartype name: str

<a id="models._models.IndexUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Unique index name.

<a id="models._models.IndexUser"></a>

## IndexUser Objects

```python
class IndexUser(msrest.serialization.Model)
```

The user who created this index.

All required parameters must be populated in order to send to Azure.

:ivar id: Required. Uniquely identify a user.
:vartype id: int
:ivar name: Required.
:vartype name: str
:ivar email: Required.
:vartype email: str
:ivar avatar: Required. URL of the user's avatar.
:vartype avatar: str

<a id="models._models.IndexUser.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Required. Uniquely identify a user.
- `name`: Required.
- `email`: Required.
- `avatar`: Required. URL of the user's avatar.

<a id="models._models.Invitation"></a>

## Invitation Objects

```python
class Invitation(msrest.serialization.Model)
```

Invitation.

:ivar identifier: Uniquely identify an invitation.
:vartype identifier: str
:ivar organization:
:vartype organization: ~affinda.models.Organization
:ivar email: The email which the invitation is sent to.
:vartype email: str
:ivar role: Known values are: "admin", "member".
:vartype role: str or ~affinda.models.OrganizationRole
:ivar status: Known values are: "pending", "accepted", "declined".
:vartype status: str or ~affinda.models.InvitationStatus
:ivar expiry_date: The date after which the invitation expires. Default is 10 days from now.
:vartype expiry_date: ~datetime.date
:ivar invited_by:
:vartype invited_by: ~affinda.models.User
:ivar responded_by:
:vartype responded_by: ~affinda.models.InvitationRespondedBy
:ivar created_dt:
:vartype created_dt: ~datetime.datetime

<a id="models._models.Invitation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Uniquely identify an invitation.
- `organization`: 
- `email`: The email which the invitation is sent to.
- `role`: Known values are: "admin", "member".
- `status`: Known values are: "pending", "accepted", "declined".
- `expiry_date`: The date after which the invitation expires. Default is 10 days from now.
- `invited_by`: 
- `responded_by`: 
- `created_dt`: 

<a id="models._models.InvitationCreate"></a>

## InvitationCreate Objects

```python
class InvitationCreate(msrest.serialization.Model)
```

InvitationCreate.

All required parameters must be populated in order to send to Azure.

:ivar organization: Required. Uniquely identify an organization.
:vartype organization: str
:ivar email: Required. The email which the invitation is sent to.
:vartype email: str
:ivar role: Required. Known values are: "admin", "member".
:vartype role: str or ~affinda.models.OrganizationRole

<a id="models._models.InvitationCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `organization`: Required. Uniquely identify an organization.
- `email`: Required. The email which the invitation is sent to.
- `role`: Required. Known values are: "admin", "member".

<a id="models._models.User"></a>

## User Objects

```python
class User(msrest.serialization.Model)
```

User.

:ivar id: Uniquely identify a user.
:vartype id: int
:ivar name:
:vartype name: str
:ivar username:
:vartype username: str
:ivar email:
:vartype email: str
:ivar avatar: URL of the user's avatar.
:vartype avatar: str

<a id="models._models.User.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Uniquely identify a user.
- `name`: 
- `username`: 
- `email`: 
- `avatar`: URL of the user's avatar.

<a id="models._models.InvitationRespondedBy"></a>

## InvitationRespondedBy Objects

```python
class InvitationRespondedBy(User)
```

InvitationRespondedBy.

:ivar id: Uniquely identify a user.
:vartype id: int
:ivar name:
:vartype name: str
:ivar username:
:vartype username: str
:ivar email:
:vartype email: str
:ivar avatar: URL of the user's avatar.
:vartype avatar: str

<a id="models._models.InvitationRespondedBy.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Uniquely identify a user.
- `name`: 
- `username`: 
- `email`: 
- `avatar`: URL of the user's avatar.

<a id="models._models.InvitationResponse"></a>

## InvitationResponse Objects

```python
class InvitationResponse(msrest.serialization.Model)
```

InvitationResponse.

:ivar status: Known values are: "accepted", "declined".
:vartype status: str or ~affinda.models.InvitationResponseStatus

<a id="models._models.InvitationResponse.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `status`: Known values are: "accepted", "declined".

<a id="models._models.InvitationUpdate"></a>

## InvitationUpdate Objects

```python
class InvitationUpdate(msrest.serialization.Model)
```

InvitationUpdate.

:ivar role: Known values are: "admin", "member".
:vartype role: str or ~affinda.models.OrganizationRole

<a id="models._models.InvitationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `role`: Known values are: "admin", "member".

<a id="models._models.Invoice"></a>

## Invoice Objects

```python
class Invoice(Document)
```

Invoice.

All required parameters must be populated in order to send to Azure.

:ivar extractor: Required. Constant filled by server.
:vartype extractor: str
:ivar meta: Required.
:vartype meta: ~affinda.models.DocumentMeta
:ivar error:
:vartype error: ~affinda.models.DocumentError
:ivar warnings:
:vartype warnings: list[~affinda.models.DocumentWarning]
:ivar data:
:vartype data: ~affinda.models.InvoiceData

<a id="models._models.Invoice.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `meta`: Required.
- `error`: 
- `warnings`: 
- `data`: 

<a id="models._models.InvoiceData"></a>

## InvoiceData Objects

```python
class InvoiceData(msrest.serialization.Model)
```

InvoiceData.

:ivar tables:
:vartype tables: list[~affinda.models.TableAnnotation]
:ivar tables_beta:
:vartype tables_beta: list[~affinda.models.TableBetaAnnotation]
:ivar invoice_date:
:vartype invoice_date: ~affinda.models.DateAnnotation
:ivar invoice_order_date:
:vartype invoice_order_date: ~affinda.models.DateAnnotation
:ivar payment_date_due:
:vartype payment_date_due: ~affinda.models.DateAnnotation
:ivar payment_amount_base:
:vartype payment_amount_base: ~affinda.models.InvoiceDataPaymentAmountBase
:ivar payment_amount_tax:
:vartype payment_amount_tax: ~affinda.models.InvoiceDataPaymentAmountTax
:ivar payment_amount_total:
:vartype payment_amount_total: ~affinda.models.InvoiceDataPaymentAmountTotal
:ivar payment_amount_paid:
:vartype payment_amount_paid: ~affinda.models.InvoiceDataPaymentAmountPaid
:ivar payment_amount_due:
:vartype payment_amount_due: ~affinda.models.InvoiceDataPaymentAmountDue
:ivar invoice_number:
:vartype invoice_number: ~affinda.models.InvoiceDataInvoiceNumber
:ivar invoice_purchase_order_number:
:vartype invoice_purchase_order_number: ~affinda.models.InvoiceDataInvoicePurchaseOrderNumber
:ivar supplier_business_number:
:vartype supplier_business_number: ~affinda.models.InvoiceDataSupplierBusinessNumber
:ivar customer_number:
:vartype customer_number: ~affinda.models.InvoiceDataCustomerNumber
:ivar customer_business_number:
:vartype customer_business_number: ~affinda.models.InvoiceDataCustomerBusinessNumber
:ivar payment_reference:
:vartype payment_reference: ~affinda.models.InvoiceDataPaymentReference
:ivar bank_account_number:
:vartype bank_account_number: ~affinda.models.InvoiceDataBankAccountNumber
:ivar supplier_vat:
:vartype supplier_vat: ~affinda.models.InvoiceDataSupplierVat
:ivar customer_vat:
:vartype customer_vat: ~affinda.models.InvoiceDataCustomerVat
:ivar bpay_biller_code:
:vartype bpay_biller_code: ~affinda.models.InvoiceDataBpayBillerCode
:ivar bpay_reference:
:vartype bpay_reference: ~affinda.models.InvoiceDataBpayReference
:ivar bank_sort_code:
:vartype bank_sort_code: ~affinda.models.InvoiceDataBankSortCode
:ivar bank_iban:
:vartype bank_iban: ~affinda.models.InvoiceDataBankIban
:ivar bank_swift:
:vartype bank_swift: ~affinda.models.InvoiceDataBankSwift
:ivar bank_bsb:
:vartype bank_bsb: ~affinda.models.InvoiceDataBankBsb
:ivar customer_contact_name:
:vartype customer_contact_name: ~affinda.models.InvoiceDataCustomerContactName
:ivar customer_company_name:
:vartype customer_company_name: ~affinda.models.InvoiceDataCustomerCompanyName
:ivar supplier_company_name:
:vartype supplier_company_name: ~affinda.models.InvoiceDataSupplierCompanyName
:ivar customer_billing_address:
:vartype customer_billing_address: ~affinda.models.LocationAnnotation
:ivar customer_delivery_address:
:vartype customer_delivery_address: ~affinda.models.LocationAnnotation
:ivar supplier_address:
:vartype supplier_address: ~affinda.models.LocationAnnotation
:ivar customer_phone_number:
:vartype customer_phone_number: ~affinda.models.InvoiceDataCustomerPhoneNumber
:ivar supplier_phone_number:
:vartype supplier_phone_number: ~affinda.models.InvoiceDataSupplierPhoneNumber
:ivar supplier_fax:
:vartype supplier_fax: ~affinda.models.InvoiceDataSupplierFax
:ivar customer_email:
:vartype customer_email: ~affinda.models.InvoiceDataCustomerEmail
:ivar supplier_email:
:vartype supplier_email: ~affinda.models.InvoiceDataSupplierEmail
:ivar supplier_website:
:vartype supplier_website: ~affinda.models.InvoiceDataSupplierWebsite
:ivar currency_code:
:vartype currency_code: ~affinda.models.CurrencyCodeAnnotation
:ivar custom_fields: Dictionary of :code:`<any>`.
:vartype custom_fields: dict[str, any]
:ivar raw_text: All of the raw text of the parsed invoice.
:vartype raw_text: str

<a id="models._models.InvoiceData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `tables`: 
- `tables_beta`: 
- `invoice_date`: 
- `invoice_order_date`: 
- `payment_date_due`: 
- `payment_amount_base`: 
- `payment_amount_tax`: 
- `payment_amount_total`: 
- `payment_amount_paid`: 
- `payment_amount_due`: 
- `invoice_number`: 
- `invoice_purchase_order_number`: 
- `supplier_business_number`: 
- `customer_number`: 
- `customer_business_number`: 
- `payment_reference`: 
- `bank_account_number`: 
- `supplier_vat`: 
- `customer_vat`: 
- `bpay_biller_code`: 
- `bpay_reference`: 
- `bank_sort_code`: 
- `bank_iban`: 
- `bank_swift`: 
- `bank_bsb`: 
- `customer_contact_name`: 
- `customer_company_name`: 
- `supplier_company_name`: 
- `customer_billing_address`: 
- `customer_delivery_address`: 
- `supplier_address`: 
- `customer_phone_number`: 
- `supplier_phone_number`: 
- `supplier_fax`: 
- `customer_email`: 
- `supplier_email`: 
- `supplier_website`: 
- `currency_code`: 
- `custom_fields`: Dictionary of :code:`<any>`.
- `raw_text`: All of the raw text of the parsed invoice.

<a id="models._models.TextAnnotation"></a>

## TextAnnotation Objects

```python
class TextAnnotation(Annotation)
```

TextAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.TextAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataBankAccountNumber"></a>

## InvoiceDataBankAccountNumber Objects

```python
class InvoiceDataBankAccountNumber(
        TextAnnotation,
        Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1)
```

InvoiceDataBankAccountNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataBankAccountNumber.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataBankBsb"></a>

## InvoiceDataBankBsb Objects

```python
class InvoiceDataBankBsb(
        TextAnnotation,
        Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1)
```

InvoiceDataBankBsb.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataBankBsb.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataBankIban"></a>

## InvoiceDataBankIban Objects

```python
class InvoiceDataBankIban(
        TextAnnotation,
        Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1)
```

InvoiceDataBankIban.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataBankIban.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataBankSortCode"></a>

## InvoiceDataBankSortCode Objects

```python
class InvoiceDataBankSortCode(
        TextAnnotation,
        Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1)
```

InvoiceDataBankSortCode.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataBankSortCode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataBankSwift"></a>

## InvoiceDataBankSwift Objects

```python
class InvoiceDataBankSwift(
        TextAnnotation,
        Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1)
```

InvoiceDataBankSwift.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataBankSwift.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataBpayBillerCode"></a>

## InvoiceDataBpayBillerCode Objects

```python
class InvoiceDataBpayBillerCode(
        TextAnnotation,
        ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1)
```

InvoiceDataBpayBillerCode.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataBpayBillerCode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataBpayReference"></a>

## InvoiceDataBpayReference Objects

```python
class InvoiceDataBpayReference(
        TextAnnotation,
        ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1)
```

InvoiceDataBpayReference.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataBpayReference.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerBusinessNumber"></a>

## InvoiceDataCustomerBusinessNumber Objects

```python
class InvoiceDataCustomerBusinessNumber(
        TextAnnotation,
        Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1
)
```

InvoiceDataCustomerBusinessNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataCustomerBusinessNumber.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerCompanyName"></a>

## InvoiceDataCustomerCompanyName Objects

```python
class InvoiceDataCustomerCompanyName(
        TextAnnotation,
        Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1
)
```

InvoiceDataCustomerCompanyName.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataCustomerCompanyName.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerContactName"></a>

## InvoiceDataCustomerContactName Objects

```python
class InvoiceDataCustomerContactName(
        TextAnnotation,
        ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1)
```

InvoiceDataCustomerContactName.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataCustomerContactName.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerEmail"></a>

## InvoiceDataCustomerEmail Objects

```python
class InvoiceDataCustomerEmail(
        TextAnnotation,
        Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1)
```

InvoiceDataCustomerEmail.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataCustomerEmail.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerNumber"></a>

## InvoiceDataCustomerNumber Objects

```python
class InvoiceDataCustomerNumber(
        TextAnnotation,
        Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1)
```

InvoiceDataCustomerNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataCustomerNumber.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerPhoneNumber"></a>

## InvoiceDataCustomerPhoneNumber Objects

```python
class InvoiceDataCustomerPhoneNumber(
        TextAnnotation,
        Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1
)
```

InvoiceDataCustomerPhoneNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataCustomerPhoneNumber.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerVat"></a>

## InvoiceDataCustomerVat Objects

```python
class InvoiceDataCustomerVat(
        TextAnnotation,
        ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1)
```

InvoiceDataCustomerVat.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataCustomerVat.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataInvoiceNumber"></a>

## InvoiceDataInvoiceNumber Objects

```python
class InvoiceDataInvoiceNumber(
        TextAnnotation,
        Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1)
```

InvoiceDataInvoiceNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataInvoiceNumber.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataInvoicePurchaseOrderNumber"></a>

## InvoiceDataInvoicePurchaseOrderNumber Objects

```python
class InvoiceDataInvoicePurchaseOrderNumber(
        TextAnnotation,
        ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1
)
```

InvoiceDataInvoicePurchaseOrderNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataInvoicePurchaseOrderNumber.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentAmountBase"></a>

## InvoiceDataPaymentAmountBase Objects

```python
class InvoiceDataPaymentAmountBase(
        TextAnnotation,
        Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1)
```

InvoiceDataPaymentAmountBase.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataPaymentAmountBase.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentAmountDue"></a>

## InvoiceDataPaymentAmountDue Objects

```python
class InvoiceDataPaymentAmountDue(
        TextAnnotation,
        ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1)
```

InvoiceDataPaymentAmountDue.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataPaymentAmountDue.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentAmountPaid"></a>

## InvoiceDataPaymentAmountPaid Objects

```python
class InvoiceDataPaymentAmountPaid(
        TextAnnotation,
        Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1)
```

InvoiceDataPaymentAmountPaid.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataPaymentAmountPaid.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentAmountTax"></a>

## InvoiceDataPaymentAmountTax Objects

```python
class InvoiceDataPaymentAmountTax(
        TextAnnotation,
        Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1)
```

InvoiceDataPaymentAmountTax.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataPaymentAmountTax.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentAmountTotal"></a>

## InvoiceDataPaymentAmountTotal Objects

```python
class InvoiceDataPaymentAmountTotal(
        TextAnnotation,
        Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1)
```

InvoiceDataPaymentAmountTotal.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataPaymentAmountTotal.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentReference"></a>

## InvoiceDataPaymentReference Objects

```python
class InvoiceDataPaymentReference(
        TextAnnotation,
        Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1)
```

InvoiceDataPaymentReference.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataPaymentReference.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierBusinessNumber"></a>

## InvoiceDataSupplierBusinessNumber Objects

```python
class InvoiceDataSupplierBusinessNumber(
        TextAnnotation,
        Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1
)
```

InvoiceDataSupplierBusinessNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataSupplierBusinessNumber.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierCompanyName"></a>

## InvoiceDataSupplierCompanyName Objects

```python
class InvoiceDataSupplierCompanyName(
        TextAnnotation,
        Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1
)
```

InvoiceDataSupplierCompanyName.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataSupplierCompanyName.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierEmail"></a>

## InvoiceDataSupplierEmail Objects

```python
class InvoiceDataSupplierEmail(
        TextAnnotation,
        Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1)
```

InvoiceDataSupplierEmail.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataSupplierEmail.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierFax"></a>

## InvoiceDataSupplierFax Objects

```python
class InvoiceDataSupplierFax(
        TextAnnotation,
        Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1)
```

InvoiceDataSupplierFax.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataSupplierFax.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierPhoneNumber"></a>

## InvoiceDataSupplierPhoneNumber Objects

```python
class InvoiceDataSupplierPhoneNumber(
        TextAnnotation,
        Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1
)
```

InvoiceDataSupplierPhoneNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataSupplierPhoneNumber.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierVat"></a>

## InvoiceDataSupplierVat Objects

```python
class InvoiceDataSupplierVat(
        TextAnnotation,
        ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1)
```

InvoiceDataSupplierVat.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataSupplierVat.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierWebsite"></a>

## InvoiceDataSupplierWebsite Objects

```python
class InvoiceDataSupplierWebsite(
        TextAnnotation,
        Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1)
```

InvoiceDataSupplierWebsite.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.InvoiceDataSupplierWebsite.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.JobDescription"></a>

## JobDescription Objects

```python
class JobDescription(Document)
```

JobDescription.

All required parameters must be populated in order to send to Azure.

:ivar extractor: Required. Constant filled by server.
:vartype extractor: str
:ivar meta: Required.
:vartype meta: ~affinda.models.DocumentMeta
:ivar error:
:vartype error: ~affinda.models.DocumentError
:ivar warnings:
:vartype warnings: list[~affinda.models.DocumentWarning]
:ivar data:
:vartype data: ~affinda.models.JobDescriptionData

<a id="models._models.JobDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `meta`: Required.
- `error`: 
- `warnings`: 
- `data`: 

<a id="models._models.JobDescriptionData"></a>

## JobDescriptionData Objects

```python
class JobDescriptionData(msrest.serialization.Model)
```

JobDescriptionData.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar job_title:
:vartype job_title: ~affinda.models.JobTitleAnnotation
:ivar contact_email:
:vartype contact_email: ~affinda.models.TextAnnotation
:ivar contact_name:
:vartype contact_name: ~affinda.models.TextAnnotation
:ivar contact_phone:
:vartype contact_phone: ~affinda.models.TextAnnotation
:ivar start_date:
:vartype start_date: ~affinda.models.DateAnnotation
:ivar end_date:
:vartype end_date: ~affinda.models.DateAnnotation
:ivar job_type:
:vartype job_type: ~affinda.models.TextAnnotation
:ivar languages:
:vartype languages: list[~affinda.models.LanguageAnnotation]
:ivar skills:
:vartype skills: list[~affinda.models.SkillAnnotation]
:ivar organization_name:
:vartype organization_name: ~affinda.models.TextAnnotation
:ivar organization_website:
:vartype organization_website: ~affinda.models.TextAnnotation
:ivar education_level:
:vartype education_level: ~affinda.models.TextAnnotation
:ivar education_accreditation:
:vartype education_accreditation: ~affinda.models.TextAnnotation
:ivar expected_remuneration:
:vartype expected_remuneration: ~affinda.models.ExpectedRemunerationAnnotation
:ivar location:
:vartype location: ~affinda.models.LocationAnnotation
:ivar certifications:
:vartype certifications: list[~affinda.models.TextAnnotation]
:ivar years_experience:
:vartype years_experience: ~affinda.models.YearsExperienceAnnotation
:ivar raw_text: All of the raw text of the parsed job description, example is shortened for
 readability.
:vartype raw_text: str

<a id="models._models.JobDescriptionData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `job_title`: 
- `contact_email`: 
- `contact_name`: 
- `contact_phone`: 
- `start_date`: 
- `end_date`: 
- `job_type`: 
- `languages`: 
- `skills`: 
- `organization_name`: 
- `organization_website`: 
- `education_level`: 
- `education_accreditation`: 
- `expected_remuneration`: 
- `location`: 
- `certifications`: 
- `years_experience`: 
- `raw_text`: All of the raw text of the parsed job description, example is shortened for
readability.

<a id="models._models.JobDescriptionDataUpdate"></a>

## JobDescriptionDataUpdate Objects

```python
class JobDescriptionDataUpdate(msrest.serialization.Model)
```

A JSON-encoded string of the ``JobDescriptionData`` object.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar job_title:
:vartype job_title: ~affinda.models.JobTitleAnnotationUpdate
:ivar contact_email:
:vartype contact_email: ~affinda.models.TextAnnotationUpdate
:ivar contact_name:
:vartype contact_name: ~affinda.models.TextAnnotationUpdate
:ivar contact_phone:
:vartype contact_phone: ~affinda.models.TextAnnotationUpdate
:ivar start_date:
:vartype start_date: ~affinda.models.DateAnnotationUpdate
:ivar end_date:
:vartype end_date: ~affinda.models.DateAnnotationUpdate
:ivar job_type:
:vartype job_type: ~affinda.models.TextAnnotationUpdate
:ivar languages:
:vartype languages: list[~affinda.models.LanguageAnnotationUpdate]
:ivar skills:
:vartype skills: list[~affinda.models.SkillAnnotationUpdate]
:ivar organization_name:
:vartype organization_name: ~affinda.models.TextAnnotationUpdate
:ivar organization_website:
:vartype organization_website: ~affinda.models.TextAnnotationUpdate
:ivar education_level:
:vartype education_level: ~affinda.models.TextAnnotationUpdate
:ivar education_accreditation:
:vartype education_accreditation: ~affinda.models.TextAnnotationUpdate
:ivar expected_remuneration:
:vartype expected_remuneration: ~affinda.models.ExpectedRemunerationAnnotationUpdate
:ivar location:
:vartype location: ~affinda.models.LocationAnnotationUpdate
:ivar certifications:
:vartype certifications: list[~affinda.models.TextAnnotationUpdate]
:ivar years_experience:
:vartype years_experience: ~affinda.models.YearsExperienceAnnotationUpdate

<a id="models._models.JobDescriptionDataUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `job_title`: 
- `contact_email`: 
- `contact_name`: 
- `contact_phone`: 
- `start_date`: 
- `end_date`: 
- `job_type`: 
- `languages`: 
- `skills`: 
- `organization_name`: 
- `organization_website`: 
- `education_level`: 
- `education_accreditation`: 
- `expected_remuneration`: 
- `location`: 
- `certifications`: 
- `years_experience`: 

<a id="models._models.JobDescriptionSearch"></a>

## JobDescriptionSearch Objects

```python
class JobDescriptionSearch(msrest.serialization.Model)
```

JobDescriptionSearch.

:ivar count: Total number of results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str
:ivar parameters:
:vartype parameters: ~affinda.models.JobDescriptionSearchParameters
:ivar results:
:vartype results: list[~affinda.models.JobDescriptionSearchResult]

<a id="models._models.JobDescriptionSearch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `count`: Total number of results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.
- `parameters`: 
- `results`: 

<a id="models._models.JobDescriptionSearchConfig"></a>

## JobDescriptionSearchConfig Objects

```python
class JobDescriptionSearchConfig(msrest.serialization.Model)
```

JobDescriptionSearchConfig.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar allow_pdf_download:
:vartype allow_pdf_download: bool
:ivar max_results: Maximum number of results that can be returned. Setting to "null" means no
 limitation.
:vartype max_results: int
:ivar display_job_title:
:vartype display_job_title: bool
:ivar display_location:
:vartype display_location: bool
:ivar display_years_experience:
:vartype display_years_experience: bool
:ivar display_occupation_group:
:vartype display_occupation_group: bool
:ivar display_education:
:vartype display_education: bool
:ivar display_skills:
:vartype display_skills: bool
:ivar display_languages:
:vartype display_languages: bool
:ivar display_management_level:
:vartype display_management_level: bool
:ivar display_keywords:
:vartype display_keywords: bool
:ivar weight_job_title:
:vartype weight_job_title: float
:ivar weight_location:
:vartype weight_location: float
:ivar weight_years_experience:
:vartype weight_years_experience: float
:ivar weight_occupation_group:
:vartype weight_occupation_group: float
:ivar weight_education:
:vartype weight_education: float
:ivar weight_skills:
:vartype weight_skills: float
:ivar weight_languages:
:vartype weight_languages: float
:ivar weight_management_level:
:vartype weight_management_level: float
:ivar weight_keywords:
:vartype weight_keywords: float
:ivar indices: List of index names.
:vartype indices: list[str]
:ivar show_index_dropdown: Controls whether or not the index dropdown is displayed to the user.
:vartype show_index_dropdown: bool
:ivar search_tool_theme: Customize the theme of the embeded search tool.
:vartype search_tool_theme: dict[str, any]
:ivar user_id: ID of the logged in user.
:vartype user_id: int
:ivar username: Username of the logged in user.
:vartype username: str
:ivar actions: A list of actions to show in the dropdown in the embedded search tool.
:vartype actions: list[~affinda.models.SearchConfigAction]
:ivar hide_toolbar: Hide the reset/import toolbar.
:vartype hide_toolbar: bool
:ivar hide_side_panel: Hide the entire side panel.
:vartype hide_side_panel: bool
:ivar custom_fields_config:
:vartype custom_fields_config: list[~affinda.models.CustomFieldConfig]

<a id="models._models.JobDescriptionSearchConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `allow_pdf_download`: 
- `max_results`: Maximum number of results that can be returned. Setting to "null" means
no limitation.
- `display_job_title`: 
- `display_location`: 
- `display_years_experience`: 
- `display_occupation_group`: 
- `display_education`: 
- `display_skills`: 
- `display_languages`: 
- `display_management_level`: 
- `display_keywords`: 
- `weight_job_title`: 
- `weight_location`: 
- `weight_years_experience`: 
- `weight_occupation_group`: 
- `weight_education`: 
- `weight_skills`: 
- `weight_languages`: 
- `weight_management_level`: 
- `weight_keywords`: 
- `indices`: List of index names.
- `show_index_dropdown`: Controls whether or not the index dropdown is displayed to the
user.
- `search_tool_theme`: Customize the theme of the embeded search tool.
- `actions`: A list of actions to show in the dropdown in the embedded search tool.
- `hide_toolbar`: Hide the reset/import toolbar.
- `hide_side_panel`: Hide the entire side panel.
- `custom_fields_config`: 

<a id="models._models.JobDescriptionSearchDetail"></a>

## JobDescriptionSearchDetail Objects

```python
class JobDescriptionSearchDetail(msrest.serialization.Model)
```

JobDescriptionSearchDetail.

:ivar job_title:
:vartype job_title: ~affinda.models.JobDescriptionSearchDetailJobTitle
:ivar location:
:vartype location: ~affinda.models.JobDescriptionSearchDetailLocation
:ivar education:
:vartype education: ~affinda.models.JobDescriptionSearchDetailEducation
:ivar skills:
:vartype skills: ~affinda.models.JobDescriptionSearchDetailSkills
:ivar experience:
:vartype experience: ~affinda.models.JobDescriptionSearchDetailExperience
:ivar occupation_group:
:vartype occupation_group: ~affinda.models.JobDescriptionSearchDetailOccupationGroup
:ivar languages:
:vartype languages: ~affinda.models.JobDescriptionSearchDetailLanguages
:ivar management_level:
:vartype management_level: ~affinda.models.JobDescriptionSearchDetailManagementLevel
:ivar search_expression:
:vartype search_expression: ~affinda.models.JobDescriptionSearchDetailSearchExpression

<a id="models._models.JobDescriptionSearchDetail.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `job_title`: 
- `location`: 
- `education`: 
- `skills`: 
- `experience`: 
- `occupation_group`: 
- `languages`: 
- `management_level`: 
- `search_expression`: 

<a id="models._models.JobDescriptionSearchDetailEducation"></a>

## JobDescriptionSearchDetailEducation Objects

```python
class JobDescriptionSearchDetailEducation(msrest.serialization.Model)
```

JobDescriptionSearchDetailEducation.

:ivar missing:
:vartype missing: ~affinda.models.JobDescriptionSearchDetailEducationMissing
:ivar value:
:vartype value: ~affinda.models.JobDescriptionSearchDetailEducationValue

<a id="models._models.JobDescriptionSearchDetailEducation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.JobDescriptionSearchDetailEducationMissing"></a>

## JobDescriptionSearchDetailEducationMissing Objects

```python
class JobDescriptionSearchDetailEducationMissing(msrest.serialization.Model)
```

JobDescriptionSearchDetailEducationMissing.

:ivar degrees:
:vartype degrees: list[str]
:ivar degree_types:
:vartype degree_types: list[str]

<a id="models._models.JobDescriptionSearchDetailEducationMissing.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `degrees`: 
- `degree_types`: 

<a id="models._models.JobDescriptionSearchDetailEducationValue"></a>

## JobDescriptionSearchDetailEducationValue Objects

```python
class JobDescriptionSearchDetailEducationValue(msrest.serialization.Model)
```

JobDescriptionSearchDetailEducationValue.

:ivar degrees:
:vartype degrees: list[str]
:ivar degree_types:
:vartype degree_types: list[str]
:ivar match:
:vartype match: bool

<a id="models._models.JobDescriptionSearchDetailEducationValue.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `degrees`: 
- `degree_types`: 
- `match`: 

<a id="models._models.JobDescriptionSearchDetailExperience"></a>

## JobDescriptionSearchDetailExperience Objects

```python
class JobDescriptionSearchDetailExperience(msrest.serialization.Model)
```

JobDescriptionSearchDetailExperience.

:ivar minimum_experience:
:vartype minimum_experience: int
:ivar maximum_experience:
:vartype maximum_experience: int
:ivar match:
:vartype match: bool

<a id="models._models.JobDescriptionSearchDetailExperience.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `minimum_experience`: 
- `maximum_experience`: 
- `match`: 

<a id="models._models.JobDescriptionSearchDetailJobTitle"></a>

## JobDescriptionSearchDetailJobTitle Objects

```python
class JobDescriptionSearchDetailJobTitle(msrest.serialization.Model)
```

JobDescriptionSearchDetailJobTitle.

:ivar missing:
:vartype missing: list[str]
:ivar value:
:vartype value: ~affinda.models.JobDescriptionSearchDetailJobTitleValue

<a id="models._models.JobDescriptionSearchDetailJobTitle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.JobDescriptionSearchDetailJobTitleValue"></a>

## JobDescriptionSearchDetailJobTitleValue Objects

```python
class JobDescriptionSearchDetailJobTitleValue(msrest.serialization.Model)
```

JobDescriptionSearchDetailJobTitleValue.

:ivar name:
:vartype name: str
:ivar company_name:
:vartype company_name: str
:ivar match:
:vartype match: bool

<a id="models._models.JobDescriptionSearchDetailJobTitleValue.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `company_name`: 
- `match`: 

<a id="models._models.JobDescriptionSearchDetailLanguages"></a>

## JobDescriptionSearchDetailLanguages Objects

```python
class JobDescriptionSearchDetailLanguages(msrest.serialization.Model)
```

JobDescriptionSearchDetailLanguages.

:ivar missing:
:vartype missing: list[~affinda.models.ResumeSearchParametersSkill]
:ivar value:
:vartype value: list[~affinda.models.JobDescriptionSearchDetailLanguagesValueItem]

<a id="models._models.JobDescriptionSearchDetailLanguages.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.JobDescriptionSearchDetailLanguagesValueItem"></a>

## JobDescriptionSearchDetailLanguagesValueItem Objects

```python
class JobDescriptionSearchDetailLanguagesValueItem(msrest.serialization.Model)
```

JobDescriptionSearchDetailLanguagesValueItem.

:ivar name:
:vartype name: str
:ivar match:
:vartype match: bool

<a id="models._models.JobDescriptionSearchDetailLanguagesValueItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `match`: 

<a id="models._models.JobDescriptionSearchDetailLocation"></a>

## JobDescriptionSearchDetailLocation Objects

```python
class JobDescriptionSearchDetailLocation(msrest.serialization.Model)
```

JobDescriptionSearchDetailLocation.

:ivar missing:
:vartype missing: list[~affinda.models.ResumeSearchParametersLocation]
:ivar value:
:vartype value: ~affinda.models.JobDescriptionSearchDetailLocationValue

<a id="models._models.JobDescriptionSearchDetailLocation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.Location"></a>

## Location Objects

```python
class Location(msrest.serialization.Model)
```

Location.

Variables are only populated by the server, and will be ignored when sending a request.

All required parameters must be populated in order to send to Azure.

:ivar formatted:
:vartype formatted: str
:ivar postal_code:
:vartype postal_code: str
:ivar state:
:vartype state: str
:ivar country:
:vartype country: str
:ivar country_code: Two letter country code (ISO 3166-1 alpha-2).
:vartype country_code: str
:ivar raw_input: Required.
:vartype raw_input: str
:ivar street_number:
:vartype street_number: str
:ivar street:
:vartype street: str
:ivar apartment_number:
:vartype apartment_number: str
:ivar city:
:vartype city: str
:ivar latitude:
:vartype latitude: float
:ivar longitude:
:vartype longitude: float

<a id="models._models.Location.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw_input`: Required.

<a id="models._models.JobDescriptionSearchDetailLocationValue"></a>

## JobDescriptionSearchDetailLocationValue Objects

```python
class JobDescriptionSearchDetailLocationValue(
        Location,
        Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1
)
```

JobDescriptionSearchDetailLocationValue.

Variables are only populated by the server, and will be ignored when sending a request.

All required parameters must be populated in order to send to Azure.

:ivar match:
:vartype match: bool
:ivar formatted:
:vartype formatted: str
:ivar postal_code:
:vartype postal_code: str
:ivar state:
:vartype state: str
:ivar country:
:vartype country: str
:ivar country_code: Two letter country code (ISO 3166-1 alpha-2).
:vartype country_code: str
:ivar raw_input: Required.
:vartype raw_input: str
:ivar street_number:
:vartype street_number: str
:ivar street:
:vartype street: str
:ivar apartment_number:
:vartype apartment_number: str
:ivar city:
:vartype city: str
:ivar latitude:
:vartype latitude: float
:ivar longitude:
:vartype longitude: float

<a id="models._models.JobDescriptionSearchDetailLocationValue.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 
- `raw_input`: Required.

<a id="models._models.JobDescriptionSearchDetailManagementLevel"></a>

## JobDescriptionSearchDetailManagementLevel Objects

```python
class JobDescriptionSearchDetailManagementLevel(msrest.serialization.Model)
```

JobDescriptionSearchDetailManagementLevel.

:ivar level: Known values are: "None", "Low", "Mid", "Upper".
:vartype level: str or ~affinda.models.ManagementLevel
:ivar match:
:vartype match: bool

<a id="models._models.JobDescriptionSearchDetailManagementLevel.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `level`: Known values are: "None", "Low", "Mid", "Upper".
- `match`: 

<a id="models._models.JobDescriptionSearchDetailOccupationGroup"></a>

## JobDescriptionSearchDetailOccupationGroup Objects

```python
class JobDescriptionSearchDetailOccupationGroup(msrest.serialization.Model)
```

JobDescriptionSearchDetailOccupationGroup.

:ivar missing:
:vartype missing: list[int]
:ivar value:
:vartype value: ~affinda.models.JobDescriptionSearchDetailOccupationGroupValue

<a id="models._models.JobDescriptionSearchDetailOccupationGroup.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.OccupationGroupSearchResult"></a>

## OccupationGroupSearchResult Objects

```python
class OccupationGroupSearchResult(msrest.serialization.Model)
```

OccupationGroupSearchResult.

All required parameters must be populated in order to send to Azure.

:ivar match:
:vartype match: bool
:ivar code: Required.
:vartype code: int
:ivar name: Required.
:vartype name: str
:ivar children:
:vartype children: list[~affinda.models.OccupationGroup]
:ivar parents:
:vartype parents: list[~affinda.models.OccupationGroup]

<a id="models._models.OccupationGroupSearchResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 
- `code`: Required.
- `name`: Required.
- `children`: 
- `parents`: 

<a id="models._models.JobDescriptionSearchDetailOccupationGroupValue"></a>

## JobDescriptionSearchDetailOccupationGroupValue Objects

```python
class JobDescriptionSearchDetailOccupationGroupValue(
        OccupationGroupSearchResult)
```

JobDescriptionSearchDetailOccupationGroupValue.

All required parameters must be populated in order to send to Azure.

:ivar match:
:vartype match: bool
:ivar code: Required.
:vartype code: int
:ivar name: Required.
:vartype name: str
:ivar children:
:vartype children: list[~affinda.models.OccupationGroup]
:ivar parents:
:vartype parents: list[~affinda.models.OccupationGroup]

<a id="models._models.JobDescriptionSearchDetailOccupationGroupValue.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 
- `code`: Required.
- `name`: Required.
- `children`: 
- `parents`: 

<a id="models._models.JobDescriptionSearchDetailSearchExpression"></a>

## JobDescriptionSearchDetailSearchExpression Objects

```python
class JobDescriptionSearchDetailSearchExpression(msrest.serialization.Model)
```

JobDescriptionSearchDetailSearchExpression.

:ivar missing:
:vartype missing: list[str]
:ivar value:
:vartype value: list[str]

<a id="models._models.JobDescriptionSearchDetailSearchExpression.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.JobDescriptionSearchDetailSkills"></a>

## JobDescriptionSearchDetailSkills Objects

```python
class JobDescriptionSearchDetailSkills(msrest.serialization.Model)
```

JobDescriptionSearchDetailSkills.

:ivar missing:
:vartype missing: list[~affinda.models.ResumeSearchParametersSkill]
:ivar value:
:vartype value: list[~affinda.models.JobDescriptionSearchDetailSkillsValueItem]

<a id="models._models.JobDescriptionSearchDetailSkills.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.JobDescriptionSearchDetailSkillsValueItem"></a>

## JobDescriptionSearchDetailSkillsValueItem Objects

```python
class JobDescriptionSearchDetailSkillsValueItem(msrest.serialization.Model)
```

JobDescriptionSearchDetailSkillsValueItem.

:ivar name:
:vartype name: str
:ivar match:
:vartype match: bool

<a id="models._models.JobDescriptionSearchDetailSkillsValueItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `match`: 

<a id="models._models.JobDescriptionSearchEmbed"></a>

## JobDescriptionSearchEmbed Objects

```python
class JobDescriptionSearchEmbed(msrest.serialization.Model)
```

JobDescriptionSearchEmbed.

:ivar url: The signed URL for the embedable search tool.
:vartype url: str

<a id="models._models.JobDescriptionSearchEmbed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `url`: The signed URL for the embedable search tool.

<a id="models._models.JobDescriptionSearchParameters"></a>

## JobDescriptionSearchParameters Objects

```python
class JobDescriptionSearchParameters(msrest.serialization.Model)
```

JobDescriptionSearchParameters.

All required parameters must be populated in order to send to Azure.

:ivar indices: Required.
:vartype indices: list[str]
:ivar resume: A random string that uniquely identify the resource.
:vartype resume: str
:ivar job_titles:
:vartype job_titles: list[str]
:ivar job_titles_required:
:vartype job_titles_required: bool
:ivar job_titles_weight:
:vartype job_titles_weight: float
:ivar total_years_experience:
:vartype total_years_experience: float
:ivar years_experience_required:
:vartype years_experience_required: bool
:ivar years_experience_weight:
:vartype years_experience_weight: float
:ivar locations:
:vartype locations: list[~affinda.models.ResumeSearchParametersLocation]
:ivar locations_weight:
:vartype locations_weight: float
:ivar locations_required:
:vartype locations_required: bool
:ivar skills:
:vartype skills: list[~affinda.models.ResumeSearchParametersSkill]
:ivar skills_weight:
:vartype skills_weight: float
:ivar languages:
:vartype languages: list[~affinda.models.ResumeSearchParametersSkill]
:ivar languages_weight:
:vartype languages_weight: float
:ivar degrees:
:vartype degrees: list[str]
:ivar degrees_required:
:vartype degrees_required: bool
:ivar degree_types:
:vartype degree_types: list[str or ~affinda.models.EducationLevel]
:ivar degree_types_required:
:vartype degree_types_required: bool
:ivar education_weight:
:vartype education_weight: float
:ivar search_expression:
:vartype search_expression: str
:ivar search_expression_required:
:vartype search_expression_required: bool
:ivar search_expression_weight:
:vartype search_expression_weight: float
:ivar soc_codes:
:vartype soc_codes: list[int]
:ivar soc_codes_weight:
:vartype soc_codes_weight: float
:ivar soc_codes_required:
:vartype soc_codes_required: bool
:ivar management_level: Known values are: "None", "Low", "Mid", "Upper".
:vartype management_level: str or ~affinda.models.ManagementLevel
:ivar management_level_required:
:vartype management_level_required: bool
:ivar management_level_weight:
:vartype management_level_weight: float
:ivar custom_data:
:vartype custom_data: list[~affinda.models.SearchParametersCustomData]

<a id="models._models.JobDescriptionSearchParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `indices`: Required.
- `resume`: A random string that uniquely identify the resource.
- `job_titles`: 
- `job_titles_required`: 
- `job_titles_weight`: 
- `total_years_experience`: 
- `years_experience_required`: 
- `years_experience_weight`: 
- `locations`: 
- `locations_weight`: 
- `locations_required`: 
- `skills`: 
- `skills_weight`: 
- `languages`: 
- `languages_weight`: 
- `degrees`: 
- `degrees_required`: 
- `degree_types`: 
- `degree_types_required`: 
- `education_weight`: 
- `search_expression`: 
- `search_expression_required`: 
- `search_expression_weight`: 
- `soc_codes`: 
- `soc_codes_weight`: 
- `soc_codes_required`: 
- `management_level`: Known values are: "None", "Low", "Mid", "Upper".
- `management_level_required`: 
- `management_level_weight`: 
- `custom_data`: 

<a id="models._models.JobDescriptionSearchResult"></a>

## JobDescriptionSearchResult Objects

```python
class JobDescriptionSearchResult(msrest.serialization.Model)
```

JobDescriptionSearchResult.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. A random string that uniquely identify the resource.
:vartype identifier: str
:ivar score: Required.
:vartype score: float
:ivar pdf: Required.
:vartype pdf: str
:ivar job_title: Required.
:vartype job_title: ~affinda.models.JobTitleSearchScoreComponent
:ivar management_level: Required.
:vartype management_level: ~affinda.models.ManagementLevelSearchScoreComponent
:ivar experience: Required.
:vartype experience: ~affinda.models.ExperienceSearchScoreComponent
:ivar skills: Required.
:vartype skills: ~affinda.models.SkillsSearchScoreComponent
:ivar languages: Required.
:vartype languages: ~affinda.models.LanguagesSearchScoreComponent
:ivar location: Required.
:vartype location: ~affinda.models.LocationSearchScoreComponent
:ivar education: Required.
:vartype education: ~affinda.models.EducationSearchScoreComponent
:ivar occupation_group:
:vartype occupation_group: ~affinda.models.OccupationGroupSearchScoreComponent
:ivar search_expression: Required.
:vartype search_expression: ~affinda.models.SearchExpressionSearchScoreComponent
:ivar organization_name: Required.
:vartype organization_name: str
:ivar custom_data: Required. Dictionary of
 <components·nqbw24·schemas·customdatasearchscorecomponent·additionalproperties>.
:vartype custom_data: dict[str,
 ~affinda.models.ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties]

<a id="models._models.JobDescriptionSearchResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. A random string that uniquely identify the resource.
- `score`: Required.
- `pdf`: Required.
- `job_title`: Required.
- `management_level`: Required.
- `experience`: Required.
- `skills`: Required.
- `languages`: Required.
- `location`: Required.
- `education`: Required.
- `occupation_group`: 
- `search_expression`: Required.
- `organization_name`: Required.
- `custom_data`: Required. Dictionary of
<components·nqbw24·schemas·customdatasearchscorecomponent·additionalproperties>.

<a id="models._models.JobTitleAnnotation"></a>

## JobTitleAnnotation Objects

```python
class JobTitleAnnotation(Annotation)
```

JobTitleAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed: Years of experience range.
:vartype parsed: ~affinda.models.JobTitleAnnotationParsed

<a id="models._models.JobTitleAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: Years of experience range.

<a id="models._models.JobTitleAnnotationParsed"></a>

## JobTitleAnnotationParsed Objects

```python
class JobTitleAnnotationParsed(msrest.serialization.Model)
```

Years of experience range.

:ivar name:
:vartype name: str
:ivar management_level:
:vartype management_level: str
:ivar classification:
:vartype classification: ~affinda.models.JobTitleAnnotationParsedClassification

<a id="models._models.JobTitleAnnotationParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `management_level`: 
- `classification`: 

<a id="models._models.JobTitleAnnotationParsedClassification"></a>

## JobTitleAnnotationParsedClassification Objects

```python
class JobTitleAnnotationParsedClassification(msrest.serialization.Model)
```

JobTitleAnnotationParsedClassification.

:ivar soc_code:
:vartype soc_code: float
:ivar title:
:vartype title: str
:ivar minor_group:
:vartype minor_group: str
:ivar sub_major_group:
:vartype sub_major_group: str
:ivar major_group:
:vartype major_group: str
:ivar minor_group_code: The 4 digit code representing the SOC2020 classification for this job
 title.
:vartype minor_group_code: int
:ivar sub_major_group_code: The 4 digit code representing the SOC2020 classification for this
 job title.
:vartype sub_major_group_code: int
:ivar major_group_code: The 4 digit code representing the SOC2020 classification for this job
 title.
:vartype major_group_code: int

<a id="models._models.JobTitleAnnotationParsedClassification.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `soc_code`: 
- `title`: 
- `minor_group`: 
- `sub_major_group`: 
- `major_group`: 
- `minor_group_code`: The 4 digit code representing the SOC2020 classification for this
job title.
- `sub_major_group_code`: The 4 digit code representing the SOC2020 classification for
this job title.
- `major_group_code`: The 4 digit code representing the SOC2020 classification for this
job title.

<a id="models._models.JobTitleParsed"></a>

## JobTitleParsed Objects

```python
class JobTitleParsed(msrest.serialization.Model)
```

JobTitleParsed.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar parsed: Matching job title to extracted text.
:vartype parsed: ~affinda.models.JobTitleParsedParsed

<a id="models._models.JobTitleParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```



<a id="models._models.JobTitleAnnotationUpdate"></a>

## JobTitleAnnotationUpdate Objects

```python
class JobTitleAnnotationUpdate(AnnotationBase, JobTitleParsed)
```

JobTitleAnnotationUpdate.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar parsed: Matching job title to extracted text.
:vartype parsed: ~affinda.models.JobTitleParsedParsed
:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle:
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles:
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar page_index:
:vartype page_index: int
:ivar raw:
:vartype raw: str
:ivar confidence: The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: The model's confidence that the text has been classified
 correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: If the document was submitted as an image, this is the
 confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified:
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar data_point:
:vartype data_point: str
:ivar content_type:
:vartype content_type: str

<a id="models._models.JobTitleAnnotationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: 
- `page_index`: 
- `raw`: 
- `confidence`: The overall confidence that the model's prediction is correct.
- `classification_confidence`: The model's confidence that the text has been classified
correctly.
- `text_extraction_confidence`: If the document was submitted as an image, this is the
confidence that the text in the image has been correctly read by the model.
- `is_verified`: 
- `is_client_verified`: 
- `is_auto_verified`: 
- `data_point`: 
- `content_type`: 

<a id="models._models.JobTitleParsedClassification"></a>

## JobTitleParsedClassification Objects

```python
class JobTitleParsedClassification(msrest.serialization.Model)
```

JobTitleParsedClassification.

:ivar soc_code:
:vartype soc_code: float
:ivar title:
:vartype title: str
:ivar minor_group:
:vartype minor_group: str
:ivar sub_major_group:
:vartype sub_major_group: str
:ivar major_group:
:vartype major_group: str
:ivar minor_group_code: The 4 digit code representing the SOC2020 classification for this job
 title.
:vartype minor_group_code: int
:ivar sub_major_group_code: The 4 digit code representing the SOC2020 classification for this
 job title.
:vartype sub_major_group_code: int
:ivar major_group_code: The 4 digit code representing the SOC2020 classification for this job
 title.
:vartype major_group_code: int

<a id="models._models.JobTitleParsedClassification.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `soc_code`: 
- `title`: 
- `minor_group`: 
- `sub_major_group`: 
- `major_group`: 
- `minor_group_code`: The 4 digit code representing the SOC2020 classification for this
job title.
- `sub_major_group_code`: The 4 digit code representing the SOC2020 classification for
this job title.
- `major_group_code`: The 4 digit code representing the SOC2020 classification for this
job title.

<a id="models._models.JobTitleParsedParsed"></a>

## JobTitleParsedParsed Objects

```python
class JobTitleParsedParsed(msrest.serialization.Model)
```

Matching job title to extracted text.

:ivar name:
:vartype name: str
:ivar management_level:
:vartype management_level: str
:ivar classification:
:vartype classification: ~affinda.models.JobTitleParsedClassification

<a id="models._models.JobTitleParsedParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `management_level`: 
- `classification`: 

<a id="models._models.JobTitleSearchScoreComponent"></a>

## JobTitleSearchScoreComponent Objects

```python
class JobTitleSearchScoreComponent(msrest.serialization.Model)
```

JobTitleSearchScoreComponent.

All required parameters must be populated in order to send to Azure.

:ivar value:
:vartype value: str
:ivar label: Required.
:vartype label: str
:ivar score:
:vartype score: float

<a id="models._models.JobTitleSearchScoreComponent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `value`: 
- `label`: Required.
- `score`: 

<a id="models._models.LanguageAnnotation"></a>

## LanguageAnnotation Objects

```python
class LanguageAnnotation(Annotation)
```

LanguageAnnotation.

Variables are only populated by the server, and will be ignored when sending a request.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.LanguageAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.

<a id="models._models.LanguageAnnotationUpdate"></a>

## LanguageAnnotationUpdate Objects

```python
class LanguageAnnotationUpdate(AnnotationBase)
```

LanguageAnnotationUpdate.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle:
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles:
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar page_index:
:vartype page_index: int
:ivar raw:
:vartype raw: str
:ivar confidence: The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: The model's confidence that the text has been classified
 correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: If the document was submitted as an image, this is the
 confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified:
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar data_point:
:vartype data_point: str
:ivar content_type:
:vartype content_type: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.LanguageAnnotationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: 
- `page_index`: 
- `raw`: 
- `confidence`: The overall confidence that the model's prediction is correct.
- `classification_confidence`: The model's confidence that the text has been classified
correctly.
- `text_extraction_confidence`: If the document was submitted as an image, this is the
confidence that the text in the image has been correctly read by the model.
- `is_verified`: 
- `is_client_verified`: 
- `is_auto_verified`: 
- `data_point`: 
- `content_type`: 

<a id="models._models.LanguagesSearchScoreComponent"></a>

## LanguagesSearchScoreComponent Objects

```python
class LanguagesSearchScoreComponent(msrest.serialization.Model)
```

LanguagesSearchScoreComponent.

All required parameters must be populated in order to send to Azure.

:ivar value:
:vartype value: str
:ivar label: Required.
:vartype label: str
:ivar score:
:vartype score: float

<a id="models._models.LanguagesSearchScoreComponent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `value`: 
- `label`: Required.
- `score`: 

<a id="models._models.LocationAnnotation"></a>

## LocationAnnotation Objects

```python
class LocationAnnotation(Annotation)
```

LocationAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~affinda.models.Location

<a id="models._models.LocationAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.LocationAnnotationUpdate"></a>

## LocationAnnotationUpdate Objects

```python
class LocationAnnotationUpdate(AnnotationBase)
```

LocationAnnotationUpdate.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle:
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles:
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar page_index:
:vartype page_index: int
:ivar raw:
:vartype raw: str
:ivar confidence: The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: The model's confidence that the text has been classified
 correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: If the document was submitted as an image, this is the
 confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified:
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar data_point:
:vartype data_point: str
:ivar content_type:
:vartype content_type: str
:ivar parsed:
:vartype parsed: ~affinda.models.LocationAnnotationUpdateParsed

<a id="models._models.LocationAnnotationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: 
- `page_index`: 
- `raw`: 
- `confidence`: The overall confidence that the model's prediction is correct.
- `classification_confidence`: The model's confidence that the text has been classified
correctly.
- `text_extraction_confidence`: If the document was submitted as an image, this is the
confidence that the text in the image has been correctly read by the model.
- `is_verified`: 
- `is_client_verified`: 
- `is_auto_verified`: 
- `data_point`: 
- `content_type`: 

<a id="models._models.LocationAnnotationUpdateParsed"></a>

## LocationAnnotationUpdateParsed Objects

```python
class LocationAnnotationUpdateParsed(Location)
```

LocationAnnotationUpdateParsed.

Variables are only populated by the server, and will be ignored when sending a request.

All required parameters must be populated in order to send to Azure.

:ivar formatted:
:vartype formatted: str
:ivar postal_code:
:vartype postal_code: str
:ivar state:
:vartype state: str
:ivar country:
:vartype country: str
:ivar country_code: Two letter country code (ISO 3166-1 alpha-2).
:vartype country_code: str
:ivar raw_input: Required.
:vartype raw_input: str
:ivar street_number:
:vartype street_number: str
:ivar street:
:vartype street: str
:ivar apartment_number:
:vartype apartment_number: str
:ivar city:
:vartype city: str
:ivar latitude:
:vartype latitude: float
:ivar longitude:
:vartype longitude: float

<a id="models._models.LocationAnnotationUpdateParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw_input`: Required.

<a id="models._models.LocationSearchScoreComponent"></a>

## LocationSearchScoreComponent Objects

```python
class LocationSearchScoreComponent(msrest.serialization.Model)
```

LocationSearchScoreComponent.

All required parameters must be populated in order to send to Azure.

:ivar value:
:vartype value: str
:ivar label: Required.
:vartype label: str
:ivar score:
:vartype score: float

<a id="models._models.LocationSearchScoreComponent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `value`: 
- `label`: Required.
- `score`: 

<a id="models._models.ManagementLevelSearchScoreComponent"></a>

## ManagementLevelSearchScoreComponent Objects

```python
class ManagementLevelSearchScoreComponent(msrest.serialization.Model)
```

ManagementLevelSearchScoreComponent.

All required parameters must be populated in order to send to Azure.

:ivar value:
:vartype value: str
:ivar label: Required.
:vartype label: str
:ivar score:
:vartype score: float

<a id="models._models.ManagementLevelSearchScoreComponent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `value`: 
- `label`: Required.
- `score`: 

<a id="models._models.Mapping"></a>

## Mapping Objects

```python
class Mapping(msrest.serialization.Model)
```

A mapping allows you to specify specific settings regarding a lookup against a MappingDataSource should be applied.

Variables are only populated by the server, and will be ignored when sending a request.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify a mapping.
:vartype identifier: str
:ivar organization: The organization that this mapping belongs to.
:vartype organization: str
:ivar data_source: Required. The mapping data source this mapping applies to.
:vartype data_source: str
:ivar score_cutoff: Higher values will result in more strict matching.
:vartype score_cutoff: float

<a id="models._models.Mapping.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `organization`: The organization that this mapping belongs to.
- `data_source`: Required. The mapping data source this mapping applies to.
- `score_cutoff`: Higher values will result in more strict matching.

<a id="models._models.MappingCreate"></a>

## MappingCreate Objects

```python
class MappingCreate(msrest.serialization.Model)
```

MappingCreate.

All required parameters must be populated in order to send to Azure.

:ivar data_source: Required. The mapping data source this mapping applies to.
:vartype data_source: str
:ivar score_cutoff: Higher values will result in more strict matching.
:vartype score_cutoff: float
:ivar organization: The organization that this mapping belongs to.
:vartype organization: str

<a id="models._models.MappingCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `data_source`: Required. The mapping data source this mapping applies to.
- `score_cutoff`: Higher values will result in more strict matching.
- `organization`: The organization that this mapping belongs to.

<a id="models._models.MappingDataSource"></a>

## MappingDataSource Objects

```python
class MappingDataSource(msrest.serialization.Model)
```

A mapping data source is used to map from raw data found by our AI models to records in your database.

Variables are only populated by the server, and will be ignored when sending a request.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify a mapping data source.
:vartype identifier: str
:ivar name:
:vartype name: str
:ivar key_property: Required. Attribute in the schema which uniquely identifiers the value.
:vartype key_property: str
:ivar display_property: Required. Attribute in the schema which is used to display the value.
:vartype display_property: str
:ivar organization: Required. The organization that this mapping data source belongs to.
:vartype organization: str
:ivar schema: The schema of the mapping data source.
:vartype schema: any

<a id="models._models.MappingDataSource.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `key_property`: Required. Attribute in the schema which uniquely identifiers the value.
- `display_property`: Required. Attribute in the schema which is used to display the
value.
- `organization`: Required. The organization that this mapping data source belongs to.
- `schema`: The schema of the mapping data source.

<a id="models._models.MappingDataSourceCreate"></a>

## MappingDataSourceCreate Objects

```python
class MappingDataSourceCreate(msrest.serialization.Model)
```

A mapping data source is used to map from raw data found by our AI models to records in your database.

All required parameters must be populated in order to send to Azure.

:ivar name:
:vartype name: str
:ivar organization: Required. The organization that this mapping data source belongs to.
:vartype organization: str
:ivar key_property: Attribute in the schema which uniquely identifiers the value.
:vartype key_property: str
:ivar display_property: Attribute in the schema which is used to display the value.
:vartype display_property: str
:ivar values:
:vartype values: list[any]
:ivar schema: The schema of the mapping data source.
:vartype schema: any

<a id="models._models.MappingDataSourceCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `organization`: Required. The organization that this mapping data source belongs to.
- `key_property`: Attribute in the schema which uniquely identifiers the value.
- `display_property`: Attribute in the schema which is used to display the value.
- `values`: 
- `schema`: The schema of the mapping data source.

<a id="models._models.MappingUpdate"></a>

## MappingUpdate Objects

```python
class MappingUpdate(msrest.serialization.Model)
```

MappingUpdate.

:ivar score_cutoff: Higher values will result in more strict matching.
:vartype score_cutoff: float

<a id="models._models.MappingUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `score_cutoff`: Higher values will result in more strict matching.

<a id="models._models.Meta"></a>

## Meta Objects

```python
class Meta(msrest.serialization.Model)
```

Meta.

:ivar identifier: Unique identifier for the document.
:vartype identifier: str
:ivar custom_identifier: Optional identifier for the document that you can set to track the
 document in the Affinda system.  Is not required to be unique.
:vartype custom_identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar ready: If true, the document has finished processing. Particularly useful if an endpoint
 request specified wait=False, when polling use this variable to determine when to stop polling.
:vartype ready: bool
:ivar ready_dt: The datetime when the document was ready.
:vartype ready_dt: ~datetime.datetime
:ivar failed: If true, some exception was raised during processing. Check the 'error' field of
 the main return object.
:vartype failed: bool
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: ~datetime.datetime
:ivar language: The document's language.
:vartype language: str
:ivar pdf: The URL to the document's pdf (if the uploaded document is not already pdf, it's
 converted to pdf as part of the parsing process).
:vartype pdf: str
:ivar parent_document: If this document is part of a splitted document, this attribute points
 to the original document that this document is splitted from.
:vartype parent_document: ~affinda.models.MetaParentDocument
:ivar child_documents: If this document has been splitted into a number of child documents,
 this attribute points to those child documents.
:vartype child_documents: list[~affinda.models.MetaChildDocumentsItem]
:ivar pages: The document's pages.
:vartype pages: list[~affinda.models.PageMeta]
:ivar is_verified: This is true if the 'confirm' button has been clicked in the Affinda
 validation tool.
:vartype is_verified: bool
:ivar review_url: Signed URL (valid for 60 minutes) to access the validation tool.  Not
 applicable for documents types such a resumes.
:vartype review_url: str
:ivar ocr_confidence: The overall confidence in the conversion of image to text.  (only
 applicable for images or PDF documents without a text layer).
:vartype ocr_confidence: float
:ivar created_dt:
:vartype created_dt: ~datetime.datetime
:ivar document_type:
:vartype document_type: str
:ivar region_bias:
:vartype region_bias: ~affinda.models.RegionBias

<a id="models._models.Meta.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Unique identifier for the document.
- `custom_identifier`: Optional identifier for the document that you can set to track the
document in the Affinda system.  Is not required to be unique.
- `file_name`: Optional filename of the file.
- `ready`: If true, the document has finished processing. Particularly useful if an
endpoint request specified wait=False, when polling use this variable to determine when to stop
polling.
- `ready_dt`: The datetime when the document was ready.
- `failed`: If true, some exception was raised during processing. Check the 'error' field
of the main return object.
- `expiry_time`: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.
- `language`: The document's language.
- `pdf`: The URL to the document's pdf (if the uploaded document is not already pdf, it's
converted to pdf as part of the parsing process).
- `parent_document`: If this document is part of a splitted document, this attribute
points to the original document that this document is splitted from.
- `child_documents`: If this document has been splitted into a number of child documents,
this attribute points to those child documents.
- `pages`: The document's pages.
- `is_verified`: This is true if the 'confirm' button has been clicked in the Affinda
validation tool.
- `review_url`: Signed URL (valid for 60 minutes) to access the validation tool.  Not
applicable for documents types such a resumes.
- `ocr_confidence`: The overall confidence in the conversion of image to text.  (only
applicable for images or PDF documents without a text layer).
- `created_dt`: 
- `document_type`: 
- `region_bias`: 

<a id="models._models.MetaChildDocumentsItem"></a>

## MetaChildDocumentsItem Objects

```python
class MetaChildDocumentsItem(msrest.serialization.Model)
```

MetaChildDocumentsItem.

:ivar identifier: Unique identifier for the document.
:vartype identifier: str

<a id="models._models.MetaChildDocumentsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Unique identifier for the document.

<a id="models._models.MetaParentDocument"></a>

## MetaParentDocument Objects

```python
class MetaParentDocument(msrest.serialization.Model)
```

If this document is part of a splitted document, this attribute points to the original document that this document is splitted from.

:ivar identifier: Unique identifier for the document.
:vartype identifier: str

<a id="models._models.MetaParentDocument.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Unique identifier for the document.

<a id="models._models.OccupationGroup"></a>

## OccupationGroup Objects

```python
class OccupationGroup(msrest.serialization.Model)
```

OccupationGroup.

All required parameters must be populated in order to send to Azure.

:ivar code: Required.
:vartype code: int
:ivar name: Required.
:vartype name: str
:ivar children: Required.
:vartype children: list[~affinda.models.OccupationGroup]

<a id="models._models.OccupationGroup.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `code`: Required.
- `name`: Required.
- `children`: Required.

<a id="models._models.OccupationGroupSearchScoreComponent"></a>

## OccupationGroupSearchScoreComponent Objects

```python
class OccupationGroupSearchScoreComponent(msrest.serialization.Model)
```

OccupationGroupSearchScoreComponent.

All required parameters must be populated in order to send to Azure.

:ivar value:
:vartype value: str
:ivar label: Required.
:vartype label: str
:ivar score:
:vartype score: float

<a id="models._models.OccupationGroupSearchScoreComponent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `value`: 
- `label`: Required.
- `score`: 

<a id="models._models.Organization"></a>

## Organization Objects

```python
class Organization(msrest.serialization.Model)
```

Organization.

:ivar identifier: Uniquely identify an organization.
:vartype identifier: str
:ivar name:
:vartype name: str
:ivar user_role: The role of the logged in user within the organization. Known values are:
 "admin", "member".
:vartype user_role: str or ~affinda.models.OrganizationUserRole
:ivar avatar: URL of the organization's avatar.
:vartype avatar: str
:ivar resthook_signature_key: Used to sign webhook payloads so you can verify their integrity.
:vartype resthook_signature_key: str
:ivar is_trial:
:vartype is_trial: bool
:ivar validation_tool_config: Configuration of the embeddable validation tool.
:vartype validation_tool_config: ~affinda.models.OrganizationValidationToolConfig
:ivar show_custom_field_creation: Whether to show the custom field creation in the UI.
:vartype show_custom_field_creation: bool

<a id="models._models.Organization.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Uniquely identify an organization.
- `name`: 
- `user_role`: The role of the logged in user within the organization. Known values are:
"admin", "member".
- `avatar`: URL of the organization's avatar.
- `resthook_signature_key`: Used to sign webhook payloads so you can verify their
integrity.
- `is_trial`: 
- `validation_tool_config`: Configuration of the embeddable validation tool.
- `show_custom_field_creation`: Whether to show the custom field creation in the UI.

<a id="models._models.OrganizationCreate"></a>

## OrganizationCreate Objects

```python
class OrganizationCreate(msrest.serialization.Model)
```

OrganizationCreate.

All required parameters must be populated in order to send to Azure.

:ivar name: Required.
:vartype name: str
:ivar avatar: Upload avatar for the organization.
:vartype avatar: IO
:ivar resthook_signature_key: Used to sign webhook payloads so you can verify their integrity.
:vartype resthook_signature_key: str

<a id="models._models.OrganizationCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Required.
- `avatar`: Upload avatar for the organization.
- `resthook_signature_key`: Used to sign webhook payloads so you can verify their
integrity.

<a id="models._models.OrganizationMembership"></a>

## OrganizationMembership Objects

```python
class OrganizationMembership(msrest.serialization.Model)
```

OrganizationMembership.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. A random string that uniquely identify the resource.
:vartype identifier: str
:ivar organization: Required. Uniquely identify an organization.
:vartype organization: str
:ivar user: Required.
:vartype user: ~affinda.models.User
:ivar role: Required. Known values are: "admin", "member".
:vartype role: str or ~affinda.models.OrganizationRole

<a id="models._models.OrganizationMembership.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. A random string that uniquely identify the resource.
- `organization`: Required. Uniquely identify an organization.
- `user`: Required.
- `role`: Required. Known values are: "admin", "member".

<a id="models._models.OrganizationMembershipUpdate"></a>

## OrganizationMembershipUpdate Objects

```python
class OrganizationMembershipUpdate(msrest.serialization.Model)
```

OrganizationMembershipUpdate.

:ivar role: Known values are: "admin", "member".
:vartype role: str or ~affinda.models.OrganizationRole

<a id="models._models.OrganizationMembershipUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `role`: Known values are: "admin", "member".

<a id="models._models.OrganizationUpdate"></a>

## OrganizationUpdate Objects

```python
class OrganizationUpdate(msrest.serialization.Model)
```

OrganizationUpdate.

:ivar name:
:vartype name: str
:ivar avatar: Upload avatar for the organization.
:vartype avatar: IO
:ivar resthook_signature_key: Used to sign webhook payloads so you can verify their integrity.
:vartype resthook_signature_key: str
:ivar validation_tool_config: Configuration of the embeddable validation tool.
:vartype validation_tool_config: ~affinda.models.ValidationToolConfig

<a id="models._models.OrganizationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `avatar`: Upload avatar for the organization.
- `resthook_signature_key`: Used to sign webhook payloads so you can verify their
integrity.
- `validation_tool_config`: Configuration of the embeddable validation tool.

<a id="models._models.OrganizationValidationToolConfig"></a>

## OrganizationValidationToolConfig Objects

```python
class OrganizationValidationToolConfig(msrest.serialization.Model)
```

Configuration of the embeddable validation tool.

:ivar theme:
:vartype theme: ~affinda.models.ThemeConfig
:ivar hide_actions: Hide the confirm document button and other actions.
:vartype hide_actions: bool
:ivar hide_collection: Hide the collection selector.
:vartype hide_collection: bool
:ivar hide_export: Hide the export menu.
:vartype hide_export: bool
:ivar hide_filename: Hide the filename input.
:vartype hide_filename: bool
:ivar hide_tags: Hide the tags editor.
:vartype hide_tags: bool
:ivar hide_warnings: Hide the warnings panel.
:vartype hide_warnings: bool
:ivar restrict_document_splitting: Disable the page editor after a document has been split
 once.
:vartype restrict_document_splitting: bool
:ivar disable_currency_formatting: Disable currency formatting of decimals values.
:vartype disable_currency_formatting: bool
:ivar disable_edit_document_metadata: Disable editing document metadata. Makes the collection
 selector, filename input and tags editor read only.
:vartype disable_edit_document_metadata: bool

<a id="models._models.OrganizationValidationToolConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `theme`: 
- `hide_actions`: Hide the confirm document button and other actions.
- `hide_collection`: Hide the collection selector.
- `hide_export`: Hide the export menu.
- `hide_filename`: Hide the filename input.
- `hide_tags`: Hide the tags editor.
- `hide_warnings`: Hide the warnings panel.
- `restrict_document_splitting`: Disable the page editor after a document has been split
once.
- `disable_currency_formatting`: Disable currency formatting of decimals values.
- `disable_edit_document_metadata`: Disable editing document metadata. Makes the
collection selector, filename input and tags editor read only.

<a id="models._models.PageMeta"></a>

## PageMeta Objects

```python
class PageMeta(msrest.serialization.Model)
```

PageMeta.

All required parameters must be populated in order to send to Azure.

:ivar id: Required.
:vartype id: int
:ivar page_index: Required. Page number within the document, starts from 0.
:vartype page_index: int
:ivar image: Required. The URL to the image of the page.
:vartype image: str
:ivar image_translated: The URL to the translated image of the page.
:vartype image_translated: str
:ivar height: Required. Height of the page's image in px.
:vartype height: float
:ivar width: Required. Width of the page's image in px.
:vartype width: float
:ivar rotation: Required. The degree of rotation applied to the page. Greater than 0 indicates
 clockwise rotation. Less than 0 indicates counter-clockwise rotation.
:vartype rotation: int

<a id="models._models.PageMeta.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Required.
- `page_index`: Required. Page number within the document, starts from 0.
- `image`: Required. The URL to the image of the page.
- `image_translated`: The URL to the translated image of the page.
- `height`: Required. Height of the page's image in px.
- `width`: Required. Width of the page's image in px.
- `rotation`: Required. The degree of rotation applied to the page. Greater than 0
indicates clockwise rotation. Less than 0 indicates counter-clockwise rotation.

<a id="models._models.PaginatedResponse"></a>

## PaginatedResponse Objects

```python
class PaginatedResponse(msrest.serialization.Model)
```

PaginatedResponse.

All required parameters must be populated in order to send to Azure.

:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.PaginatedResponse.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.PaletteColorOptions"></a>

## PaletteColorOptions Objects

```python
class PaletteColorOptions(msrest.serialization.Model)
```

PaletteColorOptions.

All required parameters must be populated in order to send to Azure.

:ivar main: Required.
:vartype main: str
:ivar light:
:vartype light: str
:ivar dark:
:vartype dark: str
:ivar contrast_text:
:vartype contrast_text: str

<a id="models._models.PaletteColorOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `main`: Required.
- `light`: 
- `dark`: 
- `contrast_text`: 

<a id="models._models.Paths11PzrpaV3ApiUsersGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## Paths11PzrpaV3ApiUsersGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class Paths11PzrpaV3ApiUsersGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

Paths11PzrpaV3ApiUsersGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[~affinda.models.ApiUserWithoutKey]

<a id="models._models.Paths11PzrpaV3ApiUsersGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.Paths1UmoszuV3MappingDataSourcesGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## Paths1UmoszuV3MappingDataSourcesGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class Paths1UmoszuV3MappingDataSourcesGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

Paths1UmoszuV3MappingDataSourcesGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[~affinda.models.MappingDataSource]

<a id="models._models.Paths1UmoszuV3MappingDataSourcesGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.Paths11QdcofV3MappingDataSourcesGetResponses200ContentApplicationJsonSchema"></a>

## Paths11QdcofV3MappingDataSourcesGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths11QdcofV3MappingDataSourcesGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        Paths1UmoszuV3MappingDataSourcesGetResponses200ContentApplicationJsonSchemaAllof1
)
```

Paths11QdcofV3MappingDataSourcesGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[~affinda.models.MappingDataSource]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.Paths11QdcofV3MappingDataSourcesGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.PathsKhpbbuV3InvitationsGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## PathsKhpbbuV3InvitationsGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class PathsKhpbbuV3InvitationsGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

PathsKhpbbuV3InvitationsGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[~affinda.models.Invitation]

<a id="models._models.PathsKhpbbuV3InvitationsGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.Paths18Wh2VcV3InvitationsGetResponses200ContentApplicationJsonSchema"></a>

## Paths18Wh2VcV3InvitationsGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths18Wh2VcV3InvitationsGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        PathsKhpbbuV3InvitationsGetResponses200ContentApplicationJsonSchemaAllof1
)
```

Paths18Wh2VcV3InvitationsGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[~affinda.models.Invitation]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.Paths18Wh2VcV3InvitationsGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.Paths1Czpnk1V3ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema"></a>

## Paths1Czpnk1V3ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema Objects

```python
class Paths1Czpnk1V3ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema(
        msrest.serialization.Model)
```

Paths1Czpnk1V3ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema.

:ivar config_override:
:vartype config_override: ~affinda.models.ResumeSearchConfig

<a id="models._models.Paths1Czpnk1V3ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `config_override`: 

<a id="models._models.Paths1Dgz0V9V3AnnotationsGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## Paths1Dgz0V9V3AnnotationsGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class Paths1Dgz0V9V3AnnotationsGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

Paths1Dgz0V9V3AnnotationsGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[~affinda.models.Annotation]

<a id="models._models.Paths1Dgz0V9V3AnnotationsGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.Paths1D5Zg6MV3AnnotationsGetResponses200ContentApplicationJsonSchema"></a>

## Paths1D5Zg6MV3AnnotationsGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths1D5Zg6MV3AnnotationsGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        Paths1Dgz0V9V3AnnotationsGetResponses200ContentApplicationJsonSchemaAllof1
)
```

Paths1D5Zg6MV3AnnotationsGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[~affinda.models.Annotation]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.Paths1D5Zg6MV3AnnotationsGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.PathsWvcyp9V3MappingsGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## PathsWvcyp9V3MappingsGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class PathsWvcyp9V3MappingsGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

PathsWvcyp9V3MappingsGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[~affinda.models.Mapping]

<a id="models._models.PathsWvcyp9V3MappingsGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.Paths1Dpvb2PV3MappingsGetResponses200ContentApplicationJsonSchema"></a>

## Paths1Dpvb2PV3MappingsGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths1Dpvb2PV3MappingsGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        PathsWvcyp9V3MappingsGetResponses200ContentApplicationJsonSchemaAllof1
)
```

Paths1Dpvb2PV3MappingsGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[~affinda.models.Mapping]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.Paths1Dpvb2PV3MappingsGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.Paths1O6IvdaV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## Paths1O6IvdaV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class Paths1O6IvdaV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

Paths1O6IvdaV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[any]

<a id="models._models.Paths1O6IvdaV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.Paths1Qojy9V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## Paths1Qojy9V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class Paths1Qojy9V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

Paths1Qojy9V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[~affinda.models.ResthookSubscription]

<a id="models._models.Paths1Qojy9V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.Paths1Qr7BnyV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchema"></a>

## Paths1Qr7BnyV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths1Qr7BnyV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        Paths1O6IvdaV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchemaAllof1
)
```

Paths1Qr7BnyV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[any]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.Paths1Qr7BnyV3MappingDataSourcesIdentifierValuesGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.Paths26Civ0V3ApiUsersGetResponses200ContentApplicationJsonSchema"></a>

## Paths26Civ0V3ApiUsersGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths26Civ0V3ApiUsersGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        Paths11PzrpaV3ApiUsersGetResponses200ContentApplicationJsonSchemaAllof1
)
```

Paths26Civ0V3ApiUsersGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[~affinda.models.ApiUserWithoutKey]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.Paths26Civ0V3ApiUsersGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.Paths2Ld2HiV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## Paths2Ld2HiV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class Paths2Ld2HiV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

Paths2Ld2HiV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchemaAllof1.

All required parameters must be populated in order to send to Azure.

:ivar results: Required.
:vartype results: list[~affinda.models.WorkspaceMembership]

<a id="models._models.Paths2Ld2HiV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: Required.

<a id="models._models.Paths4K6IzqV3DataPointChoicesGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## Paths4K6IzqV3DataPointChoicesGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class Paths4K6IzqV3DataPointChoicesGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

Paths4K6IzqV3DataPointChoicesGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[~affinda.models.DataPointChoice]

<a id="models._models.Paths4K6IzqV3DataPointChoicesGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.Paths4T5Cm5V3IndexGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## Paths4T5Cm5V3IndexGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class Paths4T5Cm5V3IndexGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

Paths4T5Cm5V3IndexGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[~affinda.models.Index]

<a id="models._models.Paths4T5Cm5V3IndexGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.Paths93Fa0ZV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## Paths93Fa0ZV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class Paths93Fa0ZV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

Paths93Fa0ZV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[~affinda.models.OrganizationMembership]

<a id="models._models.Paths93Fa0ZV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.PathsCl024WV3IndexNameDocumentsPostRequestbodyContentApplicationJsonSchema"></a>

## PathsCl024WV3IndexNameDocumentsPostRequestbodyContentApplicationJsonSchema Objects

```python
class PathsCl024WV3IndexNameDocumentsPostRequestbodyContentApplicationJsonSchema(
        msrest.serialization.Model)
```

PathsCl024WV3IndexNameDocumentsPostRequestbodyContentApplicationJsonSchema.

:ivar document:
:vartype document: str

<a id="models._models.PathsCl024WV3IndexNameDocumentsPostRequestbodyContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `document`: 

<a id="models._models.PathsDvrcp3V3IndexGetResponses200ContentApplicationJsonSchema"></a>

## PathsDvrcp3V3IndexGetResponses200ContentApplicationJsonSchema Objects

```python
class PathsDvrcp3V3IndexGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        Paths4T5Cm5V3IndexGetResponses200ContentApplicationJsonSchemaAllof1)
```

PathsDvrcp3V3IndexGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[~affinda.models.Index]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.PathsDvrcp3V3IndexGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.PathsFte27NV3IndexNameDocumentsPostResponses201ContentApplicationJsonSchema"></a>

## PathsFte27NV3IndexNameDocumentsPostResponses201ContentApplicationJsonSchema Objects

```python
class PathsFte27NV3IndexNameDocumentsPostResponses201ContentApplicationJsonSchema(
        msrest.serialization.Model)
```

PathsFte27NV3IndexNameDocumentsPostResponses201ContentApplicationJsonSchema.

:ivar document: Unique identifier for the document.
:vartype document: str

<a id="models._models.PathsFte27NV3IndexNameDocumentsPostResponses201ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `document`: Unique identifier for the document.

<a id="models._models.PathsL3R02CV3DocumentsGetResponses200ContentApplicationJsonSchemaAllof1"></a>

## PathsL3R02CV3DocumentsGetResponses200ContentApplicationJsonSchemaAllof1 Objects

```python
class PathsL3R02CV3DocumentsGetResponses200ContentApplicationJsonSchemaAllof1(
        msrest.serialization.Model)
```

PathsL3R02CV3DocumentsGetResponses200ContentApplicationJsonSchemaAllof1.

:ivar results:
:vartype results: list[~affinda.models.Document]

<a id="models._models.PathsL3R02CV3DocumentsGetResponses200ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 

<a id="models._models.PathsM3DzbgV3JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema"></a>

## PathsM3DzbgV3JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema Objects

```python
class PathsM3DzbgV3JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema(
        msrest.serialization.Model)
```

PathsM3DzbgV3JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema.

:ivar config_override:
:vartype config_override: ~affinda.models.JobDescriptionSearchConfig

<a id="models._models.PathsM3DzbgV3JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `config_override`: 

<a id="models._models.PathsMnwxgV3DataPointChoicesGetResponses200ContentApplicationJsonSchema"></a>

## PathsMnwxgV3DataPointChoicesGetResponses200ContentApplicationJsonSchema Objects

```python
class PathsMnwxgV3DataPointChoicesGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        Paths4K6IzqV3DataPointChoicesGetResponses200ContentApplicationJsonSchemaAllof1
)
```

PathsMnwxgV3DataPointChoicesGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[~affinda.models.DataPointChoice]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.PathsMnwxgV3DataPointChoicesGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.PathsO7SnenV3IndexNameDocumentsGetResponses200ContentApplicationJsonSchema"></a>

## PathsO7SnenV3IndexNameDocumentsGetResponses200ContentApplicationJsonSchema Objects

```python
class PathsO7SnenV3IndexNameDocumentsGetResponses200ContentApplicationJsonSchema(
        msrest.serialization.Model)
```

PathsO7SnenV3IndexNameDocumentsGetResponses200ContentApplicationJsonSchema.

:ivar count: Number of indexed documents in result.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str
:ivar results:
:vartype results: list[~affinda.models.Get200ApplicationJsonPropertiesItemsItem]

<a id="models._models.PathsO7SnenV3IndexNameDocumentsGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `count`: Number of indexed documents in result.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.
- `results`: 

<a id="models._models.PathsOxm5M7V3DocumentsGetResponses200ContentApplicationJsonSchema"></a>

## PathsOxm5M7V3DocumentsGetResponses200ContentApplicationJsonSchema Objects

```python
class PathsOxm5M7V3DocumentsGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        PathsL3R02CV3DocumentsGetResponses200ContentApplicationJsonSchemaAllof1
)
```

PathsOxm5M7V3DocumentsGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[~affinda.models.Document]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.PathsOxm5M7V3DocumentsGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.PathsQ5Os5RV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchema"></a>

## PathsQ5Os5RV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchema Objects

```python
class PathsQ5Os5RV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        Paths93Fa0ZV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchemaAllof1
)
```

PathsQ5Os5RV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[~affinda.models.OrganizationMembership]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.PathsQ5Os5RV3OrganizationMembershipsGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.PathsVz5Kj2V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchema"></a>

## PathsVz5Kj2V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchema Objects

```python
class PathsVz5Kj2V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        Paths1Qojy9V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchemaAllof1
)
```

PathsVz5Kj2V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results:
:vartype results: list[~affinda.models.ResthookSubscription]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.PathsVz5Kj2V3ResthookSubscriptionsGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: 
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.PathsZ1JuagV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchema"></a>

## PathsZ1JuagV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchema Objects

```python
class PathsZ1JuagV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchema(
        PaginatedResponse,
        Paths2Ld2HiV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchemaAllof1
)
```

PathsZ1JuagV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar results: Required.
:vartype results: list[~affinda.models.WorkspaceMembership]
:ivar count: Required. Number of items in results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str

<a id="models._models.PathsZ1JuagV3WorkspaceMembershipsGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `results`: Required.
- `count`: Required. Number of items in results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.

<a id="models._models.PhoneNumberAnnotation"></a>

## PhoneNumberAnnotation Objects

```python
class PhoneNumberAnnotation(Annotation)
```

PhoneNumberAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~affinda.models.PhoneNumberAnnotationParsed

<a id="models._models.PhoneNumberAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.PhoneNumberAnnotationParsed"></a>

## PhoneNumberAnnotationParsed Objects

```python
class PhoneNumberAnnotationParsed(msrest.serialization.Model)
```

PhoneNumberAnnotationParsed.

:ivar raw_text:
:vartype raw_text: str
:ivar formatted_number:
:vartype formatted_number: str
:ivar country_code:
:vartype country_code: str
:ivar international_country_code:
:vartype international_country_code: int
:ivar national_number:
:vartype national_number: str

<a id="models._models.PhoneNumberAnnotationParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw_text`: 
- `formatted_number`: 
- `country_code`: 
- `international_country_code`: 
- `national_number`: 

<a id="models._models.Rectangle"></a>

## Rectangle Objects

```python
class Rectangle(msrest.serialization.Model)
```

Rectangle.

All required parameters must be populated in order to send to Azure.

:ivar page_index:
:vartype page_index: int
:ivar x0: Required.
:vartype x0: float
:ivar y0: Required.
:vartype y0: float
:ivar x1: Required.
:vartype x1: float
:ivar y1: Required.
:vartype y1: float

<a id="models._models.Rectangle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `page_index`: 
- `x0`: Required.
- `y0`: Required.
- `x1`: Required.
- `y1`: Required.

<a id="models._models.RedactConfig"></a>

## RedactConfig Objects

```python
class RedactConfig(msrest.serialization.Model)
```

RedactConfig.

:ivar redact_headshot:
:vartype redact_headshot: bool
:ivar redact_personal_details:
:vartype redact_personal_details: bool
:ivar redact_work_details:
:vartype redact_work_details: bool
:ivar redact_referees:
:vartype redact_referees: bool
:ivar redact_education_details:
:vartype redact_education_details: bool
:ivar redact_locations:
:vartype redact_locations: bool
:ivar redact_dates:
:vartype redact_dates: bool
:ivar redact_gender:
:vartype redact_gender: bool

<a id="models._models.RedactConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `redact_headshot`: 
- `redact_personal_details`: 
- `redact_work_details`: 
- `redact_referees`: 
- `redact_education_details`: 
- `redact_locations`: 
- `redact_dates`: 
- `redact_gender`: 

<a id="models._models.RegionBias"></a>

## RegionBias Objects

```python
class RegionBias(msrest.serialization.Model)
```

RegionBias.

:ivar country: A single alpha-2 country code (e.g. AU) used by google geocoding service.
:vartype country: str
:ivar countries: A list of alpha-2 country codes used by Pelias.
:vartype countries: list[str]
:ivar square_coordinates: A list of coordinates used by Pelias in the shape of [min_lon,
 min_lat, max_lon, max_lat].
:vartype square_coordinates: list[float]

<a id="models._models.RegionBias.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `country`: A single alpha-2 country code (e.g. AU) used by google geocoding service.
- `countries`: A list of alpha-2 country codes used by Pelias.
- `square_coordinates`: A list of coordinates used by Pelias in the shape of [min_lon,
min_lat, max_lon, max_lat].

<a id="models._models.RequestError"></a>

## RequestError Objects

```python
class RequestError(msrest.serialization.Model)
```

RequestError.

All required parameters must be populated in order to send to Azure.

:ivar type: Required.
:vartype type: str
:ivar errors: Required.
:vartype errors: list[~affinda.models.RequestErrorErrorsItem]

<a id="models._models.RequestError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `type`: Required.
- `errors`: Required.

<a id="models._models.RequestErrorErrorsItem"></a>

## RequestErrorErrorsItem Objects

```python
class RequestErrorErrorsItem(msrest.serialization.Model)
```

RequestErrorErrorsItem.

All required parameters must be populated in order to send to Azure.

:ivar attr: Required.
:vartype attr: str
:ivar code: Required.
:vartype code: str
:ivar detail: Required.
:vartype detail: str

<a id="models._models.RequestErrorErrorsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `attr`: Required.
- `code`: Required.
- `detail`: Required.

<a id="models._models.ResthookSubscription"></a>

## ResthookSubscription Objects

```python
class ResthookSubscription(msrest.serialization.Model)
```

ResthookSubscription.

All required parameters must be populated in order to send to Azure.

:ivar id: Required. Resthook subscription's ID.
:vartype id: int
:ivar event: Required. The event name to subscribe to. Known values are:
 "resume.parse.succeeded", "resume.parse.failed", "resume.parse.completed",
 "invoice.parse.succeeded", "invoice.parse.failed", "invoice.parse.completed",
 "invoice.validate.completed", "document.parse.succeeded", "document.parse.failed",
 "document.parse.completed", "document.validate.completed", "document.classify.succeeded",
 "document.classify.failed", "document.classify.completed", "document.rejected".
:vartype event: str or ~affinda.models.ResthookEvent
:ivar organization: Required.
:vartype organization: ~affinda.models.Organization
:ivar workspace: Required.
:vartype workspace: ~affinda.models.ResthookSubscriptionWorkspace
:ivar target_url: Required. URL of the resthook's receiver.
:vartype target_url: str
:ivar active: Required. Resthooks only fire for active subscriptions.
:vartype active: bool
:ivar auto_deactivated: Required. Resthook subscriptions can be auto deactivated if the
 receiver continuously returns error status code over a period of time.
:vartype auto_deactivated: bool
:ivar auto_deactivate_reason: Required. The reason for the subscription being auto deactivated.
 May contains the error response that the receiver returned.
:vartype auto_deactivate_reason: str
:ivar version: Required. Version of the resthook subscription. Determines the resthook body
 being fired. Known values are: "v1", "v2", "v3".
:vartype version: str or ~affinda.models.ResthookSubscriptionVersion

<a id="models._models.ResthookSubscription.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Required. Resthook subscription's ID.
- `event`: Required. The event name to subscribe to. Known values are:
"resume.parse.succeeded", "resume.parse.failed", "resume.parse.completed",
"invoice.parse.succeeded", "invoice.parse.failed", "invoice.parse.completed",
"invoice.validate.completed", "document.parse.succeeded", "document.parse.failed",
"document.parse.completed", "document.validate.completed", "document.classify.succeeded",
"document.classify.failed", "document.classify.completed", "document.rejected".
- `organization`: Required.
- `workspace`: Required.
- `target_url`: Required. URL of the resthook's receiver.
- `active`: Required. Resthooks only fire for active subscriptions.
- `auto_deactivated`: Required. Resthook subscriptions can be auto deactivated if the
receiver continuously returns error status code over a period of time.
- `auto_deactivate_reason`: Required. The reason for the subscription being auto
deactivated. May contains the error response that the receiver returned.
- `version`: Required. Version of the resthook subscription. Determines the resthook body
being fired. Known values are: "v1", "v2", "v3".

<a id="models._models.ResthookSubscriptionCreate"></a>

## ResthookSubscriptionCreate Objects

```python
class ResthookSubscriptionCreate(msrest.serialization.Model)
```

ResthookSubscriptionCreate.

All required parameters must be populated in order to send to Azure.

:ivar target_url: Required. URL of the resthook's receiver.
:vartype target_url: str
:ivar event: Required. The event name to subscribe to. Known values are:
 "resume.parse.succeeded", "resume.parse.failed", "resume.parse.completed",
 "invoice.parse.succeeded", "invoice.parse.failed", "invoice.parse.completed",
 "invoice.validate.completed", "document.parse.succeeded", "document.parse.failed",
 "document.parse.completed", "document.validate.completed", "document.classify.succeeded",
 "document.classify.failed", "document.classify.completed", "document.rejected".
:vartype event: str or ~affinda.models.ResthookEvent
:ivar organization:
:vartype organization: str
:ivar workspace:
:vartype workspace: str
:ivar version: Version of the resthook subscription. Determines the resthook body being fired.
 Known values are: "v1", "v2", "v3".
:vartype version: str or ~affinda.models.Version

<a id="models._models.ResthookSubscriptionCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `target_url`: Required. URL of the resthook's receiver.
- `event`: Required. The event name to subscribe to. Known values are:
"resume.parse.succeeded", "resume.parse.failed", "resume.parse.completed",
"invoice.parse.succeeded", "invoice.parse.failed", "invoice.parse.completed",
"invoice.validate.completed", "document.parse.succeeded", "document.parse.failed",
"document.parse.completed", "document.validate.completed", "document.classify.succeeded",
"document.classify.failed", "document.classify.completed", "document.rejected".
- `organization`: 
- `workspace`: 
- `version`: Version of the resthook subscription. Determines the resthook body being
fired. Known values are: "v1", "v2", "v3".

<a id="models._models.ResthookSubscriptionUpdate"></a>

## ResthookSubscriptionUpdate Objects

```python
class ResthookSubscriptionUpdate(msrest.serialization.Model)
```

ResthookSubscriptionUpdate.

:ivar event: The event name to subscribe to. Known values are: "resume.parse.succeeded",
 "resume.parse.failed", "resume.parse.completed", "invoice.parse.succeeded",
 "invoice.parse.failed", "invoice.parse.completed", "invoice.validate.completed",
 "document.parse.succeeded", "document.parse.failed", "document.parse.completed",
 "document.validate.completed", "document.classify.succeeded", "document.classify.failed",
 "document.classify.completed", "document.rejected".
:vartype event: str or ~affinda.models.ResthookEvent
:ivar organization: Uniquely identify an organization.
:vartype organization: str
:ivar workspace: Uniquely identify a workspace.
:vartype workspace: str
:ivar version: Version of the resthook subscription. Determines the resthook body being fired.
 Known values are: "v1", "v2", "v3".
:vartype version: str or ~affinda.models.Version

<a id="models._models.ResthookSubscriptionUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `event`: The event name to subscribe to. Known values are: "resume.parse.succeeded",
"resume.parse.failed", "resume.parse.completed", "invoice.parse.succeeded",
"invoice.parse.failed", "invoice.parse.completed", "invoice.validate.completed",
"document.parse.succeeded", "document.parse.failed", "document.parse.completed",
"document.validate.completed", "document.classify.succeeded", "document.classify.failed",
"document.classify.completed", "document.rejected".
- `organization`: Uniquely identify an organization.
- `workspace`: Uniquely identify a workspace.
- `version`: Version of the resthook subscription. Determines the resthook body being
fired. Known values are: "v1", "v2", "v3".

<a id="models._models.ResthookSubscriptionWorkspace"></a>

## ResthookSubscriptionWorkspace Objects

```python
class ResthookSubscriptionWorkspace(msrest.serialization.Model)
```

ResthookSubscriptionWorkspace.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify a workspace.
:vartype identifier: str
:ivar name: Required.
:vartype name: str
:ivar organization: Required.
:vartype organization: ~affinda.models.Organization

<a id="models._models.ResthookSubscriptionWorkspace.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify a workspace.
- `name`: Required.
- `organization`: Required.

<a id="models._models.Resume"></a>

## Resume Objects

```python
class Resume(Document)
```

Resume.

All required parameters must be populated in order to send to Azure.

:ivar extractor: Required. Constant filled by server.
:vartype extractor: str
:ivar meta: Required.
:vartype meta: ~affinda.models.DocumentMeta
:ivar error:
:vartype error: ~affinda.models.DocumentError
:ivar warnings:
:vartype warnings: list[~affinda.models.DocumentWarning]
:ivar data: A JSON-encoded string of the ``ResumeData`` object.
:vartype data: ~affinda.models.ResumeData

<a id="models._models.Resume.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `meta`: Required.
- `error`: 
- `warnings`: 
- `data`: A JSON-encoded string of the ``ResumeData`` object.

<a id="models._models.ResumeData"></a>

## ResumeData Objects

```python
class ResumeData(msrest.serialization.Model)
```

A JSON-encoded string of the ``ResumeData`` object.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar name:
:vartype name: ~affinda.models.ResumeDataName
:ivar phone_numbers:
:vartype phone_numbers: list[str]
:ivar phone_number_details:
:vartype phone_number_details: list[~affinda.models.ResumeDataPhoneNumberDetailsItem]
:ivar websites:
:vartype websites: list[str]
:ivar emails:
:vartype emails: list[str]
:ivar date_of_birth:
:vartype date_of_birth: str
:ivar location:
:vartype location: ~affinda.models.Location
:ivar objective:
:vartype objective: str
:ivar languages:
:vartype languages: list[str or ~affinda.models.ResumeDataLanguagesItem]
:ivar language_codes:
:vartype language_codes: list[str]
:ivar summary:
:vartype summary: str
:ivar total_years_experience:
:vartype total_years_experience: int
:ivar head_shot: base64 encoded string.
:vartype head_shot: bytearray
:ivar education:
:vartype education: list[~affinda.models.Education]
:ivar profession: Prediction of the candidate's profession based on recent work experience.
:vartype profession: str
:ivar linkedin: Linkedin account associated with the candidate.
:vartype linkedin: str
:ivar work_experience:
:vartype work_experience: list[~affinda.models.ResumeDataWorkExperienceItem]
:ivar skills:
:vartype skills: list[~affinda.models.ResumeDataSkillsItem]
:ivar certifications:
:vartype certifications: list[str]
:ivar publications:
:vartype publications: list[str]
:ivar referees:
:vartype referees: list[~affinda.models.ResumeDataRefereesItem]
:ivar sections:
:vartype sections: list[~affinda.models.ResumeDataSectionsItem]
:ivar is_resume_probability: Probability that the given document is a resume. Values below 30
 suggest that the document is not a resume.
:vartype is_resume_probability: int
:ivar raw_text: All of the raw text of the parsed resume, example is shortened for readability.
:vartype raw_text: str
:ivar redacted_text: Redacted version of the text in the resume, removing PII.
:vartype redacted_text: str

<a id="models._models.ResumeData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `name`: 
- `phone_numbers`: 
- `phone_number_details`: 
- `websites`: 
- `emails`: 
- `date_of_birth`: 
- `location`: 
- `objective`: 
- `languages`: 
- `summary`: 
- `total_years_experience`: 
- `education`: 
- `work_experience`: 
- `skills`: 
- `certifications`: 
- `publications`: 
- `referees`: 
- `raw_text`: All of the raw text of the parsed resume, example is shortened for
readability.
- `redacted_text`: Redacted version of the text in the resume, removing PII.

<a id="models._models.ResumeDataName"></a>

## ResumeDataName Objects

```python
class ResumeDataName(msrest.serialization.Model)
```

ResumeDataName.

:ivar raw:
:vartype raw: str
:ivar first:
:vartype first: str
:ivar last:
:vartype last: str
:ivar middle:
:vartype middle: str
:ivar title:
:vartype title: str

<a id="models._models.ResumeDataName.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw`: 
- `first`: 
- `last`: 
- `middle`: 
- `title`: 

<a id="models._models.ResumeDataPhoneNumberDetailsItem"></a>

## ResumeDataPhoneNumberDetailsItem Objects

```python
class ResumeDataPhoneNumberDetailsItem(msrest.serialization.Model)
```

ResumeDataPhoneNumberDetailsItem.

:ivar raw_text:
:vartype raw_text: str
:ivar formatted_number:
:vartype formatted_number: str
:ivar country_code:
:vartype country_code: str
:ivar international_country_code:
:vartype international_country_code: int
:ivar national_number:
:vartype national_number: str

<a id="models._models.ResumeDataPhoneNumberDetailsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `raw_text`: 
- `formatted_number`: 
- `country_code`: 
- `international_country_code`: 
- `national_number`: 

<a id="models._models.ResumeDataRefereesItem"></a>

## ResumeDataRefereesItem Objects

```python
class ResumeDataRefereesItem(msrest.serialization.Model)
```

ResumeDataRefereesItem.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar name:
:vartype name: str
:ivar text:
:vartype text: str
:ivar email:
:vartype email: str
:ivar number:
:vartype number: str
:ivar position:
:vartype position: str

<a id="models._models.ResumeDataRefereesItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `name`: 
- `text`: 
- `email`: 
- `number`: 
- `position`: 

<a id="models._models.ResumeDataSectionsItem"></a>

## ResumeDataSectionsItem Objects

```python
class ResumeDataSectionsItem(msrest.serialization.Model)
```

ResumeDataSectionsItem.

:ivar section_type:
:vartype section_type: str
:ivar bbox:
:vartype bbox: list[float]
:ivar page_index:
:vartype page_index: int
:ivar text:
:vartype text: str

<a id="models._models.ResumeDataSectionsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `section_type`: 
- `bbox`: 
- `page_index`: 
- `text`: 

<a id="models._models.ResumeDataSkillsItem"></a>

## ResumeDataSkillsItem Objects

```python
class ResumeDataSkillsItem(msrest.serialization.Model)
```

ResumeDataSkillsItem.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar id:
:vartype id: int
:ivar emsi_id: EMSI id of this skill.
:vartype emsi_id: str
:ivar name:
:vartype name: str
:ivar last_used:
:vartype last_used: str
:ivar number_of_months:
:vartype number_of_months: int
:ivar type:
:vartype type: str
:ivar count:
:vartype count: int
:ivar weighting:
:vartype weighting: float
:ivar sources:
:vartype sources: list[~affinda.models.ResumeDataSkillsPropertiesItemsItem]

<a id="models._models.ResumeDataSkillsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: 
- `name`: 
- `last_used`: 
- `number_of_months`: 

<a id="models._models.ResumeDataSkillsPropertiesItemsItem"></a>

## ResumeDataSkillsPropertiesItemsItem Objects

```python
class ResumeDataSkillsPropertiesItemsItem(msrest.serialization.Model)
```

ResumeDataSkillsPropertiesItemsItem.

:ivar section:
:vartype section: str
:ivar position: If this skill is extracted from a "workExperience" section, the "position" is
 the index of the work experience where this skill is found, with 0 being the first work
 experience, 1 being the second work experience, and so on.
:vartype position: int
:ivar work_experience_id: If this skill is extracted from a "workExperience" section, the
 "workExperienceId" is the id of the work experience where this skill is found.
:vartype work_experience_id: int

<a id="models._models.ResumeDataSkillsPropertiesItemsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `section`: 
- `position`: If this skill is extracted from a "workExperience" section, the "position"
is the index of the work experience where this skill is found, with 0 being the first work
experience, 1 being the second work experience, and so on.
- `work_experience_id`: If this skill is extracted from a "workExperience" section, the
"workExperienceId" is the id of the work experience where this skill is found.

<a id="models._models.ResumeDataWorkExperienceItem"></a>

## ResumeDataWorkExperienceItem Objects

```python
class ResumeDataWorkExperienceItem(msrest.serialization.Model)
```

ResumeDataWorkExperienceItem.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar id:
:vartype id: int
:ivar job_title:
:vartype job_title: str
:ivar soc_code:
:vartype soc_code: str
:ivar soc_name:
:vartype soc_name: str
:ivar organization:
:vartype organization: str
:ivar industry:
:vartype industry: str
:ivar location:
:vartype location: ~affinda.models.Location
:ivar job_description:
:vartype job_description: str
:ivar dates:
:vartype dates: ~affinda.models.ResumeDataWorkExperienceItemDates
:ivar occupation:
:vartype occupation: ~affinda.models.ResumeDataWorkExperienceItemOccupation

<a id="models._models.ResumeDataWorkExperienceItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: 
- `job_title`: 
- `organization`: 
- `location`: 
- `job_description`: 
- `dates`: 

<a id="models._models.ResumeDataWorkExperienceItemDates"></a>

## ResumeDataWorkExperienceItemDates Objects

```python
class ResumeDataWorkExperienceItemDates(msrest.serialization.Model)
```

ResumeDataWorkExperienceItemDates.

:ivar start_date:
:vartype start_date: ~datetime.date
:ivar end_date:
:vartype end_date: ~datetime.date
:ivar months_in_position:
:vartype months_in_position: int
:ivar is_current:
:vartype is_current: bool
:ivar raw_text:
:vartype raw_text: str

<a id="models._models.ResumeDataWorkExperienceItemDates.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `start_date`: 
- `end_date`: 
- `months_in_position`: 
- `is_current`: 
- `raw_text`: 

<a id="models._models.ResumeDataWorkExperienceItemOccupation"></a>

## ResumeDataWorkExperienceItemOccupation Objects

```python
class ResumeDataWorkExperienceItemOccupation(msrest.serialization.Model)
```

ResumeDataWorkExperienceItemOccupation.

:ivar job_title: The raw (not normalized) job title pulled from the work experience entry.
:vartype job_title: str
:ivar job_title_normalized: Mapped onto the EMSI job title taxonomy if a sufficiently close
 match exists.
:vartype job_title_normalized: str
:ivar emsi_id: EMSI id of the normalised job title.
:vartype emsi_id: str
:ivar management_level: Known values are: "None", "Low", "Mid", "Upper".
:vartype management_level: str or ~affinda.models.ManagementLevel
:ivar classification:
:vartype classification:
 ~affinda.models.Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification

<a id="models._models.ResumeDataWorkExperienceItemOccupation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `job_title`: The raw (not normalized) job title pulled from the work experience entry.
- `job_title_normalized`: Mapped onto the EMSI job title taxonomy if a sufficiently close
match exists.
- `emsi_id`: EMSI id of the normalised job title.
- `management_level`: Known values are: "None", "Low", "Mid", "Upper".
- `classification`: 

<a id="models._models.ResumeRedact"></a>

## ResumeRedact Objects

```python
class ResumeRedact(Document)
```

ResumeRedact.

All required parameters must be populated in order to send to Azure.

:ivar extractor: Required. Constant filled by server.
:vartype extractor: str
:ivar meta: Required.
:vartype meta: ~affinda.models.DocumentMeta
:ivar error:
:vartype error: ~affinda.models.DocumentError
:ivar warnings:
:vartype warnings: list[~affinda.models.DocumentWarning]
:ivar data:
:vartype data: ~affinda.models.ResumeRedactData

<a id="models._models.ResumeRedact.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `meta`: Required.
- `error`: 
- `warnings`: 
- `data`: 

<a id="models._models.ResumeRedactData"></a>

## ResumeRedactData Objects

```python
class ResumeRedactData(msrest.serialization.Model)
```

ResumeRedactData.

:ivar redacted_pdf: URL to download the redacted resume.
:vartype redacted_pdf: str

<a id="models._models.ResumeRedactData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `redacted_pdf`: URL to download the redacted resume.

<a id="models._models.ResumeSearch"></a>

## ResumeSearch Objects

```python
class ResumeSearch(msrest.serialization.Model)
```

ResumeSearch.

:ivar count: Total number of results.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str
:ivar parameters:
:vartype parameters: ~affinda.models.ResumeSearchParameters
:ivar results:
:vartype results: list[~affinda.models.ResumeSearchResult]

<a id="models._models.ResumeSearch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `count`: Total number of results.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.
- `parameters`: 
- `results`: 

<a id="models._models.ResumeSearchConfig"></a>

## ResumeSearchConfig Objects

```python
class ResumeSearchConfig(msrest.serialization.Model)
```

ResumeSearchConfig.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar allow_pdf_download:
:vartype allow_pdf_download: bool
:ivar max_results: Maximum number of results that can be returned. Setting to "null" means no
 limitation.
:vartype max_results: int
:ivar display_job_title:
:vartype display_job_title: bool
:ivar display_location:
:vartype display_location: bool
:ivar display_years_experience:
:vartype display_years_experience: bool
:ivar display_occupation_group:
:vartype display_occupation_group: bool
:ivar display_education:
:vartype display_education: bool
:ivar display_skills:
:vartype display_skills: bool
:ivar display_languages:
:vartype display_languages: bool
:ivar display_management_level:
:vartype display_management_level: bool
:ivar display_keywords:
:vartype display_keywords: bool
:ivar weight_job_title:
:vartype weight_job_title: float
:ivar weight_location:
:vartype weight_location: float
:ivar weight_years_experience:
:vartype weight_years_experience: float
:ivar weight_occupation_group:
:vartype weight_occupation_group: float
:ivar weight_education:
:vartype weight_education: float
:ivar weight_skills:
:vartype weight_skills: float
:ivar weight_languages:
:vartype weight_languages: float
:ivar weight_management_level:
:vartype weight_management_level: float
:ivar weight_keywords:
:vartype weight_keywords: float
:ivar indices: List of index names.
:vartype indices: list[str]
:ivar show_index_dropdown: Controls whether or not the index dropdown is displayed to the user.
:vartype show_index_dropdown: bool
:ivar search_tool_theme: Customize the theme of the embeded search tool.
:vartype search_tool_theme: dict[str, any]
:ivar user_id: ID of the logged in user.
:vartype user_id: int
:ivar username: Username of the logged in user.
:vartype username: str
:ivar actions: A list of actions to show in the dropdown in the embedded search tool.
:vartype actions: list[~affinda.models.SearchConfigAction]
:ivar hide_toolbar: Hide the reset/import toolbar.
:vartype hide_toolbar: bool
:ivar hide_side_panel: Hide the entire side panel.
:vartype hide_side_panel: bool
:ivar custom_fields_config:
:vartype custom_fields_config: list[~affinda.models.CustomFieldConfig]

<a id="models._models.ResumeSearchConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `allow_pdf_download`: 
- `max_results`: Maximum number of results that can be returned. Setting to "null" means
no limitation.
- `display_job_title`: 
- `display_location`: 
- `display_years_experience`: 
- `display_occupation_group`: 
- `display_education`: 
- `display_skills`: 
- `display_languages`: 
- `display_management_level`: 
- `display_keywords`: 
- `weight_job_title`: 
- `weight_location`: 
- `weight_years_experience`: 
- `weight_occupation_group`: 
- `weight_education`: 
- `weight_skills`: 
- `weight_languages`: 
- `weight_management_level`: 
- `weight_keywords`: 
- `indices`: List of index names.
- `show_index_dropdown`: Controls whether or not the index dropdown is displayed to the
user.
- `search_tool_theme`: Customize the theme of the embeded search tool.
- `actions`: A list of actions to show in the dropdown in the embedded search tool.
- `hide_toolbar`: Hide the reset/import toolbar.
- `hide_side_panel`: Hide the entire side panel.
- `custom_fields_config`: 

<a id="models._models.ResumeSearchDetail"></a>

## ResumeSearchDetail Objects

```python
class ResumeSearchDetail(msrest.serialization.Model)
```

ResumeSearchDetail.

:ivar job_title:
:vartype job_title: ~affinda.models.ResumeSearchDetailJobTitle
:ivar location:
:vartype location: ~affinda.models.ResumeSearchDetailLocation
:ivar education:
:vartype education: ~affinda.models.ResumeSearchDetailEducation
:ivar skills:
:vartype skills: ~affinda.models.ResumeSearchDetailSkills
:ivar experience:
:vartype experience: ~affinda.models.ResumeSearchDetailExperience
:ivar occupation_group:
:vartype occupation_group: ~affinda.models.ResumeSearchDetailOccupationGroup
:ivar languages:
:vartype languages: ~affinda.models.ResumeSearchDetailLanguages
:ivar management_level:
:vartype management_level: ~affinda.models.ResumeSearchDetailManagementLevel
:ivar search_expression:
:vartype search_expression: ~affinda.models.ResumeSearchDetailSearchExpression

<a id="models._models.ResumeSearchDetail.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `job_title`: 
- `location`: 
- `education`: 
- `skills`: 
- `experience`: 
- `occupation_group`: 
- `languages`: 
- `management_level`: 
- `search_expression`: 

<a id="models._models.ResumeSearchDetailEducation"></a>

## ResumeSearchDetailEducation Objects

```python
class ResumeSearchDetailEducation(msrest.serialization.Model)
```

ResumeSearchDetailEducation.

:ivar missing:
:vartype missing: ~affinda.models.ResumeSearchDetailEducationMissing
:ivar value:
:vartype value: list[~affinda.models.ResumeSearchDetailEducationValueItem]

<a id="models._models.ResumeSearchDetailEducation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.ResumeSearchDetailEducationMissing"></a>

## ResumeSearchDetailEducationMissing Objects

```python
class ResumeSearchDetailEducationMissing(msrest.serialization.Model)
```

ResumeSearchDetailEducationMissing.

:ivar degrees:
:vartype degrees: list[str]
:ivar highest_degree_types:
:vartype highest_degree_types: list[str]
:ivar institutions:
:vartype institutions: list[str]
:ivar current_student:
:vartype current_student: bool
:ivar recent_graduate:
:vartype recent_graduate: bool

<a id="models._models.ResumeSearchDetailEducationMissing.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `degrees`: 
- `highest_degree_types`: 
- `institutions`: 
- `current_student`: 
- `recent_graduate`: 

<a id="models._models.ResumeSearchDetailEducationValueItem"></a>

## ResumeSearchDetailEducationValueItem Objects

```python
class ResumeSearchDetailEducationValueItem(
        Education,
        ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1
)
```

ResumeSearchDetailEducationValueItem.

:ivar match:
:vartype match: bool
:ivar id:
:vartype id: int
:ivar organization:
:vartype organization: str
:ivar accreditation:
:vartype accreditation: ~affinda.models.Accreditation
:ivar grade:
:vartype grade: ~affinda.models.EducationGrade
:ivar location:
:vartype location: ~affinda.models.Location
:ivar dates:
:vartype dates: ~affinda.models.EducationDates

<a id="models._models.ResumeSearchDetailEducationValueItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 
- `id`: 
- `organization`: 
- `accreditation`: 
- `grade`: 
- `location`: 
- `dates`: 

<a id="models._models.ResumeSearchDetailExperience"></a>

## ResumeSearchDetailExperience Objects

```python
class ResumeSearchDetailExperience(msrest.serialization.Model)
```

ResumeSearchDetailExperience.

:ivar years:
:vartype years: int
:ivar match:
:vartype match: bool

<a id="models._models.ResumeSearchDetailExperience.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `years`: 
- `match`: 

<a id="models._models.ResumeSearchDetailJobTitle"></a>

## ResumeSearchDetailJobTitle Objects

```python
class ResumeSearchDetailJobTitle(msrest.serialization.Model)
```

ResumeSearchDetailJobTitle.

:ivar missing:
:vartype missing: list[str]
:ivar value:
:vartype value: list[~affinda.models.ResumeSearchDetailJobTitleValueItem]

<a id="models._models.ResumeSearchDetailJobTitle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.ResumeSearchDetailJobTitleValueItem"></a>

## ResumeSearchDetailJobTitleValueItem Objects

```python
class ResumeSearchDetailJobTitleValueItem(msrest.serialization.Model)
```

ResumeSearchDetailJobTitleValueItem.

:ivar name:
:vartype name: str
:ivar start_date:
:vartype start_date: str
:ivar end_date:
:vartype end_date: str
:ivar company_name:
:vartype company_name: str
:ivar match:
:vartype match: bool

<a id="models._models.ResumeSearchDetailJobTitleValueItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `start_date`: 
- `end_date`: 
- `company_name`: 
- `match`: 

<a id="models._models.ResumeSearchDetailLanguages"></a>

## ResumeSearchDetailLanguages Objects

```python
class ResumeSearchDetailLanguages(msrest.serialization.Model)
```

ResumeSearchDetailLanguages.

:ivar missing:
:vartype missing: list[~affinda.models.ResumeSearchParametersSkill]
:ivar value:
:vartype value: list[~affinda.models.ResumeSearchDetailLanguagesValueItem]

<a id="models._models.ResumeSearchDetailLanguages.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.ResumeSkill"></a>

## ResumeSkill Objects

```python
class ResumeSkill(msrest.serialization.Model)
```

ResumeSkill.

:ivar name:
:vartype name: str
:ivar last_used:
:vartype last_used: str
:ivar number_of_months:
:vartype number_of_months: int
:ivar type:
:vartype type: str
:ivar sources:
:vartype sources: list[~affinda.models.ResumeSkillSourcesItem]

<a id="models._models.ResumeSkill.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `last_used`: 
- `number_of_months`: 
- `type`: 
- `sources`: 

<a id="models._models.ResumeSearchDetailLanguagesValueItem"></a>

## ResumeSearchDetailLanguagesValueItem Objects

```python
class ResumeSearchDetailLanguagesValueItem(
        ResumeSkill,
        Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1
)
```

ResumeSearchDetailLanguagesValueItem.

:ivar match:
:vartype match: bool
:ivar name:
:vartype name: str
:ivar last_used:
:vartype last_used: str
:ivar number_of_months:
:vartype number_of_months: int
:ivar type:
:vartype type: str
:ivar sources:
:vartype sources: list[~affinda.models.ResumeSkillSourcesItem]

<a id="models._models.ResumeSearchDetailLanguagesValueItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 
- `name`: 
- `last_used`: 
- `number_of_months`: 
- `type`: 
- `sources`: 

<a id="models._models.ResumeSearchDetailLocation"></a>

## ResumeSearchDetailLocation Objects

```python
class ResumeSearchDetailLocation(msrest.serialization.Model)
```

ResumeSearchDetailLocation.

:ivar missing:
:vartype missing: list[~affinda.models.ResumeSearchParametersLocation]
:ivar value:
:vartype value: ~affinda.models.ResumeSearchDetailLocationValue

<a id="models._models.ResumeSearchDetailLocation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.ResumeSearchDetailLocationValue"></a>

## ResumeSearchDetailLocationValue Objects

```python
class ResumeSearchDetailLocationValue(
        Location,
        ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1
)
```

ResumeSearchDetailLocationValue.

Variables are only populated by the server, and will be ignored when sending a request.

All required parameters must be populated in order to send to Azure.

:ivar match:
:vartype match: bool
:ivar formatted:
:vartype formatted: str
:ivar postal_code:
:vartype postal_code: str
:ivar state:
:vartype state: str
:ivar country:
:vartype country: str
:ivar country_code: Two letter country code (ISO 3166-1 alpha-2).
:vartype country_code: str
:ivar raw_input: Required.
:vartype raw_input: str
:ivar street_number:
:vartype street_number: str
:ivar street:
:vartype street: str
:ivar apartment_number:
:vartype apartment_number: str
:ivar city:
:vartype city: str
:ivar latitude:
:vartype latitude: float
:ivar longitude:
:vartype longitude: float

<a id="models._models.ResumeSearchDetailLocationValue.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 
- `raw_input`: Required.

<a id="models._models.ResumeSearchDetailManagementLevel"></a>

## ResumeSearchDetailManagementLevel Objects

```python
class ResumeSearchDetailManagementLevel(msrest.serialization.Model)
```

ResumeSearchDetailManagementLevel.

:ivar level: Known values are: "None", "Low", "Mid", "Upper".
:vartype level: str or ~affinda.models.ManagementLevel
:ivar match:
:vartype match: bool

<a id="models._models.ResumeSearchDetailManagementLevel.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `level`: Known values are: "None", "Low", "Mid", "Upper".
- `match`: 

<a id="models._models.ResumeSearchDetailOccupationGroup"></a>

## ResumeSearchDetailOccupationGroup Objects

```python
class ResumeSearchDetailOccupationGroup(msrest.serialization.Model)
```

ResumeSearchDetailOccupationGroup.

:ivar missing:
:vartype missing: list[int]
:ivar value:
:vartype value: list[~affinda.models.OccupationGroupSearchResult]

<a id="models._models.ResumeSearchDetailOccupationGroup.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.ResumeSearchDetailSearchExpression"></a>

## ResumeSearchDetailSearchExpression Objects

```python
class ResumeSearchDetailSearchExpression(msrest.serialization.Model)
```

ResumeSearchDetailSearchExpression.

:ivar missing:
:vartype missing: list[str]
:ivar value:
:vartype value: list[str]

<a id="models._models.ResumeSearchDetailSearchExpression.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.ResumeSearchDetailSkills"></a>

## ResumeSearchDetailSkills Objects

```python
class ResumeSearchDetailSkills(msrest.serialization.Model)
```

ResumeSearchDetailSkills.

:ivar missing:
:vartype missing: list[~affinda.models.ResumeSearchParametersSkill]
:ivar value:
:vartype value: list[~affinda.models.ResumeSearchDetailSkillsValueItem]

<a id="models._models.ResumeSearchDetailSkills.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.ResumeSearchDetailSkillsValueItem"></a>

## ResumeSearchDetailSkillsValueItem Objects

```python
class ResumeSearchDetailSkillsValueItem(
        ResumeSkill,
        ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1
)
```

ResumeSearchDetailSkillsValueItem.

:ivar match:
:vartype match: bool
:ivar name:
:vartype name: str
:ivar last_used:
:vartype last_used: str
:ivar number_of_months:
:vartype number_of_months: int
:ivar type:
:vartype type: str
:ivar sources:
:vartype sources: list[~affinda.models.ResumeSkillSourcesItem]

<a id="models._models.ResumeSearchDetailSkillsValueItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 
- `name`: 
- `last_used`: 
- `number_of_months`: 
- `type`: 
- `sources`: 

<a id="models._models.ResumeSearchEmbed"></a>

## ResumeSearchEmbed Objects

```python
class ResumeSearchEmbed(msrest.serialization.Model)
```

ResumeSearchEmbed.

:ivar url: The signed URL for the embedable search tool.
:vartype url: str

<a id="models._models.ResumeSearchEmbed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `url`: The signed URL for the embedable search tool.

<a id="models._models.ResumeSearchMatch"></a>

## ResumeSearchMatch Objects

```python
class ResumeSearchMatch(msrest.serialization.Model)
```

ResumeSearchMatch.

:ivar score: The matching score between the provided resume and job description.
:vartype score: float
:ivar details:
:vartype details: ~affinda.models.ResumeSearchMatchDetails

<a id="models._models.ResumeSearchMatch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `score`: The matching score between the provided resume and job description.
- `details`: 

<a id="models._models.ResumeSearchMatchDetails"></a>

## ResumeSearchMatchDetails Objects

```python
class ResumeSearchMatchDetails(msrest.serialization.Model)
```

ResumeSearchMatchDetails.

:ivar job_title:
:vartype job_title: ~affinda.models.JobTitleSearchScoreComponent
:ivar management_level:
:vartype management_level: ~affinda.models.ManagementLevelSearchScoreComponent
:ivar experience:
:vartype experience: ~affinda.models.ExperienceSearchScoreComponent
:ivar skills:
:vartype skills: ~affinda.models.SkillsSearchScoreComponent
:ivar languages:
:vartype languages: ~affinda.models.LanguagesSearchScoreComponent
:ivar location:
:vartype location: ~affinda.models.LocationSearchScoreComponent
:ivar education:
:vartype education: ~affinda.models.EducationSearchScoreComponent
:ivar occupation_group:
:vartype occupation_group: ~affinda.models.OccupationGroupSearchScoreComponent
:ivar search_expression:
:vartype search_expression: ~affinda.models.SearchExpressionSearchScoreComponent

<a id="models._models.ResumeSearchMatchDetails.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `job_title`: 
- `management_level`: 
- `experience`: 
- `skills`: 
- `languages`: 
- `location`: 
- `education`: 
- `occupation_group`: 
- `search_expression`: 

<a id="models._models.ResumeSearchParameters"></a>

## ResumeSearchParameters Objects

```python
class ResumeSearchParameters(msrest.serialization.Model)
```

ResumeSearchParameters.

All required parameters must be populated in order to send to Azure.

:ivar indices: Required.
:vartype indices: list[str]
:ivar job_description: A random string that uniquely identify the resource.
:vartype job_description: str
:ivar resume: A random string that uniquely identify the resource.
:vartype resume: str
:ivar job_titles:
:vartype job_titles: list[str]
:ivar job_titles_current_only: Search only through the canditate's current job.
:vartype job_titles_current_only: bool
:ivar job_titles_required:
:vartype job_titles_required: bool
:ivar job_titles_weight:
:vartype job_titles_weight: float
:ivar years_experience_min: Minimum years of total work experience.
:vartype years_experience_min: int
:ivar years_experience_max: Maximum years of total work experience.
:vartype years_experience_max: int
:ivar years_experience_required:
:vartype years_experience_required: bool
:ivar years_experience_weight:
:vartype years_experience_weight: float
:ivar locations: Search by location name or by coordinates.
:vartype locations: list[~affinda.models.ResumeSearchParametersLocation]
:ivar locations_weight:
:vartype locations_weight: float
:ivar locations_required:
:vartype locations_required: bool
:ivar skills:
:vartype skills: list[~affinda.models.ResumeSearchParametersSkill]
:ivar skills_weight:
:vartype skills_weight: float
:ivar languages:
:vartype languages: list[~affinda.models.ResumeSearchParametersSkill]
:ivar languages_weight:
:vartype languages_weight: float
:ivar institutions:
:vartype institutions: list[str]
:ivar institutions_required:
:vartype institutions_required: bool
:ivar degrees:
:vartype degrees: list[str]
:ivar degrees_required:
:vartype degrees_required: bool
:ivar highest_degree_types:
:vartype highest_degree_types: list[str or ~affinda.models.EducationLevel]
:ivar highest_degree_types_required:
:vartype highest_degree_types_required: bool
:ivar is_current_student: Search for student canditates.
:vartype is_current_student: bool
:ivar is_current_student_required:
:vartype is_current_student_required: bool
:ivar is_recent_graduate: Search for canditates that graduated less than a year ago.
:vartype is_recent_graduate: bool
:ivar is_recent_graduate_required:
:vartype is_recent_graduate_required: bool
:ivar education_weight:
:vartype education_weight: float
:ivar search_expression: Search through resumes' raw text.
:vartype search_expression: str
:ivar search_expression_required:
:vartype search_expression_required: bool
:ivar search_expression_weight:
:vartype search_expression_weight: float
:ivar soc_codes:
:vartype soc_codes: list[int]
:ivar soc_codes_weight:
:vartype soc_codes_weight: float
:ivar soc_codes_required:
:vartype soc_codes_required: bool
:ivar management_level: Known values are: "None", "Low", "Mid", "Upper".
:vartype management_level: str or ~affinda.models.ManagementLevel
:ivar management_level_required:
:vartype management_level_required: bool
:ivar management_level_weight:
:vartype management_level_weight: float
:ivar custom_data:
:vartype custom_data: list[~affinda.models.ResumeSearchParametersCustomData]

<a id="models._models.ResumeSearchParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `indices`: Required.
- `job_description`: A random string that uniquely identify the resource.
- `resume`: A random string that uniquely identify the resource.
- `job_titles`: 
- `job_titles_current_only`: Search only through the canditate's current job.
- `job_titles_required`: 
- `job_titles_weight`: 
- `years_experience_min`: Minimum years of total work experience.
- `years_experience_max`: Maximum years of total work experience.
- `years_experience_required`: 
- `years_experience_weight`: 
- `locations`: Search by location name or by coordinates.
- `locations_weight`: 
- `locations_required`: 
- `skills`: 
- `skills_weight`: 
- `languages`: 
- `languages_weight`: 
- `institutions`: 
- `institutions_required`: 
- `degrees`: 
- `degrees_required`: 
- `highest_degree_types`: 
- `highest_degree_types_required`: 
- `is_current_student`: Search for student canditates.
- `is_current_student_required`: 
- `is_recent_graduate`: Search for canditates that graduated less than a year ago.
- `is_recent_graduate_required`: 
- `education_weight`: 
- `search_expression`: Search through resumes' raw text.
- `search_expression_required`: 
- `search_expression_weight`: 
- `soc_codes`: 
- `soc_codes_weight`: 
- `soc_codes_required`: 
- `management_level`: Known values are: "None", "Low", "Mid", "Upper".
- `management_level_required`: 
- `management_level_weight`: 
- `custom_data`: 

<a id="models._models.SearchParametersCustomData"></a>

## SearchParametersCustomData Objects

```python
class SearchParametersCustomData(msrest.serialization.Model)
```

SearchParametersCustomData.

All required parameters must be populated in order to send to Azure.

:ivar filter_type: Required. Data points of "text" type support only "equals" filterType,
 others support both "equals" and "range". Known values are: "equals", "range".
:vartype filter_type: str or ~affinda.models.SearchParametersCustomDataFilterType
:ivar data_point: Required. The data point's slug.
:vartype data_point: str
:ivar query: Required. "equals" searches require the "value" key inside the query, and "range"
 searches require at least one of "gte" (greater than or equal) and "lte" (less than or equal).
:vartype query: any
:ivar required:
:vartype required: bool
:ivar weight:
:vartype weight: float

<a id="models._models.SearchParametersCustomData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `filter_type`: Required. Data points of "text" type support only "equals" filterType,
others support both "equals" and "range". Known values are: "equals", "range".
- `data_point`: Required. The data point's slug.
- `query`: Required. "equals" searches require the "value" key inside the query, and
"range" searches require at least one of "gte" (greater than or equal) and "lte" (less than or
equal).
- `required`: 
- `weight`: 

<a id="models._models.ResumeSearchParametersCustomData"></a>

## ResumeSearchParametersCustomData Objects

```python
class ResumeSearchParametersCustomData(SearchParametersCustomData)
```

ResumeSearchParametersCustomData.

All required parameters must be populated in order to send to Azure.

:ivar filter_type: Required. Data points of "text" type support only "equals" filterType,
 others support both "equals" and "range". Known values are: "equals", "range".
:vartype filter_type: str or ~affinda.models.SearchParametersCustomDataFilterType
:ivar data_point: Required. The data point's slug.
:vartype data_point: str
:ivar query: Required. "equals" searches require the "value" key inside the query, and "range"
 searches require at least one of "gte" (greater than or equal) and "lte" (less than or equal).
:vartype query: any
:ivar required:
:vartype required: bool
:ivar weight:
:vartype weight: float

<a id="models._models.ResumeSearchParametersCustomData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `filter_type`: Required. Data points of "text" type support only "equals" filterType,
others support both "equals" and "range". Known values are: "equals", "range".
- `data_point`: Required. The data point's slug.
- `query`: Required. "equals" searches require the "value" key inside the query, and
"range" searches require at least one of "gte" (greater than or equal) and "lte" (less than or
equal).
- `required`: 
- `weight`: 

<a id="models._models.ResumeSearchParametersLocation"></a>

## ResumeSearchParametersLocation Objects

```python
class ResumeSearchParametersLocation(msrest.serialization.Model)
```

ResumeSearchParametersLocation.

:ivar name:
:vartype name: str
:ivar coordinates:
:vartype coordinates: ~affinda.models.ResumeSearchParametersLocationCoordinates
:ivar distance:
:vartype distance: int
:ivar unit: Known values are: "km", "mi". Default value: "km".
:vartype unit: str or ~affinda.models.SearchLocationUnit

<a id="models._models.ResumeSearchParametersLocation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `coordinates`: 
- `distance`: 
- `unit`: Known values are: "km", "mi". Default value: "km".

<a id="models._models.ResumeSearchParametersLocationCoordinates"></a>

## ResumeSearchParametersLocationCoordinates Objects

```python
class ResumeSearchParametersLocationCoordinates(msrest.serialization.Model)
```

ResumeSearchParametersLocationCoordinates.

:ivar latitude:
:vartype latitude: float
:ivar longitude:
:vartype longitude: float

<a id="models._models.ResumeSearchParametersLocationCoordinates.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `latitude`: 
- `longitude`: 

<a id="models._models.ResumeSearchParametersSkill"></a>

## ResumeSearchParametersSkill Objects

```python
class ResumeSearchParametersSkill(msrest.serialization.Model)
```

ResumeSearchParametersSkill.

:ivar name:
:vartype name: str
:ivar required:
:vartype required: bool

<a id="models._models.ResumeSearchParametersSkill.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `required`: 

<a id="models._models.ResumeSearchResult"></a>

## ResumeSearchResult Objects

```python
class ResumeSearchResult(msrest.serialization.Model)
```

ResumeSearchResult.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. A random string that uniquely identify the resource.
:vartype identifier: str
:ivar score: Required.
:vartype score: float
:ivar pdf: Required.
:vartype pdf: str
:ivar name:
:vartype name: str
:ivar job_title: Required.
:vartype job_title: ~affinda.models.JobTitleSearchScoreComponent
:ivar management_level: Required.
:vartype management_level: ~affinda.models.ManagementLevelSearchScoreComponent
:ivar experience: Required.
:vartype experience: ~affinda.models.ExperienceSearchScoreComponent
:ivar skills: Required.
:vartype skills: ~affinda.models.SkillsSearchScoreComponent
:ivar languages: Required.
:vartype languages: ~affinda.models.LanguagesSearchScoreComponent
:ivar location: Required.
:vartype location: ~affinda.models.LocationSearchScoreComponent
:ivar education: Required.
:vartype education: ~affinda.models.EducationSearchScoreComponent
:ivar occupation_group: Required.
:vartype occupation_group: ~affinda.models.OccupationGroupSearchScoreComponent
:ivar search_expression: Required.
:vartype search_expression: ~affinda.models.SearchExpressionSearchScoreComponent
:ivar custom_data: Required. Dictionary of
 <components·nqbw24·schemas·customdatasearchscorecomponent·additionalproperties>.
:vartype custom_data: dict[str,
 ~affinda.models.ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties]

<a id="models._models.ResumeSearchResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. A random string that uniquely identify the resource.
- `score`: Required.
- `pdf`: Required.
- `name`: 
- `job_title`: Required.
- `management_level`: Required.
- `experience`: Required.
- `skills`: Required.
- `languages`: Required.
- `location`: Required.
- `education`: Required.
- `occupation_group`: Required.
- `search_expression`: Required.
- `custom_data`: Required. Dictionary of
<components·nqbw24·schemas·customdatasearchscorecomponent·additionalproperties>.

<a id="models._models.ResumeSkillSourcesItem"></a>

## ResumeSkillSourcesItem Objects

```python
class ResumeSkillSourcesItem(msrest.serialization.Model)
```

ResumeSkillSourcesItem.

:ivar section: Known values are: "Achievements", "AdditionalInformation", "Education",
 "Extracurriculars", "Organisations", "Other", "PersonalDetails", "Projects", "Publications",
 "Referees", "Skills", "Summary", "Training", "WorkExperience", "NotPopulated", "Header",
 "Footer", "Skills/Interests/Languages", "Training/Certifications",
 "Extracurriculars/Leadership".
:vartype section: str or ~affinda.models.ResumeSkillSourcesItemSection
:ivar position:
:vartype position: int

<a id="models._models.ResumeSkillSourcesItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `section`: Known values are: "Achievements", "AdditionalInformation", "Education",
"Extracurriculars", "Organisations", "Other", "PersonalDetails", "Projects", "Publications",
"Referees", "Skills", "Summary", "Training", "WorkExperience", "NotPopulated", "Header",
"Footer", "Skills/Interests/Languages", "Training/Certifications",
"Extracurriculars/Leadership".
- `position`: 

<a id="models._models.RowAnnotation"></a>

## RowAnnotation Objects

```python
class RowAnnotation(Annotation)
```

RowAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~affinda.models.RowAnnotationParsed

<a id="models._models.RowAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.RowAnnotationParsed"></a>

## RowAnnotationParsed Objects

```python
class RowAnnotationParsed(msrest.serialization.Model)
```

RowAnnotationParsed.

:ivar item_code:
:vartype item_code: ~affinda.models.TextAnnotation
:ivar item_date:
:vartype item_date: ~affinda.models.DateAnnotation
:ivar item_description:
:vartype item_description: ~affinda.models.TextAnnotation
:ivar item_unit:
:vartype item_unit: ~affinda.models.TextAnnotation
:ivar item_unit_price:
:vartype item_unit_price: ~affinda.models.FloatAnnotation
:ivar item_quantity:
:vartype item_quantity: ~affinda.models.FloatAnnotation
:ivar item_discount:
:vartype item_discount: ~affinda.models.TextAnnotation
:ivar item_base_total:
:vartype item_base_total: ~affinda.models.FloatAnnotation
:ivar item_tax_rate:
:vartype item_tax_rate: ~affinda.models.TextAnnotation
:ivar item_tax_total:
:vartype item_tax_total: ~affinda.models.FloatAnnotation
:ivar item_total:
:vartype item_total: ~affinda.models.FloatAnnotation
:ivar item_other:
:vartype item_other: ~affinda.models.TextAnnotation

<a id="models._models.RowAnnotationParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `item_code`: 
- `item_date`: 
- `item_description`: 
- `item_unit`: 
- `item_unit_price`: 
- `item_quantity`: 
- `item_discount`: 
- `item_base_total`: 
- `item_tax_rate`: 
- `item_tax_total`: 
- `item_total`: 
- `item_other`: 

<a id="models._models.RowBetaAnnotation"></a>

## RowBetaAnnotation Objects

```python
class RowBetaAnnotation(Annotation)
```

RowBetaAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~affinda.models.RowBetaAnnotationParsed

<a id="models._models.RowBetaAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.RowBetaAnnotationParsed"></a>

## RowBetaAnnotationParsed Objects

```python
class RowBetaAnnotationParsed(msrest.serialization.Model)
```

RowBetaAnnotationParsed.

:ivar item_code_beta:
:vartype item_code_beta: ~affinda.models.TextAnnotation
:ivar item_date_beta:
:vartype item_date_beta: ~affinda.models.DateAnnotation
:ivar item_description_beta:
:vartype item_description_beta: ~affinda.models.TextAnnotation
:ivar item_unit_beta:
:vartype item_unit_beta: ~affinda.models.TextAnnotation
:ivar item_unit_price_beta:
:vartype item_unit_price_beta: ~affinda.models.FloatAnnotation
:ivar item_quantity_beta:
:vartype item_quantity_beta: ~affinda.models.FloatAnnotation
:ivar item_discount_beta:
:vartype item_discount_beta: ~affinda.models.TextAnnotation
:ivar item_base_total_beta:
:vartype item_base_total_beta: ~affinda.models.FloatAnnotation
:ivar item_tax_rate_beta:
:vartype item_tax_rate_beta: ~affinda.models.TextAnnotation
:ivar item_tax_total_beta:
:vartype item_tax_total_beta: ~affinda.models.FloatAnnotation
:ivar item_total_beta:
:vartype item_total_beta: ~affinda.models.FloatAnnotation
:ivar item_other_beta:
:vartype item_other_beta: ~affinda.models.TextAnnotation

<a id="models._models.RowBetaAnnotationParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `item_code_beta`: 
- `item_date_beta`: 
- `item_description_beta`: 
- `item_unit_beta`: 
- `item_unit_price_beta`: 
- `item_quantity_beta`: 
- `item_discount_beta`: 
- `item_base_total_beta`: 
- `item_tax_rate_beta`: 
- `item_tax_total_beta`: 
- `item_total_beta`: 
- `item_other_beta`: 

<a id="models._models.SearchConfigAction"></a>

## SearchConfigAction Objects

```python
class SearchConfigAction(msrest.serialization.Model)
```

SearchConfigAction.

All required parameters must be populated in order to send to Azure.

:ivar label: Required. Human readable label to display in the UI.
:vartype label: str
:ivar event_name: Required. Name of the event to be triggered.
:vartype event_name: str

<a id="models._models.SearchConfigAction.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `label`: Required. Human readable label to display in the UI.
- `event_name`: Required. Name of the event to be triggered.

<a id="models._models.SearchExpressionSearchScoreComponent"></a>

## SearchExpressionSearchScoreComponent Objects

```python
class SearchExpressionSearchScoreComponent(msrest.serialization.Model)
```

SearchExpressionSearchScoreComponent.

All required parameters must be populated in order to send to Azure.

:ivar label: Required.
:vartype label: str
:ivar value:
:vartype value: str
:ivar score:
:vartype score: float

<a id="models._models.SearchExpressionSearchScoreComponent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `label`: Required.
- `value`: 
- `score`: 

<a id="models._models.SkillAnnotation"></a>

## SkillAnnotation Objects

```python
class SkillAnnotation(Annotation)
```

SkillAnnotation.

Variables are only populated by the server, and will be ignored when sending a request.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: str

<a id="models._models.SkillAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.

<a id="models._models.SkillAnnotationUpdate"></a>

## SkillAnnotationUpdate Objects

```python
class SkillAnnotationUpdate(AnnotationBase)
```

SkillAnnotationUpdate.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle:
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles:
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar page_index:
:vartype page_index: int
:ivar raw:
:vartype raw: str
:ivar confidence: The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: The model's confidence that the text has been classified
 correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: If the document was submitted as an image, this is the
 confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified:
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar data_point:
:vartype data_point: str
:ivar content_type:
:vartype content_type: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.SkillAnnotationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: 
- `page_index`: 
- `raw`: 
- `confidence`: The overall confidence that the model's prediction is correct.
- `classification_confidence`: The model's confidence that the text has been classified
correctly.
- `text_extraction_confidence`: If the document was submitted as an image, this is the
confidence that the text in the image has been correctly read by the model.
- `is_verified`: 
- `is_client_verified`: 
- `is_auto_verified`: 
- `data_point`: 
- `content_type`: 

<a id="models._models.SkillsSearchScoreComponent"></a>

## SkillsSearchScoreComponent Objects

```python
class SkillsSearchScoreComponent(msrest.serialization.Model)
```

SkillsSearchScoreComponent.

All required parameters must be populated in order to send to Azure.

:ivar value:
:vartype value: str
:ivar label: Required.
:vartype label: str
:ivar score:
:vartype score: float

<a id="models._models.SkillsSearchScoreComponent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `value`: 
- `label`: Required.
- `score`: 

<a id="models._models.TableAnnotation"></a>

## TableAnnotation Objects

```python
class TableAnnotation(Annotation)
```

TableAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~affinda.models.TableAnnotationParsed

<a id="models._models.TableAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.TableAnnotationParsed"></a>

## TableAnnotationParsed Objects

```python
class TableAnnotationParsed(msrest.serialization.Model)
```

TableAnnotationParsed.

:ivar rows:
:vartype rows: list[~affinda.models.RowAnnotation]

<a id="models._models.TableAnnotationParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `rows`: 

<a id="models._models.TableBetaAnnotation"></a>

## TableBetaAnnotation Objects

```python
class TableBetaAnnotation(Annotation)
```

TableBetaAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~affinda.models.TableBetaAnnotationParsed

<a id="models._models.TableBetaAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.TableBetaAnnotationParsed"></a>

## TableBetaAnnotationParsed Objects

```python
class TableBetaAnnotationParsed(msrest.serialization.Model)
```

TableBetaAnnotationParsed.

:ivar rows:
:vartype rows: list[~affinda.models.RowBetaAnnotation]

<a id="models._models.TableBetaAnnotationParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `rows`: 

<a id="models._models.Tag"></a>

## Tag Objects

```python
class Tag(msrest.serialization.Model)
```

Tag.

All required parameters must be populated in order to send to Azure.

:ivar id: Required. Uniquely identify a tag.
:vartype id: int
:ivar name: Required.
:vartype name: str
:ivar workspace: Required. Uniquely identify a workspace.
:vartype workspace: str
:ivar document_count: Required. Number of documents tagged with this.
:vartype document_count: int

<a id="models._models.Tag.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Required. Uniquely identify a tag.
- `name`: Required.
- `workspace`: Required. Uniquely identify a workspace.
- `document_count`: Required. Number of documents tagged with this.

<a id="models._models.TagCreate"></a>

## TagCreate Objects

```python
class TagCreate(msrest.serialization.Model)
```

TagCreate.

All required parameters must be populated in order to send to Azure.

:ivar name: Required.
:vartype name: str
:ivar workspace: Required. Uniquely identify a workspace.
:vartype workspace: str

<a id="models._models.TagCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Required.
- `workspace`: Required. Uniquely identify a workspace.

<a id="models._models.TagUpdate"></a>

## TagUpdate Objects

```python
class TagUpdate(msrest.serialization.Model)
```

TagUpdate.

:ivar name:
:vartype name: str
:ivar workspace: Uniquely identify a workspace.
:vartype workspace: str

<a id="models._models.TagUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `workspace`: Uniquely identify a workspace.

<a id="models._models.TextAnnotationUpdate"></a>

## TextAnnotationUpdate Objects

```python
class TextAnnotationUpdate(AnnotationBase)
```

TextAnnotationUpdate.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle:
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles:
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar page_index:
:vartype page_index: int
:ivar raw:
:vartype raw: str
:ivar confidence: The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: The model's confidence that the text has been classified
 correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: If the document was submitted as an image, this is the
 confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified:
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar data_point:
:vartype data_point: str
:ivar content_type:
:vartype content_type: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.TextAnnotationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: 
- `page_index`: 
- `raw`: 
- `confidence`: The overall confidence that the model's prediction is correct.
- `classification_confidence`: The model's confidence that the text has been classified
correctly.
- `text_extraction_confidence`: If the document was submitted as an image, this is the
confidence that the text in the image has been correctly read by the model.
- `is_verified`: 
- `is_client_verified`: 
- `is_auto_verified`: 
- `data_point`: 
- `content_type`: 
- `parsed`: 

<a id="models._models.ThemeConfig"></a>

## ThemeConfig Objects

```python
class ThemeConfig(msrest.serialization.Model)
```

ThemeConfig.

:ivar palette:
:vartype palette: ~affinda.models.ThemeConfigPalette
:ivar typography:
:vartype typography: ~affinda.models.ThemeConfigTypography
:ivar border_radius:
:vartype border_radius: float
:ivar font_url:
:vartype font_url: str

<a id="models._models.ThemeConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `palette`: 
- `typography`: 
- `border_radius`: 
- `font_url`: 

<a id="models._models.ThemeConfigPalette"></a>

## ThemeConfigPalette Objects

```python
class ThemeConfigPalette(msrest.serialization.Model)
```

ThemeConfigPalette.

:ivar mode: Known values are: "light", "dark".
:vartype mode: str or ~affinda.models.ThemeConfigPaletteMode
:ivar background:
:vartype background: ~affinda.models.ThemeConfigPaletteBackground
:ivar text:
:vartype text: ~affinda.models.ThemeConfigPaletteText
:ivar divider:
:vartype divider: str
:ivar primary:
:vartype primary: ~affinda.models.PaletteColorOptions
:ivar secondary:
:vartype secondary: ~affinda.models.PaletteColorOptions
:ivar success:
:vartype success: ~affinda.models.PaletteColorOptions
:ivar annotation:
:vartype annotation: ~affinda.models.PaletteColorOptions
:ivar error:
:vartype error: ~affinda.models.PaletteColorOptions
:ivar info:
:vartype info: ~affinda.models.PaletteColorOptions
:ivar warning:
:vartype warning: ~affinda.models.PaletteColorOptions

<a id="models._models.ThemeConfigPalette.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `mode`: Known values are: "light", "dark".
- `background`: 
- `text`: 
- `divider`: 
- `primary`: 
- `secondary`: 
- `success`: 
- `annotation`: 
- `error`: 
- `info`: 
- `warning`: 

<a id="models._models.ThemeConfigPaletteBackground"></a>

## ThemeConfigPaletteBackground Objects

```python
class ThemeConfigPaletteBackground(msrest.serialization.Model)
```

ThemeConfigPaletteBackground.

:ivar default:
:vartype default: str
:ivar paper:
:vartype paper: str

<a id="models._models.ThemeConfigPaletteBackground.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `default`: 
- `paper`: 

<a id="models._models.ThemeConfigPaletteText"></a>

## ThemeConfigPaletteText Objects

```python
class ThemeConfigPaletteText(msrest.serialization.Model)
```

ThemeConfigPaletteText.

:ivar primary:
:vartype primary: str
:ivar secondary:
:vartype secondary: str
:ivar disabled:
:vartype disabled: str

<a id="models._models.ThemeConfigPaletteText.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `primary`: 
- `secondary`: 
- `disabled`: 

<a id="models._models.ThemeConfigTypography"></a>

## ThemeConfigTypography Objects

```python
class ThemeConfigTypography(msrest.serialization.Model)
```

ThemeConfigTypography.

:ivar font_family:
:vartype font_family: str
:ivar font_size:
:vartype font_size: str
:ivar font_weight_regular:
:vartype font_weight_regular: str
:ivar font_weight_medium:
:vartype font_weight_medium: str
:ivar font_weight_bold:
:vartype font_weight_bold: str

<a id="models._models.ThemeConfigTypography.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `font_family`: 
- `font_size`: 
- `font_weight_regular`: 
- `font_weight_medium`: 
- `font_weight_bold`: 

<a id="models._models.UrlAnnotation"></a>

## UrlAnnotation Objects

```python
class UrlAnnotation(Annotation)
```

UrlAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed:
:vartype parsed: ~affinda.models.UrlAnnotationParsed

<a id="models._models.UrlAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: 

<a id="models._models.UrlAnnotationParsed"></a>

## UrlAnnotationParsed Objects

```python
class UrlAnnotationParsed(msrest.serialization.Model)
```

UrlAnnotationParsed.

:ivar url:
:vartype url: str
:ivar domain:
:vartype domain: str

<a id="models._models.UrlAnnotationParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `url`: 
- `domain`: 

<a id="models._models.UsageByCollection"></a>

## UsageByCollection Objects

```python
class UsageByCollection(msrest.serialization.Model)
```

Monthly credits consumption.

All required parameters must be populated in order to send to Azure.

:ivar month: Required. Month of the usage.
:vartype month: str
:ivar count: Required. Usage count.
:vartype count: int

<a id="models._models.UsageByCollection.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `month`: Required. Month of the usage.
- `count`: Required. Usage count.

<a id="models._models.UsageByWorkspace"></a>

## UsageByWorkspace Objects

```python
class UsageByWorkspace(msrest.serialization.Model)
```

Monthly credits consumption.

All required parameters must be populated in order to send to Azure.

:ivar month: Required. Month of the usage.
:vartype month: str
:ivar count: Required. Usage count.
:vartype count: int

<a id="models._models.UsageByWorkspace.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `month`: Required. Month of the usage.
- `count`: Required. Usage count.

<a id="models._models.UserNullable"></a>

## UserNullable Objects

```python
class UserNullable(msrest.serialization.Model)
```

UserNullable.

:ivar id: Uniquely identify a user.
:vartype id: int
:ivar name:
:vartype name: str
:ivar username:
:vartype username: str
:ivar email:
:vartype email: str
:ivar avatar: URL of the user's avatar.
:vartype avatar: str

<a id="models._models.UserNullable.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: Uniquely identify a user.
- `name`: 
- `username`: 
- `email`: 
- `avatar`: URL of the user's avatar.

<a id="models._models.ValidationToolConfig"></a>

## ValidationToolConfig Objects

```python
class ValidationToolConfig(msrest.serialization.Model)
```

Configuration of the embeddable validation tool.

:ivar theme:
:vartype theme: ~affinda.models.ThemeConfig
:ivar hide_actions: Hide the confirm document button and other actions.
:vartype hide_actions: bool
:ivar hide_collection: Hide the collection selector.
:vartype hide_collection: bool
:ivar hide_export: Hide the export menu.
:vartype hide_export: bool
:ivar hide_filename: Hide the filename input.
:vartype hide_filename: bool
:ivar hide_tags: Hide the tags editor.
:vartype hide_tags: bool
:ivar hide_warnings: Hide the warnings panel.
:vartype hide_warnings: bool
:ivar restrict_document_splitting: Disable the page editor after a document has been split
 once.
:vartype restrict_document_splitting: bool
:ivar disable_currency_formatting: Disable currency formatting of decimals values.
:vartype disable_currency_formatting: bool
:ivar disable_edit_document_metadata: Disable editing document metadata. Makes the collection
 selector, filename input and tags editor read only.
:vartype disable_edit_document_metadata: bool

<a id="models._models.ValidationToolConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `theme`: 
- `hide_actions`: Hide the confirm document button and other actions.
- `hide_collection`: Hide the collection selector.
- `hide_export`: Hide the export menu.
- `hide_filename`: Hide the filename input.
- `hide_tags`: Hide the tags editor.
- `hide_warnings`: Hide the warnings panel.
- `restrict_document_splitting`: Disable the page editor after a document has been split
once.
- `disable_currency_formatting`: Disable currency formatting of decimals values.
- `disable_edit_document_metadata`: Disable editing document metadata. Makes the
collection selector, filename input and tags editor read only.

<a id="models._models.Workspace"></a>

## Workspace Objects

```python
class Workspace(msrest.serialization.Model)
```

Workspace.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify a workspace.
:vartype identifier: str
:ivar organization:
:vartype organization: ~affinda.models.Organization
:ivar name:
:vartype name: str
:ivar visibility: Visibility "organization" means everyone in the organization can access the
 workspace. Visibility "private" means only people explicitly added can access the workspace.
 Known values are: "organization", "private".
:vartype visibility: str or ~affinda.models.WorkspaceVisibility
:ivar collections:
:vartype collections: list[~affinda.models.WorkspaceCollectionsItem]
:ivar reject_invalid_documents: If true, the uploaded document will be rejected if it's of the
 wrong document type, or if its document type cannot be determined. No credits will be consumed.
:vartype reject_invalid_documents: bool
:ivar reject_duplicates: If "true", parsing will fail when the uploaded document is duplicate
 of an existing document, no credits will be consumed. If "false", will parse the document
 normally whether its a duplicate or not. If not provided, will fallback to the workspace
 settings.
:vartype reject_duplicates: bool
:ivar members:
:vartype members: list[~affinda.models.User]
:ivar unvalidated_docs_count: Number of unvalidated documents in the workspace.
:vartype unvalidated_docs_count: int
:ivar confirmed_docs_count: Number of validated documents in the workspace.
:vartype confirmed_docs_count: int
:ivar ingest_email: When you send email to this address, any document attached in the body will
 be uploaded to this workspace.
:vartype ingest_email: str
:ivar whitelist_ingest_addresses: If specified, only emails from these addresses will be
 ingested for parsing. Wild cards are allowed, e.g. "*@eyefind.info".
:vartype whitelist_ingest_addresses: list[str]
:ivar document_splitter: Option "leave" means no document splitting at all. Option
 "conservative" means we don't actually split documents the documents, but will add a warning to
 documents that may require a split. Option "recommended" means we split documents that are
 highly likely to require a split, and add warnings to documents that might require one. Option
 "aggressive" means we split all documents that are likely to require a split. Known values are:
 "leave", "conservative", "recommended", "aggressive".
:vartype document_splitter: str or ~affinda.models.WorkspaceSplitDocumentsOptions

<a id="models._models.Workspace.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify a workspace.
- `organization`: 
- `name`: 
- `visibility`: Visibility "organization" means everyone in the organization can access
the workspace. Visibility "private" means only people explicitly added can access the
workspace. Known values are: "organization", "private".
- `collections`: 
- `reject_invalid_documents`: If true, the uploaded document will be rejected if it's of
the wrong document type, or if its document type cannot be determined. No credits will be
consumed.
- `reject_duplicates`: If "true", parsing will fail when the uploaded document is
duplicate of an existing document, no credits will be consumed. If "false", will parse the
document normally whether its a duplicate or not. If not provided, will fallback to the
workspace settings.
- `members`: 
- `unvalidated_docs_count`: Number of unvalidated documents in the workspace.
- `confirmed_docs_count`: Number of validated documents in the workspace.
- `ingest_email`: When you send email to this address, any document attached in the body
will be uploaded to this workspace.
- `whitelist_ingest_addresses`: If specified, only emails from these addresses will be
ingested for parsing. Wild cards are allowed, e.g. "*@eyefind.info".
- `document_splitter`: Option "leave" means no document splitting at all. Option
"conservative" means we don't actually split documents the documents, but will add a warning to
documents that may require a split. Option "recommended" means we split documents that are
highly likely to require a split, and add warnings to documents that might require one. Option
"aggressive" means we split all documents that are likely to require a split. Known values are:
"leave", "conservative", "recommended", "aggressive".

<a id="models._models.WorkspaceCollectionsItem"></a>

## WorkspaceCollectionsItem Objects

```python
class WorkspaceCollectionsItem(msrest.serialization.Model)
```

WorkspaceCollectionsItem.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify a collection.
:vartype identifier: str
:ivar name: Required.
:vartype name: str
:ivar extractor: Required.
:vartype extractor: ~affinda.models.WorkspaceCollectionsItemExtractor
:ivar unvalidated_docs_count: Number of unvalidated documents in the collection.
:vartype unvalidated_docs_count: int
:ivar confirmed_docs_count: Number of validated documents in the collection.
:vartype confirmed_docs_count: int

<a id="models._models.WorkspaceCollectionsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify a collection.
- `name`: Required.
- `extractor`: Required.
- `unvalidated_docs_count`: Number of unvalidated documents in the collection.
- `confirmed_docs_count`: Number of validated documents in the collection.

<a id="models._models.WorkspaceCollectionsItemExtractor"></a>

## WorkspaceCollectionsItemExtractor Objects

```python
class WorkspaceCollectionsItemExtractor(msrest.serialization.Model)
```

WorkspaceCollectionsItemExtractor.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Uniquely identify an extractor.
:vartype identifier: str
:ivar name: Required.
:vartype name: str
:ivar name_plural: Required.
:vartype name_plural: str
:ivar base_extractor:
:vartype base_extractor: ~affinda.models.BaseExtractor
:ivar category:
:vartype category: str
:ivar validatable: Required.
:vartype validatable: bool
:ivar is_custom:
:vartype is_custom: bool
:ivar created_dt:
:vartype created_dt: ~datetime.datetime

<a id="models._models.WorkspaceCollectionsItemExtractor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Uniquely identify an extractor.
- `name`: Required.
- `name_plural`: Required.
- `base_extractor`: 
- `category`: 
- `validatable`: Required.
- `is_custom`: 
- `created_dt`: 

<a id="models._models.WorkspaceCreate"></a>

## WorkspaceCreate Objects

```python
class WorkspaceCreate(msrest.serialization.Model)
```

WorkspaceCreate.

All required parameters must be populated in order to send to Azure.

:ivar organization: Required. Uniquely identify an organization.
:vartype organization: str
:ivar name: Required.
:vartype name: str
:ivar visibility: Visibility "organization" means everyone in the organization can access the
 workspace. Visibility "private" means only people explicitly added can access the workspace.
 Known values are: "organization", "private".
:vartype visibility: str or ~affinda.models.WorkspaceVisibility
:ivar reject_invalid_documents: If true, the uploaded document will be rejected if it's of the
 wrong document type, or if its document type cannot be determined. No credits will be consumed.
:vartype reject_invalid_documents: bool
:ivar reject_duplicates: If "true", parsing will fail when the uploaded document is duplicate
 of an existing document, no credits will be consumed. If "false", will parse the document
 normally whether its a duplicate or not. If not provided, will fallback to the workspace
 settings.
:vartype reject_duplicates: bool
:ivar whitelist_ingest_addresses: If specified, only emails from these addresses will be
 ingested for parsing. Wild cards are allowed, e.g. "*@eyefind.info".
:vartype whitelist_ingest_addresses: list[str]
:ivar document_splitter: Option "leave" means no document splitting at all. Option
 "conservative" means we don't actually split documents the documents, but will add a warning to
 documents that may require a split. Option "recommended" means we split documents that are
 highly likely to require a split, and add warnings to documents that might require one. Option
 "aggressive" means we split all documents that are likely to require a split. Known values are:
 "leave", "conservative", "recommended", "aggressive".
:vartype document_splitter: str or ~affinda.models.WorkspaceSplitDocumentsOptions

<a id="models._models.WorkspaceCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `organization`: Required. Uniquely identify an organization.
- `name`: Required.
- `visibility`: Visibility "organization" means everyone in the organization can access
the workspace. Visibility "private" means only people explicitly added can access the
workspace. Known values are: "organization", "private".
- `reject_invalid_documents`: If true, the uploaded document will be rejected if it's of
the wrong document type, or if its document type cannot be determined. No credits will be
consumed.
- `reject_duplicates`: If "true", parsing will fail when the uploaded document is
duplicate of an existing document, no credits will be consumed. If "false", will parse the
document normally whether its a duplicate or not. If not provided, will fallback to the
workspace settings.
- `whitelist_ingest_addresses`: If specified, only emails from these addresses will be
ingested for parsing. Wild cards are allowed, e.g. "*@eyefind.info".
- `document_splitter`: Option "leave" means no document splitting at all. Option
"conservative" means we don't actually split documents the documents, but will add a warning to
documents that may require a split. Option "recommended" means we split documents that are
highly likely to require a split, and add warnings to documents that might require one. Option
"aggressive" means we split all documents that are likely to require a split. Known values are:
"leave", "conservative", "recommended", "aggressive".

<a id="models._models.WorkspaceMembership"></a>

## WorkspaceMembership Objects

```python
class WorkspaceMembership(msrest.serialization.Model)
```

WorkspaceMembership.

:ivar identifier: Uniquely identify a membership.
:vartype identifier: str
:ivar workspace: Uniquely identify a workspace.
:vartype workspace: str
:ivar user:
:vartype user: ~affinda.models.User

<a id="models._models.WorkspaceMembership.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Uniquely identify a membership.
- `workspace`: Uniquely identify a workspace.
- `user`: 

<a id="models._models.WorkspaceMembershipCreate"></a>

## WorkspaceMembershipCreate Objects

```python
class WorkspaceMembershipCreate(msrest.serialization.Model)
```

WorkspaceMembershipCreate.

:ivar workspace: Uniquely identify a workspace.
:vartype workspace: str
:ivar user: Uniquely identify a user.
:vartype user: int

<a id="models._models.WorkspaceMembershipCreate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `workspace`: Uniquely identify a workspace.
- `user`: Uniquely identify a user.

<a id="models._models.WorkspaceUpdate"></a>

## WorkspaceUpdate Objects

```python
class WorkspaceUpdate(msrest.serialization.Model)
```

WorkspaceUpdate.

:ivar name:
:vartype name: str
:ivar visibility: Visibility "organization" means everyone in the organization can access the
 workspace. Visibility "private" means only people explicitly added can access the workspace.
 Known values are: "organization", "private".
:vartype visibility: str or ~affinda.models.WorkspaceVisibility
:ivar reject_invalid_documents: If true, the uploaded document will be rejected if it's of the
 wrong document type, or if its document type cannot be determined. No credits will be consumed.
:vartype reject_invalid_documents: bool
:ivar reject_duplicates: If "true", parsing will fail when the uploaded document is duplicate
 of an existing document, no credits will be consumed. If "false", will parse the document
 normally whether its a duplicate or not. If not provided, will fallback to the workspace
 settings.
:vartype reject_duplicates: bool
:ivar whitelist_ingest_addresses: If specified, only emails from these addresses will be
 ingested for parsing. Wild cards are allowed, e.g. "*@eyefind.info".
:vartype whitelist_ingest_addresses: list[str]
:ivar document_splitter: Option "leave" means no document splitting at all. Option
 "conservative" means we don't actually split documents the documents, but will add a warning to
 documents that may require a split. Option "recommended" means we split documents that are
 highly likely to require a split, and add warnings to documents that might require one. Option
 "aggressive" means we split all documents that are likely to require a split. Known values are:
 "leave", "conservative", "recommended", "aggressive".
:vartype document_splitter: str or ~affinda.models.WorkspaceSplitDocumentsOptions

<a id="models._models.WorkspaceUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `visibility`: Visibility "organization" means everyone in the organization can access
the workspace. Visibility "private" means only people explicitly added can access the
workspace. Known values are: "organization", "private".
- `reject_invalid_documents`: If true, the uploaded document will be rejected if it's of
the wrong document type, or if its document type cannot be determined. No credits will be
consumed.
- `reject_duplicates`: If "true", parsing will fail when the uploaded document is
duplicate of an existing document, no credits will be consumed. If "false", will parse the
document normally whether its a duplicate or not. If not provided, will fallback to the
workspace settings.
- `whitelist_ingest_addresses`: If specified, only emails from these addresses will be
ingested for parsing. Wild cards are allowed, e.g. "*@eyefind.info".
- `document_splitter`: Option "leave" means no document splitting at all. Option
"conservative" means we don't actually split documents the documents, but will add a warning to
documents that may require a split. Option "recommended" means we split documents that are
highly likely to require a split, and add warnings to documents that might require one. Option
"aggressive" means we split all documents that are likely to require a split. Known values are:
"leave", "conservative", "recommended", "aggressive".

<a id="models._models.YearsExperienceAnnotation"></a>

## YearsExperienceAnnotation Objects

```python
class YearsExperienceAnnotation(Annotation)
```

YearsExperienceAnnotation.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id: Required. Annotation's ID.
:vartype id: int
:ivar rectangle: Required. x/y coordinates for the rectangular bounding box containing the
 data.
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles: Required. x/y coordinates for the rectangles containing the data. An
 annotation can be contained within multiple rectangles.
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar document: Required. Unique identifier for the document.
:vartype document: str
:ivar page_index: Required. The page number within the document, starting from 0.
:vartype page_index: int
:ivar raw: Required. Raw data extracted from the before any post-processing.
:vartype raw: str
:ivar confidence: Required. The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: Required. The model's confidence that the text has been
 classified correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: Required. If the document was submitted as an image, this is
 the confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified: Required. Indicates whether the data has been validated, either by a human
 using our validation tool or through auto-validation rules.
:vartype is_verified: bool
:ivar is_client_verified: Required. Indicates whether the data has been validated by a human.
:vartype is_client_verified: bool
:ivar is_auto_verified: Required. Indicates whether the data has been auto-validated.
:vartype is_auto_verified: bool
:ivar data_point: Required. Data point's identifier.
:vartype data_point: str
:ivar content_type: Required. The different data types of annotations. Known values are:
 "text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
 "location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
 "skill", "yearsexperience", "group", "table_deprecated", "url", "image".
:vartype content_type: str or ~affinda.models.AnnotationContentType
:ivar parent: The parent annotation's ID.
:vartype parent: int
:ivar parsed: Years of experience range.
:vartype parsed: ~affinda.models.YearsExperienceAnnotationParsed

<a id="models._models.YearsExperienceAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: Required. Annotation's ID.
- `rectangle`: Required. x/y coordinates for the rectangular bounding box containing the
data.
- `rectangles`: Required. x/y coordinates for the rectangles containing the data. An
annotation can be contained within multiple rectangles.
- `document`: Required. Unique identifier for the document.
- `page_index`: Required. The page number within the document, starting from 0.
- `raw`: Required. Raw data extracted from the before any post-processing.
- `confidence`: Required. The overall confidence that the model's prediction is correct.
- `classification_confidence`: Required. The model's confidence that the text has been
classified correctly.
- `text_extraction_confidence`: Required. If the document was submitted as an image, this
is the confidence that the text in the image has been correctly read by the model.
- `is_verified`: Required. Indicates whether the data has been validated, either by a
human using our validation tool or through auto-validation rules.
- `is_client_verified`: Required. Indicates whether the data has been validated by a
human.
- `is_auto_verified`: Required. Indicates whether the data has been auto-validated.
- `data_point`: Required. Data point's identifier.
- `content_type`: Required. The different data types of annotations. Known values are:
"text", "integer", "float", "decimal", "date", "datetime", "daterange", "boolean", "enum",
"location", "phonenumber", "json", "table", "expectedremuneration", "jobtitle", "language",
"skill", "yearsexperience", "group", "table_deprecated", "url", "image".
- `parent`: The parent annotation's ID.
- `parsed`: Years of experience range.

<a id="models._models.YearsExperienceAnnotationParsed"></a>

## YearsExperienceAnnotationParsed Objects

```python
class YearsExperienceAnnotationParsed(msrest.serialization.Model)
```

Years of experience range.

:ivar minimum: Minimum years of experience.
:vartype minimum: float
:ivar maximum: Maximum years of experience.
:vartype maximum: float

<a id="models._models.YearsExperienceAnnotationParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `minimum`: Minimum years of experience.
- `maximum`: Maximum years of experience.

<a id="models._models.YearsExperienceAnnotationUpdate"></a>

## YearsExperienceAnnotationUpdate Objects

```python
class YearsExperienceAnnotationUpdate(AnnotationBase)
```

YearsExperienceAnnotationUpdate.

Variables are only populated by the server, and will be ignored when sending a request.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle:
:vartype rectangle: ~affinda.models.Rectangle
:ivar rectangles:
:vartype rectangles: list[~affinda.models.Rectangle]
:ivar page_index:
:vartype page_index: int
:ivar raw:
:vartype raw: str
:ivar confidence: The overall confidence that the model's prediction is correct.
:vartype confidence: float
:ivar classification_confidence: The model's confidence that the text has been classified
 correctly.
:vartype classification_confidence: float
:ivar text_extraction_confidence: If the document was submitted as an image, this is the
 confidence that the text in the image has been correctly read by the model.
:vartype text_extraction_confidence: float
:ivar is_verified:
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar data_point:
:vartype data_point: str
:ivar content_type:
:vartype content_type: str
:ivar parsed: Years of experience range.
:vartype parsed: ~affinda.models.YearsExperienceAnnotationUpdateParsed

<a id="models._models.YearsExperienceAnnotationUpdate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: 
- `page_index`: 
- `raw`: 
- `confidence`: The overall confidence that the model's prediction is correct.
- `classification_confidence`: The model's confidence that the text has been classified
correctly.
- `text_extraction_confidence`: If the document was submitted as an image, this is the
confidence that the text in the image has been correctly read by the model.
- `is_verified`: 
- `is_client_verified`: 
- `is_auto_verified`: 
- `data_point`: 
- `content_type`: 
- `parsed`: Years of experience range.

<a id="models._models.YearsExperienceAnnotationUpdateParsed"></a>

## YearsExperienceAnnotationUpdateParsed Objects

```python
class YearsExperienceAnnotationUpdateParsed(msrest.serialization.Model)
```

Years of experience range.

:ivar minimum: Minimum years of experience.
:vartype minimum: float
:ivar maximum: Maximum years of experience.
:vartype maximum: float

<a id="models._models.YearsExperienceAnnotationUpdateParsed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `minimum`: Minimum years of experience.
- `maximum`: Maximum years of experience.

