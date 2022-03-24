<a id="models._models"></a>

# models.\_models

<a id="models._models.Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification"></a>

## Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification Objects

```python
class Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification(msrest.serialization.Model)
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

<a id="models._models.Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword title: SOC2020 classification for this job title.
:paramtype title: str
:keyword minor_group: SOC2020 minor group.
:paramtype minor_group: str
:keyword sub_major_group: SOC2020 sub major group.
:paramtype sub_major_group: str
:keyword major_group: SOC2020 major group.
:paramtype major_group: str
:keyword soc_code: The 4 digit code representing the SOC2020 classification for this job title.
:paramtype soc_code: int

<a id="models._models.Error"></a>

## Error Objects

```python
class Error(msrest.serialization.Model)
```

Error.

:ivar error_code:
:vartype error_code: str
:ivar error_detail:
:vartype error_detail: str

<a id="models._models.Error.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword error_code:
:paramtype error_code: str
:keyword error_detail:
:paramtype error_detail: str

<a id="models._models.Get200ApplicationJsonPropertiesItemsItem"></a>

## Get200ApplicationJsonPropertiesItemsItem Objects

```python
class Get200ApplicationJsonPropertiesItemsItem(msrest.serialization.Model)
```

Get200ApplicationJsonPropertiesItemsItem.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Unique identifier for the document. If creating a document and left
 blank, one will be automatically generated.
:vartype identifier: str
:ivar format_file: Required. URL to a template to apply.
:vartype format_file: str

<a id="models._models.Get200ApplicationJsonPropertiesItemsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword identifier: Required. Unique identifier for the document. If creating a document and
left blank, one will be automatically generated.
:paramtype identifier: str
:keyword format_file: Required. URL to a template to apply.
:paramtype format_file: str

<a id="models._models.GetAllDocumentsResults"></a>

## GetAllDocumentsResults Objects

```python
class GetAllDocumentsResults(msrest.serialization.Model)
```

GetAllDocumentsResults.

:ivar count: Number of documents in result.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str
:ivar results:
:vartype results: list[~affinda.models.Meta]

<a id="models._models.GetAllDocumentsResults.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword count: Number of documents in result.
:paramtype count: int
:keyword next: URL to request next page of results.
:paramtype next: str
:keyword previous: URL to request previous page of results.
:paramtype previous: str
:keyword results:
:paramtype results: list[~affinda.models.Meta]

<a id="models._models.GetAllInvoicesResults"></a>

## GetAllInvoicesResults Objects

```python
class GetAllInvoicesResults(msrest.serialization.Model)
```

GetAllInvoicesResults.

:ivar count: Number of documents in result.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str
:ivar results:
:vartype results: list[~affinda.models.Meta]

<a id="models._models.GetAllInvoicesResults.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword count: Number of documents in result.
:paramtype count: int
:keyword next: URL to request next page of results.
:paramtype next: str
:keyword previous: URL to request previous page of results.
:paramtype previous: str
:keyword results:
:paramtype results: list[~affinda.models.Meta]

<a id="models._models.Invoice"></a>

## Invoice Objects

```python
class Invoice(msrest.serialization.Model)
```

Invoice.

All required parameters must be populated in order to send to Azure.

:ivar data: Required.
:vartype data: ~affinda.models.InvoiceData
:ivar meta: Required.
:vartype meta: ~affinda.models.Meta
:ivar error: Required.
:vartype error: ~affinda.models.Error

<a id="models._models.Invoice.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword data: Required.
:paramtype data: ~affinda.models.InvoiceData
:keyword meta: Required.
:paramtype meta: ~affinda.models.Meta
:keyword error: Required.
:paramtype error: ~affinda.models.Error

<a id="models._models.InvoiceData"></a>

## InvoiceData Objects

```python
class InvoiceData(msrest.serialization.Model)
```

InvoiceData.

:ivar invoice_date:
:vartype invoice_date: str
:ivar invoice_order_date:
:vartype invoice_order_date: str
:ivar payment_date_due:
:vartype payment_date_due: str
:ivar payment_amount_base:
:vartype payment_amount_base: str
:ivar payment_amount_tax:
:vartype payment_amount_tax: str
:ivar payment_amount_total:
:vartype payment_amount_total: str
:ivar payment_amount_paid:
:vartype payment_amount_paid: str
:ivar payment_amount_due:
:vartype payment_amount_due: str
:ivar invoice_number:
:vartype invoice_number: str
:ivar invoice_purchase_order_number:
:vartype invoice_purchase_order_number: str
:ivar supplier_business_number:
:vartype supplier_business_number: str
:ivar customer_number:
:vartype customer_number: str
:ivar customer_business_number:
:vartype customer_business_number: str
:ivar payment_reference:
:vartype payment_reference: str
:ivar bank_account_number:
:vartype bank_account_number: str
:ivar supplier_vat:
:vartype supplier_vat: str
:ivar customer_vat:
:vartype customer_vat: str
:ivar bpay_biller_code:
:vartype bpay_biller_code: str
:ivar bpay_reference:
:vartype bpay_reference: str
:ivar bank_sort_code:
:vartype bank_sort_code: str
:ivar bank_iban:
:vartype bank_iban: str
:ivar bank_swift:
:vartype bank_swift: str
:ivar bank_bsb:
:vartype bank_bsb: str
:ivar customer_contact_name:
:vartype customer_contact_name: str
:ivar customer_company_name:
:vartype customer_company_name: str
:ivar supplier_company_name:
:vartype supplier_company_name: str
:ivar customer_billing_address:
:vartype customer_billing_address: ~affinda.models.Location
:ivar customer_delivery_address:
:vartype customer_delivery_address: ~affinda.models.Location
:ivar supplier_address:
:vartype supplier_address: ~affinda.models.Location
:ivar customer_phone_number:
:vartype customer_phone_number: str
:ivar supplier_phone_number:
:vartype supplier_phone_number: str
:ivar supplier_fax:
:vartype supplier_fax: str
:ivar customer_email:
:vartype customer_email: str
:ivar supplier_email:
:vartype supplier_email: str
:ivar supplier_website:
:vartype supplier_website: str

<a id="models._models.InvoiceData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword invoice_date:
:paramtype invoice_date: str
:keyword invoice_order_date:
:paramtype invoice_order_date: str
:keyword payment_date_due:
:paramtype payment_date_due: str
:keyword payment_amount_base:
:paramtype payment_amount_base: str
:keyword payment_amount_tax:
:paramtype payment_amount_tax: str
:keyword payment_amount_total:
:paramtype payment_amount_total: str
:keyword payment_amount_paid:
:paramtype payment_amount_paid: str
:keyword payment_amount_due:
:paramtype payment_amount_due: str
:keyword invoice_number:
:paramtype invoice_number: str
:keyword invoice_purchase_order_number:
:paramtype invoice_purchase_order_number: str
:keyword supplier_business_number:
:paramtype supplier_business_number: str
:keyword customer_number:
:paramtype customer_number: str
:keyword customer_business_number:
:paramtype customer_business_number: str
:keyword payment_reference:
:paramtype payment_reference: str
:keyword bank_account_number:
:paramtype bank_account_number: str
:keyword supplier_vat:
:paramtype supplier_vat: str
:keyword customer_vat:
:paramtype customer_vat: str
:keyword bpay_biller_code:
:paramtype bpay_biller_code: str
:keyword bpay_reference:
:paramtype bpay_reference: str
:keyword bank_sort_code:
:paramtype bank_sort_code: str
:keyword bank_iban:
:paramtype bank_iban: str
:keyword bank_swift:
:paramtype bank_swift: str
:keyword bank_bsb:
:paramtype bank_bsb: str
:keyword customer_contact_name:
:paramtype customer_contact_name: str
:keyword customer_company_name:
:paramtype customer_company_name: str
:keyword supplier_company_name:
:paramtype supplier_company_name: str
:keyword customer_billing_address:
:paramtype customer_billing_address: ~affinda.models.Location
:keyword customer_delivery_address:
:paramtype customer_delivery_address: ~affinda.models.Location
:keyword supplier_address:
:paramtype supplier_address: ~affinda.models.Location
:keyword customer_phone_number:
:paramtype customer_phone_number: str
:keyword supplier_phone_number:
:paramtype supplier_phone_number: str
:keyword supplier_fax:
:paramtype supplier_fax: str
:keyword customer_email:
:paramtype customer_email: str
:keyword supplier_email:
:paramtype supplier_email: str
:keyword supplier_website:
:paramtype supplier_website: str

<a id="models._models.Location"></a>

## Location Objects

```python
class Location(msrest.serialization.Model)
```

Location.

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

<a id="models._models.Location.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword formatted:
:paramtype formatted: str
:keyword postal_code:
:paramtype postal_code: str
:keyword state:
:paramtype state: str
:keyword country:
:paramtype country: str
:keyword country_code: Two letter country code (ISO 3166-1 alpha-2).
:paramtype country_code: str
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

<a id="models._models.Meta"></a>

## Meta Objects

```python
class Meta(msrest.serialization.Model)
```

Meta.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Unique identifier for the document. If creating a document and left
 blank, one will be automatically generated.
:vartype identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar ready: Required. If true, the document has finished processing. Particularly useful if an
 endpoint request specified wait=False, when polling use this variable to determine when to stop
 polling.
:vartype ready: bool
:ivar ready_dt: The datetime when the document was ready.
:vartype ready_dt: ~datetime.datetime
:ivar failed: Required. If true, some exception was raised during processing. Check the 'error'
 field of the main return object.
:vartype failed: bool
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: str

<a id="models._models.Meta.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword identifier: Required. Unique identifier for the document. If creating a document and
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
:keyword expiry_time: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.
:paramtype expiry_time: str

<a id="models._models.Paths1BwrvmkInvoicesPostRequestbodyContentMultipartFormDataSchema"></a>

## Paths1BwrvmkInvoicesPostRequestbodyContentMultipartFormDataSchema Objects

```python
class Paths1BwrvmkInvoicesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model)
```

Paths1BwrvmkInvoicesPostRequestbodyContentMultipartFormDataSchema.

:ivar file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML, PNG,
 JPG.
:vartype file: IO
:ivar identifier: Unique identifier for the document. If creating a document and left blank,
 one will be automatically generated.
:vartype identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar url: URL to file to download and process.
:vartype url: bool
:ivar wait: If "true" (default), will return a response only after processing has completed. If
 "false", will return an empty data object which can be polled at the GET endpoint until
 processing is complete.
:vartype wait: bool
:ivar language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:vartype language: str
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: str

<a id="models._models.Paths1BwrvmkInvoicesPostRequestbodyContentMultipartFormDataSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML,
PNG, JPG.
:paramtype file: IO
:keyword identifier: Unique identifier for the document. If creating a document and left blank,
one will be automatically generated.
:paramtype identifier: str
:keyword file_name: Optional filename of the file.
:paramtype file_name: str
:keyword url: URL to file to download and process.
:paramtype url: bool
:keyword wait: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
:paramtype wait: bool
:keyword language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:paramtype language: str
:keyword expiry_time: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.
:paramtype expiry_time: str

<a id="models._models.Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema"></a>

## Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema.

:ivar count: Number of documents in result.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str
:ivar results:
:vartype results: list[~affinda.models.Get200ApplicationJsonPropertiesItemsItem]

<a id="models._models.Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword count: Number of documents in result.
:paramtype count: int
:keyword next: URL to request next page of results.
:paramtype next: str
:keyword previous: URL to request previous page of results.
:paramtype previous: str
:keyword results:
:paramtype results: list[~affinda.models.Get200ApplicationJsonPropertiesItemsItem]

<a id="models._models.Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema"></a>

## Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema Objects

```python
class Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model)
```

Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema.

:ivar file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML, PNG,
 JPG.
:vartype file: IO
:ivar identifier: Unique identifier for the document. If creating a document and left blank,
 one will be automatically generated.
:vartype identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar url: URL to file to download and process.
:vartype url: str
:ivar wait: If "true" (default), will return a response only after processing has completed. If
 "false", will return an empty data object which can be polled at the GET endpoint until
 processing is complete.
:vartype wait: bool
:ivar language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:vartype language: str
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: str

<a id="models._models.Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML,
PNG, JPG.
:paramtype file: IO
:keyword identifier: Unique identifier for the document. If creating a document and left blank,
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
:keyword language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:paramtype language: str
:keyword expiry_time: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.
:paramtype expiry_time: str

<a id="models._models.Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema"></a>

## Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema Objects

```python
class Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model)
```

Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema.

:ivar file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML, PNG,
 JPG.
:vartype file: IO
:ivar identifier: Unique identifier for the document. If creating a document and left blank,
 one will be automatically generated.
:vartype identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar url: URL to file to download and process.
:vartype url: str
:ivar language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:vartype language: str
:ivar wait: If "true" (default), will return a response only after processing has completed. If
 "false", will return an empty data object which can be polled at the GET endpoint until
 processing is complete.
:vartype wait: bool
:ivar redact_headshot: Whether to redact headshot.
:vartype redact_headshot: bool
:ivar redact_personal_details: Whether to redact personal details (e.g. name, address).
:vartype redact_personal_details: bool
:ivar redact_work_details: Whether to redact work details (e.g. company names).
:vartype redact_work_details: bool
:ivar redact_education_details: Whether to redact education details (e.g. university names).
:vartype redact_education_details: bool
:ivar redact_referees: Whether to redact referee details.
:vartype redact_referees: bool
:ivar redact_locations: Whether to redact location names.
:vartype redact_locations: bool
:ivar redact_dates: Whether to redact dates.
:vartype redact_dates: bool
:ivar redact_gender: Whether to redact gender.
:vartype redact_gender: bool
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: str

<a id="models._models.Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML,
PNG, JPG.
:paramtype file: IO
:keyword identifier: Unique identifier for the document. If creating a document and left blank,
one will be automatically generated.
:paramtype identifier: str
:keyword file_name: Optional filename of the file.
:paramtype file_name: str
:keyword url: URL to file to download and process.
:paramtype url: str
:keyword language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:paramtype language: str
:keyword wait: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
:paramtype wait: bool
:keyword redact_headshot: Whether to redact headshot.
:paramtype redact_headshot: bool
:keyword redact_personal_details: Whether to redact personal details (e.g. name, address).
:paramtype redact_personal_details: bool
:keyword redact_work_details: Whether to redact work details (e.g. company names).
:paramtype redact_work_details: bool
:keyword redact_education_details: Whether to redact education details (e.g. university names).
:paramtype redact_education_details: bool
:keyword redact_referees: Whether to redact referee details.
:paramtype redact_referees: bool
:keyword redact_locations: Whether to redact location names.
:paramtype redact_locations: bool
:keyword redact_dates: Whether to redact dates.
:paramtype redact_dates: bool
:keyword redact_gender: Whether to redact gender.
:paramtype redact_gender: bool
:keyword expiry_time: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.
:paramtype expiry_time: str

<a id="models._models.PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema"></a>

## PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema Objects

```python
class PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model)
```

PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema.

All required parameters must be populated in order to send to Azure.

:ivar file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML, PNG,
 JPG.
:vartype file: IO
:ivar identifier: Unique identifier for the document. If creating a document and left blank,
 one will be automatically generated.
:vartype identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar url: URL to file to download and process.
:vartype url: str
:ivar language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:vartype language: str
:ivar resume_format: Required. Identifier of the format used.
:vartype resume_format: str
:ivar wait: If "true" (default), will return a response only after processing has completed. If
 "false", will return an empty data object which can be polled at the GET endpoint until
 processing is complete.
:vartype wait: bool

<a id="models._models.PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML,
PNG, JPG.
:paramtype file: IO
:keyword identifier: Unique identifier for the document. If creating a document and left blank,
one will be automatically generated.
:paramtype identifier: str
:keyword file_name: Optional filename of the file.
:paramtype file_name: str
:keyword url: URL to file to download and process.
:paramtype url: str
:keyword language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:paramtype language: str
:keyword resume_format: Required. Identifier of the format used.
:paramtype resume_format: str
:keyword wait: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
:paramtype wait: bool

<a id="models._models.RedactedResume"></a>

## RedactedResume Objects

```python
class RedactedResume(msrest.serialization.Model)
```

RedactedResume.

All required parameters must be populated in order to send to Azure.

:ivar data: Required.
:vartype data: ~affinda.models.RedactedResumeData
:ivar meta: Required.
:vartype meta: ~affinda.models.Meta
:ivar error: Required.
:vartype error: ~affinda.models.Error

<a id="models._models.RedactedResume.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword data: Required.
:paramtype data: ~affinda.models.RedactedResumeData
:keyword meta: Required.
:paramtype meta: ~affinda.models.Meta
:keyword error: Required.
:paramtype error: ~affinda.models.Error

<a id="models._models.RedactedResumeData"></a>

## RedactedResumeData Objects

```python
class RedactedResumeData(msrest.serialization.Model)
```

RedactedResumeData.

:ivar redacted_pdf: URL to redacted PDF.
:vartype redacted_pdf: str

<a id="models._models.RedactedResumeData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword redacted_pdf: URL to redacted PDF.
:paramtype redacted_pdf: str

<a id="models._models.ReformattedResume"></a>

## ReformattedResume Objects

```python
class ReformattedResume(msrest.serialization.Model)
```

ReformattedResume.

All required parameters must be populated in order to send to Azure.

:ivar data: Required.
:vartype data: ~affinda.models.ReformattedResumeData
:ivar meta: Required.
:vartype meta: ~affinda.models.Meta
:ivar error: Required.
:vartype error: ~affinda.models.Error

<a id="models._models.ReformattedResume.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword data: Required.
:paramtype data: ~affinda.models.ReformattedResumeData
:keyword meta: Required.
:paramtype meta: ~affinda.models.Meta
:keyword error: Required.
:paramtype error: ~affinda.models.Error

<a id="models._models.ReformattedResumeData"></a>

## ReformattedResumeData Objects

```python
class ReformattedResumeData(msrest.serialization.Model)
```

ReformattedResumeData.

:ivar reformatted_file:
:vartype reformatted_file: str

<a id="models._models.ReformattedResumeData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword reformatted_file:
:paramtype reformatted_file: str

<a id="models._models.RequestError"></a>

## RequestError Objects

```python
class RequestError(msrest.serialization.Model)
```

RequestError.

All required parameters must be populated in order to send to Azure.

:ivar detail: Required.
:vartype detail: str
:ivar status_code: Required.
:vartype status_code: int

<a id="models._models.RequestError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword detail: Required.
:paramtype detail: str
:keyword status_code: Required.
:paramtype status_code: int

<a id="models._models.Resume"></a>

## Resume Objects

```python
class Resume(msrest.serialization.Model)
```

Resume.

All required parameters must be populated in order to send to Azure.

:ivar data: Required.
:vartype data: ~affinda.models.ResumeData
:ivar meta: Required.
:vartype meta: ~affinda.models.Meta
:ivar error: Required.
:vartype error: ~affinda.models.Error

<a id="models._models.Resume.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword data: Required.
:paramtype data: ~affinda.models.ResumeData
:keyword meta: Required.
:paramtype meta: ~affinda.models.Meta
:keyword error: Required.
:paramtype error: ~affinda.models.Error

<a id="models._models.ResumeData"></a>

## ResumeData Objects

```python
class ResumeData(msrest.serialization.Model)
```

ResumeData.

:ivar name:
:vartype name: ~affinda.models.ResumeDataName
:ivar phone_numbers:
:vartype phone_numbers: list[str]
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
:vartype languages: list[str]
:ivar summary:
:vartype summary: str
:ivar total_years_experience:
:vartype total_years_experience: int
:ivar head_shot: base64 encoded string.
:vartype head_shot: bytearray
:ivar education:
:vartype education: list[~affinda.models.ResumeDataEducationItem]
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
:ivar raw_text: All of the raw text of the parsed resume, example is shortened for readiblity.
:vartype raw_text: str

<a id="models._models.ResumeData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

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
30 suggest that the document is not a resume.
:paramtype is_resume_probability: int
:keyword raw_text: All of the raw text of the parsed resume, example is shortened for
readiblity.
:paramtype raw_text: str

<a id="models._models.ResumeDataEducationItem"></a>

## ResumeDataEducationItem Objects

```python
class ResumeDataEducationItem(msrest.serialization.Model)
```

ResumeDataEducationItem.

:ivar organization:
:vartype organization: str
:ivar accreditation:
:vartype accreditation: ~affinda.models.ResumeDataEducationItemAccreditation
:ivar grade:
:vartype grade: ~affinda.models.ResumeDataEducationItemGrade
:ivar location:
:vartype location: ~affinda.models.Location
:ivar dates:
:vartype dates: ~affinda.models.ResumeDataEducationItemDates

<a id="models._models.ResumeDataEducationItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

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

<a id="models._models.ResumeDataEducationItemAccreditation"></a>

## ResumeDataEducationItemAccreditation Objects

```python
class ResumeDataEducationItemAccreditation(msrest.serialization.Model)
```

ResumeDataEducationItemAccreditation.

:ivar education:
:vartype education: str
:ivar input_str:
:vartype input_str: str
:ivar match_str:
:vartype match_str: str
:ivar education_level:
:vartype education_level: str

<a id="models._models.ResumeDataEducationItemAccreditation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword education:
:paramtype education: str
:keyword input_str:
:paramtype input_str: str
:keyword match_str:
:paramtype match_str: str
:keyword education_level:
:paramtype education_level: str

<a id="models._models.ResumeDataEducationItemDates"></a>

## ResumeDataEducationItemDates Objects

```python
class ResumeDataEducationItemDates(msrest.serialization.Model)
```

ResumeDataEducationItemDates.

:ivar completion_date:
:vartype completion_date: ~datetime.date
:ivar is_current:
:vartype is_current: bool
:ivar start_date:
:vartype start_date: ~datetime.date

<a id="models._models.ResumeDataEducationItemDates.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword completion_date:
:paramtype completion_date: ~datetime.date
:keyword is_current:
:paramtype is_current: bool
:keyword start_date:
:paramtype start_date: ~datetime.date

<a id="models._models.ResumeDataEducationItemGrade"></a>

## ResumeDataEducationItemGrade Objects

```python
class ResumeDataEducationItemGrade(msrest.serialization.Model)
```

ResumeDataEducationItemGrade.

:ivar raw:
:vartype raw: str
:ivar metric:
:vartype metric: str
:ivar value:
:vartype value: str

<a id="models._models.ResumeDataEducationItemGrade.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword raw:
:paramtype raw: str
:keyword metric:
:paramtype metric: str
:keyword value:
:paramtype value: str

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

<a id="models._models.ResumeDataRefereesItem"></a>

## ResumeDataRefereesItem Objects

```python
class ResumeDataRefereesItem(msrest.serialization.Model)
```

ResumeDataRefereesItem.

:ivar name:
:vartype name: str
:ivar text:
:vartype text: str
:ivar email:
:vartype email: str
:ivar number:
:vartype number: str

<a id="models._models.ResumeDataRefereesItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword name:
:paramtype name: str
:keyword text:
:paramtype text: str
:keyword email:
:paramtype email: str
:keyword number:
:paramtype number: str

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

:keyword section_type:
:paramtype section_type: str
:keyword bbox:
:paramtype bbox: list[float]
:keyword page_index:
:paramtype page_index: int
:keyword text:
:paramtype text: str

<a id="models._models.ResumeDataSkillsItem"></a>

## ResumeDataSkillsItem Objects

```python
class ResumeDataSkillsItem(msrest.serialization.Model)
```

ResumeDataSkillsItem.

:ivar name:
:vartype name: str
:ivar last_used:
:vartype last_used: str
:ivar number_of_months:
:vartype number_of_months: int
:ivar type:
:vartype type: str
:ivar sources:
:vartype sources: list[~affinda.models.ResumeDataSkillsPropertiesItemsItem]

<a id="models._models.ResumeDataSkillsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

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

<a id="models._models.ResumeDataSkillsPropertiesItemsItem"></a>

## ResumeDataSkillsPropertiesItemsItem Objects

```python
class ResumeDataSkillsPropertiesItemsItem(msrest.serialization.Model)
```

ResumeDataSkillsPropertiesItemsItem.

:ivar section:
:vartype section: str
:ivar position:
:vartype position: int

<a id="models._models.ResumeDataSkillsPropertiesItemsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword section:
:paramtype section: str
:keyword position:
:paramtype position: int

<a id="models._models.ResumeDataWorkExperienceItem"></a>

## ResumeDataWorkExperienceItem Objects

```python
class ResumeDataWorkExperienceItem(msrest.serialization.Model)
```

ResumeDataWorkExperienceItem.

:ivar job_title:
:vartype job_title: str
:ivar organization:
:vartype organization: str
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
:keyword occupation:
:paramtype occupation: ~affinda.models.ResumeDataWorkExperienceItemOccupation

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

<a id="models._models.ResumeDataWorkExperienceItemDates.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword start_date:
:paramtype start_date: ~datetime.date
:keyword end_date:
:paramtype end_date: ~datetime.date
:keyword months_in_position:
:paramtype months_in_position: int
:keyword is_current:
:paramtype is_current: bool

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
:ivar management_level: Possible values include: "None", "Low", "Mid", "Upper".
:vartype management_level: str or ~affinda.models.Enum0
:ivar classification:
:vartype classification:
 ~affinda.models.Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification

<a id="models._models.ResumeDataWorkExperienceItemOccupation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

:keyword job_title: The raw (not normalized) job title pulled from the work experience entry.
:paramtype job_title: str
:keyword job_title_normalized: Mapped onto the EMSI job title taxonomy if a sufficiently close
match exists.
:paramtype job_title_normalized: str
:keyword management_level: Possible values include: "None", "Low", "Mid", "Upper".
:paramtype management_level: str or ~affinda.models.Enum0
:keyword classification:
:paramtype classification:
~affinda.models.Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification

