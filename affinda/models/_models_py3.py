# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.5.1, generator: @autorest/python@5.9.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import IO, List, Optional

import msrest.serialization


class Components8Sxs33Responses400ErrorContentApplicationJsonSchema(
    msrest.serialization.Model
):
    """Components8Sxs33Responses400ErrorContentApplicationJsonSchema.

    :param status_code:
    :type status_code: int
    :param detail:
    :type detail: str
    """

    _attribute_map = {
        "status_code": {"key": "statusCode", "type": "int"},
        "detail": {"key": "detail", "type": "str"},
    }

    def __init__(
        self,
        *,
        status_code: Optional[int] = None,
        detail: Optional[str] = None,
        **kwargs,
    ):
        super(
            Components8Sxs33Responses400ErrorContentApplicationJsonSchema, self
        ).__init__(**kwargs)
        self.status_code = status_code
        self.detail = detail


class ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema(
    msrest.serialization.Model
):
    """ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema.

    :param detail:
    :type detail: str
    :param status_code:
    :type status_code: int
    """

    _attribute_map = {
        "detail": {"key": "detail", "type": "str"},
        "status_code": {"key": "statusCode", "type": "int"},
    }

    def __init__(
        self,
        *,
        detail: Optional[str] = None,
        status_code: Optional[int] = None,
        **kwargs,
    ):
        super(
            ComponentsMzfa75Responses401ErrorContentApplicationJsonSchema, self
        ).__init__(**kwargs)
        self.detail = detail
        self.status_code = status_code


class ComponentsP4H6CrResponses404ErrorContentApplicationJsonSchema(
    msrest.serialization.Model
):
    """ComponentsP4H6CrResponses404ErrorContentApplicationJsonSchema.

    :param detail:
    :type detail: str
    :param status_code:
    :type status_code: int
    """

    _attribute_map = {
        "detail": {"key": "detail", "type": "str"},
        "status_code": {"key": "statusCode", "type": "int"},
    }

    def __init__(
        self,
        *,
        detail: Optional[str] = None,
        status_code: Optional[int] = None,
        **kwargs,
    ):
        super(
            ComponentsP4H6CrResponses404ErrorContentApplicationJsonSchema, self
        ).__init__(**kwargs)
        self.detail = detail
        self.status_code = status_code


class Error(msrest.serialization.Model):
    """Error.

    :param error_code:
    :type error_code: str
    :param error_detail:
    :type error_detail: str
    """

    _attribute_map = {
        "error_code": {"key": "errorCode", "type": "str"},
        "error_detail": {"key": "errorDetail", "type": "str"},
    }

    def __init__(
        self,
        *,
        error_code: Optional[str] = None,
        error_detail: Optional[str] = None,
        **kwargs,
    ):
        super(Error, self).__init__(**kwargs)
        self.error_code = error_code
        self.error_detail = error_detail


class Get200ApplicationJsonPropertiesItemsItem(msrest.serialization.Model):
    """Get200ApplicationJsonPropertiesItemsItem.

    All required parameters must be populated in order to send to Azure.

    :param identifier: Required. Unique identifier for the resume. If creating a document and left
     blank, one will be automatically generated.
    :type identifier: str
    :param format_file: Required. The template to apply.
    :type format_file: str
    """

    _validation = {
        "identifier": {"required": True},
        "format_file": {"required": True},
    }

    _attribute_map = {
        "identifier": {"key": "identifier", "type": "str"},
        "format_file": {"key": "formatFile", "type": "str"},
    }

    def __init__(self, *, identifier: str, format_file: str, **kwargs):
        super(Get200ApplicationJsonPropertiesItemsItem, self).__init__(**kwargs)
        self.identifier = identifier
        self.format_file = format_file


class GetAllDocumentsResults(msrest.serialization.Model):
    """GetAllDocumentsResults.

    :param count:
    :type count: int
    :param next:
    :type next: str
    :param previous:
    :type previous: str
    :param results:
    :type results: list[~affinda.models.Meta]
    """

    _attribute_map = {
        "count": {"key": "count", "type": "int"},
        "next": {"key": "next", "type": "str"},
        "previous": {"key": "previous", "type": "str"},
        "results": {"key": "results", "type": "[Meta]"},
    }

    def __init__(
        self,
        *,
        count: Optional[int] = None,
        next: Optional[str] = None,
        previous: Optional[str] = None,
        results: Optional[List["Meta"]] = None,
        **kwargs,
    ):
        super(GetAllDocumentsResults, self).__init__(**kwargs)
        self.count = count
        self.next = next
        self.previous = previous
        self.results = results


