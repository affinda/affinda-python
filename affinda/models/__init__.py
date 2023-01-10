# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.3, generator: @autorest/python@5.16.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Accreditation
    from ._models_py3 import Annotation
    from ._models_py3 import Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1
    from ._models_py3 import Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1
    from ._models_py3 import Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1
    from ._models_py3 import (
        Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1,
    )
    from ._models_py3 import (
        Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1,
    )
    from ._models_py3 import Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1
    from ._models_py3 import (
        Components1Bq3Q31SchemasJobdescriptionsearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1,
    )
    from ._models_py3 import Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1
    from ._models_py3 import Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1
    from ._models_py3 import Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1
    from ._models_py3 import Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1
    from ._models_py3 import Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1
    from ._models_py3 import Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1
    from ._models_py3 import Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1
    from ._models_py3 import (
        Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1,
    )
    from ._models_py3 import (
        Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification,
    )
    from ._models_py3 import Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1
    from ._models_py3 import Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1
    from ._models_py3 import Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1
    from ._models_py3 import Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1
    from ._models_py3 import Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1
    from ._models_py3 import Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1
    from ._models_py3 import (
        Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1,
    )
    from ._models_py3 import Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1
    from ._models_py3 import Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1
    from ._models_py3 import Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1
    from ._models_py3 import ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1
    from ._models_py3 import (
        ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1,
    )
    from ._models_py3 import ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1
    from ._models_py3 import ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1
    from ._models_py3 import ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1
    from ._models_py3 import (
        ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1,
    )
    from ._models_py3 import (
        ComponentsK7P1F5SchemasResumesearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1,
    )
    from ._models_py3 import (
        ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1,
    )
    from ._models_py3 import (
        ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties,
    )
    from ._models_py3 import (
        ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1,
    )
    from ._models_py3 import ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1
    from ._models_py3 import ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1
    from ._models_py3 import DateAnnotation
    from ._models_py3 import Education
    from ._models_py3 import EducationDates
    from ._models_py3 import EducationGrade
    from ._models_py3 import EducationSearchScoreComponent
    from ._models_py3 import EnumAnnotationSerializer
    from ._models_py3 import Error
    from ._models_py3 import ExpectedRemunerationAnnotation
    from ._models_py3 import ExpectedRemunerationAnnotationParsed
    from ._models_py3 import ExperienceSearchScoreComponent
    from ._models_py3 import Get200ApplicationJsonPropertiesItemsItem
    from ._models_py3 import GetAllDocumentsResults
    from ._models_py3 import GetAllInvoicesResults
    from ._models_py3 import GetAllJobDescriptionsResults
    from ._models_py3 import IndexRequestBody
    from ._models_py3 import Invoice
    from ._models_py3 import InvoiceData
    from ._models_py3 import InvoiceDataBankAccountNumber
    from ._models_py3 import InvoiceDataBankBsb
    from ._models_py3 import InvoiceDataBankIban
    from ._models_py3 import InvoiceDataBankSortCode
    from ._models_py3 import InvoiceDataBankSwift
    from ._models_py3 import InvoiceDataBpayBillerCode
    from ._models_py3 import InvoiceDataBpayReference
    from ._models_py3 import InvoiceDataCustomerBusinessNumber
    from ._models_py3 import InvoiceDataCustomerCompanyName
    from ._models_py3 import InvoiceDataCustomerContactName
    from ._models_py3 import InvoiceDataCustomerEmail
    from ._models_py3 import InvoiceDataCustomerNumber
    from ._models_py3 import InvoiceDataCustomerPhoneNumber
    from ._models_py3 import InvoiceDataCustomerVat
    from ._models_py3 import InvoiceDataInvoiceNumber
    from ._models_py3 import InvoiceDataInvoicePurchaseOrderNumber
    from ._models_py3 import InvoiceDataPaymentAmountBase
    from ._models_py3 import InvoiceDataPaymentAmountDue
    from ._models_py3 import InvoiceDataPaymentAmountPaid
    from ._models_py3 import InvoiceDataPaymentAmountTax
    from ._models_py3 import InvoiceDataPaymentAmountTotal
    from ._models_py3 import InvoiceDataPaymentReference
    from ._models_py3 import InvoiceDataSupplierBusinessNumber
    from ._models_py3 import InvoiceDataSupplierCompanyName
    from ._models_py3 import InvoiceDataSupplierEmail
    from ._models_py3 import InvoiceDataSupplierFax
    from ._models_py3 import InvoiceDataSupplierPhoneNumber
    from ._models_py3 import InvoiceDataSupplierVat
    from ._models_py3 import InvoiceDataSupplierWebsite
    from ._models_py3 import InvoiceDataTablesItem
    from ._models_py3 import InvoiceRequestBody
    from ._models_py3 import JobDescription
    from ._models_py3 import JobDescriptionData
    from ._models_py3 import JobDescriptionRequestBody
    from ._models_py3 import JobDescriptionSearch
    from ._models_py3 import JobDescriptionSearchConfig
    from ._models_py3 import JobDescriptionSearchConfigActionsItem
    from ._models_py3 import JobDescriptionSearchDetail
    from ._models_py3 import JobDescriptionSearchDetailEducation
    from ._models_py3 import JobDescriptionSearchDetailEducationMissing
    from ._models_py3 import JobDescriptionSearchDetailEducationValue
    from ._models_py3 import JobDescriptionSearchDetailExperience
    from ._models_py3 import JobDescriptionSearchDetailJobTitle
    from ._models_py3 import JobDescriptionSearchDetailJobTitleValue
    from ._models_py3 import JobDescriptionSearchDetailLanguages
    from ._models_py3 import JobDescriptionSearchDetailLanguagesValueItem
    from ._models_py3 import JobDescriptionSearchDetailLocation
    from ._models_py3 import JobDescriptionSearchDetailLocationValue
    from ._models_py3 import JobDescriptionSearchDetailManagementLevel
    from ._models_py3 import JobDescriptionSearchDetailOccupationGroup
    from ._models_py3 import JobDescriptionSearchDetailOccupationGroupValueItem
    from ._models_py3 import JobDescriptionSearchDetailSearchExpression
    from ._models_py3 import JobDescriptionSearchDetailSkills
    from ._models_py3 import JobDescriptionSearchDetailSkillsValueItem
    from ._models_py3 import JobDescriptionSearchEmbed
    from ._models_py3 import JobDescriptionSearchParameters
    from ._models_py3 import JobDescriptionSearchResult
    from ._models_py3 import JobTitleAnnotation
    from ._models_py3 import JobTitleAnnotationParsed
    from ._models_py3 import JobTitleAnnotationParsedClassification
    from ._models_py3 import JobTitleSearchScoreComponent
    from ._models_py3 import LanguageAnnotation
    from ._models_py3 import LanguagesSearchScoreComponent
    from ._models_py3 import Location
    from ._models_py3 import LocationAnnotation
    from ._models_py3 import LocationSearchScoreComponent
    from ._models_py3 import ManagementLevelSearchScoreComponent
    from ._models_py3 import Meta
    from ._models_py3 import OccupationGroup
    from ._models_py3 import OccupationGroupSearchScoreComponent
    from ._models_py3 import PageMeta
    from ._models_py3 import Paths1Mc0Je6IndexPostResponses201ContentApplicationJsonSchema
    from ._models_py3 import Paths1Y6A2MfUsersPostResponses201ContentApplicationJsonSchemaAllof1
    from ._models_py3 import (
        Paths2T1Oc0ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema,
    )
    from ._models_py3 import Paths6Pypg5IndexGetResponses200ContentApplicationJsonSchema
    from ._models_py3 import (
        PathsCoo0XpIndexNameDocumentsPostResponses201ContentApplicationJsonSchema,
    )
    from ._models_py3 import (
        PathsFqn8P8JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema,
    )
    from ._models_py3 import (
        PathsGpptmIndexNameDocumentsPostRequestbodyContentApplicationJsonSchema,
    )
    from ._models_py3 import (
        PathsHryo8IndexNameDocumentsGetResponses200ContentApplicationJsonSchemaPropertiesResultsItems,
    )
    from ._models_py3 import (
        PathsRvverlIndexNameDocumentsGetResponses200ContentApplicationJsonSchema,
    )
    from ._models_py3 import PathsTop5ZkUsersPostResponses201ContentApplicationJsonSchema
    from ._models_py3 import PathsWjaaeuUsersGetResponses200ContentApplicationJsonSchema
    from ._models_py3 import Rectangle
    from ._models_py3 import RedactedResume
    from ._models_py3 import RedactedResumeData
    from ._models_py3 import RedactedResumeRequestBody
    from ._models_py3 import RequestError
    from ._models_py3 import RequestErrorErrorsItem
    from ._models_py3 import Resume
    from ._models_py3 import ResumeData
    from ._models_py3 import ResumeDataName
    from ._models_py3 import ResumeDataRefereesItem
    from ._models_py3 import ResumeDataSectionsItem
    from ._models_py3 import ResumeDataSkillsItem
    from ._models_py3 import ResumeDataSkillsPropertiesItemsItem
    from ._models_py3 import ResumeDataWorkExperienceItem
    from ._models_py3 import ResumeDataWorkExperienceItemDates
    from ._models_py3 import ResumeDataWorkExperienceItemOccupation
    from ._models_py3 import ResumeRequestBody
    from ._models_py3 import ResumeSearch
    from ._models_py3 import ResumeSearchConfig
    from ._models_py3 import ResumeSearchDetail
    from ._models_py3 import ResumeSearchDetailEducation
    from ._models_py3 import ResumeSearchDetailEducationMissing
    from ._models_py3 import ResumeSearchDetailEducationValueItem
    from ._models_py3 import ResumeSearchDetailExperience
    from ._models_py3 import ResumeSearchDetailJobTitle
    from ._models_py3 import ResumeSearchDetailJobTitleValueItem
    from ._models_py3 import ResumeSearchDetailLanguages
    from ._models_py3 import ResumeSearchDetailLanguagesValueItem
    from ._models_py3 import ResumeSearchDetailLocation
    from ._models_py3 import ResumeSearchDetailLocationValue
    from ._models_py3 import ResumeSearchDetailManagementLevel
    from ._models_py3 import ResumeSearchDetailOccupationGroup
    from ._models_py3 import ResumeSearchDetailOccupationGroupValueItem
    from ._models_py3 import ResumeSearchDetailSearchExpression
    from ._models_py3 import ResumeSearchDetailSkills
    from ._models_py3 import ResumeSearchDetailSkillsValueItem
    from ._models_py3 import ResumeSearchEmbed
    from ._models_py3 import ResumeSearchMatch
    from ._models_py3 import ResumeSearchMatchDetails
    from ._models_py3 import ResumeSearchParameters
    from ._models_py3 import ResumeSearchParametersCustomData
    from ._models_py3 import ResumeSearchParametersLocation
    from ._models_py3 import ResumeSearchParametersLocationCoordinates
    from ._models_py3 import ResumeSearchParametersSkill
    from ._models_py3 import ResumeSearchResult
    from ._models_py3 import ResumeSkill
    from ._models_py3 import ResumeSkillSourcesItem
    from ._models_py3 import RowAnnotation
    from ._models_py3 import SearchExpressionSearchScoreComponent
    from ._models_py3 import SkillAnnotation
    from ._models_py3 import SkillsSearchScoreComponent
    from ._models_py3 import SplitRelation
    from ._models_py3 import TextAnnotation
    from ._models_py3 import User
    from ._models_py3 import YearsExperienceAnnotation
    from ._models_py3 import YearsExperienceAnnotationParsed
