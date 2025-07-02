from typing import (  # noqa: F401
    IO,
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Generic,
    List,
    Literal,
    Optional,
    Type,
    TypeVar,
    Union,
    overload,
)

from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from pydantic_core import ValidationError

from ._affinda_api_operations import (
    AffindaAPIOperationsMixin as AffindaAPIOperationsMixinGenerated,
)

if TYPE_CHECKING:
    import datetime  # noqa: F401

    from pydantic import BaseModel  # noqa: F401

    from .. import models as _models  # noqa: F401

    T = TypeVar("T")
    ClsType = Optional[
        Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]
    ]

    # Type for enhanced Document with parsed attribute
    TModel = TypeVar("TModel", bound="BaseModel")

    class ResultWithParsed(_models.Document, Generic[TModel]):
        parsed: TModel

    class ResultWithOptionalParsed(_models.Document, Generic[TModel]):
        parsed: Optional[TModel]


# We want to patch the generated AffindaAPIOperationsMixin class, and override its get_document method.
class AffindaAPIOperationsMixin(AffindaAPIOperationsMixinGenerated):
    @overload
    async def get_document(
        self,
        identifier,  # type: str
        format=...,  # type: Optional[Union[str, "_models.DocumentFormat"]]
        compact=...,  # type: Optional[bool]
        camel_case=...,  # type: Optional[bool]
        data_model=...,  # type: None
        ignore_validation_errors=...,  # type: bool
        **kwargs,  # type: Any
    ):
        # type: (...) -> "_models.Document"
        ...

    @overload
    async def get_document(
        self,
        identifier,  # type: str
        format=...,  # type: Optional[Union[str, "_models.DocumentFormat"]]
        compact=...,  # type: Optional[bool]
        camel_case=...,  # type: Optional[bool]
        data_model=...,  # type: Type["TModel"]
        ignore_validation_errors=...,  # type: Literal[False]
        **kwargs,  # type: Any
    ):
        # type: (...) -> "ResultWithParsed[TModel]"
        ...

    @overload
    async def get_document(
        self,
        identifier,  # type: str
        format=...,  # type: Optional[Union[str, "_models.DocumentFormat"]]
        compact=...,  # type: Optional[bool]
        camel_case=...,  # type: Optional[bool]
        data_model=...,  # type: Type["TModel"]
        ignore_validation_errors=...,  # type: Literal[True]
        **kwargs,  # type: Any
    ):
        # type: (...) -> "ResultWithOptionalParsed[TModel]"
        ...

    async def get_document(
        self,
        identifier,  # type: str
        format=None,  # type: Optional[Union[str, "_models.DocumentFormat"]]
        compact=None,  # type: Optional[bool]
        camel_case=None,  # type: Optional[bool]
        data_model=None,  # type: Optional[Type["TModel"]]
        ignore_validation_errors=False,  # type: bool
        **kwargs,  # type: Any
    ):
        # type: (...) -> Union["_models.Document", "ResultWithParsed[TModel]", "ResultWithOptionalParsed[TModel]"]
        if data_model:
            compact = True
            camel_case = False

        deserialized = await super().get_document(
            identifier,
            format=format,
            compact=compact,
            camel_case=camel_case,
            **kwargs,
        )

        if data_model:
            try:
                deserialized.parsed = data_model.model_validate(deserialized.data)
            except ValidationError:
                if not ignore_validation_errors:
                    raise
                deserialized.parsed = None

        return deserialized

    get_document.metadata = {"url": "/v3/documents/{identifier}"}  # type: ignore

    @overload
    async def create_document(
        self,
        camel_case=...,  # type: Optional[bool]
        file=...,  # type: Optional[IO]
        url=...,  # type: Optional[str]
        data=...,  # type: Any
        collection=...,  # type: Optional[str]
        document_type=...,  # type: Optional[str]
        workspace=...,  # type: Optional[str]
        wait=...,  # type: Optional[bool]
        identifier=...,  # type: Optional[str]
        custom_identifier=...,  # type: Optional[str]
        file_name=...,  # type: Optional[str]
        expiry_time=...,  # type: Optional[datetime.datetime]
        language=...,  # type: Optional[str]
        reject_duplicates=...,  # type: Optional[bool]
        region_bias=...,  # type: Optional[str]
        low_priority=...,  # type: Optional[bool]
        compact=...,  # type: Optional[bool]
        delete_after_parse=...,  # type: Optional[bool]
        enable_validation_tool=...,  # type: Optional[bool]
        use_ocr=...,  # type: Optional[bool]
        warning_messages=...,  # type: Optional[List[_models.DocumentWarning]]
        data_model=...,  # type: None
        ignore_validation_errors=...,  # type: bool
        **kwargs,  # type: Any
    ):
        # type: (...) -> "_models.Document"
        ...

    @overload
    async def create_document(
        self,
        camel_case=...,  # type: Optional[bool]
        file=...,  # type: Optional[IO]
        url=...,  # type: Optional[str]
        data=...,  # type: Any
        collection=...,  # type: Optional[str]
        document_type=...,  # type: Optional[str]
        workspace=...,  # type: Optional[str]
        wait=...,  # type: Optional[bool]
        identifier=...,  # type: Optional[str]
        custom_identifier=...,  # type: Optional[str]
        file_name=...,  # type: Optional[str]
        expiry_time=...,  # type: Optional[datetime.datetime]
        language=...,  # type: Optional[str]
        reject_duplicates=...,  # type: Optional[bool]
        region_bias=...,  # type: Optional[str]
        low_priority=...,  # type: Optional[bool]
        compact=...,  # type: Optional[bool]
        delete_after_parse=...,  # type: Optional[bool]
        enable_validation_tool=...,  # type: Optional[bool]
        use_ocr=...,  # type: Optional[bool]
        warning_messages=...,  # type: Optional[List[_models.DocumentWarning]]
        data_model=...,  # type: Type["TModel"]
        ignore_validation_errors=...,  # type: Literal[False]
        **kwargs,  # type: Any
    ):
        # type: (...) -> "ResultWithParsed[TModel]"
        ...

    @overload
    async def create_document(
        self,
        camel_case=...,  # type: Optional[bool]
        file=...,  # type: Optional[IO]
        url=...,  # type: Optional[str]
        data=...,  # type: Any
        collection=...,  # type: Optional[str]
        document_type=...,  # type: Optional[str]
        workspace=...,  # type: Optional[str]
        wait=...,  # type: Optional[bool]
        identifier=...,  # type: Optional[str]
        custom_identifier=...,  # type: Optional[str]
        file_name=...,  # type: Optional[str]
        expiry_time=...,  # type: Optional[datetime.datetime]
        language=...,  # type: Optional[str]
        reject_duplicates=...,  # type: Optional[bool]
        region_bias=...,  # type: Optional[str]
        low_priority=...,  # type: Optional[bool]
        compact=...,  # type: Optional[bool]
        delete_after_parse=...,  # type: Optional[bool]
        enable_validation_tool=...,  # type: Optional[bool]
        use_ocr=...,  # type: Optional[bool]
        warning_messages=...,  # type: Optional[List[_models.DocumentWarning]]
        data_model=...,  # type: Type["TModel"]
        ignore_validation_errors=...,  # type: Literal[True]
        **kwargs,  # type: Any
    ):
        # type: (...) -> "ResultWithOptionalParsed[TModel]"
        ...

    async def create_document(
        self,
        camel_case=None,  # type: Optional[bool]
        file=None,  # type: Optional[IO]
        url=None,  # type: Optional[str]
        data=None,  # type: Any
        collection=None,  # type: Optional[str]
        document_type=None,  # type: Optional[str]
        workspace=None,  # type: Optional[str]
        wait=True,  # type: Optional[bool]
        identifier=None,  # type: Optional[str]
        custom_identifier=None,  # type: Optional[str]
        file_name=None,  # type: Optional[str]
        expiry_time=None,  # type: Optional[datetime.datetime]
        language=None,  # type: Optional[str]
        reject_duplicates=None,  # type: Optional[bool]
        region_bias=None,  # type: Optional[str]
        low_priority=None,  # type: Optional[bool]
        compact=None,  # type: Optional[bool]
        delete_after_parse=None,  # type: Optional[bool]
        enable_validation_tool=None,  # type: Optional[bool]
        use_ocr=None,  # type: Optional[bool]
        warning_messages=None,  # type: Optional[List[_models.DocumentWarning]]
        data_model=None,  # type: Optional[Type["TModel"]]
        ignore_validation_errors=False,  # type: bool
        **kwargs,  # type: Any
    ):
        # type: (...) -> Union["_models.Document", "ResultWithParsed[TModel]", "ResultWithOptionalParsed[TModel]"]
        if data_model:
            compact = True
            camel_case = False

        deserialized = await super().create_document(
            camel_case=camel_case,
            file=file,
            url=url,
            data=data,
            collection=collection,
            document_type=document_type,
            workspace=workspace,
            wait=wait,
            identifier=identifier,
            custom_identifier=custom_identifier,
            file_name=file_name,
            expiry_time=expiry_time,
            language=language,
            reject_duplicates=reject_duplicates,
            region_bias=region_bias,
            low_priority=low_priority,
            compact=compact,
            delete_after_parse=delete_after_parse,
            enable_validation_tool=enable_validation_tool,
            use_ocr=use_ocr,
            warning_messages=warning_messages,
            **kwargs,
        )

        if data_model:
            try:
                deserialized.parsed = data_model.model_validate(deserialized.data)
            except ValidationError:
                if not ignore_validation_errors:
                    raise
                deserialized.parsed = None

        return deserialized

    create_document.metadata = {"url": "/v3/documents"}  # type: ignore

    @overload
    async def update_document(
        self,
        identifier,  # type: str
        body,  # type: _models.DocumentUpdate
        compact=...,  # type: Optional[bool]
        camel_case=...,  # type: Optional[bool]
        data_model=...,  # type: None
        ignore_validation_errors=...,  # type: bool
        **kwargs,  # type: Any
    ):
        # type: (...) -> "_models.Document"
        ...

    @overload
    async def update_document(
        self,
        identifier,  # type: str
        body,  # type: _models.DocumentUpdate
        compact=...,  # type: Optional[bool]
        camel_case=...,  # type: Optional[bool]
        data_model=...,  # type: Type["TModel"]
        ignore_validation_errors=...,  # type: Literal[False]
        **kwargs,  # type: Any
    ):
        # type: (...) -> "ResultWithParsed[TModel]"
        ...

    @overload
    async def update_document(
        self,
        identifier,  # type: str
        body,  # type: _models.DocumentUpdate
        compact=...,  # type: Optional[bool]
        camel_case=...,  # type: Optional[bool]
        data_model=...,  # type: Type["TModel"]
        ignore_validation_errors=...,  # type: Literal[True]
        **kwargs,  # type: Any
    ):
        # type: (...) -> "ResultWithOptionalParsed[TModel]"
        ...

    async def update_document(
        self,
        identifier,  # type: str
        body,  # type: _models.DocumentUpdate
        compact=None,  # type: Optional[bool]
        camel_case=None,  # type: Optional[bool]
        data_model=None,  # type: Optional[Type["TModel"]]
        ignore_validation_errors=False,  # type: bool
        **kwargs,  # type: Any
    ):
        # type: (...) -> Union["_models.Document", "ResultWithParsed[TModel]", "ResultWithOptionalParsed[TModel]"]
        if data_model:
            compact = True
            camel_case = False

        deserialized = await super().update_document(
            identifier,
            body,
            compact=compact,
            camel_case=camel_case,
            **kwargs,
        )

        if data_model:
            try:
                deserialized.parsed = data_model.model_validate(deserialized.data)
            except ValidationError:
                if not ignore_validation_errors:
                    raise
                deserialized.parsed = None

        return deserialized

    update_document.metadata = {"url": "/v3/documents/{identifier}"}  # type: ignore


__all__ = [
    "AffindaAPIOperationsMixin",
]


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
