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
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str

<a id="models._models.Annotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.

<a id="models._models.Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1"></a>

## Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1 Objects

```python
class Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1(msrest.serialization.Model)
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
class Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1(msrest.serialization.Model)
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
class Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1(msrest.serialization.Model)
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
class Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1(msrest.serialization.Model)
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
class Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1(msrest.serialization.Model)
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
class Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1(msrest.serialization.Model)
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

<a id="models._models.Components1Bq3Q31SchemasJobdescriptionsearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1"></a>

## Components1Bq3Q31SchemasJobdescriptionsearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1 Objects

```python
class Components1Bq3Q31SchemasJobdescriptionsearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1(msrest.serialization.Model)
```

Components1Bq3Q31SchemasJobdescriptionsearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1.

:ivar match:
:vartype match: bool

<a id="models._models.Components1Bq3Q31SchemasJobdescriptionsearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 

<a id="models._models.Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1"></a>

## Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1 Objects

```python
class Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1(msrest.serialization.Model)
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
class Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1(msrest.serialization.Model)
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
class Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1(msrest.serialization.Model)
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
class Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1(msrest.serialization.Model)
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
class Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1(msrest.serialization.Model)
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
class Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1(msrest.serialization.Model)
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
class Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1(msrest.serialization.Model)
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
class Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1(msrest.serialization.Model)
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

**Arguments**:

- `title`: SOC2020 classification for this job title.
- `minor_group`: SOC2020 minor group.
- `sub_major_group`: SOC2020 sub major group.
- `major_group`: SOC2020 major group.
- `soc_code`: The 4 digit code representing the SOC2020 classification for this job title.

<a id="models._models.Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1"></a>

## Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1 Objects

```python
class Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1(msrest.serialization.Model)
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
class Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1(msrest.serialization.Model)
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
class Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1(msrest.serialization.Model)
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
class Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1(msrest.serialization.Model)
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
class Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1(msrest.serialization.Model)
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
class Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1(msrest.serialization.Model)
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
class Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1(msrest.serialization.Model)
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
class Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1(msrest.serialization.Model)
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
class Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1(msrest.serialization.Model)
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
class Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1(msrest.serialization.Model)
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
class ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1(msrest.serialization.Model)
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
class ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1(msrest.serialization.Model)
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
class ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1(msrest.serialization.Model)
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
class ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1(msrest.serialization.Model)
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
class ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1(msrest.serialization.Model)
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
class ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1(msrest.serialization.Model)
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

<a id="models._models.ComponentsK7P1F5SchemasResumesearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1"></a>

## ComponentsK7P1F5SchemasResumesearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1 Objects

```python
class ComponentsK7P1F5SchemasResumesearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1(msrest.serialization.Model)
```

ComponentsK7P1F5SchemasResumesearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1.

:ivar match:
:vartype match: bool

<a id="models._models.ComponentsK7P1F5SchemasResumesearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 

<a id="models._models.ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1"></a>

## ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1 Objects

```python
class ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1(msrest.serialization.Model)
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
class ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties(msrest.serialization.Model)
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
class ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1(msrest.serialization.Model)
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
class ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1(msrest.serialization.Model)
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
class ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1(msrest.serialization.Model)
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
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

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

<a id="models._models.EducationDates.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `completion_date`: 
- `is_current`: 
- `start_date`: 

<a id="models._models.EducationGrade"></a>

## EducationGrade Objects

```python
class EducationGrade(msrest.serialization.Model)
```

EducationGrade.

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

<a id="models._models.EnumAnnotationSerializer"></a>

## EnumAnnotationSerializer Objects

```python
class EnumAnnotationSerializer(Annotation)
```

EnumAnnotationSerializer.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
:ivar parsed:
:vartype parsed: str

<a id="models._models.EnumAnnotationSerializer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

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

**Arguments**:

- `error_code`: 
- `error_detail`: 

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
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
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

<a id="models._models.Get200ApplicationJsonPropertiesItemsItem"></a>

## Get200ApplicationJsonPropertiesItemsItem Objects

```python
class Get200ApplicationJsonPropertiesItemsItem(msrest.serialization.Model)
```

Get200ApplicationJsonPropertiesItemsItem.

All required parameters must be populated in order to send to Azure.

:ivar name: Required.
:vartype name: str
:ivar document_type: Known values are: "resumes", "job_descriptions".
:vartype document_type: str or
 ~affinda.models.GetResponses200ContentApplicationJsonSchemaResultsItemDocumentType

<a id="models._models.Get200ApplicationJsonPropertiesItemsItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: Required.
- `document_type`: Known values are: "resumes", "job_descriptions".

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

**Arguments**:

- `count`: Number of documents in result.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.
- `results`: 

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

**Arguments**:

- `count`: Number of documents in result.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.
- `results`: 

<a id="models._models.GetAllJobDescriptionsResults"></a>

## GetAllJobDescriptionsResults Objects

```python
class GetAllJobDescriptionsResults(msrest.serialization.Model)
```

GetAllJobDescriptionsResults.

:ivar count: Number of documents in result.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str
:ivar results:
:vartype results: list[~affinda.models.Meta]

<a id="models._models.GetAllJobDescriptionsResults.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `count`: Number of documents in result.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.
- `results`: 

<a id="models._models.IndexRequestBody"></a>

## IndexRequestBody Objects

```python
class IndexRequestBody(msrest.serialization.Model)
```