class Location(msrest.serialization.Model):
    """Location.

    All required parameters must be populated in order to send to Azure.

    :param formatted:
    :type formatted: str
    :param postal_code:
    :type postal_code: str
    :param state:
    :type state: str
    :param country:
    :type country: str
    :param raw_input: Required.
    :type raw_input: str
    :param street_number:
    :type street_number: str
    :param street:
    :type street: str
    :param apartment_number:
    :type apartment_number: str
    :param city:
    :type city: str
    """

    _validation = {
        "raw_input": {"required": True},
    }

    _attribute_map = {
        "formatted": {"key": "formatted", "type": "str"},
        "postal_code": {"key": "postalCode", "type": "str"},
        "state": {"key": "state", "type": "str"},
        "country": {"key": "country", "type": "str"},
        "raw_input": {"key": "rawInput", "type": "str"},
        "street_number": {"key": "streetNumber", "type": "str"},
        "street": {"key": "street", "type": "str"},
        "apartment_number": {"key": "apartmentNumber", "type": "str"},
        "city": {"key": "city", "type": "str"},
    }

    def __init__(
        self,
        *,
        raw_input: str,
        formatted: Optional[str] = None,
        postal_code: Optional[str] = None,
        state: Optional[str] = None,
        country: Optional[str] = None,
        street_number: Optional[str] = None,
        street: Optional[str] = None,
        apartment_number: Optional[str] = None,
        city: Optional[str] = None,
        **kwargs,
    ):
        super(Location, self).__init__(**kwargs)
        self.formatted = formatted
        self.postal_code = postal_code
        self.state = state
        self.country = country
        self.raw_input = raw_input
        self.street_number = street_number
        self.street = street
        self.apartment_number = apartment_number
        self.city = city


class Meta(msrest.serialization.Model):
    """Meta.

    All required parameters must be populated in order to send to Azure.

    :param identifier: Required. Unique identifier for the resume. If creating a document and left
     blank, one will be automatically generated.
    :type identifier: str
    :param file_name: Optional filename of the file.
    :type file_name: str
    :param ready: Required. If true, the document has finished processing. Particularly useful if
     an endpoint request specified wait=False, when polling use this variable to determine when to
     stop polling.
    :type ready: bool
    :param ready_dt: The datetime when the document was ready.
    :type ready_dt: ~datetime.datetime
    :param failed: Required. If true, some exception was raised during processing. Check the
     'error' field of the main return object.
    :type failed: bool
    :param expiry_time: The date/time in ISO-8601 format when the resume will be automatically
     deleted.  Defaults to no expiry.
    :type expiry_time: str
    """

    _validation = {
        "identifier": {"required": True},
        "ready": {"required": True},
        "failed": {"required": True},
    }

    _attribute_map = {
        "identifier": {"key": "identifier", "type": "str"},
        "file_name": {"key": "fileName", "type": "str"},
        "ready": {"key": "ready", "type": "bool"},
        "ready_dt": {"key": "readyDt", "type": "iso-8601"},
        "failed": {"key": "failed", "type": "bool"},
        "expiry_time": {"key": "expiryTime", "type": "str"},
    }

    def __init__(
        self,
        *,
        identifier: str,
        ready: bool,
        failed: bool,
        file_name: Optional[str] = None,
        ready_dt: Optional[datetime.datetime] = None,
        expiry_time: Optional[str] = None,
        **kwargs,
    ):
        super(Meta, self).__init__(**kwargs)
        self.identifier = identifier
        self.file_name = file_name
        self.ready = ready
        self.ready_dt = ready_dt
        self.failed = failed
        self.expiry_time = expiry_time


class Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema(
    msrest.serialization.Model
):
    """Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema.

    :param count:
    :type count: int
    :param next:
    :type next: str
    :param previous:
    :type previous: str
    :param results:
    :type results: list[~affinda.models.Get200ApplicationJsonPropertiesItemsItem]
    """

    _attribute_map = {
        "count": {"key": "count", "type": "int"},
        "next": {"key": "next", "type": "str"},
        "previous": {"key": "previous", "type": "str"},
        "results": {
            "key": "results",
            "type": "[Get200ApplicationJsonPropertiesItemsItem]",
        },
    }

    def __init__(
        self,
        *,
        count: Optional[int] = None,
        next: Optional[str] = None,
        previous: Optional[str] = None,
        results: Optional[List["Get200ApplicationJsonPropertiesItemsItem"]] = None,
        **kwargs,
    ):
        super(
            Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema, self
        ).__init__(**kwargs)
        self.count = count
        self.next = next
        self.previous = previous
        self.results = results


class Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema(
    msrest.serialization.Model
):
    """Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema.

    :param file: File as binary data blob.
    :type file: IO
    :param identifier: Unique identifier for the resume. If creating a document and left blank, one
     will be automatically generated.
    :type identifier: str
    :param file_name: Optional filename of the file.
    :type file_name: str
    :param url: URL to file to download and process.
    :type url: str
    :param wait: If true (default), will return a response only after processing has completed. If
     false, will return an empty data object which can be polled at the GET endpoint until
     processing is complete.
    :type wait: bool
    :param resume_language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for
     Chinese.
    :type resume_language: str
    :param expiry_time: The date/time in ISO-8601 format when the resume will be automatically
     deleted.  Defaults to no expiry.
    :type expiry_time: str
    """

    _attribute_map = {
        "file": {"key": "file", "type": "IO"},
        "identifier": {"key": "identifier", "type": "str"},
        "file_name": {"key": "fileName", "type": "str"},
        "url": {"key": "url", "type": "str"},
        "wait": {"key": "wait", "type": "bool"},
        "resume_language": {"key": "resumeLanguage", "type": "str"},
        "expiry_time": {"key": "expiryTime", "type": "str"},
    }

    def __init__(
        self,
        *,
        file: Optional[IO] = None,
        identifier: Optional[str] = None,
        file_name: Optional[str] = None,
        url: Optional[str] = None,
        wait: Optional[bool] = None,
        resume_language: Optional[str] = None,
        expiry_time: Optional[str] = None,
        **kwargs,
    ):
        super(
            Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema, self
        ).__init__(**kwargs)
        self.file = file
        self.identifier = identifier
        self.file_name = file_name
        self.url = url
        self.wait = wait
        self.resume_language = resume_language
        self.expiry_time = expiry_time


class Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema(
    msrest.serialization.Model
):
    """Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema.

    :param file: File as binary data blob.
    :type file: IO
    :param identifier: Unique identifier for the resume. If creating a document and left blank, one
     will be automatically generated.
    :type identifier: str
    :param file_name: Optional filename of the file.
    :type file_name: str
    :param url: URL to file to download and process.
    :type url: str
    :param resume_language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for
     Chinese.
    :type resume_language: str
    :param wait: If true (default), will return a response only after processing has completed. If
     false, will return an empty data object which can be polled at the GET endpoint until
     processing is complete.
    :type wait: bool
    :param redact_headshot: Whether to redact headshot.
    :type redact_headshot: bool
    :param redact_personal_details: Whether to redact personal details (e.g. name, address).
    :type redact_personal_details: bool
    :param redact_work_details: Whether to redact work details (e.g. company names).
    :type redact_work_details: bool
    :param redact_education_details: Whether to redact education details (e.g. university names).
    :type redact_education_details: bool
    :param redact_referees: Whether to redact referee details.
    :type redact_referees: bool
    :param redact_locations: Whether to redact location names.
    :type redact_locations: bool
    :param redact_dates: Whether to redact dates.
    :type redact_dates: bool
    :param expiry_time: The date/time in ISO-8601 format when the resume will be automatically
     deleted.  Defaults to no expiry.
    :type expiry_time: str
    """

    _attribute_map = {
        "file": {"key": "file", "type": "IO"},
        "identifier": {"key": "identifier", "type": "str"},
        "file_name": {"key": "fileName", "type": "str"},
        "url": {"key": "url", "type": "str"},
        "resume_language": {"key": "resumeLanguage", "type": "str"},
        "wait": {"key": "wait", "type": "bool"},
        "redact_headshot": {"key": "redactHeadshot", "type": "bool"},
        "redact_personal_details": {"key": "redactPersonalDetails", "type": "bool"},
        "redact_work_details": {"key": "redactWorkDetails", "type": "bool"},
        "redact_education_details": {"key": "redactEducationDetails", "type": "bool"},
        "redact_referees": {"key": "redactReferees", "type": "bool"},
        "redact_locations": {"key": "redactLocations", "type": "bool"},
        "redact_dates": {"key": "redactDates", "type": "bool"},
        "expiry_time": {"key": "expiryTime", "type": "str"},
    }

    def __init__(
        self,
        *,
        file: Optional[IO] = None,
        identifier: Optional[str] = None,
        file_name: Optional[str] = None,
        url: Optional[str] = None,
        resume_language: Optional[str] = None,
        wait: Optional[bool] = None,
        redact_headshot: Optional[bool] = True,
        redact_personal_details: Optional[bool] = True,
        redact_work_details: Optional[bool] = True,
        redact_education_details: Optional[bool] = True,
        redact_referees: Optional[bool] = True,
        redact_locations: Optional[bool] = True,
        redact_dates: Optional[bool] = True,
        expiry_time: Optional[str] = None,
        **kwargs,
    ):
        super(
            Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema,
            self,
        ).__init__(**kwargs)
        self.file = file
        self.identifier = identifier
        self.file_name = file_name
        self.url = url
        self.resume_language = resume_language
        self.wait = wait
        self.redact_headshot = redact_headshot
        self.redact_personal_details = redact_personal_details
        self.redact_work_details = redact_work_details
        self.redact_education_details = redact_education_details
        self.redact_referees = redact_referees
        self.redact_locations = redact_locations
        self.redact_dates = redact_dates
        self.expiry_time = expiry_time


class PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema(
    msrest.serialization.Model
):
    """PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema.

    All required parameters must be populated in order to send to Azure.

    :param file: File as binary data blob.
    :type file: IO
    :param identifier: Unique identifier for the resume. If creating a document and left blank, one
     will be automatically generated.
    :type identifier: str
    :param file_name: Optional filename of the file.
    :type file_name: str
    :param url: URL to file to download and process.
    :type url: str
    :param resume_language: Language code in ISO 639-1 format. Must specify zh-cn or zh-tw for
     Chinese.
    :type resume_language: str
    :param resume_format: Required. Identifier of the format used.
    :type resume_format: str
    :param wait: If true (default), will return a response only after processing has completed. If
     false, will return an empty data object which can be polled at the GET endpoint until
     processing is complete.
    :type wait: bool
    """

    _validation = {
        "resume_format": {"required": True},
    }

    _attribute_map = {
        "file": {"key": "file", "type": "IO"},
        "identifier": {"key": "identifier", "type": "str"},
        "file_name": {"key": "fileName", "type": "str"},
        "url": {"key": "url", "type": "str"},
        "resume_language": {"key": "resumeLanguage", "type": "str"},
        "resume_format": {"key": "resumeFormat", "type": "str"},
        "wait": {"key": "wait", "type": "bool"},
    }

    def __init__(
        self,
        *,
        resume_format: str,
        file: Optional[IO] = None,
        identifier: Optional[str] = None,
        file_name: Optional[str] = None,
        url: Optional[str] = None,
        resume_language: Optional[str] = None,
        wait: Optional[bool] = None,
        **kwargs,
    ):
        super(
            PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema,
            self,
        ).__init__(**kwargs)
        self.file = file
        self.identifier = identifier
        self.file_name = file_name
        self.url = url
        self.resume_language = resume_language
        self.resume_format = resume_format
        self.wait = wait


class RedactedResume(msrest.serialization.Model):
    """RedactedResume.

    All required parameters must be populated in order to send to Azure.

    :param data: Required.
    :type data: ~affinda.models.RedactedResumeData
    :param meta: Required.
    :type meta: ~affinda.models.Meta
    :param error: Required.
    :type error: ~affinda.models.Error
    """

    _validation = {
        "data": {"required": True},
        "meta": {"required": True},
        "error": {"required": True},
    }

    _attribute_map = {
        "data": {"key": "data", "type": "RedactedResumeData"},
        "meta": {"key": "meta", "type": "Meta"},
        "error": {"key": "error", "type": "Error"},
    }

    def __init__(
        self, *, data: "RedactedResumeData", meta: "Meta", error: "Error", **kwargs
    ):
        super(RedactedResume, self).__init__(**kwargs)
        self.data = data
        self.meta = meta
        self.error = error


