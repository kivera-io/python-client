from gql import gql
from typing import Sequence

class getMethods:

    _GetAwsIamProxyAccessByIdQuery = """
    query GetAwsIamProxyAccessById($id: Int!) {
    AwsIamProxyAccess(where: {id: {_eq: $id}}) {
        id
        role_arn
        proxy_id
        organization_id
    }
}
    """

    def GetAwsIamProxyAccessById(self, id: int):
        query = gql(self._GetAwsIamProxyAccessByIdQuery)
        variables = {
            "id": id,
        }
        operation_name = "GetAwsIamProxyAccessById"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )

    _GetAwsIamProxyAccessByRoleQuery = """
    query GetAwsIamProxyAccessByRole($role_arn: String!) {
    AwsIamProxyAccess(where: {role_arn: {_eq: $role_arn}}) {
        id
        role_arn
        proxy_id
        organization_id
    }
}
    """

    def GetAwsIamProxyAccessByRole(self, role_arn: str):
        query = gql(self._GetAwsIamProxyAccessByRoleQuery)
        variables = {
            "role_arn": role_arn,
        }
        operation_name = "GetAwsIamProxyAccessByRole"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
