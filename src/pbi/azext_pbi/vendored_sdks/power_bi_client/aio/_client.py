# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.4, generator: @autorest/python@6.9.7)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import PowerBIClientConfiguration
from .operations import (
    AdminOperations,
    AppsOperations,
    AvailableFeaturesOperations,
    CapacitiesOperations,
    DashboardsOperations,
    DataflowStorageAccountsOperations,
    DataflowsOperations,
    DatasetsOperations,
    EmbedTokenOperations,
    GatewaysOperations,
    GoalNotesOperations,
    GoalValuesOperations,
    GoalsOperations,
    GoalsStatusRulesOperations,
    GroupsOperations,
    ImportsOperations,
    InformationProtectionOperations,
    PipelinesOperations,
    ProfilesOperations,
    ReportsOperations,
    ScorecardsOperations,
    TemplateAppsOperations,
    TilesOperations,
    UsersOperations,
    WidelySharedArtifactsOperations,
    WorkspaceInfoOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class PowerBIClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """PowerBIClient.

    :ivar datasets: DatasetsOperations operations
    :vartype datasets: power_bi_client.aio.operations.DatasetsOperations
    :ivar users: UsersOperations operations
    :vartype users: power_bi_client.aio.operations.UsersOperations
    :ivar imports: ImportsOperations operations
    :vartype imports: power_bi_client.aio.operations.ImportsOperations
    :ivar reports: ReportsOperations operations
    :vartype reports: power_bi_client.aio.operations.ReportsOperations
    :ivar dashboards: DashboardsOperations operations
    :vartype dashboards: power_bi_client.aio.operations.DashboardsOperations
    :ivar tiles: TilesOperations operations
    :vartype tiles: power_bi_client.aio.operations.TilesOperations
    :ivar apps: AppsOperations operations
    :vartype apps: power_bi_client.aio.operations.AppsOperations
    :ivar dataflows: DataflowsOperations operations
    :vartype dataflows: power_bi_client.aio.operations.DataflowsOperations
    :ivar gateways: GatewaysOperations operations
    :vartype gateways: power_bi_client.aio.operations.GatewaysOperations
    :ivar groups: GroupsOperations operations
    :vartype groups: power_bi_client.aio.operations.GroupsOperations
    :ivar capacities: CapacitiesOperations operations
    :vartype capacities: power_bi_client.aio.operations.CapacitiesOperations
    :ivar available_features: AvailableFeaturesOperations operations
    :vartype available_features: power_bi_client.aio.operations.AvailableFeaturesOperations
    :ivar pipelines: PipelinesOperations operations
    :vartype pipelines: power_bi_client.aio.operations.PipelinesOperations
    :ivar dataflow_storage_accounts: DataflowStorageAccountsOperations operations
    :vartype dataflow_storage_accounts:
     power_bi_client.aio.operations.DataflowStorageAccountsOperations
    :ivar workspace_info: WorkspaceInfoOperations operations
    :vartype workspace_info: power_bi_client.aio.operations.WorkspaceInfoOperations
    :ivar widely_shared_artifacts: WidelySharedArtifactsOperations operations
    :vartype widely_shared_artifacts:
     power_bi_client.aio.operations.WidelySharedArtifactsOperations
    :ivar admin: AdminOperations operations
    :vartype admin: power_bi_client.aio.operations.AdminOperations
    :ivar embed_token: EmbedTokenOperations operations
    :vartype embed_token: power_bi_client.aio.operations.EmbedTokenOperations
    :ivar information_protection: InformationProtectionOperations operations
    :vartype information_protection: power_bi_client.aio.operations.InformationProtectionOperations
    :ivar profiles: ProfilesOperations operations
    :vartype profiles: power_bi_client.aio.operations.ProfilesOperations
    :ivar template_apps: TemplateAppsOperations operations
    :vartype template_apps: power_bi_client.aio.operations.TemplateAppsOperations
    :ivar scorecards: ScorecardsOperations operations
    :vartype scorecards: power_bi_client.aio.operations.ScorecardsOperations
    :ivar goals: GoalsOperations operations
    :vartype goals: power_bi_client.aio.operations.GoalsOperations
    :ivar goals_status_rules: GoalsStatusRulesOperations operations
    :vartype goals_status_rules: power_bi_client.aio.operations.GoalsStatusRulesOperations
    :ivar goal_values: GoalValuesOperations operations
    :vartype goal_values: power_bi_client.aio.operations.GoalValuesOperations
    :ivar goal_notes: GoalNotesOperations operations
    :vartype goal_notes: power_bi_client.aio.operations.GoalNotesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword endpoint: Service URL. Default value is "https://api.powerbi.com".
    :paramtype endpoint: str
    """

    def __init__(
        self, credential: "AsyncTokenCredential", *, endpoint: str = "https://api.powerbi.com", **kwargs: Any
    ) -> None:
        self._config = PowerBIClientConfiguration(credential=credential, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.datasets = DatasetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.users = UsersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.imports = ImportsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.reports = ReportsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.dashboards = DashboardsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.tiles = TilesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.apps = AppsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.dataflows = DataflowsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.gateways = GatewaysOperations(self._client, self._config, self._serialize, self._deserialize)
        self.groups = GroupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.capacities = CapacitiesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.available_features = AvailableFeaturesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.pipelines = PipelinesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.dataflow_storage_accounts = DataflowStorageAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.workspace_info = WorkspaceInfoOperations(self._client, self._config, self._serialize, self._deserialize)
        self.widely_shared_artifacts = WidelySharedArtifactsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.admin = AdminOperations(self._client, self._config, self._serialize, self._deserialize)
        self.embed_token = EmbedTokenOperations(self._client, self._config, self._serialize, self._deserialize)
        self.information_protection = InformationProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.profiles = ProfilesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.template_apps = TemplateAppsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.scorecards = ScorecardsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.goals = GoalsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.goals_status_rules = GoalsStatusRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.goal_values = GoalValuesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.goal_notes = GoalNotesOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "PowerBIClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
