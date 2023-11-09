from azure.cli.core import AzCommandsLoader
from azure.cli.core.commands import CliCommandType

import azext_pbi._help


class PowerBICLICommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        pbi_custom = CliCommandType(operations_tmpl='azext_pbi.custom#{}')
        super(PowerBICLICommandsLoader, self).__init__(cli_ctx=cli_ctx, custom_command_type=pbi_custom)

    def load_command_table(self, args):
        from .commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from ._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = PowerBICLICommandsLoader