IndexRequestBody.

:ivar name:
:vartype name: str
:ivar document_type: Known values are: "resumes", "job_descriptions".
:vartype document_type: str or ~affinda.models.PostContentSchemaDocumentType

<a id="models._models.IndexRequestBody.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `document_type`: Known values are: "resumes", "job_descriptions".

<a id="models._models.Invoice"></a>

## Invoice Objects

```python
class Invoice(msrest.serialization.Model)
```

Invoice.

All required parameters must be populated in order to send to Azure.

:ivar client_verified_dt: Required.
:vartype client_verified_dt: str
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

**Arguments**:

- `client_verified_dt`: Required.
- `data`: Required.
- `meta`: Required.
- `error`: Required.

<a id="models._models.InvoiceData"></a>

## InvoiceData Objects

```python
class InvoiceData(msrest.serialization.Model)
```

InvoiceData.

:ivar tables:
:vartype tables: list[~affinda.models.InvoiceDataTablesItem]
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
:vartype currency_code: ~affinda.models.EnumAnnotationSerializer
:ivar custom_fields: Dictionary of :code:`<any>`.
:vartype custom_fields: dict[str, any]

<a id="models._models.InvoiceData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `tables`: 
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
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataBankAccountNumber"></a>

## InvoiceDataBankAccountNumber Objects

```python
class InvoiceDataBankAccountNumber(TextAnnotation,  Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1)
```

InvoiceDataBankAccountNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataBankBsb"></a>

## InvoiceDataBankBsb Objects

```python
class InvoiceDataBankBsb(TextAnnotation,  Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1)
```

InvoiceDataBankBsb.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataBankIban"></a>

## InvoiceDataBankIban Objects

```python
class InvoiceDataBankIban(TextAnnotation,  Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1)
```

InvoiceDataBankIban.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataBankSortCode"></a>

## InvoiceDataBankSortCode Objects

```python
class InvoiceDataBankSortCode(TextAnnotation,  Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1)
```

InvoiceDataBankSortCode.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataBankSwift"></a>

## InvoiceDataBankSwift Objects

```python
class InvoiceDataBankSwift(TextAnnotation,  Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1)
```

InvoiceDataBankSwift.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataBpayBillerCode"></a>

## InvoiceDataBpayBillerCode Objects

```python
class InvoiceDataBpayBillerCode(TextAnnotation,  ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1)
```

InvoiceDataBpayBillerCode.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataBpayReference"></a>

## InvoiceDataBpayReference Objects

```python
class InvoiceDataBpayReference(TextAnnotation,  ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1)
```

InvoiceDataBpayReference.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerBusinessNumber"></a>

## InvoiceDataCustomerBusinessNumber Objects

```python
class InvoiceDataCustomerBusinessNumber(TextAnnotation,  Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1)
```

InvoiceDataCustomerBusinessNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerCompanyName"></a>

## InvoiceDataCustomerCompanyName Objects

```python
class InvoiceDataCustomerCompanyName(TextAnnotation,  Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1)
```

InvoiceDataCustomerCompanyName.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerContactName"></a>

## InvoiceDataCustomerContactName Objects

```python
class InvoiceDataCustomerContactName(TextAnnotation,  ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1)
```

InvoiceDataCustomerContactName.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerEmail"></a>

## InvoiceDataCustomerEmail Objects

```python
class InvoiceDataCustomerEmail(TextAnnotation,  Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1)
```

InvoiceDataCustomerEmail.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerNumber"></a>

## InvoiceDataCustomerNumber Objects

```python
class InvoiceDataCustomerNumber(TextAnnotation,  Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1)
```

InvoiceDataCustomerNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerPhoneNumber"></a>

## InvoiceDataCustomerPhoneNumber Objects

```python
class InvoiceDataCustomerPhoneNumber(TextAnnotation,  Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1)
```

InvoiceDataCustomerPhoneNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataCustomerVat"></a>

## InvoiceDataCustomerVat Objects

```python
class InvoiceDataCustomerVat(TextAnnotation,  ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1)
```

InvoiceDataCustomerVat.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataInvoiceNumber"></a>

## InvoiceDataInvoiceNumber Objects

```python
class InvoiceDataInvoiceNumber(TextAnnotation,  Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1)
```

InvoiceDataInvoiceNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataInvoicePurchaseOrderNumber"></a>

## InvoiceDataInvoicePurchaseOrderNumber Objects

```python
class InvoiceDataInvoicePurchaseOrderNumber(TextAnnotation,  ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1)
```

InvoiceDataInvoicePurchaseOrderNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentAmountBase"></a>

## InvoiceDataPaymentAmountBase Objects

```python
class InvoiceDataPaymentAmountBase(TextAnnotation,  Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1)
```

InvoiceDataPaymentAmountBase.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentAmountDue"></a>

## InvoiceDataPaymentAmountDue Objects

```python
class InvoiceDataPaymentAmountDue(TextAnnotation,  ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1)
```

InvoiceDataPaymentAmountDue.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentAmountPaid"></a>

## InvoiceDataPaymentAmountPaid Objects

```python
class InvoiceDataPaymentAmountPaid(TextAnnotation,  Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1)
```

InvoiceDataPaymentAmountPaid.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentAmountTax"></a>

## InvoiceDataPaymentAmountTax Objects

