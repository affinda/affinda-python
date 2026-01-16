from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Generic,
    Optional,
    Type,  # noqa: F401
    TypeVar,
    overload,
)

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from pydantic_core import ValidationError

from .. import models as _models  # noqa: F401
from .._vendor import _convert_request  # noqa: TID252
from ._affinda_api_operations import (
    AffindaAPIOperationsMixin as AffindaAPIOperationsMixinGenerated,
)
from ._affinda_api_operations import build_get_document_request

if TYPE_CHECKING:
    import datetime  # noqa: F401

    from pydantic import BaseModel  # noqa: F401

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


class AffindaAPIOperationsMixin(AffindaAPIOperationsMixinGenerated):
    @overload
    def get_document(
        self,
        identifier,  # type: str
        format=...,  # type: Optional[Union[str, "_models.DocumentFormat"]]
        compact=...,  # type: Optional[bool]
        data_model=...,  # type: None
        ignore_validation_errors=...,  # type: bool
        **kwargs,  # type: Any
    ):
        # type: (...) -> "_models.Document"
        ...

    @overload
    def get_document(
        self,
        identifier,  # type: str
        format=...,  # type: Optional[Union[str, "_models.DocumentFormat"]]
        compact=...,  # type: Optional[bool]
        data_model=...,  # type: Type["TModel"]
        ignore_validation_errors=...,  # type: Literal[False]
        **kwargs,  # type: Any
    ):
        # type: (...) -> "ResultWithParsed[TModel]"
        ...

    @overload
    def get_document(
        self,
        identifier,  # type: str
        format=...,  # type: Optional[Union[str, "_models.DocumentFormat"]]
        compact=...,  # type: Optional[bool]
        data_model=...,  # type: Type["TModel"]
        ignore_validation_errors=...,  # type: Literal[True]
        **kwargs,  # type: Any
    ):
        # type: (...) -> "ResultWithOptionalParsed[TModel]"
        ...

    def get_document(
        self,
        identifier,  # type: str
        format=None,  # type: Optional[Union[str, "_models.DocumentFormat"]]
        compact=None,  # type: Optional[bool]
        data_model=None,  # type: Optional[Type["TModel"]]
        ignore_validation_errors=False,  # type: bool
        **kwargs,  # type: Any
    ):
        # type: (...) -> Union["_models.Document", "ResultWithParsed[TModel]", "ResultWithOptionalParsed[TModel]"]
        if data_model:
            compact = True

        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(
                response=response, model=self._deserialize(_models.RequestError, response)
            ),
            401: lambda response: ClientAuthenticationError(
                response=response, model=self._deserialize(_models.RequestError, response)
            ),
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Document]

        request = build_get_document_request(
            identifier=identifier,
            format=format,
            compact=compact,
            template_url=self.get_document.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "region": self._serialize.url("self._config.region", self._config.region, "str"),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.RequestError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize("Document", pipeline_response)

        if cls:
            deserialized = cls(pipeline_response, deserialized, {})

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
    def create_document(
        self,
        file=...,  # type: Optional[IO]
        url=...,  # type: Optional[str]
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
    def create_document(
        self,
        file=...,  # type: Optional[IO]
        url=...,  # type: Optional[str]
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
    def create_document(
        self,
        file=...,  # type: Optional[IO]
        url=...,  # type: Optional[str]
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

    def create_document(
        self,
        file=None,  # type: Optional[IO]
        url=None,  # type: Optional[str]
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

        deserialized = super().create_document(
            file=file,
            url=url,
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
    def update_document(
        self,
        identifier,  # type: str
        body,  # type: _models.DocumentUpdate
        compact=...,  # type: Optional[bool]
        data_model=...,  # type: None
        ignore_validation_errors=...,  # type: bool
        **kwargs,  # type: Any
    ):
        # type: (...) -> "_models.Document"
        ...

    @overload
    def update_document(
        self,
        identifier,  # type: str
        body,  # type: _models.DocumentUpdate
        compact=...,  # type: Optional[bool]
        data_model=...,  # type: Type["TModel"]
        ignore_validation_errors=...,  # type: Literal[False]
        **kwargs,  # type: Any
    ):
        # type: (...) -> "ResultWithParsed[TModel]"
        ...

    @overload
    def update_document(
        self,
        identifier,  # type: str
        body,  # type: _models.DocumentUpdate
        compact=...,  # type: Optional[bool]
        data_model=...,  # type: Type["TModel"]
        ignore_validation_errors=...,  # type: Literal[True]
        **kwargs,  # type: Any
    ):
        # type: (...) -> "ResultWithOptionalParsed[TModel]"
        ...

    def update_document(
        self,
        identifier,  # type: str
        body,  # type: _models.DocumentUpdate
        compact=None,  # type: Optional[bool]
        data_model=None,  # type: Optional[Type["TModel"]]
        ignore_validation_errors=False,  # type: bool
        **kwargs,  # type: Any
    ):
        # type: (...) -> Union["_models.Document", "ResultWithParsed[TModel]", "ResultWithOptionalParsed[TModel]"]
        if data_model:
            compact = True

        deserialized = super().update_document(
            identifier,
            body,
            compact=compact,
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
