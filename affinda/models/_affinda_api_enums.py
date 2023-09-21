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
    DOCUMENT_REJECTED = "document.rejected"


class ResthookSubscriptionVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Version of the resthook subscription. Determines the resthook body being fired."""

    V1 = "v1"
    V2 = "v2"
    V3 = "v3"


class ResumeDataLanguagesItem(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    AINU = "Ainu"
    AKAN = "Akan"
    AKKADIAN = "Akkadian"
    AMHARIC = "Amharic"
    ANAM = "Anam"
    ARABIC = "Arabic"
    ARAMAIC = "Aramaic"
    AREM = "Arem"
    ARMENIAN = "Armenian"
    AWADHI = "Awadhi"
    AYMARA = "Aymara"
    AZARI = "Azari"
    BAGHELI = "Bagheli"
    BAGRI = "Bagri"
    BAHASA = "Bahasa"
    BAMBARA = "Bambara"
    BANGALA = "Bangala"
    BARDI = "Bardi"
    BASSA = "Bassa"
    BATAK = "Batak"
    BELARUSIAN = "Belarusian"
    BEMBA = "Bemba"
    BENGA = "Benga"
    BENGALI = "Bengali"
    BERBER = "Berber"
    BHOJPURI = "Bhojpuri"
    BISLAMA = "Bislama"
    BRAHUI = "Brahui"
    BULGARIAN = "Bulgarian"
    BUNU = "Bunu"
    CAMBODIAN = "Cambodian"
    CAREW = "Carew"
    CARIB = "Carib"
    CATALAN = "Catalan"
    CEBUANO = "Cebuano"
    CHAKMA = "Chakma"
    CHAMORRO = "Chamorro"
    CHANGO = "Chango"
    CHEWA = "Chewa"
    CROATIAN = "Croatian"
    CZECH = "Czech"
    DAGBANI = "Dagbani"
    DANISH = "Danish"
    DARI = "Dari"
    DAYI = "Dayi"
    DHATKI = "Dhatki"
    DHIVEHI = "Dhivehi"
    DINKA = "Dinka"
    DOGRI = "Dogri"
    DUALA = "Duala"
    DUTCH = "Dutch"
    ENGLISH = "English"
    ESPERANTO = "Esperanto"
    ESTONIAN = "Estonian"
    EWONDO = "Ewondo"
    FAROESE = "Faroese"
    FILIPINO = "Filipino"
    FINNISH = "Finnish"
    FORMULA = "Formula"
    FRENCH = "French"
    FRISIAN = "Frisian"
    FRIULIAN = "Friulian"
    FULA = "Fula"
    GAELIC = "Gaelic"
    GALO = "Galo"
    GARHWALI = "Garhwali"
    GARIFUNA = "Garifuna"
    GERMAN = "German"
    GIKUYU = "Gikuyu"
    GUJARATI = "Gujarati"
    GUJERATI = "Gujerati"
    GWERE = "Gwere"
    HAWAIIAN = "Hawaiian"
    HAYA = "Haya"
    HEBREW = "Hebrew"
    HINDI = "Hindi"
    HMU = "Hmu"
    HOKKIEN = "Hokkien"
    HOPI = "Hopi"
    HUNGARIAN = "Hungarian"
    HUP = "Hup"
    IBANAG = "Ibanag"
    IGBO = "Igbo"
    ILOKANO = "Ilokano"
    INDONESIAN = "Indonesian"
    INTERMEDIATE = "Intermediate"
    IRISH = "Irish"
    ITALIAN = "Italian"
    JAPANESE = "Japanese"
    JIBA = "Jiba"
    KACHIN = "Kachin"
    KALENJIN = "Kalenjin"
    KAMAYO = "Kamayo"
    KANNADA = "Kannada"
    KAONDE = "Kaonde"
    KAYAN = "Kayan"
    KHANDESHI = "Khandeshi"
    KHMER = "Khmer"
    KIKUYU = "Kikuyu"
    KODAVA = "Kodava"
    KOMA = "Koma"
    KONGO = "Kongo"
    KONKANI = "Konkani"
    KOREAN = "Korean"
    KORWA = "Korwa"
    KREYOL = "Kreyol"
    KRIO = "Krio"
    KUMAONI = "Kumaoni"
    KURDISH = "Kurdish"
    KURUKH = "Kurukh"
    KWA = "Kwa"
    LADINO = "Ladino"
    LANGO = "Lango"
    LATVIAN = "Latvian"
    LAWA = "Lawa"
    LINGALA = "Lingala"
    LITHUANIAN = "Lithuanian"
    LULE = "Lule"
    LUXEMBOURGISH = "Luxembourgish"
    MAGAHI = "Magahi"
    MAITHILI = "Maithili"
    MALAY = "Malay"
    MALAYALAM = "Malayalam"
    MALAYSIAN = "Malaysian"
    MALVI = "Malvi"
    MANINKA = "Maninka"
    MANIPURI = "Manipuri"
    MANX = "Manx"
    MARATHI = "Marathi"
    MAYAN = "Mayan"
    MEDUMBA = "Medumba"
    MEMONI = "Memoni"
    MEWARI = "Mewari"
    MIZO = "Mizo"
    MONTENEGRIN = "Montenegrin"
    MWAN = "Mwan"
    MWANGA = "Mwanga"
    NDEBELE = "Ndebele"
    NEPALI = "Nepali"
    NIMADI = "Nimadi"
    ORIYA = "Oriya"
    OROMO = "Oromo"
    OVAMBO = "Ovambo"
    PAMONA = "Pamona"
    PANGASINAN = "Pangasinan"
    PASHTO = "Pashto"
    PHOENICIAN = "Phoenician"
    POLISH = "Polish"
    PORTUGUESE = "Portuguese"
    PULAAR = "Pulaar"
    PULAR = "Pular"
    PUNJABI = "Punjabi"
    QUECHA = "Quecha"
    RAJASTHANI = "Rajasthani"
    ROMANIAN = "Romanian"
    RUSSIAN = "Russian"
    SAKHA = "Sakha"
    SANGO = "Sango"
    SANTHALI = "Santhali"
    SARAIKI = "Saraiki"
    SEIM = "Seim"
    SHADING = "Shading"
    SHAMA = "Shama"
    SHAN = "Shan"
    SHONA = "Shona"
    SILESIAN = "Silesian"
    SINDHI = "Sindhi"
    SLOVAK = "Slovak"
    SLOVENE = "Slovene"
    SOGA = "Soga"
    SOGDIAN = "Sogdian"
    SOTHO = "Sotho"
    SPANISH = "Spanish"
    SUDANESE = "Sudanese"
    SUMERIAN = "Sumerian"
    SURAJPURI = "Surajpuri"
    SURIGAONON = "Surigaonon"
    SWATI = "Swati"
    SWAZI = "Swazi"
    SWEDISH = "Swedish"
    TAGALOG = "Tagalog"
    TAMIL = "Tamil"
    TAUSUG = "Tausug"
    TELUGU = "Telugu"
    TETUM = "Tetum"
    THARU = "Tharu"
    TIBETAN = "Tibetan"
    TIGRINYA = "Tigrinya"
    TRIPURI = "Tripuri"
    TSWANA = "Tswana"
    TULU = "Tulu"
    TURKISH = "Turkish"
    TUWALI = "Tuwali"
    UBI = "Ubi"
    UKRAINIAN = "Ukrainian"
    URDU = "Urdu"
    VEPS = "Veps"
    VIETNAMESE = "Vietnamese"
    WAGDI = "Wagdi"
    WAZIRI = "Waziri"
    XHOSA = "Xhosa"
    YIDDISH = "Yiddish"
    YORUBA = "Yoruba"


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