class RedactedResumeData(msrest.serialization.Model):
    """RedactedResumeData.

    :param redacted_pdf:
    :type redacted_pdf: str
    """

    _attribute_map = {
        "redacted_pdf": {"key": "redactedPdf", "type": "str"},
    }

    def __init__(self, *, redacted_pdf: Optional[str] = None, **kwargs):
        super(RedactedResumeData, self).__init__(**kwargs)
        self.redacted_pdf = redacted_pdf


class ReformattedResume(msrest.serialization.Model):
    """ReformattedResume.

    All required parameters must be populated in order to send to Azure.

    :param data: Required.
    :type data: ~affinda.models.ReformattedResumeData
    :param meta: Required.
    :type meta: ~affinda.models.Meta
    :param error: Required.
    :type error: ~affinda.models.Error
    """

    _validation = {
        "data": {"required": True},
        "meta": {"required": True},
        "error": {"required": True},
    }

    _attribute_map = {
        "data": {"key": "data", "type": "ReformattedResumeData"},
        "meta": {"key": "meta", "type": "Meta"},
        "error": {"key": "error", "type": "Error"},
    }

    def __init__(
        self, *, data: "ReformattedResumeData", meta: "Meta", error: "Error", **kwargs
    ):
        super(ReformattedResume, self).__init__(**kwargs)
        self.data = data
        self.meta = meta
        self.error = error


class ReformattedResumeData(msrest.serialization.Model):
    """ReformattedResumeData.

    :param reformatted_file:
    :type reformatted_file: str
    """

    _attribute_map = {
        "reformatted_file": {"key": "reformattedFile", "type": "str"},
    }

    def __init__(self, *, reformatted_file: Optional[str] = None, **kwargs):
        super(ReformattedResumeData, self).__init__(**kwargs)
        self.reformatted_file = reformatted_file


class Resume(msrest.serialization.Model):
    """Resume.

    All required parameters must be populated in order to send to Azure.

    :param data: Required.
    :type data: ~affinda.models.ResumeData
    :param meta: Required.
    :type meta: ~affinda.models.Meta
    :param error: Required.
    :type error: ~affinda.models.Error
    """

    _validation = {
        "data": {"required": True},
        "meta": {"required": True},
        "error": {"required": True},
    }

    _attribute_map = {
        "data": {"key": "data", "type": "ResumeData"},
        "meta": {"key": "meta", "type": "Meta"},
        "error": {"key": "error", "type": "Error"},
    }

    def __init__(self, *, data: "ResumeData", meta: "Meta", error: "Error", **kwargs):
        super(Resume, self).__init__(**kwargs)
        self.data = data
        self.meta = meta
        self.error = error


