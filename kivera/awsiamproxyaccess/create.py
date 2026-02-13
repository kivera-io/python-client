from gql import gql
from typing import Sequence

class createMethods:

    _CreateAwsIamProxyAccessQuery = """
    mutation CreateAwsIamProxyAccess($organization_id: Int!, $role_arn: String!, $proxy_id: Int!) {
  insert_AwsIamProxyAccess(objects: {
    organization_id: $organization_id,
    role_arn: $role_arn,
    proxy_id: $proxy_id
  }) {
    returning {
      id
    }
  }
}
    """

    def CreateAwsIamProxyAccess(self, organization_id: int, role_arn: str, proxy_id: int):
        query = gql(self._CreateAwsIamProxyAccessQuery)
        variables = {
            "organization_id": organization_id,
            "role_arn": role_arn,
            "proxy_id": proxy_id,
        }
        operation_name = "CreateAwsIamProxyAccess"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
