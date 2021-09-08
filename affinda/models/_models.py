# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.5.1, generator: @autorest/python@5.9.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


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

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.error_code = kwargs.get("error_code", None)
        self.error_detail = kwargs.get("error_detail", None)


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

    def __init__(self, **kwargs):
        super(Get200ApplicationJsonPropertiesItemsItem, self).__init__(**kwargs)
        self.identifier = kwargs["identifier"]
        self.format_file = kwargs["format_file"]


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

    def __init__(self, **kwargs):
        super(GetAllDocumentsResults, self).__init__(**kwargs)
        self.count = kwargs.get("count", None)
        self.next = kwargs.get("next", None)
        self.previous = kwargs.get("previous", None)
        self.results = kwargs.get("results", None)


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

    def __init__(self, **kwargs):
        super(Location, self).__init__(**kwargs)
        self.formatted = kwargs.get("formatted", None)
        self.postal_code = kwargs.get("postal_code", None)
        self.state = kwargs.get("state", None)
        self.country = kwargs.get("country", None)
        self.raw_input = kwargs["raw_input"]
        self.street_number = kwargs.get("street_number", None)
        self.street = kwargs.get("street", None)
        self.apartment_number = kwargs.get("apartment_number", None)
        self.city = kwargs.get("city", None)


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

    def __init__(self, **kwargs):
        super(Meta, self).__init__(**kwargs)
        self.identifier = kwargs["identifier"]
        self.file_name = kwargs.get("file_name", None)
        self.ready = kwargs["ready"]
        self.ready_dt = kwargs.get("ready_dt", None)
        self.failed = kwargs["failed"]
        self.expiry_time = kwargs.get("expiry_time", None)


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

    def __init__(self, **kwargs):
        super(
            Paths1UtuacyResumeFormatsGetResponses200ContentApplicationJsonSchema, self
        ).__init__(**kwargs)
        self.count = kwargs.get("count", None)
        self.next = kwargs.get("next", None)
        self.previous = kwargs.get("previous", None)
        self.results = kwargs.get("results", None)


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
    :param wait: If "true" (default), will return a response only after processing has completed.
     If "false", will return an empty data object which can be polled at the GET endpoint until
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

    def __init__(self, **kwargs):
        super(
            Paths7EskthResumesPostRequestbodyContentMultipartFormDataSchema, self
        ).__init__(**kwargs)
        self.file = kwargs.get("file", None)
        self.identifier = kwargs.get("identifier", None)
        self.file_name = kwargs.get("file_name", None)
        self.url = kwargs.get("url", None)
        self.wait = kwargs.get("wait", True)
        self.resume_language = kwargs.get("resume_language", None)
        self.expiry_time = kwargs.get("expiry_time", None)


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
    :param wait: If "true" (default), will return a response only after processing has completed.
     If "false", will return an empty data object which can be polled at the GET endpoint until
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

    def __init__(self, **kwargs):
        super(
            Paths8DdhfcRedactedResumesPostRequestbodyContentMultipartFormDataSchema,
            self,
        ).__init__(**kwargs)
        self.file = kwargs.get("file", None)
        self.identifier = kwargs.get("identifier", None)
        self.file_name = kwargs.get("file_name", None)
        self.url = kwargs.get("url", None)
        self.resume_language = kwargs.get("resume_language", None)
        self.wait = kwargs.get("wait", True)
        self.redact_headshot = kwargs.get("redact_headshot", True)
        self.redact_personal_details = kwargs.get("redact_personal_details", True)
        self.redact_work_details = kwargs.get("redact_work_details", True)
        self.redact_education_details = kwargs.get("redact_education_details", True)
        self.redact_referees = kwargs.get("redact_referees", True)
        self.redact_locations = kwargs.get("redact_locations", True)
        self.redact_dates = kwargs.get("redact_dates", True)
        self.expiry_time = kwargs.get("expiry_time", None)


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
    :param wait: If "true" (default), will return a response only after processing has completed.
     If "false", will return an empty data object which can be polled at the GET endpoint until
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

    def __init__(self, **kwargs):
        super(
            PathsYzn84IReformattedResumesPostRequestbodyContentMultipartFormDataSchema,
            self,
        ).__init__(**kwargs)
        self.file = kwargs.get("file", None)
        self.identifier = kwargs.get("identifier", None)
        self.file_name = kwargs.get("file_name", None)
        self.url = kwargs.get("url", None)
        self.resume_language = kwargs.get("resume_language", None)
        self.resume_format = kwargs["resume_format"]
        self.wait = kwargs.get("wait", True)


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

    def __init__(self, **kwargs):
        super(RedactedResume, self).__init__(**kwargs)
        self.data = kwargs["data"]
        self.meta = kwargs["meta"]
        self.error = kwargs["error"]


