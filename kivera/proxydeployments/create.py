from gql import gql
from typing import Sequence

class createMethods:

    _CreateProxyDeploymentQuery = """
    mutation CreateProxyDeployment($proxy_id: Int!, $status: String! = "PENDING", $config_version: String!, $config: jsonb, $deployed: Boolean = false, $comment: String) {
  insert_ProxyDeployments(objects: {config: $config, config_version: $config_version, proxy_id: $proxy_id, status: $status, deployed: $deployed, comment: $comment}) {
    affected_rows
  }
}
    """

    def CreateProxyDeployment(self, proxy_id: int, config_version: str, status: dict = None, config: dict = None, deployed: dict = None, comment: str = None):
        query = gql(self._CreateProxyDeploymentQuery)
        variables = {
            "proxy_id": proxy_id,
            "status": status,
            "config_version": config_version,
            "config": config,
            "deployed": deployed,
            "comment": comment,
        }
        operation_name = "CreateProxyDeployment"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