```python
class InvoiceDataPaymentAmountTax(TextAnnotation,  Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1)
```

InvoiceDataPaymentAmountTax.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentAmountTotal"></a>

## InvoiceDataPaymentAmountTotal Objects

```python
class InvoiceDataPaymentAmountTotal(TextAnnotation,  Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1)
```

InvoiceDataPaymentAmountTotal.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataPaymentReference"></a>

## InvoiceDataPaymentReference Objects

```python
class InvoiceDataPaymentReference(TextAnnotation,  Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1)
```

InvoiceDataPaymentReference.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierBusinessNumber"></a>

## InvoiceDataSupplierBusinessNumber Objects

```python
class InvoiceDataSupplierBusinessNumber(TextAnnotation,  Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1)
```

InvoiceDataSupplierBusinessNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierCompanyName"></a>

## InvoiceDataSupplierCompanyName Objects

```python
class InvoiceDataSupplierCompanyName(TextAnnotation,  Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1)
```

InvoiceDataSupplierCompanyName.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierEmail"></a>

## InvoiceDataSupplierEmail Objects

```python
class InvoiceDataSupplierEmail(TextAnnotation,  Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1)
```

InvoiceDataSupplierEmail.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierFax"></a>

## InvoiceDataSupplierFax Objects

```python
class InvoiceDataSupplierFax(TextAnnotation,  Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1)
```

InvoiceDataSupplierFax.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierPhoneNumber"></a>

## InvoiceDataSupplierPhoneNumber Objects

```python
class InvoiceDataSupplierPhoneNumber(TextAnnotation,  Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1)
```

InvoiceDataSupplierPhoneNumber.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierVat"></a>

## InvoiceDataSupplierVat Objects

```python
class InvoiceDataSupplierVat(TextAnnotation,  ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1)
```

InvoiceDataSupplierVat.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataSupplierWebsite"></a>

## InvoiceDataSupplierWebsite Objects

```python
class InvoiceDataSupplierWebsite(TextAnnotation,  Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1)
```

InvoiceDataSupplierWebsite.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

<a id="models._models.InvoiceDataTablesItem"></a>

## InvoiceDataTablesItem Objects

```python
class InvoiceDataTablesItem(msrest.serialization.Model)
```

InvoiceDataTablesItem.

:ivar rows:
:vartype rows: list[~affinda.models.RowAnnotation]

<a id="models._models.InvoiceDataTablesItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `rows`: 

<a id="models._models.InvoiceRequestBody"></a>

## InvoiceRequestBody Objects

```python
class InvoiceRequestBody(msrest.serialization.Model)
```

InvoiceRequestBody.

:ivar file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML, PNG,
 JPG.
:vartype file: IO
:ivar url: URL to an invoice to download and process.
:vartype url: str
:ivar identifier: Unique identifier for the document. If creating a document and left blank,
 one will be automatically generated.
:vartype identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar wait: If "true" (default), will return a response only after processing has completed. If
 "false", will return an empty data object which can be polled at the GET endpoint until
 processing is complete.
:vartype wait: bool
:ivar reject_duplicates: If "true", parsing will fail when the uploaded document is duplicate
 of an existing document. If "false" (default), will parse the document normally whether its a
 duplicate or not.
:vartype reject_duplicates: bool
:ivar language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:vartype language: str
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: ~datetime.datetime

<a id="models._models.InvoiceRequestBody.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `file`: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML,
PNG, JPG.
- `url`: URL to an invoice to download and process.
- `identifier`: Unique identifier for the document. If creating a document and left blank,
one will be automatically generated.
- `file_name`: Optional filename of the file.
- `wait`: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
- `reject_duplicates`: If "true", parsing will fail when the uploaded document is
duplicate of an existing document. If "false" (default), will parse the document normally
whether its a duplicate or not.
- `language`: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
- `expiry_time`: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.

<a id="models._models.JobDescription"></a>

## JobDescription Objects

```python
class JobDescription(msrest.serialization.Model)
```

JobDescription.

All required parameters must be populated in order to send to Azure.

:ivar data: Required.
:vartype data: ~affinda.models.JobDescriptionData
:ivar meta: Required.
:vartype meta: ~affinda.models.Meta
:ivar error: Required.
:vartype error: ~affinda.models.Error

<a id="models._models.JobDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `data`: Required.
- `meta`: Required.
- `error`: Required.

<a id="models._models.JobDescriptionData"></a>

## JobDescriptionData Objects

```python
class JobDescriptionData(msrest.serialization.Model)
```

JobDescriptionData.

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

<a id="models._models.JobDescriptionData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

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

<a id="models._models.JobDescriptionRequestBody"></a>

## JobDescriptionRequestBody Objects

```python
class JobDescriptionRequestBody(msrest.serialization.Model)
```

JobDescriptionRequestBody.

:ivar file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML, PNG,
 JPG.
:vartype file: IO
:ivar url: URL to a job description to download and process.
:vartype url: str
:ivar identifier: Unique identifier for the document. If creating a document and left blank,
 one will be automatically generated.
:vartype identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar wait: If "true" (default), will return a response only after processing has completed. If
 "false", will return an empty data object which can be polled at the GET endpoint until
 processing is complete.
