# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.4, generator: @autorest/python@6.9.7)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import DatasetsOperations
from ._operations import UsersOperations
from ._operations import ImportsOperations
from ._operations import ReportsOperations
from ._operations import DashboardsOperations
from ._operations import TilesOperations
from ._operations import AppsOperations
from ._operations import DataflowsOperations
from ._operations import GatewaysOperations
from ._operations import GroupsOperations
from ._operations import CapacitiesOperations
from ._operations import AvailableFeaturesOperations
from ._operations import PipelinesOperations
from ._operations import DataflowStorageAccountsOperations
from ._operations import WorkspaceInfoOperations
from ._operations import WidelySharedArtifactsOperations
from ._operations import AdminOperations
from ._operations import EmbedTokenOperations
from ._operations import InformationProtectionOperations
from ._operations import ProfilesOperations
from ._operations import TemplateAppsOperations
from ._operations import ScorecardsOperations
from ._operations import GoalsOperations
from ._operations import GoalsStatusRulesOperations
from ._operations import GoalValuesOperations
from ._operations import GoalNotesOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "DatasetsOperations",
    "UsersOperations",
    "ImportsOperations",
    "ReportsOperations",
    "DashboardsOperations",
    "TilesOperations",
    "AppsOperations",
    "DataflowsOperations",
    "GatewaysOperations",
    "GroupsOperations",
    "CapacitiesOperations",
    "AvailableFeaturesOperations",
    "PipelinesOperations",
    "DataflowStorageAccountsOperations",
    "WorkspaceInfoOperations",
    "WidelySharedArtifactsOperations",
    "AdminOperations",
    "EmbedTokenOperations",
    "InformationProtectionOperations",
    "ProfilesOperations",
    "TemplateAppsOperations",
    "ScorecardsOperations",
    "GoalsOperations",
    "GoalsStatusRulesOperations",
    "GoalValuesOperations",
    "GoalNotesOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
