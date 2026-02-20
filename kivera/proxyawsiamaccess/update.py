from gql import gql
from typing import Sequence

class updateMethods:

    _UpdateProxyAwsIamAccessQuery = """
    mutation UpdateProxyAwsIamAccess($id: Int!, $role_arn: String!, $proxy_id: Int!) {
    update_ProxyAwsIamAccess_by_pk(
        pk_columns: {id: $id},
        _set: {
            role_arn: $role_arn,
            proxy_id: $proxy_id
    }) {
        id
        role_arn
        proxy_id
        organization_id
    }
}
    """

    def UpdateProxyAwsIamAccess(self, id: int, role_arn: str, proxy_id: int):
        query = gql(self._UpdateProxyAwsIamAccessQuery)
        variables = {
            "id": id,
            "role_arn": role_arn,
            "proxy_id": proxy_id,
        }
        operation_name = "UpdateProxyAwsIamAccess"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
