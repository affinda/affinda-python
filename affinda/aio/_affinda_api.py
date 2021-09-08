# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.5.1, generator: @autorest/python@5.9.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, Optional, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

from .. import models
from ._configuration import AffindaAPIConfiguration
from .operations import AffindaAPIOperationsMixin

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class AffindaAPI(AffindaAPIOperationsMixin):
    """Affinda API client for Python.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param limit: The numbers of documents to return, defaults to 300.
    :type limit: int
    :param offset: The number of documents to skip before starting to collect the result set.
    :type offset: int
    :param base_url: Service URL. Default value is 'https://api.affinda.com/v1'.
    :type base_url: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        limit: Optional[int] = 300,
        offset: Optional[int] = None,
        base_url: str = "https://api.affinda.com/v1",
        **kwargs: Any,
    ) -> None:
        self._config = AffindaAPIConfiguration(credential, limit, offset, **kwargs)
        self._client = AsyncPipelineClient(
            base_url=base_url, config=self._config, **kwargs
        )

        client_models = {
            k: v for k, v in models.__dict__.items() if isinstance(v, type)
        }
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False

    def _send_request(
        self, request: HttpRequest, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AffindaAPI":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
