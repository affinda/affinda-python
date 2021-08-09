from azure.core.credentials import AccessToken


class TokenCredential:
    """Manually defined as from azure.core.credentials doesn't actually define it any more..."""

    def __init__(self, token: str, expires_on: int = 0):
        self.token = token
        self.expires_on = expires_on

    def get_token(self, *scopes, **kwargs):
        return AccessToken(self.token, self.expires_on)