class ResumeData(msrest.serialization.Model):
    """ResumeData.

    :param name:
    :type name: ~affinda.models.ResumeDataName
    :param phone_numbers:
    :type phone_numbers: list[str]
    :param websites:
    :type websites: list[str]
    :param emails:
    :type emails: list[str]
    :param date_of_birth:
    :type date_of_birth: str
    :param location:
    :type location: ~affinda.models.Location
    :param objective:
    :type objective: str
    :param languages:
    :type languages: list[str]
    :param summary:
    :type summary: str
    :param total_years_experience:
    :type total_years_experience: int
    :param head_shot: base64 encoded string.
    :type head_shot: IO
    :param education:
    :type education: list[~affinda.models.ResumeDataEducationItem]
    :param work_experience:
    :type work_experience: list[~affinda.models.ResumeDataWorkExperienceItem]
    :param skills:
    :type skills: list[~affinda.models.ResumeDataSkillsItem]
    :param certifications:
    :type certifications: list[str]
    :param publications:
    :type publications: list[str]
    :param referees:
    :type referees: list[~affinda.models.ResumeDataRefereesItem]
    :param sections:
    :type sections: list[~affinda.models.ResumeDataSectionsItem]
    :param is_resume_probability: Probability that the given document is a resume. Values below 30
     suggest that the resume is not a resume.
    :type is_resume_probability: int
    :param raw_text: All of the raw text of the parsed resume, example is shortened for readiblity.
    :type raw_text: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "ResumeDataName"},
        "phone_numbers": {"key": "phoneNumbers", "type": "[str]"},
        "websites": {"key": "websites", "type": "[str]"},
        "emails": {"key": "emails", "type": "[str]"},
        "date_of_birth": {"key": "dateOfBirth", "type": "str"},
        "location": {"key": "location", "type": "Location"},
        "objective": {"key": "objective", "type": "str"},
        "languages": {"key": "languages", "type": "[str]"},
        "summary": {"key": "summary", "type": "str"},
        "total_years_experience": {"key": "totalYearsExperience", "type": "int"},
        "head_shot": {"key": "headShot", "type": "IO"},
        "education": {"key": "education", "type": "[ResumeDataEducationItem]"},
        "work_experience": {
            "key": "workExperience",
            "type": "[ResumeDataWorkExperienceItem]",
        },
        "skills": {"key": "skills", "type": "[ResumeDataSkillsItem]"},
        "certifications": {"key": "certifications", "type": "[str]"},
        "publications": {"key": "publications", "type": "[str]"},
        "referees": {"key": "referees", "type": "[ResumeDataRefereesItem]"},
        "sections": {"key": "sections", "type": "[ResumeDataSectionsItem]"},
        "is_resume_probability": {"key": "isResumeProbability", "type": "int"},
        "raw_text": {"key": "rawText", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: Optional["ResumeDataName"] = None,
        phone_numbers: Optional[List[str]] = None,
        websites: Optional[List[str]] = None,
        emails: Optional[List[str]] = None,
        date_of_birth: Optional[str] = None,
        location: Optional["Location"] = None,
        objective: Optional[str] = None,
        languages: Optional[List[str]] = None,
        summary: Optional[str] = None,
        total_years_experience: Optional[int] = None,
        head_shot: Optional[IO] = None,
        education: Optional[List["ResumeDataEducationItem"]] = None,
        work_experience: Optional[List["ResumeDataWorkExperienceItem"]] = None,
        skills: Optional[List["ResumeDataSkillsItem"]] = None,
        certifications: Optional[List[str]] = None,
        publications: Optional[List[str]] = None,
        referees: Optional[List["ResumeDataRefereesItem"]] = None,
        sections: Optional[List["ResumeDataSectionsItem"]] = None,
        is_resume_probability: Optional[int] = None,
        raw_text: Optional[str] = None,
        **kwargs,
    ):
        super(ResumeData, self).__init__(**kwargs)
        self.name = name
        self.phone_numbers = phone_numbers
        self.websites = websites
        self.emails = emails
        self.date_of_birth = date_of_birth
        self.location = location
        self.objective = objective
        self.languages = languages
        self.summary = summary
        self.total_years_experience = total_years_experience
        self.head_shot = head_shot
        self.education = education
        self.work_experience = work_experience
        self.skills = skills
        self.certifications = certifications
        self.publications = publications
        self.referees = referees
        self.sections = sections
        self.is_resume_probability = is_resume_probability
        self.raw_text = raw_text


class ResumeDataEducationItem(msrest.serialization.Model):
    """ResumeDataEducationItem.

    :param organization:
    :type organization: str
    :param accreditation:
    :type accreditation: ~affinda.models.ResumeDataEducationItemAccreditation
    :param grade:
    :type grade: ~affinda.models.ResumeDataEducationItemGrade
    :param location:
    :type location: ~affinda.models.Location
    :param dates:
    :type dates: ~affinda.models.ResumeDataEducationItemDates
    """

    _attribute_map = {
        "organization": {"key": "organization", "type": "str"},
        "accreditation": {
            "key": "accreditation",
            "type": "ResumeDataEducationItemAccreditation",
        },
        "grade": {"key": "grade", "type": "ResumeDataEducationItemGrade"},
        "location": {"key": "location", "type": "Location"},
        "dates": {"key": "dates", "type": "ResumeDataEducationItemDates"},
    }

    def __init__(
        self,
        *,
        organization: Optional[str] = None,
        accreditation: Optional["ResumeDataEducationItemAccreditation"] = None,
        grade: Optional["ResumeDataEducationItemGrade"] = None,
        location: Optional["Location"] = None,
        dates: Optional["ResumeDataEducationItemDates"] = None,
        **kwargs,
    ):
        super(ResumeDataEducationItem, self).__init__(**kwargs)
        self.organization = organization
        self.accreditation = accreditation
        self.grade = grade
        self.location = location
        self.dates = dates


class ResumeDataEducationItemAccreditation(msrest.serialization.Model):
    """ResumeDataEducationItemAccreditation.

    :param education:
    :type education: str
    :param input_str:
    :type input_str: str
    :param match_str:
    :type match_str: str
    :param education_level:
    :type education_level: str
    """

    _attribute_map = {
        "education": {"key": "education", "type": "str"},
        "input_str": {"key": "inputStr", "type": "str"},
        "match_str": {"key": "matchStr", "type": "str"},
        "education_level": {"key": "educationLevel", "type": "str"},
    }

    def __init__(
        self,
        *,
        education: Optional[str] = None,
        input_str: Optional[str] = None,
        match_str: Optional[str] = None,
        education_level: Optional[str] = None,
        **kwargs,
    ):
        super(ResumeDataEducationItemAccreditation, self).__init__(**kwargs)
        self.education = education
        self.input_str = input_str
        self.match_str = match_str
        self.education_level = education_level


class ResumeDataEducationItemDates(msrest.serialization.Model):
    """ResumeDataEducationItemDates.

    :param completion_date:
    :type completion_date: ~datetime.date
    :param is_current:
    :type is_current: bool
    :param start_date:
    :type start_date: ~datetime.date
    """

    _attribute_map = {
        "completion_date": {"key": "completionDate", "type": "date"},
        "is_current": {"key": "isCurrent", "type": "bool"},
        "start_date": {"key": "startDate", "type": "date"},
    }

    def __init__(
        self,
        *,
        completion_date: Optional[datetime.date] = None,
        is_current: Optional[bool] = None,
        start_date: Optional[datetime.date] = None,
        **kwargs,
    ):
        super(ResumeDataEducationItemDates, self).__init__(**kwargs)
        self.completion_date = completion_date
        self.is_current = is_current
        self.start_date = start_date


class ResumeDataEducationItemGrade(msrest.serialization.Model):
    """ResumeDataEducationItemGrade.

    :param raw:
    :type raw: str
    :param metric:
    :type metric: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        "raw": {"key": "raw", "type": "str"},
        "metric": {"key": "metric", "type": "str"},
        "value": {"key": "value", "type": "str"},
    }

    def __init__(
        self,
        *,
        raw: Optional[str] = None,
        metric: Optional[str] = None,
        value: Optional[str] = None,
        **kwargs,
    ):
        super(ResumeDataEducationItemGrade, self).__init__(**kwargs)
        self.raw = raw
        self.metric = metric
        self.value = value


