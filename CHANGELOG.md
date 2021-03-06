# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