:vartype wait: bool
:ivar reject_duplicates: If "true", parsing will fail when the uploaded document is duplicate
 of an existing document. If "false" (default), will parse the document normally whether its a
 duplicate or not.
:vartype reject_duplicates: bool
:ivar language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:vartype language: str
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: ~datetime.datetime

<a id="models._models.JobDescriptionRequestBody.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `file`: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML,
PNG, JPG.
- `url`: URL to a job description to download and process.
- `identifier`: Unique identifier for the document. If creating a document and left blank,
one will be automatically generated.
- `file_name`: Optional filename of the file.
- `wait`: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
- `reject_duplicates`: If "true", parsing will fail when the uploaded document is
duplicate of an existing document. If "false" (default), will parse the document normally
whether its a duplicate or not.
- `language`: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
- `expiry_time`: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.

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
:ivar search_tool_theme: Customize the theme of the embeded search tool.
:vartype search_tool_theme: dict[str, any]
:ivar user_id: ID of the logged in user.
:vartype user_id: int
:ivar username: Username of the logged in user.
:vartype username: str

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
- `search_tool_theme`: Customize the theme of the embeded search tool.

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
class JobDescriptionSearchDetailLocationValue(Location,  Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1)
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
:vartype value: list[~affinda.models.JobDescriptionSearchDetailOccupationGroupValueItem]

<a id="models._models.JobDescriptionSearchDetailOccupationGroup.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

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

<a id="models._models.JobDescriptionSearchDetailOccupationGroupValueItem"></a>

## JobDescriptionSearchDetailOccupationGroupValueItem Objects

```python
class JobDescriptionSearchDetailOccupationGroupValueItem(OccupationGroup,  Components1Bq3Q31SchemasJobdescriptionsearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1)
```

JobDescriptionSearchDetailOccupationGroupValueItem.

All required parameters must be populated in order to send to Azure.

:ivar match:
:vartype match: bool
:ivar code: Required.
:vartype code: int
:ivar name: Required.
:vartype name: str
:ivar children: Required.
:vartype children: list[~affinda.models.OccupationGroup]

<a id="models._models.JobDescriptionSearchDetailOccupationGroupValueItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 
- `code`: Required.
- `name`: Required.
- `children`: Required.

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
:ivar resume: Unique identifier for the document. If creating a document and left blank, one
 will be automatically generated.
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

<a id="models._models.JobDescriptionSearchParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `indices`: Required.
- `resume`: Unique identifier for the document. If creating a document and left blank, one
will be automatically generated.
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

<a id="models._models.JobDescriptionSearchResult"></a>

## JobDescriptionSearchResult Objects

```python
class JobDescriptionSearchResult(msrest.serialization.Model)
```

JobDescriptionSearchResult.

All required parameters must be populated in order to send to Azure.

:ivar identifier: Required. Unique identifier for the document. If creating a document and left
 blank, one will be automatically generated.
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

<a id="models._models.JobDescriptionSearchResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Required. Unique identifier for the document. If creating a document and
left blank, one will be automatically generated.
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
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
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

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

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
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

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

<a id="models._models.Meta"></a>

## Meta Objects

```python
class Meta(msrest.serialization.Model)
```

Meta.

Variables are only populated by the server, and will be ignored when sending a request.

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
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
:vartype expiry_time: ~datetime.datetime
:ivar language: The document's language.
:vartype language: str
:ivar pdf: The URL to the document's pdf (if the uploaded document is not already pdf, it's
 converted to pdf as part of the parsing process).
:vartype pdf: str
:ivar parent_document: If this document is part of a splitted document, this attribute points
 to the original document that this document is splitted from.
:vartype parent_document: ~affinda.models.SplitRelation
:ivar child_documents: If this document has been splitted into a number of child documents,
 this attribute points to those child documents.
:vartype child_documents: list[~affinda.models.SplitRelation]
:ivar pages: The document's pages.
:vartype pages: list[~affinda.models.PageMeta]
:ivar is_verified: This is true if the "confirm" button has been clicked in the Affinda
 validation tool.
:vartype is_verified: bool
:ivar review_url: Signed URL (valid for 60 minutes) to access the validation tool.  Not
 applicable for documents types such a resumes.
:vartype review_url: str
:ivar ocr_confidence: The overall confidence in the conversion of image to text.  (only
 applicable for images or PDF documents without a text layer).
:vartype ocr_confidence: float

<a id="models._models.Meta.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `additional_properties`: Unmatched properties from the message are deserialized to this
collection.
- `identifier`: Required. Unique identifier for the document. If creating a document and
left blank, one will be automatically generated.
- `file_name`: Optional filename of the file.
- `ready`: Required. If true, the document has finished processing. Particularly useful if
an endpoint request specified wait=False, when polling use this variable to determine when to
stop polling.
- `ready_dt`: The datetime when the document was ready.
- `failed`: Required. If true, some exception was raised during processing. Check the
'error' field of the main return object.
- `expiry_time`: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.
- `language`: The document's language.
- `pages`: The document's pages.
- `is_verified`: This is true if the "confirm" button has been clicked in the Affinda
validation tool.
- `review_url`: Signed URL (valid for 60 minutes) to access the validation tool.  Not
applicable for documents types such a resumes.
- `ocr_confidence`: The overall confidence in the conversion of image to text.  (only
applicable for images or PDF documents without a text layer).

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