class ResumeDataName(msrest.serialization.Model):
    """ResumeDataName.

    :param raw:
    :type raw: str
    :param first:
    :type first: str
    :param last:
    :type last: str
    :param middle:
    :type middle: str
    :param title:
    :type title: str
    """

    _attribute_map = {
        "raw": {"key": "raw", "type": "str"},
        "first": {"key": "first", "type": "str"},
        "last": {"key": "last", "type": "str"},
        "middle": {"key": "middle", "type": "str"},
        "title": {"key": "title", "type": "str"},
    }

    def __init__(
        self,
        *,
        raw: Optional[str] = None,
        first: Optional[str] = None,
        last: Optional[str] = None,
        middle: Optional[str] = None,
        title: Optional[str] = None,
        **kwargs,
    ):
        super(ResumeDataName, self).__init__(**kwargs)
        self.raw = raw
        self.first = first
        self.last = last
        self.middle = middle
        self.title = title


class ResumeDataRefereesItem(msrest.serialization.Model):
    """ResumeDataRefereesItem.

    :param name:
    :type name: str
    :param text:
    :type text: str
    :param email:
    :type email: str
    :param number:
    :type number: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "text": {"key": "text", "type": "str"},
        "email": {"key": "email", "type": "str"},
        "number": {"key": "number", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        text: Optional[str] = None,
        email: Optional[str] = None,
        number: Optional[str] = None,
        **kwargs,
    ):
        super(ResumeDataRefereesItem, self).__init__(**kwargs)
        self.name = name
        self.text = text
        self.email = email
        self.number = number


class ResumeDataSectionsItem(msrest.serialization.Model):
    """ResumeDataSectionsItem.

    :param section_type:
    :type section_type: str
    :param bbox:
    :type bbox: list[float]
    :param page_index:
    :type page_index: int
    :param text:
    :type text: str
    """

    _validation = {
        "bbox": {"max_items": 4, "min_items": 4},
    }

    _attribute_map = {
        "section_type": {"key": "sectionType", "type": "str"},
        "bbox": {"key": "bbox", "type": "[float]"},
        "page_index": {"key": "pageIndex", "type": "int"},
        "text": {"key": "text", "type": "str"},
    }

    def __init__(
        self,
        *,
        section_type: Optional[str] = None,
        bbox: Optional[List[float]] = None,
        page_index: Optional[int] = None,
        text: Optional[str] = None,
        **kwargs,
    ):
        super(ResumeDataSectionsItem, self).__init__(**kwargs)
        self.section_type = section_type
        self.bbox = bbox
        self.page_index = page_index
        self.text = text


class ResumeDataSkillsItem(msrest.serialization.Model):
    """ResumeDataSkillsItem.

    :param name:
    :type name: str
    :param last_used:
    :type last_used: str
    :param number_of_months:
    :type number_of_months: int
    :param type:
    :type type: str
    :param sources:
    :type sources: list[~affinda.models.ResumeDataSkillsPropertiesItemsItem]
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "last_used": {"key": "lastUsed", "type": "str"},
        "number_of_months": {"key": "numberOfMonths", "type": "int"},
        "type": {"key": "type", "type": "str"},
        "sources": {"key": "sources", "type": "[ResumeDataSkillsPropertiesItemsItem]"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        last_used: Optional[str] = None,
        number_of_months: Optional[int] = None,
        type: Optional[str] = None,
        sources: Optional[List["ResumeDataSkillsPropertiesItemsItem"]] = None,
        **kwargs,
    ):
        super(ResumeDataSkillsItem, self).__init__(**kwargs)
        self.name = name
        self.last_used = last_used
        self.number_of_months = number_of_months
        self.type = type
        self.sources = sources


