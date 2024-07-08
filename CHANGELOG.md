# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [4.23.0] - 2024-07-08
### Added
- Ability to filter index by name
- Ability to set workspace for MappingDataSource

## [4.22.2] - 2024-05-03
### Removed
- Removed unnecessary models of InvoiceData fields

## [4.22.1] - 2024-05-03
### Fixed
- Fix invoice data deserialization

## [4.22.0] - 2024-04-24
### Added
- Added filter and sort options for mapping data source endpoint

## [4.21.0] - 2024-04-10
### Fixed
- Fix invoiceData annotation required fields to match underling text annotation

### Changed
- Reduce maximum limit from 300 to 100 and remove default value

## [4.20.0] - 2024-03-26
### Changed
- Use ruff instead of black to format code, run check and format on code

### Added
- Add AnnotationBatchUpdate endpoint

## [4.19.0] - 2024-03-07
### Added
- Add validation_results endpoints
- Add US1 region
- Add strict attribute to RegionBias
- Add hideReject, hideEditPages, hideRunOcr and hideReparse options to Organization validationToolConfig
- `compact` parameter for upload document endpoint

## [4.18.0] - 2024-01-31
### Added
- Add sourceEmailAddress to DocumentMeta model
- Add tablesBeta to InvoiceData model
- Add sourceEmailAddress to document meta

## [4.17.0] - 2024-01-16
### Added
- Added "website" data point type
- Add mapping and dataSource to the field endpoints
- Add list mapping data sources endpoint

### Removed
- Removed "cell" data point type

### Changed
- Add URL annotation type

## [4.16.0] - 2023-12-04
### Added
- Add data mapping
- Add dropNullEnums to Field
- Added AnnotationContentType
- Added show_custom_field_creation to Organization
- Introduce endpoints to deal with data sources that can be created by customers, and used to map data onto a picklist, or lookup values for downstream validation

## [4.15.0] - 2023-11-14
### Added
- Add PATCH /index/<name> endpoint
- Add user to Index object
- Add "compact" query parameter to GET /documents/<identifier> endpoint
- Add "compact" query parameter to POST /documents endpoint

## [4.14.0] - 2023-11-08
### Added
- Add `parent` field to `Annotation`

### Fixed
- Make `Annotation.rectangles` field non-nullable
- Make `Annotation.document` field required

### Changed
- Remove enum constraint from `ordering` on the `getAllDocuments` operation

## [4.13.0] - 2023-10-24
### Added
- Add display_enum_value config to Collection field config

### Changed
- Migrate display_enum_value from DataPoint to Collection field config

### Removed
- Remove display_enum_value from DataPoint

## [4.12.0] - 2023-10-19
### Added
- Add disableEditDocumentMetadata option to validation tool config
- Add field custom_identifier to DocumentMeta model
- Allow specifying custom_identifier when create/update document

### Deprecated
- Deprecate writing to identifier when creating/updating document

## [4.11.0] - 2023-10-03
### Added
- Add SOC group codes to classification

## [4.10.0] - 2023-09-21
### Added
- Allow creating workspace-scope webhook
- Add "document.rejected" webhook event

## [4.9.0] - 2023-07-26
### Added
- Allow create and enable/disable child fields in Collection.fieldsLayout

### Deprecated
- Deprecate `fields` in favor of `enabledChildFields` and `disabledChildFields` in Collection.fieldsLayout

## [4.8.1] - 2023-07-19
### Fixed
- Serialisation of Document to Invoice, Resume etc in async get_document()

## [4.8.0] - 2023-07-19
### Changed
- Make Field.slug nullable and not required

### Deprecated
- Deprecate Field.slug

### Added
- Support for custom base URL and http scheme in async client

## [4.7.2] - 2023-07-07
### Changed
- Set CustomFieldConfig default to 0.5

### Fixed
- Fixed serialisation of Document to Invoice, Resume etc in get_document()

## [4.7.1] - 2023-06-28
### Added
- Add xml response to api spec to GET /v3/documenets to match existing functionality

## [4.7.0] - 2023-06-27
### Added
- Allow create/update data point's `parent` and `displayEnumValue` property
- Allow explicitly set a document as low_priority

### Changed
- Make `slug` and `organization` required when creating data point

### Removed
- Remove data point's `similarTo` property

## [4.6.0] - 2023-06-16
### Added
- Add `tailoredExtractorRequested` to Collection
- Add endpoint for update resumes and JD data

## [4.5.1] - 2023-06-14
### Added
- Add `rawText` to invoice data

