from gql import gql
from typing import Sequence

class listMethods:

    _ListProxyAwsIamAccessQuery = """
    query ListProxyAwsIamAccess {
    ProxyAwsIamAccess {
        id
        role_arn
        proxy_id
        organization_id
    }
}
    """

    def ListProxyAwsIamAccess(self):
        query = gql(self._ListProxyAwsIamAccessQuery)
        variables = {
        }
        operation_name = "ListProxyAwsIamAccess"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
