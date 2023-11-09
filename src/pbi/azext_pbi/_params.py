from knack.arguments import CLIArgumentType

workspace_type = CLIArgumentType(
    help='Workspace name',
    options_list=['--workspace', '-w']
)


def load_arguments(self, _):
    with self.argument_context('pbi workspace show') as c:
        c.argument('workspace', workspace_type)