<a id="models._models.PageMeta"></a>

## PageMeta Objects

```python
class PageMeta(msrest.serialization.Model)
```

PageMeta.

:ivar id:
:vartype id: int
:ivar page_index: Page number within the document, starts from 0.
:vartype page_index: int
:ivar image: The URL to the image of the page.
:vartype image: str
:ivar height: Height of the page's image in px.
:vartype height: float
:ivar width: Width of the page's image in px.
:vartype width: float
:ivar rotation: The degree of rotation applied to the page. Greater than 0 indicates clockwise
 rotation. Less than 0 indicates counter-clockwise rotation.
:vartype rotation: int

<a id="models._models.PageMeta.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: 
- `page_index`: Page number within the document, starts from 0.
- `image`: The URL to the image of the page.
- `height`: Height of the page's image in px.
- `width`: Width of the page's image in px.
- `rotation`: The degree of rotation applied to the page. Greater than 0 indicates
clockwise rotation. Less than 0 indicates counter-clockwise rotation.

<a id="models._models.Paths1Mc0Je6IndexPostResponses201ContentApplicationJsonSchema"></a>

## Paths1Mc0Je6IndexPostResponses201ContentApplicationJsonSchema Objects

```python
class Paths1Mc0Je6IndexPostResponses201ContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths1Mc0Je6IndexPostResponses201ContentApplicationJsonSchema.

:ivar name:
:vartype name: str
:ivar document_type: Known values are: "resumes", "job_descriptions".
:vartype document_type: str or ~affinda.models.Enum5

<a id="models._models.Paths1Mc0Je6IndexPostResponses201ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `name`: 
- `document_type`: Known values are: "resumes", "job_descriptions".

<a id="models._models.Paths1Y6A2MfUsersPostResponses201ContentApplicationJsonSchemaAllof1"></a>

## Paths1Y6A2MfUsersPostResponses201ContentApplicationJsonSchemaAllof1 Objects

```python
class Paths1Y6A2MfUsersPostResponses201ContentApplicationJsonSchemaAllof1(msrest.serialization.Model)
```

Paths1Y6A2MfUsersPostResponses201ContentApplicationJsonSchemaAllof1.

:ivar api_key: API key used to authenticate for future requests.  This key is only retrievable
 at the initial creation of the user.
:vartype api_key: str

<a id="models._models.Paths1Y6A2MfUsersPostResponses201ContentApplicationJsonSchemaAllof1.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `api_key`: API key used to authenticate for future requests.  This key is only
retrievable at the initial creation of the user.

<a id="models._models.Paths2T1Oc0ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema"></a>

## Paths2T1Oc0ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema Objects

```python
class Paths2T1Oc0ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths2T1Oc0ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema.

:ivar config_override:
:vartype config_override: ~affinda.models.ResumeSearchConfig

<a id="models._models.Paths2T1Oc0ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `config_override`: 

<a id="models._models.Paths6Pypg5IndexGetResponses200ContentApplicationJsonSchema"></a>

## Paths6Pypg5IndexGetResponses200ContentApplicationJsonSchema Objects

```python
class Paths6Pypg5IndexGetResponses200ContentApplicationJsonSchema(msrest.serialization.Model)
```

Paths6Pypg5IndexGetResponses200ContentApplicationJsonSchema.

:ivar count: Number of indexes in result.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str
:ivar results:
:vartype results: list[~affinda.models.Get200ApplicationJsonPropertiesItemsItem]

<a id="models._models.Paths6Pypg5IndexGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `count`: Number of indexes in result.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.
- `results`: 

<a id="models._models.PathsCoo0XpIndexNameDocumentsPostResponses201ContentApplicationJsonSchema"></a>

## PathsCoo0XpIndexNameDocumentsPostResponses201ContentApplicationJsonSchema Objects

```python
class PathsCoo0XpIndexNameDocumentsPostResponses201ContentApplicationJsonSchema(msrest.serialization.Model)
```

PathsCoo0XpIndexNameDocumentsPostResponses201ContentApplicationJsonSchema.

:ivar document: Unique identifier for the document.
:vartype document: str

<a id="models._models.PathsCoo0XpIndexNameDocumentsPostResponses201ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `document`: Unique identifier for the document.

<a id="models._models.PathsFqn8P8JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema"></a>

## PathsFqn8P8JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema Objects

```python
class PathsFqn8P8JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model)
```

PathsFqn8P8JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema.

:ivar config_override:
:vartype config_override: ~affinda.models.JobDescriptionSearchConfig

<a id="models._models.PathsFqn8P8JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `config_override`: 

<a id="models._models.PathsGpptmIndexNameDocumentsPostRequestbodyContentApplicationJsonSchema"></a>

## PathsGpptmIndexNameDocumentsPostRequestbodyContentApplicationJsonSchema Objects

```python
class PathsGpptmIndexNameDocumentsPostRequestbodyContentApplicationJsonSchema(msrest.serialization.Model)
```

PathsGpptmIndexNameDocumentsPostRequestbodyContentApplicationJsonSchema.

:ivar document:
:vartype document: str

<a id="models._models.PathsGpptmIndexNameDocumentsPostRequestbodyContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `document`: 

<a id="models._models.PathsHryo8IndexNameDocumentsGetResponses200ContentApplicationJsonSchemaPropertiesResultsItems"></a>

