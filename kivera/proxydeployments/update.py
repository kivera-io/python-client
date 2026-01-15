from gql import gql
from typing import Sequence

class updateMethods:

    _UpdateProxyDeploymentQuery = """
    mutation UpdateProxyDeployment($id: Int!, $status: String!, $deployed: Boolean = false, $comment: String) {
  update_ProxyDeployments_by_pk(pk_columns:{id: $id}, _set: {status: $status, deployed: $deployed, comment: $comment}) {
    id
    config
    created_by_user_id
    date_created
    User {
      given_name
      family_name
      id
      email
    }
    config_version
    status
    deployed
    comment
    proxy_id
    date_modified
    actioned_by_user_id
  }
}
    """

    def UpdateProxyDeployment(self, id: int, status: str, deployed: dict = None, comment: str = None):
        query = gql(self._UpdateProxyDeploymentQuery)
        variables = {
            "id": id,
            "status": status,
            "deployed": deployed,
            "comment": comment,
        }
        operation_name = "UpdateProxyDeployment"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
