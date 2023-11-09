from azure.core.exceptions import ResourceNotFoundError
from ._client_factory import _powerbi_client_factory
from .version import VERSION


def pbi_version():
    return {
        'version': VERSION
    }


def pbi_workspace_list(cmd):
    client = _powerbi_client_factory(cmd.cli_ctx)
    groups = client.groups.get_groups()
    return groups['value']


def pbi_workspace_show(cmd, workspace):
    client = _powerbi_client_factory(cmd.cli_ctx)
    groups = client.groups.get_groups()
    for d in groups['value']:
        if d['name'] == workspace:
            return d
    raise ResourceNotFoundError(f'Workspace "{workspace}" is not found')