## PathsHryo8IndexNameDocumentsGetResponses200ContentApplicationJsonSchemaPropertiesResultsItems Objects

```python
class PathsHryo8IndexNameDocumentsGetResponses200ContentApplicationJsonSchemaPropertiesResultsItems(msrest.serialization.Model)
```

PathsHryo8IndexNameDocumentsGetResponses200ContentApplicationJsonSchemaPropertiesResultsItems.

:ivar document:
:vartype document: str

<a id="models._models.PathsHryo8IndexNameDocumentsGetResponses200ContentApplicationJsonSchemaPropertiesResultsItems.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `document`: 

<a id="models._models.PathsRvverlIndexNameDocumentsGetResponses200ContentApplicationJsonSchema"></a>

## PathsRvverlIndexNameDocumentsGetResponses200ContentApplicationJsonSchema Objects

```python
class PathsRvverlIndexNameDocumentsGetResponses200ContentApplicationJsonSchema(msrest.serialization.Model)
```

PathsRvverlIndexNameDocumentsGetResponses200ContentApplicationJsonSchema.

:ivar count: Number of indexed documents in result.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str
:ivar results:
:vartype results:
 list[~affinda.models.PathsHryo8IndexNameDocumentsGetResponses200ContentApplicationJsonSchemaPropertiesResultsItems]

<a id="models._models.PathsRvverlIndexNameDocumentsGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `count`: Number of indexed documents in result.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.
- `results`: 

<a id="models._models.User"></a>

## User Objects

```python
class User(msrest.serialization.Model)
```

User.

All required parameters must be populated in order to send to Azure.

:ivar id:
:vartype id: int
:ivar name:
:vartype name: str
:ivar username: Required.
:vartype username: str
:ivar email:
:vartype email: str
:ivar api_key:
:vartype api_key: str

<a id="models._models.User.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: 
- `name`: 
- `username`: Required.
- `email`: 
- `api_key`: 

<a id="models._models.PathsTop5ZkUsersPostResponses201ContentApplicationJsonSchema"></a>

## PathsTop5ZkUsersPostResponses201ContentApplicationJsonSchema Objects

```python
class PathsTop5ZkUsersPostResponses201ContentApplicationJsonSchema(User,  Paths1Y6A2MfUsersPostResponses201ContentApplicationJsonSchemaAllof1)
```

PathsTop5ZkUsersPostResponses201ContentApplicationJsonSchema.

All required parameters must be populated in order to send to Azure.

:ivar id:
:vartype id: int
:ivar name:
:vartype name: str
:ivar username: Required.
:vartype username: str
:ivar email:
:vartype email: str
:ivar api_key:
:vartype api_key: str

<a id="models._models.PathsTop5ZkUsersPostResponses201ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `id`: 
- `name`: 
- `username`: Required.
- `email`: 
- `api_key`: 

<a id="models._models.PathsWjaaeuUsersGetResponses200ContentApplicationJsonSchema"></a>

## PathsWjaaeuUsersGetResponses200ContentApplicationJsonSchema Objects

```python
class PathsWjaaeuUsersGetResponses200ContentApplicationJsonSchema(msrest.serialization.Model)
```

PathsWjaaeuUsersGetResponses200ContentApplicationJsonSchema.

:ivar count: Number of indexes in result.
:vartype count: int
:ivar next: URL to request next page of results.
:vartype next: str
:ivar previous: URL to request previous page of results.
:vartype previous: str
:ivar results:
:vartype results: list[~affinda.models.User]

<a id="models._models.PathsWjaaeuUsersGetResponses200ContentApplicationJsonSchema.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `count`: Number of indexes in result.
- `next`: URL to request next page of results.
- `previous`: URL to request previous page of results.
- `results`: 

<a id="models._models.Rectangle"></a>

## Rectangle Objects

```python
class Rectangle(msrest.serialization.Model)
```

Rectangle.

All required parameters must be populated in order to send to Azure.

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

- `x0`: Required.
- `y0`: Required.
- `x1`: Required.
- `y1`: Required.

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

**Arguments**:

- `data`: Required.
- `meta`: Required.
- `error`: Required.

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

**Arguments**:

- `redacted_pdf`: URL to redacted PDF.

<a id="models._models.RedactedResumeRequestBody"></a>

## RedactedResumeRequestBody Objects

```python
class RedactedResumeRequestBody(msrest.serialization.Model)
```

RedactedResumeRequestBody.

:ivar file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML, PNG,
 JPG.
:vartype file: IO
:ivar identifier: Unique identifier for the document. If creating a document and left blank,
 one will be automatically generated.
:vartype identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar url: URL to a resume to download and process.
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
:vartype redact_gender: str
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: ~datetime.datetime

<a id="models._models.RedactedResumeRequestBody.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `file`: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML,
PNG, JPG.
- `identifier`: Unique identifier for the document. If creating a document and left blank,
one will be automatically generated.
- `file_name`: Optional filename of the file.
- `url`: URL to a resume to download and process.
- `language`: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
- `wait`: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
- `redact_headshot`: Whether to redact headshot.
- `redact_personal_details`: Whether to redact personal details (e.g. name, address).
- `redact_work_details`: Whether to redact work details (e.g. company names).
- `redact_education_details`: Whether to redact education details (e.g. university names).
- `redact_referees`: Whether to redact referee details.
- `redact_locations`: Whether to redact location names.
- `redact_dates`: Whether to redact dates.
- `redact_gender`: Whether to redact gender.
- `expiry_time`: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.

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

