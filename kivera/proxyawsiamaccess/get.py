from gql import gql
from typing import Sequence

class getMethods:

    _GetProxyAwsIamAccessByIdQuery = """
    query GetProxyAwsIamAccessById($id: Int!) {
    ProxyAwsIamAccess(where: {id: {_eq: $id}}) {
        id
        role_arn
        proxy_id
        organization_id
    }
}
    """

    def GetProxyAwsIamAccessById(self, id: int):
        query = gql(self._GetProxyAwsIamAccessByIdQuery)
        variables = {
            "id": id,
        }
        operation_name = "GetProxyAwsIamAccessById"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )

    _GetProxyAwsIamAccessByRoleQuery = """
    query GetProxyAwsIamAccessByRole($role_arn: String!) {
    ProxyAwsIamAccess(where: {role_arn: {_eq: $role_arn}}) {
        id
        role_arn
        proxy_id
        organization_id
    }
}
    """

    def GetProxyAwsIamAccessByRole(self, role_arn: str):
        query = gql(self._GetProxyAwsIamAccessByRoleQuery)
        variables = {
            "role_arn": role_arn,
        }
        operation_name = "GetProxyAwsIamAccessByRole"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
