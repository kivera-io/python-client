from gql import gql
from typing import Sequence

class updateMethods:

    _UpdateActionMetadataOverridesQuery = """
    mutation UpdateActionMetadataOverrides($id: Int!, $metadata: jsonb!) {
  update_ActionMetadataOverrides_by_pk(
    pk_columns: { id: $id }
    _set: { metadata: $metadata }
  ) {
    id
    metadata
    provider_id
    organization_id
    created_at
    updated_at
    created_by
    updated_by
  }
}
    """

    def UpdateActionMetadataOverrides(self, id: int, metadata: dict):
        query = gql(self._UpdateActionMetadataOverridesQuery)
        variables = {
            "id": id,
            "metadata": metadata,
        }
        operation_name = "UpdateActionMetadataOverrides"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
