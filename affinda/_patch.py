# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import Any

from azure.core.pipeline import PipelineRequest
from azure.core.pipeline.policies import BearerTokenCredentialPolicy

from ._affinda_api import AffindaAPI as AffindaAPIGenerated
from .token_credential import TokenCredential


class BearerTokenWithoutTLSEnforcementPolicy(BearerTokenCredentialPolicy):
    """
    Patch the credential policy to no longer enforce https, allows the client lib
    to be used with http://localhost etc
    """

    def on_request(self, request: PipelineRequest):
        request.context.options["enforce_https"] = False
        return super().on_request(request)


class AffindaAPI(AffindaAPIGenerated):
    def __init__(
        self,
        credential: TokenCredential,
        base_url="https://api.affinda.com/v2",  # type: str
        **kwargs,  # type: Any
    ):
        super().__init__(
            credential=credential,
            base_url=base_url,
            authentication_policy=kwargs.pop(
                "authentication_policy", BearerTokenWithoutTLSEnforcementPolicy(credential)
            ),
            **kwargs,
        )


__all__ = ["AffindaAPI"]


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
