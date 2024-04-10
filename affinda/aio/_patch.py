# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""

from typing import TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.pipeline import PipelineRequest
from azure.core.pipeline.policies import AsyncBearerTokenCredentialPolicy
from msrest import Deserializer, Serializer

from .. import models
from ._affinda_api import AffindaAPI as AffindaAPIGenerated
from ._configuration import AffindaAPIConfiguration
from .token_credential import AsyncTokenCredential

if TYPE_CHECKING:
    pass


class AsyncBearerTokenWithoutTLSEnforcementPolicy(AsyncBearerTokenCredentialPolicy):
    """
    Patch the credential policy to no longer enforce https, allows the client lib
    to be used with http://localhost etc
    """

    async def on_request(self, request: PipelineRequest):
        request.context.options["enforce_https"] = False
        return await super().on_request(request)


class AffindaAPI(AffindaAPIGenerated):
    def __init__(
        self,
        credential,  # type: "IAsyncTokenCredential"
        region="api",  # type: Union[str, "_models.Region"]
        **kwargs,  # type: Any
    ):
        if "base_url" not in kwargs:
            _base_url = "https://{region}.affinda.com"
        else:
            _base_url = kwargs.pop("base_url")

        if "authentication_policy" not in kwargs:
            kwargs["authentication_policy"] = AsyncBearerTokenWithoutTLSEnforcementPolicy(
                credential
            )

        self._config = AffindaAPIConfiguration(credential=credential, region=region, **kwargs)
        self._client = AsyncPipelineClient(base_url=_base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False


__all__ = ["AffindaAPI", "AsyncTokenCredential"]


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
