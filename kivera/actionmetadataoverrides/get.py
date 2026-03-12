from gql import gql
from typing import Sequence

class getMethods:

    _GetActionMetadataOverridesQuery = """
    query GetActionMetadataOverrides($id: Int!) {
  ActionMetadataOverrides_by_pk(id: $id) {
    id
    organization_id
    provider_id
    metadata
    created_at
    updated_at
    created_by
    updated_by
  }
}
    """

    def GetActionMetadataOverrides(self, id: int):
        query = gql(self._GetActionMetadataOverridesQuery)
        variables = {
            "id": id,
        }
        operation_name = "GetActionMetadataOverrides"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
