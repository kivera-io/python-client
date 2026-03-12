from gql import gql
from typing import Sequence

class deleteMethods:

    _DeleteActionMetadataOverridesQuery = """
    mutation DeleteActionMetadataOverrides($id: Int!) {
  delete_ActionMetadataOverrides_by_pk(id: $id) {
    id
  }
}
    """

    def DeleteActionMetadataOverrides(self, id: int):
        query = gql(self._DeleteActionMetadataOverridesQuery)
        variables = {
            "id": id,
        }
        operation_name = "DeleteActionMetadataOverrides"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
