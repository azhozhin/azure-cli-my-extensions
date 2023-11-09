def load_command_table(self, args):
    with self.command_group('pbi') as g:
        g.custom_command('version', 'pbi_version')

    with self.command_group('pbi workspace') as g:
        g.custom_command('list', 'pbi_workspace_list')
        g.custom_command('show', 'pbi_workspace_show')
