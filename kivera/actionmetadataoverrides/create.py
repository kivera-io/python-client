from gql import gql
from typing import Sequence

class createMethods:

    _CreateActionMetadataOverridesQuery = """
    mutation CreateActionMetadataOverrides(
  $org_id: Int!
  $provider_id: Int!
  $metadata: jsonb!
) {
  insert_ActionMetadataOverrides_one(
    object: {
      organization_id: $org_id
      provider_id: $provider_id
      metadata: $metadata
    }
  ) {
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

    def CreateActionMetadataOverrides(self):
        query = gql(self._CreateActionMetadataOverridesQuery)
        variables = {
        }
        operation_name = "CreateActionMetadataOverrides"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