<a id="models._models.Resume"></a>

## Resume Objects

```python
class Resume(msrest.serialization.Model)
```

Resume.

All required parameters must be populated in order to send to Azure.

:ivar data: Required. A JSON-encoded string of the ``ResumeData`` object.
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

**Arguments**:

- `data`: Required. A JSON-encoded string of the ``ResumeData`` object.
- `meta`: Required.
- `error`: Required.

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
:ivar raw_text: All of the raw text of the parsed resume, example is shortened for readiblity.
:vartype raw_text: str

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
- `websites`: 
- `emails`: 
- `date_of_birth`: 
- `location`: 
- `objective`: 
- `summary`: 
- `total_years_experience`: 
- `education`: 
- `work_experience`: 
- `skills`: 
- `certifications`: 
- `publications`: 
- `referees`: 
- `raw_text`: All of the raw text of the parsed resume, example is shortened for
readiblity.

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

**Arguments**:

- `name`: 
- `text`: 
- `email`: 
- `number`: 

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
- `management_level`: Known values are: "None", "Low", "Mid", "Upper".
- `classification`: 

<a id="models._models.ResumeRequestBody"></a>

## ResumeRequestBody Objects

```python
class ResumeRequestBody(msrest.serialization.Model)
```

ResumeRequestBody.

:ivar file: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML, PNG,
 JPG.
:vartype file: IO
:ivar url: URL to a resume to download and process.
:vartype url: str
:ivar data: A JSON-encoded string of the ``ResumeData`` object.
:vartype data: ~affinda.models.ResumeData
:ivar identifier: Unique identifier for the document. If creating a document and left blank,
 one will be automatically generated.
:vartype identifier: str
:ivar file_name: Optional filename of the file.
:vartype file_name: str
:ivar wait: If "true" (default), will return a response only after processing has completed. If
 "false", will return an empty data object which can be polled at the GET endpoint until
 processing is complete.
:vartype wait: bool
:ivar reject_duplicates: If "true", parsing will fail when the uploaded document is duplicate
 of an existing document. If "false" (default), will parse the document normally whether its a
 duplicate or not.
:vartype reject_duplicates: bool
:ivar language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
:vartype language: str
:ivar expiry_time: The date/time in ISO-8601 format when the document will be automatically
 deleted.  Defaults to no expiry.
:vartype expiry_time: ~datetime.datetime

<a id="models._models.ResumeRequestBody.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `file`: File as binary data blob. Supported formats: PDF, DOC, DOCX, TXT, RTF, HTML,
PNG, JPG.
- `url`: URL to a resume to download and process.
- `data`: A JSON-encoded string of the ``ResumeData`` object.
- `identifier`: Unique identifier for the document. If creating a document and left blank,
one will be automatically generated.
- `file_name`: Optional filename of the file.
- `wait`: If "true" (default), will return a response only after processing has completed.
If "false", will return an empty data object which can be polled at the GET endpoint until
processing is complete.
- `reject_duplicates`: If "true", parsing will fail when the uploaded document is
duplicate of an existing document. If "false" (default), will parse the document normally
whether its a duplicate or not.
- `language`: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for Chinese.
- `expiry_time`: The date/time in ISO-8601 format when the document will be automatically
deleted.  Defaults to no expiry.

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
:ivar search_tool_theme: Customize the theme of the embeded search tool.
:vartype search_tool_theme: dict[str, any]
:ivar user_id: ID of the logged in user.
:vartype user_id: int
:ivar username: Username of the logged in user.
:vartype username: str

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
- `search_tool_theme`: Customize the theme of the embeded search tool.

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
class ResumeSearchDetailEducationValueItem(Education,  ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1)
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
class ResumeSearchDetailLanguagesValueItem(ResumeSkill,  Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1)
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
class ResumeSearchDetailLocationValue(Location,  ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1)
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
:vartype value: list[~affinda.models.ResumeSearchDetailOccupationGroupValueItem]

<a id="models._models.ResumeSearchDetailOccupationGroup.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `missing`: 
- `value`: 

<a id="models._models.ResumeSearchDetailOccupationGroupValueItem"></a>

## ResumeSearchDetailOccupationGroupValueItem Objects

```python
class ResumeSearchDetailOccupationGroupValueItem(OccupationGroup,  ComponentsK7P1F5SchemasResumesearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1)
```

ResumeSearchDetailOccupationGroupValueItem.

All required parameters must be populated in order to send to Azure.

:ivar match:
:vartype match: bool
:ivar code: Required.
:vartype code: int
:ivar name: Required.
:vartype name: str
:ivar children: Required.
:vartype children: list[~affinda.models.OccupationGroup]

<a id="models._models.ResumeSearchDetailOccupationGroupValueItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `match`: 
- `code`: Required.
- `name`: Required.
- `children`: Required.

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
class ResumeSearchDetailSkillsValueItem(ResumeSkill,  ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1)
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
:ivar job_description: Unique identifier for the document. If creating a document and left
 blank, one will be automatically generated.
:vartype job_description: str
:ivar resume: Unique identifier for the document. If creating a document and left blank, one
 will be automatically generated.
