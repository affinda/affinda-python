# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.6, generator: @autorest/python@5.16.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class EducationLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    SCHOOL = "school"
    CERTIFICATE = "certificate"
    BACHELORS = "bachelors"
    MASTERS = "masters"
    DOCTORAL = "doctoral"


class Enum2(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    HR_XML = "hr-xml"


class Enum5(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    RESUMES = "resumes"
    JOB_DESCRIPTIONS = "job_descriptions"


class Enum8(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    RESUMES = "resumes"
    JOB_DESCRIPTIONS = "job_descriptions"


class GetResponses200ContentApplicationJsonSchemaResultsItemDocumentType(
    str, Enum, metaclass=CaseInsensitiveEnumMeta
):

    RESUMES = "resumes"
    JOB_DESCRIPTIONS = "job_descriptions"


class ManagementLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    NONE = "None"
    LOW = "Low"
    MID = "Mid"
    UPPER = "Upper"


class PostContentSchemaDocumentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    RESUMES = "resumes"
    JOB_DESCRIPTIONS = "job_descriptions"


class Region(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """region - server parameter"""

    API = "api"
    API_EU1 = "api.eu1"


class ResthookEvent(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The event name to subscribe to."""

    RESUME_PARSE_SUCCEEDED = "resume.parse.succeeded"
    RESUME_PARSE_FAILED = "resume.parse.failed"
    RESUME_PARSE_COMPLETED = "resume.parse.completed"
    INVOICE_PARSE_SUCCEEDED = "invoice.parse.succeeded"
    INVOICE_PARSE_FAILED = "invoice.parse.failed"
    INVOICE_PARSE_COMPLETED = "invoice.parse.completed"
    INVOICE_VALIDATE_COMPLETED = "invoice.validate.completed"
    DOCUMENT_PARSE_SUCCEEDED = "document.parse.succeeded"
    DOCUMENT_PARSE_FAILED = "document.parse.failed"
    DOCUMENT_PARSE_COMPLETED = "document.parse.completed"
    DOCUMENT_VALIDATE_COMPLETED = "document.validate.completed"
    DOCUMENT_CLASSIFY_SUCCEEDED = "document.classify.succeeded"
    DOCUMENT_CLASSIFY_FAILED = "document.classify.failed"
    DOCUMENT_CLASSIFY_COMPLETED = "document.classify.completed"


class ResthookSubscriptionVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Version of the resthook subscription. Determines the resthook body being fired."""

    V1 = "v1"
    V2 = "v2"
    V3 = "v3"


class ResumeDataLanguagesItem(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    AINU = "ainu"
    AKAN = "akan"
    AKKADIAN = "akkadian"
    AMHARIC = "amharic"
    ANAM = "anam"
    ARABIC = "arabic"
    ARAMAIC = "aramaic"
    AREM = "arem"
    ARMENIAN = "armenian"
    AWADHI = "awadhi"
    AYMARA = "aymara"
    AZARI = "azari"
    BAGHELI = "bagheli"
    BAGRI = "bagri"
    BAHASA = "bahasa"
    BAMBARA = "bambara"
    BANGALA = "bangala"
    BARDI = "bardi"
    BASSA = "bassa"
    BATAK = "batak"
    BELARUSIAN = "belarusian"
    BEMBA = "bemba"
    BENGA = "benga"
    BENGALI = "bengali"
    BERBER = "berber"
    BHOJPURI = "bhojpuri"
    BISLAMA = "bislama"
    BRAHUI = "brahui"
    BULGARIAN = "bulgarian"
    BUNU = "bunu"
    CAMBODIAN = "cambodian"
    CAREW = "carew"
    CARIB = "carib"
    CATALAN = "catalan"
    CEBUANO = "cebuano"
    CHAKMA = "chakma"
    CHAMORRO = "chamorro"
    CHANGO = "chango"
    CHEWA = "chewa"
    CROATIAN = "croatian"
    CZECH = "czech"
    DAGBANI = "dagbani"
    DANISH = "danish"
    DARI = "dari"
    DAYI = "dayi"
    DHATKI = "dhatki"
    DHIVEHI = "dhivehi"
    DINKA = "dinka"
    DOGRI = "dogri"
    DUALA = "duala"
    DUTCH = "dutch"
    ENGLISH = "english"
    ESPERANTO = "esperanto"
    ESTONIAN = "estonian"
    EWONDO = "ewondo"
    FAROESE = "faroese"
    FILIPINO = "filipino"
    FINNISH = "finnish"
    FORMULA = "formula"
    FRENCH = "french"
    FRISIAN = "frisian"
    FRIULIAN = "friulian"
    FULA = "fula"
    GAELIC = "gaelic"
    GALO = "galo"
    GARHWALI = "garhwali"
    GARIFUNA = "garifuna"
    GERMAN = "german"
    GIKUYU = "gikuyu"
    GUJARATI = "gujarati"
    GUJERATI = "gujerati"
    GWERE = "gwere"
    HAWAIIAN = "hawaiian"
    HAYA = "haya"
    HEBREW = "hebrew"
    HINDI = "hindi"
    HMU = "hmu"
    HOKKIEN = "hokkien"
    HOPI = "hopi"
    HUNGARIAN = "hungarian"
    HUP = "hup"
    IBANAG = "ibanag"
    IGBO = "igbo"
    ILOKANO = "ilokano"
    INDONESIAN = "indonesian"
    INTERMEDIATE = "intermediate"
    IRISH = "irish"
    ITALIAN = "italian"
    JAPANESE = "japanese"
    JIBA = "jiba"
    KACHIN = "kachin"
    KALENJIN = "kalenjin"
    KAMAYO = "kamayo"
    KANNADA = "kannada"
    KAONDE = "kaonde"
    KAYAN = "kayan"
    KHANDESHI = "khandeshi"
    KHMER = "khmer"
    KIKUYU = "kikuyu"
    KODAVA = "kodava"
    KOMA = "koma"
    KONGO = "kongo"
    KONKANI = "konkani"
    KOREAN = "korean"
    KORWA = "korwa"
    KREYOL = "kreyol"
    KRIO = "krio"
    KUMAONI = "kumaoni"
    KURDISH = "kurdish"
    KURUKH = "kurukh"
    KWA = "kwa"
    LADINO = "ladino"
    LANGO = "lango"
    LATVIAN = "latvian"
    LAWA = "lawa"
    LINGALA = "lingala"
    LITHUANIAN = "lithuanian"
    LULE = "lule"
    LUXEMBOURGISH = "luxembourgish"
    MAGAHI = "magahi"
    MAITHILI = "maithili"
    MALAY = "malay"
    MALAYALAM = "malayalam"
    MALAYSIAN = "malaysian"
    MALVI = "malvi"
    MANINKA = "maninka"
    MANIPURI = "manipuri"
    MANX = "manx"
    MARATHI = "marathi"
    MAYAN = "mayan"
    MEDUMBA = "medumba"
    MEMONI = "memoni"
    MEWARI = "mewari"
    MIZO = "mizo"
    MONTENEGRIN = "montenegrin"
    MWAN = "mwan"
    MWANGA = "mwanga"
    NDEBELE = "ndebele"
    NEPALI = "nepali"
    NIMADI = "nimadi"
    ORIYA = "oriya"
    OROMO = "oromo"
    OVAMBO = "ovambo"
    PAMONA = "pamona"
    PANGASINAN = "pangasinan"
    PASHTO = "pashto"
    PHOENICIAN = "phoenician"
    POLISH = "polish"
    PORTUGUESE = "portuguese"
    PULAAR = "pulaar"
    PULAR = "pular"
    PUNJABI = "punjabi"
    QUECHA = "quecha"
    RAJASTHANI = "rajasthani"
    ROMANIAN = "romanian"
    RUSSIAN = "russian"
    SAKHA = "sakha"
    SANGO = "sango"
    SANTHALI = "santhali"
    SARAIKI = "saraiki"
    SEIM = "seim"
    SHADING = "shading"
    SHAMA = "shama"
    SHAN = "shan"
    SHONA = "shona"
    SILESIAN = "silesian"
    SINDHI = "sindhi"
    SLOVAK = "slovak"
    SLOVENE = "slovene"
    SOGA = "soga"
    SOGDIAN = "sogdian"
    SOTHO = "sotho"
    SPANISH = "spanish"
    SUDANESE = "sudanese"
    SUMERIAN = "sumerian"
    SURAJPURI = "surajpuri"
    SURIGAONON = "surigaonon"
    SWATI = "swati"
    SWAZI = "swazi"
    SWEDISH = "swedish"
    TAGALOG = "tagalog"
    TAMIL = "tamil"
    TAUSUG = "tausug"
    TELUGU = "telugu"
    TETUM = "tetum"
    THARU = "tharu"
    TIBETAN = "tibetan"
    TIGRINYA = "tigrinya"
    TRIPURI = "tripuri"
    TSWANA = "tswana"
    TULU = "tulu"
    TURKISH = "turkish"
    TUWALI = "tuwali"
    UBI = "ubi"
    UKRAINIAN = "ukrainian"
    URDU = "urdu"
    VEPS = "veps"
    VIETNAMESE = "vietnamese"
    WAGDI = "wagdi"
    WAZIRI = "waziri"
    XHOSA = "xhosa"
    YIDDISH = "yiddish"
    YORUBA = "yoruba"


class ResumeSkillSourcesItemSection(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    ACHIEVEMENTS = "Achievements"
    ADDITIONAL_INFORMATION = "AdditionalInformation"
    EDUCATION = "Education"
    EXTRACURRICULARS = "Extracurriculars"
    ORGANISATIONS = "Organisations"
    OTHER = "Other"
    PERSONAL_DETAILS = "PersonalDetails"
    PROJECTS = "Projects"
    PUBLICATIONS = "Publications"
    REFEREES = "Referees"
    SKILLS = "Skills"
    SUMMARY = "Summary"
    TRAINING = "Training"
    WORK_EXPERIENCE = "WorkExperience"
    NOT_POPULATED = "NotPopulated"
    HEADER = "Header"
    FOOTER = "Footer"
    SKILLS_INTERESTS_LANGUAGES = "Skills/Interests/Languages"
    TRAINING_CERTIFICATIONS = "Training/Certifications"
    EXTRACURRICULARS_LEADERSHIP = "Extracurriculars/Leadership"


class SearchLocationUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    KM = "km"
    MI = "mi"


class SearchParametersCustomDataFilterType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Data points of "text" type support only "equals" filterType, others support both "equals" and
    "range"
    """

    EQUALS = "equals"
    RANGE = "range"


class Version(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Version of the resthook subscription. Determines the resthook body being fired."""

    V1 = "v1"
    V2 = "v2"
    V3 = "v3"
