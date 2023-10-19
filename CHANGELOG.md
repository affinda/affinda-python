# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.7.0] - 2023-10-19
### Added
- Add field custom_identifier to DocumentMeta model
- Allow specifying custom_identifier when create/update document

### Deprecated
- Deprecate writing to identifier when creating/updating document

## [3.6.0] - 2023-10-03
### Added
- Add SOC group codes to classification

## [3.5.0] - 2023-09-21
### Added
- Add "document.rejected" webhook event

## [3.4.0] - 2023-07-19
### Changed
- Set CustomFieldConfig default to 0.5

### Added
- Support for custom base URL and http scheme in async client

## [3.3.0] - 2023-06-27
### Changed
- rawText is now not nullable
- Allow custom resume fields to be nullable
- Allow custom job description fields to be nullable
- Make "pdf" property in SearchResults nullable
- Nest line item table rows correctly.
- Make `slug` and `organization` required when creating data point

### Fixed
- Allow rejectDuplicates to be null
- Update python_requires to be PEP compliant
- Set resumes GET document format to be an enum

### Added
- Phone number details to Resume Candidate info
- "data" to job description create
- Custom fields to Job Descriptions
- Add custom data to job description search results
- Add custom data to job description search results
- Add international_country_code to phone number details
- Add customData field to JD search param/result serializers
- rawText field to JobDescription Model
- Required fields for resthook subscriptions
- Ability to post/patch languages for resumes in v2
- Allow create/update data point's `parent` and `displayEnumValue` property
- Allow explicitly set a document as low_priority

### Removed
- Remove data point's `similarTo` property

## [3.2.1] - 2023-03-30
### Changed
- "Rectangles" attribute in Annotation updates to readonly

## [3.2.0] - 2023-03-15
### Fixed
- Fix JD create/update after v2/v3 split
- Ensure list endpoints have 'results' and 'count' properties required

## [3.1.0] - 2023-03-10
### Fixed
- Fixed GET request array object types for invoices, resumes, redacted resumes and job_descriptions

## [3.0.2] - 2023-03-09
### Fixed
- Fixed ImportError due to un-needed patch file for v2 api endpoitns

## [3.0.1] - 2023-03-09
### Added
- Add redactedText to resume data

## [3.0.0] - 2023-03-09
### Added
- Add resthook subscription endpoints
- Add py.typed marker file
- Added PATCH support for Job Descriptions
- Add `confirmed_by` field to document meta
- Add link to affinda help docs for resthook creation
- Add activate resthook subscription endpoint

### Changed
- Remove extractor's `id` field, use `identifier` field instead
- Rework document polymorphism, the model used to deserialize document response is now automatically chosen based on the document's extractor
- Make Document.Meta.confirmedBy nullable

### Removed
- Remove extractor's `id` field
- Removed v3 endpoints, see newer major release for v3 compatible release

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
