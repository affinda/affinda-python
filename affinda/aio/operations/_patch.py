from typing import TYPE_CHECKING

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest

from ... import models as _models  # noqa: TID252
from ..._vendor import _convert_request  # noqa: TID252

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar, Union  # noqa: F401

    T = TypeVar("T")
    ClsType = Optional[
        Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]
    ]

from ._affinda_api_operations import (
    AffindaAPIOperationsMixin as AffindaAPIOperationsMixinGenerated,
)
from ._affinda_api_operations import build_get_document_request


# We want to patch the generated AffindaAPIOperationsMixin class, and override its get_document method.
class AffindaAPIOperationsMixin(AffindaAPIOperationsMixinGenerated):
    # Modify this method as the autogenerate one creates duplicate methods, see
    # https://github.com/Azure/autorest.python/issues/1555
    async def get_document(
        self,
        identifier,  # type: str
        format=None,  # type: Optional[Union[str, "_models.DocumentFormat"]]
        compact=None,  # type: Optional[bool]
        **kwargs,  # type: Any
    ):
        # type: (...) -> Union[_models.Document, _models.Resume, _models.Invoice, _models.JobDescription]
        """Get specific document.

        Return a specific document.

        :param identifier: Document's identifier.
        :type identifier: str
        :param format: Specify which format you want the response to be. Default is "json".
        :type format: str or ~affinda.models.DocumentFormat
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Document, or the result of cls(response)
        :rtype: ~affinda.models.Document
        :raises: ~azure.core.exceptions.HttpResponseError
        """
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

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_document.metadata = {"url": "/v3/documents/{identifier}"}  # type: ignore


__all__ = [
    "AffindaAPIOperationsMixin",
]


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
