from gql import gql
from typing import Sequence

class deleteMethods:

    _DeleteProxyAwsIamAccessQuery = """
    mutation DeleteProxyAwsIamAccess($id: Int!) {
    delete_ProxyAwsIamAccess_by_pk(id: $id) {
        id
    }
}
    """

    def DeleteProxyAwsIamAccess(self, id: int):
        query = gql(self._DeleteProxyAwsIamAccessQuery)
        variables = {
            "id": id,
        }
        operation_name = "DeleteProxyAwsIamAccess"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
