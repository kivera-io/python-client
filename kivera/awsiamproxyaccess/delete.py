from gql import gql
from typing import Sequence

class deleteMethods:

    _DeleteAwsIamProxyAccessQuery = """
    mutation DeleteAwsIamProxyAccess($id: Int!) {
    delete_AwsIamProxyAccess_by_pk(id: $id) {
        id
    }
}
    """

    def DeleteAwsIamProxyAccess(self, id: int):
        query = gql(self._DeleteAwsIamProxyAccessQuery)
        variables = {
            "id": id,
        }
        operation_name = "DeleteAwsIamProxyAccess"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