class RedactedResumeData(msrest.serialization.Model):
    """RedactedResumeData.

    :param redacted_pdf:
    :type redacted_pdf: str
    """

    _attribute_map = {
        "redacted_pdf": {"key": "redactedPdf", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(RedactedResumeData, self).__init__(**kwargs)
        self.redacted_pdf = kwargs.get("redacted_pdf", None)


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

    def __init__(self, **kwargs):
        super(ReformattedResume, self).__init__(**kwargs)
        self.data = kwargs["data"]
        self.meta = kwargs["meta"]
        self.error = kwargs["error"]


class ReformattedResumeData(msrest.serialization.Model):
    """ReformattedResumeData.

    :param reformatted_file:
    :type reformatted_file: str
    """

    _attribute_map = {
        "reformatted_file": {"key": "reformattedFile", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(ReformattedResumeData, self).__init__(**kwargs)
        self.reformatted_file = kwargs.get("reformatted_file", None)


class RequestError(msrest.serialization.Model):
    """RequestError.

    All required parameters must be populated in order to send to Azure.

    :param detail: Required.
    :type detail: str
    :param status_code: Required.
    :type status_code: int
    """

    _validation = {
        "detail": {"required": True},
        "status_code": {"required": True},
    }

    _attribute_map = {
        "detail": {"key": "detail", "type": "str"},
        "status_code": {"key": "statusCode", "type": "int"},
    }

    def __init__(self, **kwargs):
        super(RequestError, self).__init__(**kwargs)
        self.detail = kwargs["detail"]
        self.status_code = kwargs["status_code"]


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

    def __init__(self, **kwargs):
        super(Resume, self).__init__(**kwargs)
        self.data = kwargs["data"]
        self.meta = kwargs["meta"]
        self.error = kwargs["error"]


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
    :type head_shot: bytearray
    :param education:
    :type education: list[~affinda.models.ResumeDataEducationItem]
    :param profession: Prediction of the candidate's profession based on recent work experience.
    :type profession: str
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
        "head_shot": {"key": "headShot", "type": "bytearray"},
        "education": {"key": "education", "type": "[ResumeDataEducationItem]"},
        "profession": {"key": "profession", "type": "str"},
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

    def __init__(self, **kwargs):
        super(ResumeData, self).__init__(**kwargs)
        self.name = kwargs.get("name", None)
        self.phone_numbers = kwargs.get("phone_numbers", None)
        self.websites = kwargs.get("websites", None)
        self.emails = kwargs.get("emails", None)
        self.date_of_birth = kwargs.get("date_of_birth", None)
        self.location = kwargs.get("location", None)
        self.objective = kwargs.get("objective", None)
        self.languages = kwargs.get("languages", None)
        self.summary = kwargs.get("summary", None)
        self.total_years_experience = kwargs.get("total_years_experience", None)
        self.head_shot = kwargs.get("head_shot", None)
        self.education = kwargs.get("education", None)
        self.profession = kwargs.get("profession", None)
        self.work_experience = kwargs.get("work_experience", None)
        self.skills = kwargs.get("skills", None)
        self.certifications = kwargs.get("certifications", None)
        self.publications = kwargs.get("publications", None)
        self.referees = kwargs.get("referees", None)
        self.sections = kwargs.get("sections", None)
        self.is_resume_probability = kwargs.get("is_resume_probability", None)
        self.raw_text = kwargs.get("raw_text", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataEducationItem, self).__init__(**kwargs)
        self.organization = kwargs.get("organization", None)
        self.accreditation = kwargs.get("accreditation", None)
        self.grade = kwargs.get("grade", None)
        self.location = kwargs.get("location", None)
        self.dates = kwargs.get("dates", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataEducationItemAccreditation, self).__init__(**kwargs)
        self.education = kwargs.get("education", None)
        self.input_str = kwargs.get("input_str", None)
        self.match_str = kwargs.get("match_str", None)
        self.education_level = kwargs.get("education_level", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataEducationItemDates, self).__init__(**kwargs)
        self.completion_date = kwargs.get("completion_date", None)
        self.is_current = kwargs.get("is_current", None)
        self.start_date = kwargs.get("start_date", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataEducationItemGrade, self).__init__(**kwargs)
        self.raw = kwargs.get("raw", None)
        self.metric = kwargs.get("metric", None)
        self.value = kwargs.get("value", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataName, self).__init__(**kwargs)
        self.raw = kwargs.get("raw", None)
        self.first = kwargs.get("first", None)
        self.last = kwargs.get("last", None)
        self.middle = kwargs.get("middle", None)
        self.title = kwargs.get("title", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataRefereesItem, self).__init__(**kwargs)
        self.name = kwargs.get("name", None)
        self.text = kwargs.get("text", None)
        self.email = kwargs.get("email", None)
        self.number = kwargs.get("number", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataSectionsItem, self).__init__(**kwargs)
        self.section_type = kwargs.get("section_type", None)
        self.bbox = kwargs.get("bbox", None)
        self.page_index = kwargs.get("page_index", None)
        self.text = kwargs.get("text", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataSkillsItem, self).__init__(**kwargs)
        self.name = kwargs.get("name", None)
        self.last_used = kwargs.get("last_used", None)
        self.number_of_months = kwargs.get("number_of_months", None)
        self.type = kwargs.get("type", None)
        self.sources = kwargs.get("sources", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataSkillsPropertiesItemsItem, self).__init__(**kwargs)
        self.section = kwargs.get("section", None)
        self.position = kwargs.get("position", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataWorkExperienceItem, self).__init__(**kwargs)
        self.job_title = kwargs.get("job_title", None)
        self.organization = kwargs.get("organization", None)
        self.location = kwargs.get("location", None)
        self.job_description = kwargs.get("job_description", None)
        self.dates = kwargs.get("dates", None)


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

    def __init__(self, **kwargs):
        super(ResumeDataWorkExperienceItemDates, self).__init__(**kwargs)
        self.start_date = kwargs.get("start_date", None)
        self.end_date = kwargs.get("end_date", None)
        self.months_in_position = kwargs.get("months_in_position", None)
        self.is_current = kwargs.get("is_current", None)
