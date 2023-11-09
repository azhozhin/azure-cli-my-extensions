from knack.help_files import helps

helps['pbi'] = """
    type: group
    short-summary: Commands to interact wityh PowerBI service
"""

helps['pbi version'] = """
    type: command
    short-summary: Show version of extension
    examples:
      - name: Show extension version
        text: |-
            az pbi version
"""

helps['pbi workspace'] = """
    type: group
    short-summary: Workspace level commands
"""

helps['pbi workspace list'] = """
    type: command
    short-summary: List all workspaces visible to current user
    examples:
      - name: List all workspaces
        text: |-
            az pbi workspace list
"""

helps['pbi workspace show'] = """
    type: command
    short-summary: Show workspace details by name
    examples:
      - name: Show workspace details
        text: |-
            az pbi workspace show --workspace "My Workspace Name"
"""