:vartype resume: str
:ivar job_titles:
:vartype job_titles: list[str]
:ivar job_titles_current_only:
:vartype job_titles_current_only: bool
:ivar job_titles_required:
:vartype job_titles_required: bool
:ivar job_titles_weight:
:vartype job_titles_weight: float
:ivar years_experience_min:
:vartype years_experience_min: int
:ivar years_experience_max:
:vartype years_experience_max: int
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
:ivar is_current_student:
:vartype is_current_student: bool
:ivar is_current_student_required:
:vartype is_current_student_required: bool
:ivar is_recent_graduate:
:vartype is_recent_graduate: bool
:ivar is_recent_graduate_required:
:vartype is_recent_graduate_required: bool
:ivar is_top_student:
:vartype is_top_student: bool
:ivar is_top_student_required:
:vartype is_top_student_required: bool
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
:vartype custom_data: list[~affinda.models.ResumeSearchParametersCustomData]

<a id="models._models.ResumeSearchParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `indices`: Required.
- `job_description`: Unique identifier for the document. If creating a document and left
blank, one will be automatically generated.
- `resume`: Unique identifier for the document. If creating a document and left blank, one
will be automatically generated.
- `job_titles`: 
- `job_titles_current_only`: 
- `job_titles_required`: 
- `job_titles_weight`: 
- `years_experience_min`: 
- `years_experience_max`: 
- `years_experience_required`: 
- `years_experience_weight`: 
- `locations`: 
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
- `is_current_student`: 
- `is_current_student_required`: 
- `is_recent_graduate`: 
- `is_recent_graduate_required`: 
- `is_top_student`: 
- `is_top_student_required`: 
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

<a id="models._models.ResumeSearchParametersCustomData"></a>

## ResumeSearchParametersCustomData Objects

```python
class ResumeSearchParametersCustomData(msrest.serialization.Model)
```

ResumeSearchParametersCustomData.

All required parameters must be populated in order to send to Azure.

:ivar filter_type: Required. Known values are: "equals", "range".
:vartype filter_type: str or ~affinda.models.ResumeSearchParametersCustomDataFilterType
:ivar data_point: Required.
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

- `filter_type`: Required. Known values are: "equals", "range".
- `data_point`: Required.
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
:ivar unit: Known values are: "km", "mi".
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
- `unit`: Known values are: "km", "mi".

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

:ivar identifier: Required. Unique identifier for the document. If creating a document and left
 blank, one will be automatically generated.
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

- `identifier`: Required. Unique identifier for the document. If creating a document and
left blank, one will be automatically generated.
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
 "Footer".
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
"Footer".
- `position`: 

<a id="models._models.RowAnnotation"></a>

## RowAnnotation Objects

```python
class RowAnnotation(msrest.serialization.Model)
```

RowAnnotation.

:ivar code:
:vartype code: str
:ivar date:
:vartype date: str
:ivar description:
:vartype description: str
:ivar unit:
:vartype unit: str
:ivar unit_price:
:vartype unit_price: float
:ivar quantity:
:vartype quantity: float
:ivar discount:
:vartype discount: str
:ivar base_total:
:vartype base_total: float
:ivar tax_rate:
:vartype tax_rate: str
:ivar tax_total:
:vartype tax_total: float
:ivar total:
:vartype total: float
:ivar other:
:vartype other: str
:ivar custom_fields: Dictionary of :code:`<any>`.
:vartype custom_fields: dict[str, any]

<a id="models._models.RowAnnotation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `code`: 
- `date`: 
- `description`: 
- `unit`: 
- `unit_price`: 
- `quantity`: 
- `discount`: 
- `base_total`: 
- `tax_rate`: 
- `tax_total`: 
- `total`: 
- `other`: 
- `custom_fields`: Dictionary of :code:`<any>`.

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

All required parameters must be populated in order to send to Azure.

:ivar additional_properties: Unmatched properties from the message are deserialized to this
 collection.
:vartype additional_properties: dict[str, any]
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
- `parsed`: 

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

<a id="models._models.SplitRelation"></a>

## SplitRelation Objects

```python
class SplitRelation(msrest.serialization.Model)
```

SplitRelation.

:ivar identifier: Unique identifier for the document. If creating a document and left blank,
 one will be automatically generated.
:vartype identifier: str

<a id="models._models.SplitRelation.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**kwargs)
```

**Arguments**:

- `identifier`: Unique identifier for the document. If creating a document and left blank,
one will be automatically generated.

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
:ivar id:
:vartype id: int
:ivar rectangle: Required.
:vartype rectangle: ~affinda.models.Rectangle
:ivar page_index: Required.
:vartype page_index: int
:ivar raw: Required.
:vartype raw: str
:ivar confidence: Required.
:vartype confidence: float
:ivar is_verified: Required.
:vartype is_verified: bool
:ivar is_client_verified:
:vartype is_client_verified: bool
:ivar is_auto_verified:
:vartype is_auto_verified: bool
:ivar classification: Required.
:vartype classification: str
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
- `id`: 
- `rectangle`: Required.
- `page_index`: Required.
- `raw`: Required.
- `confidence`: Required.
- `is_verified`: Required.
- `is_client_verified`: 
- `is_auto_verified`: 
- `classification`: Required.
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

