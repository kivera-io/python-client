from gql import gql
from typing import Sequence

class listMethods:

    _ListProxyDeploymentsQuery = """
    query ListProxyDeployments {
  ProxyDeployments {
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
    proxy_id
    date_modified
    actioned_by_user_id
  }
}
    """

    def ListProxyDeployments(self):
        query = gql(self._ListProxyDeploymentsQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
