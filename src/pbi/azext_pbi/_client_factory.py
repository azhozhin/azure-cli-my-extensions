from .vendored_sdks.power_bi_client import PowerBIClient
from azure.cli.core._profile import Profile


def _powerbi_client_factory(cli_ctx) -> PowerBIClient:
    profile = Profile(cli_ctx)
    resource = 'https://analysis.windows.net/powerbi/api'
    credential_scopes = [f'{resource}/.default']
    credential, subscription_id, _ = profile.get_login_credentials(resource)
    client = PowerBIClient(credential=credential, credential_scopes=credential_scopes)
    return client