class ResumeDataSkillsPropertiesItemsItem(msrest.serialization.Model):
    """ResumeDataSkillsPropertiesItemsItem.

    :param section:
    :type section: str
    :param position:
    :type position: int
    """

    _attribute_map = {
        "section": {"key": "section", "type": "str"},
        "position": {"key": "position", "type": "int"},
    }

    def __init__(
        self, *, section: Optional[str] = None, position: Optional[int] = None, **kwargs
    ):
        super(ResumeDataSkillsPropertiesItemsItem, self).__init__(**kwargs)
        self.section = section
        self.position = position


class ResumeDataWorkExperienceItem(msrest.serialization.Model):
    """ResumeDataWorkExperienceItem.

    :param job_title:
    :type job_title: str
    :param organization:
    :type organization: str
    :param location:
    :type location: ~affinda.models.Location
    :param job_description:
    :type job_description: str
    :param dates:
    :type dates: ~affinda.models.ResumeDataWorkExperienceItemDates
    """

    _attribute_map = {
        "job_title": {"key": "jobTitle", "type": "str"},
        "organization": {"key": "organization", "type": "str"},
        "location": {"key": "location", "type": "Location"},
        "job_description": {"key": "jobDescription", "type": "str"},
        "dates": {"key": "dates", "type": "ResumeDataWorkExperienceItemDates"},
    }

    def __init__(
        self,
        *,
        job_title: Optional[str] = None,
        organization: Optional[str] = None,
        location: Optional["Location"] = None,
        job_description: Optional[str] = None,
        dates: Optional["ResumeDataWorkExperienceItemDates"] = None,
        **kwargs,
    ):
        super(ResumeDataWorkExperienceItem, self).__init__(**kwargs)
        self.job_title = job_title
        self.organization = organization
        self.location = location
        self.job_description = job_description
        self.dates = dates


class ResumeDataWorkExperienceItemDates(msrest.serialization.Model):
    """ResumeDataWorkExperienceItemDates.

    :param start_date:
    :type start_date: ~datetime.date
    :param end_date:
    :type end_date: ~datetime.date
    :param months_in_position:
    :type months_in_position: int
    :param is_current:
    :type is_current: bool
    """

    _attribute_map = {
        "start_date": {"key": "startDate", "type": "date"},
        "end_date": {"key": "endDate", "type": "date"},
        "months_in_position": {"key": "monthsInPosition", "type": "int"},
        "is_current": {"key": "isCurrent", "type": "bool"},
    }

    def __init__(
        self,
        *,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        months_in_position: Optional[int] = None,
        is_current: Optional[bool] = None,
        **kwargs,
    ):
        super(ResumeDataWorkExperienceItemDates, self).__init__(**kwargs)
        self.start_date = start_date
        self.end_date = end_date
        self.months_in_position = months_in_position
        self.is_current = is_current