## [4.5.0] - 2023-06-09
### Added
- Ability to post/patch languages for resumes in v2
- Add `include_public` parameter to /data_points endpoint
- Add `base_extractor` parameter to collection creation endpoint

### Changed
- Make `extractor` a non required field (internal use)

## [4.4.0] - 2023-06-07
### Added
- Endpoints for add/remove tag for documents
- Identifier field in DocumentUpdate model
- Allow setting `region_bias` when uploading document
- rawText field to JobDescription Model
- Required fields for resthook subscriptions
- Add `fieldsLayout` to `Collection` schema

### Deprecated
- Deprecate `Collection.fields` in favor of `Collection.fieldsLayout`

## [4.3.5] - 2023-05-09
### Changed
- Nest line item table rows correctly.

## [4.3.4] - 2023-05-09
### Changed
- Nest line item table rows correctly.

## [4.3.3] - 2023-05-09
### Added
- Add `Organization.validationToolConfig` for configuration of the embeddable validation tool
- Phone number details to Resume Candidate info
- Add some filters to `GET /documents` endpoint: `failed`, `ready`, `validatable`
- Custom fields to Job Descriptions
- Add custom data to job description search results
- Add international_country_code to phone number details

### Changed
- Provide additional filters for data point choices, and allow data point choices to be specified for any existing text field.
- Allow custom resume fields to be nullable
- Allow custom job description fields to be nullable
- Make "pdf" property in SearchResults nullable

### Removed
- Remove `include_child` filter from `/data_points` endpoint

### Fixed
- Update python_requires to be PEP compliant

## [4.3.2] - 2023-04-20
### Changed
- rawText is now not nullable
- OccupationGroupSearchResult.children is now optional

### Fixed
- Allow rejectDuplicates to be null

## [4.3.1] - 2023-03-29
### Added
- Add `whitelistIngestAddresses` to Workspace

### Fixed
- Make search config action fields required

## [4.3.0] - 2023-03-28
### Added
- Adding group annotation content type
- Add rejectDuplicates setting to workspace
- Add `hideToolbar` to resume & JD search config
- Add ExtractorConfig object to Collection

## [4.2.0] - 2023-03-20
### Fixed
- fixed - Use OccupationGroupResult for v3 SearchAndMatch detail
- Fixed return type for InvoiceData.currencyCode

### Changed
- Don't require Field.slug

### Added
- Add redactedText field to ResumeData

## [4.1.0] - 2023-03-15
### Fixed
- Fixed type and path of data_point and data_point_choices
- Fixed missing data field on base Document type
- Fixed search and match return types
- fixed document error return types
- Ensure list endpoints have 'results' and 'count' properties required

### Changed
- Minor re-ordering of API spec paths
- Change Document API tag from Document API - Upload Documents to Document API - Document

## [4.0.1] - 2023-03-10
### Fixed
- Fixed resume search response object

## [4.0.0] - 2023-03-09
### Added
- Add resthook subscription endpoints
- Add py.typed marker file
- Add link to affinda help docs for resthook creation

### Changed
- Remove extractor's `id` field, use `identifier` field instead

### Removed
- Remove extractor's `id` field
- Removed v2 endpoints

## [2.1.0] - 2023-02-06
### Added
- Add document.collection.extractor.identifier to DocumentMeta
- Add cell to valid content types
- Add EU API server to api docs
- Add latitude and longtitude to Location
- Add expectedremuneration, jobtitle, language, skill and yearsexperience to AnnotationContentType
- re-add DataPoint.simlarTo
- Add `exclude` parameter to /documents query
- add ingest email to Workspace and Collection

### Changed
- Updated endpoints for old v2 and newer v3 to point to the correct places.
- Changed Document top level structure to more closely resemble api v2 with top level keys of meta, data and error
- ResumeSearchParamaters.resume, ResumeSearchParameters.jobdescription, JobDescriptionSearchParameters.resume, DataPoint.organization
- Update azure-core version in setup.cfg and pin setuptools as latest version doens't buld

### Fixed
- Fixed various nullable fields not being nullable, and vice versa

### Removed
- Master/child accounts endpoints

## [2.0.0] - 2023-01-13
### Added
- Added endpoints: Organization, Membership, Invitation, tags
- Added name, organization to DataPoint, change id to identifier
- Add new objects schemas Organization, OrganizationMembership, Invitation

### Changed
- Identifier instead of id as URL param
- Update data point filters
- Allow unlimited nesting in field config
- Change document state from "export" to "archive"

### Fixed
- Collection identifier should be nullable
- Don't paginate extractors endpoint
- Fix avatar uploads
- Allow writing resthookSignatureKey

