from azure.cli.testsdk import ScenarioTest


class WorkspaceScenarioTest(ScenarioTest):

    def test_workspace(self):
        workspace_name = 'Admin monitoring'
        self.cmd('az pbi workspace list').checks = [
            self.check('length([])', 3)
        ]

        self.kwargs.update({
            "name": workspace_name,
        })

        self.cmd('az pbi workspace show --workspace "{name}"', checks=[
            self.check('isOnDedicatedCapacity', False),
            self.check('isReadOnly', False),
            self.check('name', workspace_name),
            self.check('type', 'AdminInsights'),
        ])