except (SyntaxError, ImportError):
    from ._models import Accreditation  # type: ignore
    from ._models import Annotation  # type: ignore
    from ._models import Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1  # type: ignore
    from ._models import Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1  # type: ignore
    from ._models import Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1  # type: ignore
    from ._models import Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1  # type: ignore
    from ._models import Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1  # type: ignore
    from ._models import Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1  # type: ignore
    from ._models import Components1Bq3Q31SchemasJobdescriptionsearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1  # type: ignore
    from ._models import Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1  # type: ignore
    from ._models import Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1  # type: ignore
    from ._models import Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1  # type: ignore
    from ._models import Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1  # type: ignore
    from ._models import Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1  # type: ignore
    from ._models import Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1  # type: ignore
    from ._models import Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1  # type: ignore
    from ._models import Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1  # type: ignore
    from ._models import Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification  # type: ignore
    from ._models import Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1  # type: ignore
    from ._models import Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1  # type: ignore
    from ._models import Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1  # type: ignore
    from ._models import Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1  # type: ignore
    from ._models import Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1  # type: ignore
    from ._models import Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1  # type: ignore
    from ._models import Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1  # type: ignore
    from ._models import Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1  # type: ignore
    from ._models import Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1  # type: ignore
    from ._models import Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1  # type: ignore
    from ._models import ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1  # type: ignore
    from ._models import ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1  # type: ignore
    from ._models import ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1  # type: ignore
    from ._models import ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1  # type: ignore
    from ._models import ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1  # type: ignore
    from ._models import ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1  # type: ignore
    from ._models import ComponentsK7P1F5SchemasResumesearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1  # type: ignore
    from ._models import ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1  # type: ignore
    from ._models import ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties  # type: ignore
    from ._models import ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1  # type: ignore
    from ._models import ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1  # type: ignore
    from ._models import ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1  # type: ignore
    from ._models import DateAnnotation  # type: ignore
    from ._models import Education  # type: ignore
    from ._models import EducationDates  # type: ignore
    from ._models import EducationGrade  # type: ignore
    from ._models import EducationSearchScoreComponent  # type: ignore
    from ._models import EnumAnnotationSerializer  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import ExpectedRemunerationAnnotation  # type: ignore
    from ._models import ExpectedRemunerationAnnotationParsed  # type: ignore
    from ._models import ExperienceSearchScoreComponent  # type: ignore
    from ._models import Get200ApplicationJsonPropertiesItemsItem  # type: ignore
    from ._models import GetAllDocumentsResults  # type: ignore
    from ._models import GetAllInvoicesResults  # type: ignore
    from ._models import GetAllJobDescriptionsResults  # type: ignore
    from ._models import IndexRequestBody  # type: ignore
    from ._models import Invoice  # type: ignore
    from ._models import InvoiceData  # type: ignore
    from ._models import InvoiceDataBankAccountNumber  # type: ignore
    from ._models import InvoiceDataBankBsb  # type: ignore
    from ._models import InvoiceDataBankIban  # type: ignore
    from ._models import InvoiceDataBankSortCode  # type: ignore
    from ._models import InvoiceDataBankSwift  # type: ignore
    from ._models import InvoiceDataBpayBillerCode  # type: ignore
    from ._models import InvoiceDataBpayReference  # type: ignore
    from ._models import InvoiceDataCustomerBusinessNumber  # type: ignore
    from ._models import InvoiceDataCustomerCompanyName  # type: ignore
    from ._models import InvoiceDataCustomerContactName  # type: ignore
    from ._models import InvoiceDataCustomerEmail  # type: ignore
    from ._models import InvoiceDataCustomerNumber  # type: ignore
    from ._models import InvoiceDataCustomerPhoneNumber  # type: ignore
    from ._models import InvoiceDataCustomerVat  # type: ignore
    from ._models import InvoiceDataInvoiceNumber  # type: ignore
    from ._models import InvoiceDataInvoicePurchaseOrderNumber  # type: ignore
    from ._models import InvoiceDataPaymentAmountBase  # type: ignore
    from ._models import InvoiceDataPaymentAmountDue  # type: ignore
    from ._models import InvoiceDataPaymentAmountPaid  # type: ignore
    from ._models import InvoiceDataPaymentAmountTax  # type: ignore
    from ._models import InvoiceDataPaymentAmountTotal  # type: ignore
    from ._models import InvoiceDataPaymentReference  # type: ignore
    from ._models import InvoiceDataSupplierBusinessNumber  # type: ignore
    from ._models import InvoiceDataSupplierCompanyName  # type: ignore
    from ._models import InvoiceDataSupplierEmail  # type: ignore
    from ._models import InvoiceDataSupplierFax  # type: ignore
    from ._models import InvoiceDataSupplierPhoneNumber  # type: ignore
    from ._models import InvoiceDataSupplierVat  # type: ignore
    from ._models import InvoiceDataSupplierWebsite  # type: ignore
    from ._models import InvoiceDataTablesItem  # type: ignore
    from ._models import InvoiceRequestBody  # type: ignore
    from ._models import JobDescription  # type: ignore
    from ._models import JobDescriptionData  # type: ignore
    from ._models import JobDescriptionRequestBody  # type: ignore
    from ._models import JobDescriptionSearch  # type: ignore
    from ._models import JobDescriptionSearchConfig  # type: ignore
    from ._models import JobDescriptionSearchConfigActionsItem  # type: ignore
    from ._models import JobDescriptionSearchDetail  # type: ignore
    from ._models import JobDescriptionSearchDetailEducation  # type: ignore
    from ._models import JobDescriptionSearchDetailEducationMissing  # type: ignore
    from ._models import JobDescriptionSearchDetailEducationValue  # type: ignore
    from ._models import JobDescriptionSearchDetailExperience  # type: ignore
    from ._models import JobDescriptionSearchDetailJobTitle  # type: ignore
    from ._models import JobDescriptionSearchDetailJobTitleValue  # type: ignore
    from ._models import JobDescriptionSearchDetailLanguages  # type: ignore
    from ._models import JobDescriptionSearchDetailLanguagesValueItem  # type: ignore
    from ._models import JobDescriptionSearchDetailLocation  # type: ignore
    from ._models import JobDescriptionSearchDetailLocationValue  # type: ignore
    from ._models import JobDescriptionSearchDetailManagementLevel  # type: ignore
    from ._models import JobDescriptionSearchDetailOccupationGroup  # type: ignore
    from ._models import JobDescriptionSearchDetailOccupationGroupValueItem  # type: ignore
    from ._models import JobDescriptionSearchDetailSearchExpression  # type: ignore
    from ._models import JobDescriptionSearchDetailSkills  # type: ignore
    from ._models import JobDescriptionSearchDetailSkillsValueItem  # type: ignore
    from ._models import JobDescriptionSearchEmbed  # type: ignore
    from ._models import JobDescriptionSearchParameters  # type: ignore
    from ._models import JobDescriptionSearchResult  # type: ignore
    from ._models import JobTitleAnnotation  # type: ignore
    from ._models import JobTitleAnnotationParsed  # type: ignore
    from ._models import JobTitleAnnotationParsedClassification  # type: ignore
    from ._models import JobTitleSearchScoreComponent  # type: ignore
    from ._models import LanguageAnnotation  # type: ignore
    from ._models import LanguagesSearchScoreComponent  # type: ignore
    from ._models import Location  # type: ignore
    from ._models import LocationAnnotation  # type: ignore
    from ._models import LocationSearchScoreComponent  # type: ignore
    from ._models import ManagementLevelSearchScoreComponent  # type: ignore
    from ._models import Meta  # type: ignore
    from ._models import OccupationGroup  # type: ignore
    from ._models import OccupationGroupSearchScoreComponent  # type: ignore
    from ._models import PageMeta  # type: ignore
    from ._models import Paths1Mc0Je6IndexPostResponses201ContentApplicationJsonSchema  # type: ignore
    from ._models import Paths1Y6A2MfUsersPostResponses201ContentApplicationJsonSchemaAllof1  # type: ignore
    from ._models import Paths2T1Oc0ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema  # type: ignore
    from ._models import Paths6Pypg5IndexGetResponses200ContentApplicationJsonSchema  # type: ignore
    from ._models import PathsCoo0XpIndexNameDocumentsPostResponses201ContentApplicationJsonSchema  # type: ignore
    from ._models import PathsFqn8P8JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema  # type: ignore
    from ._models import PathsGpptmIndexNameDocumentsPostRequestbodyContentApplicationJsonSchema  # type: ignore
    from ._models import PathsHryo8IndexNameDocumentsGetResponses200ContentApplicationJsonSchemaPropertiesResultsItems  # type: ignore
    from ._models import PathsRvverlIndexNameDocumentsGetResponses200ContentApplicationJsonSchema  # type: ignore
    from ._models import PathsTop5ZkUsersPostResponses201ContentApplicationJsonSchema  # type: ignore
    from ._models import PathsWjaaeuUsersGetResponses200ContentApplicationJsonSchema  # type: ignore
    from ._models import Rectangle  # type: ignore
    from ._models import RedactedResume  # type: ignore
    from ._models import RedactedResumeData  # type: ignore
    from ._models import RedactedResumeRequestBody  # type: ignore
    from ._models import RequestError  # type: ignore
    from ._models import RequestErrorErrorsItem  # type: ignore
    from ._models import Resume  # type: ignore
    from ._models import ResumeData  # type: ignore
    from ._models import ResumeDataName  # type: ignore
    from ._models import ResumeDataRefereesItem  # type: ignore
    from ._models import ResumeDataSectionsItem  # type: ignore
    from ._models import ResumeDataSkillsItem  # type: ignore
    from ._models import ResumeDataSkillsPropertiesItemsItem  # type: ignore
    from ._models import ResumeDataWorkExperienceItem  # type: ignore
    from ._models import ResumeDataWorkExperienceItemDates  # type: ignore
    from ._models import ResumeDataWorkExperienceItemOccupation  # type: ignore
    from ._models import ResumeRequestBody  # type: ignore
    from ._models import ResumeSearch  # type: ignore
    from ._models import ResumeSearchConfig  # type: ignore
    from ._models import ResumeSearchDetail  # type: ignore
    from ._models import ResumeSearchDetailEducation  # type: ignore
    from ._models import ResumeSearchDetailEducationMissing  # type: ignore
    from ._models import ResumeSearchDetailEducationValueItem  # type: ignore
    from ._models import ResumeSearchDetailExperience  # type: ignore
    from ._models import ResumeSearchDetailJobTitle  # type: ignore
    from ._models import ResumeSearchDetailJobTitleValueItem  # type: ignore
    from ._models import ResumeSearchDetailLanguages  # type: ignore
    from ._models import ResumeSearchDetailLanguagesValueItem  # type: ignore
    from ._models import ResumeSearchDetailLocation  # type: ignore
    from ._models import ResumeSearchDetailLocationValue  # type: ignore
    from ._models import ResumeSearchDetailManagementLevel  # type: ignore
    from ._models import ResumeSearchDetailOccupationGroup  # type: ignore
    from ._models import ResumeSearchDetailOccupationGroupValueItem  # type: ignore
    from ._models import ResumeSearchDetailSearchExpression  # type: ignore
    from ._models import ResumeSearchDetailSkills  # type: ignore
    from ._models import ResumeSearchDetailSkillsValueItem  # type: ignore
    from ._models import ResumeSearchEmbed  # type: ignore
    from ._models import ResumeSearchMatch  # type: ignore
    from ._models import ResumeSearchMatchDetails  # type: ignore
    from ._models import ResumeSearchParameters  # type: ignore
    from ._models import ResumeSearchParametersCustomData  # type: ignore
    from ._models import ResumeSearchParametersLocation  # type: ignore
    from ._models import ResumeSearchParametersLocationCoordinates  # type: ignore
    from ._models import ResumeSearchParametersSkill  # type: ignore
    from ._models import ResumeSearchResult  # type: ignore
    from ._models import ResumeSkill  # type: ignore
    from ._models import ResumeSkillSourcesItem  # type: ignore
    from ._models import RowAnnotation  # type: ignore
    from ._models import SearchExpressionSearchScoreComponent  # type: ignore
    from ._models import SkillAnnotation  # type: ignore
    from ._models import SkillsSearchScoreComponent  # type: ignore
    from ._models import SplitRelation  # type: ignore
    from ._models import TextAnnotation  # type: ignore
    from ._models import User  # type: ignore
    from ._models import YearsExperienceAnnotation  # type: ignore
    from ._models import YearsExperienceAnnotationParsed  # type: ignore