## [1.9.0] - 2023-01-12
* Yanked as this was a breaking release, see newer release for more info

## [1.8.0] - 2023-01-12
### Changed
- Allow non TLS http requests

## [1.7.0] - 2023-01-10
### Added
- Add rectangles to Annotation, add position to referee, add actions to JobDescriptionSearchConfig

## [1.6.0] - 2023-01-09
### Fixed
- Bump version to force new release

## [1.5.1] - 2023-01-08
### Changed
- Allowing a few more fields in ResumeData to be null

## [1.5.0] - 2022-11-17
### Fixed
- Document meta pages without images should be nullable
- Small fixes for accreditiation and education return objects
- Various nullable fields in the API spec

### Security
- Bumped package versions for patch reasons

### Added
- Add reject_duplicates to document upload endpoint
- XML 404 response schema
- CustomData to resume search spec
- suggest skills and job titles endpoints

### Changed
- Update spec to allow XML content-type return from resumes, make totalYearsExperience nullable
- Allow additonalproperties for custom data upload (resumes) and search

## [1.4.2] - 2022-09-23
### Changed
- Update API spec to match API response.

## [1.4.1] - 2022-09-23
### Added
- Add job description search config and embed endpoints
- Update index endpoint with document type parameter

### Fixed
- Fix casing of some properties to match API response.

## [1.4.0] - 2022-08-25
### Changed
- Update modelerfour version to latest
- Update types of objects for some endpoints using AllOf attributes for better client library generation
- Changed and updated tag order to better match documentation needs
- Updated autorest client version

### Deprecated
- Depreciated resume_formats and reformatted_resumes endpoints

### Added
- Reverse match functionality - search job descriptions with a resume, or with a set of parameters.

## [1.3.1] - 2022-08-10
### Added
- Add search expression to 1v1 match

## [1.3.0] - 2022-07-27
### Added
- Add ability to find other candidates that have similar attributes to a resume
- Add an endpoint to get the matching score between a resume and a job description

## [1.2.0] - 2022-07-04
### Added
- add "tables" property to InvoiceData

## [1.1.0] - 2022-07-03
### Added
- Ability to update resume data in the search system
- New endpoint for creating and managing users within a master account

## [1.0.2] - 2022-05-07
### Fixed
- Make expiry time native date time

## [1.0.1] - 2022-05-01
### Added
- Add review URL in the invoice response that allows embedding of the Affinda Invoice Review UI

## [1.0.0] - 2022-04-28
### Added
- added confidence

### Changed
- changed strings to objects

## [0.4.1] - 2022-04-19
### Fixed
- Fixes bug in create_invoice when URL is not specified

## [0.4.0] - 2022-04-13
### Changed
- Update autorest depedencies

## [0.3.0] - 2022-04-06
### Added
- Resume search

## [0.2.2] - 2022-03-25
### Added
- Add iso 3166 country code to locations

## [0.2.1] - 2021-12-09
### Added
- Bump version

## [0.2.0] - 2021-10-06
### Added
- Invoices endpoint

### Removed
- Removed 'url' format from url strings in api spec

## [0.1.13] - 2021-10-05
### Changed
- Pin azure-core to 1.18.0

## [0.1.12] - 2021-10-05
### Changed
- Pin azure-core

## [0.1.11] - 2021-10-05
### Changed
- Pinning azure-core dependency due to incompatible changes in 1.19

## [0.1.10] - 2021-09-30
### Added
- Adding LinkedIn to ResumeData

### Changed
- Reformatted code with black
- Minor changes
- Very minor formatting changes

## [0.1.9] - 2021-09-08
### Added
- Profession in ResumeData model
- Unified Error models

## [0.1.8] - 2021-09-06
### Fixed
- wait=true in API spec

## [0.1.7] - 2021-09-05
### Fixed
- Code samples naming conversion

## [0.1.6] - 2021-09-05
### Changed
- Description of some endpoints to match updats in API spec
- Moved samples to their own [./docs/samples_python.md](./docs/samples_python.md) file

## [0.1.5] - 2021-08-25
### Added
- Added flake, editorconfig, tox.ini etc files to match best practices for existing Draftable/Affinda projects (thanks
- @ralish!)

## [0.1.4] - 2021-08-18
### Fixed
- Update README.md to fix install instructions

## [0.1.3] - 2021-08-18
### Fixed
- Update README.md to hard link to github hosted logo to fix display on PyPi

## [0.1.2] - 2021-08-18
* Initial release
