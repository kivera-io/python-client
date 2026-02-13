from gql import gql
from typing import Sequence

class listMethods:

    _ListAwsIamProxyAccessQuery = """
    query ListAwsIamProxyAccess {
    AwsIamProxyAccess {
        id
        role_arn
        proxy_id
        organization_id
    }
}
    """

    def ListAwsIamProxyAccess(self):
        query = gql(self._ListAwsIamProxyAccessQuery)
        variables = {
        }
        operation_name = "ListAwsIamProxyAccess"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