from ._affinda_api_enums import (
    EducationLevel,
    Enum2,
    Enum5,
    GetResponses200ContentApplicationJsonSchemaResultsItemDocumentType,
    ManagementLevel,
    PostContentSchemaDocumentType,
    ResumeSearchParametersCustomDataFilterType,
    ResumeSkillSourcesItemSection,
    SearchLocationUnit,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Accreditation",
    "Annotation",
    "Components105Abr3SchemasInvoicedataPropertiesCustomernumberAllof1",
    "Components10Thcs2SchemasInvoicedataPropertiesSupplieremailAllof1",
    "Components1127QwqSchemasInvoicedataPropertiesBankibanAllof1",
    "Components158Lya5SchemasInvoicedataPropertiesCustomerbusinessnumberAllof1",
    "Components159Ji55SchemasResumesearchdetailPropertiesLanguagesPropertiesValueItemsAllof1",
    "Components17JmwpjSchemasInvoicedataPropertiesSupplierwebsiteAllof1",
    "Components1Bq3Q31SchemasJobdescriptionsearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1",
    "Components1Fe3VqtSchemasInvoicedataPropertiesSupplierfaxAllof1",
    "Components1Hr2XldSchemasInvoicedataPropertiesSupplierphonenumberAllof1",
    "Components1O8OpknSchemasInvoicedataPropertiesCustomercompanynameAllof1",
    "Components1P4Fl61SchemasInvoicedataPropertiesSuppliercompanynameAllof1",
    "Components1QdassaSchemasInvoicedataPropertiesBanksortcodeAllof1",
    "Components1Roa72HSchemasInvoicedataPropertiesBankswiftAllof1",
    "Components1RrxgkvSchemasInvoicedataPropertiesBankbsbAllof1",
    "Components1TlnsonSchemasJobdescriptionsearchdetailPropertiesLocationPropertiesValueAllof1",
    "Components1TryetgSchemasResumedataPropertiesWorkexperienceItemsPropertiesOccupationPropertiesClassification",
    "Components1Vvtu5NSchemasInvoicedataPropertiesPaymentamountpaidAllof1",
    "Components1W3SqeuSchemasInvoicedataPropertiesPaymentamountbaseAllof1",
    "Components1Y7HcurSchemasInvoicedataPropertiesCustomeremailAllof1",
    "Components1YsiqwnSchemasInvoicedataPropertiesCustomerphonenumberAllof1",
    "Components2XnshtSchemasInvoicedataPropertiesPaymentreferenceAllof1",
    "Components4A2PzvSchemasInvoicedataPropertiesPaymentamounttotalAllof1",
    "Components5D6NjySchemasInvoicedataPropertiesSupplierbusinessnumberAllof1",
    "Components5Rnu7ESchemasInvoicedataPropertiesInvoicenumberAllof1",
    "Components6Zm20BSchemasInvoicedataPropertiesPaymentamounttaxAllof1",
    "Components74A7C1SchemasInvoicedataPropertiesBankaccountnumberAllof1",
    "ComponentsA69Bd0SchemasInvoicedataPropertiesBpaybillercodeAllof1",
    "ComponentsAq75Z8SchemasInvoicedataPropertiesInvoicepurchaseordernumberAllof1",
    "ComponentsB3U7OaSchemasInvoicedataPropertiesSuppliervatAllof1",
    "ComponentsBeazccSchemasInvoicedataPropertiesCustomervatAllof1",
    "ComponentsEtsq6MSchemasInvoicedataPropertiesPaymentamountdueAllof1",
    "ComponentsH65QjbSchemasResumesearchdetailPropertiesSkillsPropertiesValueItemsAllof1",
    "ComponentsK7P1F5SchemasResumesearchdetailPropertiesOccupationgroupPropertiesValueItemsAllof1",
    "ComponentsN9ShogSchemasResumesearchdetailPropertiesLocationPropertiesValueAllof1",
    "ComponentsNqbw24SchemasCustomdatasearchscorecomponentAdditionalproperties",
    "ComponentsSxu0N3SchemasResumesearchdetailPropertiesEducationPropertiesValueItemsAllof1",
    "ComponentsW32SuaSchemasInvoicedataPropertiesBpayreferenceAllof1",
    "ComponentsWv2QrxSchemasInvoicedataPropertiesCustomercontactnameAllof1",
    "DateAnnotation",
    "Education",
    "EducationDates",
    "EducationGrade",
    "EducationSearchScoreComponent",
    "EnumAnnotationSerializer",
    "Error",
    "ExpectedRemunerationAnnotation",
    "ExpectedRemunerationAnnotationParsed",
    "ExperienceSearchScoreComponent",
    "Get200ApplicationJsonPropertiesItemsItem",
    "GetAllDocumentsResults",
    "GetAllInvoicesResults",
    "GetAllJobDescriptionsResults",
    "IndexRequestBody",
    "Invoice",
    "InvoiceData",
    "InvoiceDataBankAccountNumber",
    "InvoiceDataBankBsb",
    "InvoiceDataBankIban",
    "InvoiceDataBankSortCode",
    "InvoiceDataBankSwift",
    "InvoiceDataBpayBillerCode",
    "InvoiceDataBpayReference",
    "InvoiceDataCustomerBusinessNumber",
    "InvoiceDataCustomerCompanyName",
    "InvoiceDataCustomerContactName",
    "InvoiceDataCustomerEmail",
    "InvoiceDataCustomerNumber",
    "InvoiceDataCustomerPhoneNumber",
    "InvoiceDataCustomerVat",
    "InvoiceDataInvoiceNumber",
    "InvoiceDataInvoicePurchaseOrderNumber",
    "InvoiceDataPaymentAmountBase",
    "InvoiceDataPaymentAmountDue",
    "InvoiceDataPaymentAmountPaid",
    "InvoiceDataPaymentAmountTax",
    "InvoiceDataPaymentAmountTotal",
    "InvoiceDataPaymentReference",
    "InvoiceDataSupplierBusinessNumber",
    "InvoiceDataSupplierCompanyName",
    "InvoiceDataSupplierEmail",
    "InvoiceDataSupplierFax",
    "InvoiceDataSupplierPhoneNumber",
    "InvoiceDataSupplierVat",
    "InvoiceDataSupplierWebsite",
    "InvoiceDataTablesItem",
    "InvoiceRequestBody",
    "JobDescription",
    "JobDescriptionData",
    "JobDescriptionRequestBody",
    "JobDescriptionSearch",
    "JobDescriptionSearchConfig",
    "JobDescriptionSearchConfigActionsItem",
    "JobDescriptionSearchDetail",
    "JobDescriptionSearchDetailEducation",
    "JobDescriptionSearchDetailEducationMissing",
    "JobDescriptionSearchDetailEducationValue",
    "JobDescriptionSearchDetailExperience",
    "JobDescriptionSearchDetailJobTitle",
    "JobDescriptionSearchDetailJobTitleValue",
    "JobDescriptionSearchDetailLanguages",
    "JobDescriptionSearchDetailLanguagesValueItem",
    "JobDescriptionSearchDetailLocation",
    "JobDescriptionSearchDetailLocationValue",
    "JobDescriptionSearchDetailManagementLevel",
    "JobDescriptionSearchDetailOccupationGroup",
    "JobDescriptionSearchDetailOccupationGroupValueItem",
    "JobDescriptionSearchDetailSearchExpression",
    "JobDescriptionSearchDetailSkills",
    "JobDescriptionSearchDetailSkillsValueItem",
    "JobDescriptionSearchEmbed",
    "JobDescriptionSearchParameters",
    "JobDescriptionSearchResult",
    "JobTitleAnnotation",
    "JobTitleAnnotationParsed",
    "JobTitleAnnotationParsedClassification",
    "JobTitleSearchScoreComponent",
    "LanguageAnnotation",
    "LanguagesSearchScoreComponent",
    "Location",
    "LocationAnnotation",
    "LocationSearchScoreComponent",
    "ManagementLevelSearchScoreComponent",
    "Meta",
    "OccupationGroup",
    "OccupationGroupSearchScoreComponent",
    "PageMeta",
    "Paths1Mc0Je6IndexPostResponses201ContentApplicationJsonSchema",
    "Paths1Y6A2MfUsersPostResponses201ContentApplicationJsonSchemaAllof1",
    "Paths2T1Oc0ResumeSearchEmbedPostRequestbodyContentApplicationJsonSchema",
    "Paths6Pypg5IndexGetResponses200ContentApplicationJsonSchema",
    "PathsCoo0XpIndexNameDocumentsPostResponses201ContentApplicationJsonSchema",
    "PathsFqn8P8JobDescriptionSearchEmbedPostRequestbodyContentApplicationJsonSchema",
    "PathsGpptmIndexNameDocumentsPostRequestbodyContentApplicationJsonSchema",
    "PathsHryo8IndexNameDocumentsGetResponses200ContentApplicationJsonSchemaPropertiesResultsItems",
    "PathsRvverlIndexNameDocumentsGetResponses200ContentApplicationJsonSchema",
    "PathsTop5ZkUsersPostResponses201ContentApplicationJsonSchema",
    "PathsWjaaeuUsersGetResponses200ContentApplicationJsonSchema",
    "Rectangle",
    "RedactedResume",
    "RedactedResumeData",
    "RedactedResumeRequestBody",
    "RequestError",
    "RequestErrorErrorsItem",
    "Resume",
    "ResumeData",
    "ResumeDataName",
    "ResumeDataRefereesItem",
    "ResumeDataSectionsItem",
    "ResumeDataSkillsItem",
    "ResumeDataSkillsPropertiesItemsItem",
    "ResumeDataWorkExperienceItem",
    "ResumeDataWorkExperienceItemDates",
    "ResumeDataWorkExperienceItemOccupation",
    "ResumeRequestBody",
    "ResumeSearch",
    "ResumeSearchConfig",
    "ResumeSearchDetail",
    "ResumeSearchDetailEducation",
    "ResumeSearchDetailEducationMissing",
    "ResumeSearchDetailEducationValueItem",
    "ResumeSearchDetailExperience",
    "ResumeSearchDetailJobTitle",
    "ResumeSearchDetailJobTitleValueItem",
    "ResumeSearchDetailLanguages",
    "ResumeSearchDetailLanguagesValueItem",
    "ResumeSearchDetailLocation",
    "ResumeSearchDetailLocationValue",
    "ResumeSearchDetailManagementLevel",
    "ResumeSearchDetailOccupationGroup",
    "ResumeSearchDetailOccupationGroupValueItem",
    "ResumeSearchDetailSearchExpression",
    "ResumeSearchDetailSkills",
    "ResumeSearchDetailSkillsValueItem",
    "ResumeSearchEmbed",
    "ResumeSearchMatch",
    "ResumeSearchMatchDetails",
    "ResumeSearchParameters",
    "ResumeSearchParametersCustomData",
    "ResumeSearchParametersLocation",
    "ResumeSearchParametersLocationCoordinates",
    "ResumeSearchParametersSkill",
    "ResumeSearchResult",
    "ResumeSkill",
    "ResumeSkillSourcesItem",
    "RowAnnotation",
    "SearchExpressionSearchScoreComponent",
    "SkillAnnotation",
    "SkillsSearchScoreComponent",
    "SplitRelation",
    "TextAnnotation",
    "User",
    "YearsExperienceAnnotation",
    "YearsExperienceAnnotationParsed",
    "EducationLevel",
    "Enum2",
    "Enum5",
    "GetResponses200ContentApplicationJsonSchemaResultsItemDocumentType",
    "ManagementLevel",
    "PostContentSchemaDocumentType",
    "ResumeSearchParametersCustomDataFilterType",
    "ResumeSkillSourcesItemSection",
    "SearchLocationUnit",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
