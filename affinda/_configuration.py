# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@5.16.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from ._version import VERSION

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Union

    from azure.core.credentials import TokenCredential


class AffindaAPIConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for AffindaAPI.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param region: region - server parameter. Default value is "api".
    :type region: str or ~affinda.models.Region
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        region="api",  # type: Union[str, "_models.Region"]
        **kwargs,  # type: Any
    ):
        # type: (...) -> None
        super(AffindaAPIConfiguration, self).__init__(**kwargs)
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")
        if region is None:
            raise ValueError("Parameter 'region' must not be None.")

        self.credential = credential
        self.region = region
        self.credential_scopes = kwargs.pop(
            "credential_scopes", ["https://management.azure.com/.default"]
        )
        kwargs.setdefault("sdk_moniker", "affinda/{}".format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(
            **kwargs
        )
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(
            **kwargs
        )
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(
            **kwargs
        )
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(
            **kwargs
        )
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.BearerTokenCredentialPolicy(
                self.credential, *self.credential_scopes, **kwargs
            )
