from gql import gql
from typing import Sequence

class listMethods:

    _ListActionMetadataOverridesQuery = """
    query ListActionMetadataOverrides {
  ActionMetadataOverrides {
    id
    organization_id
    Provider {
      id
      name
    }
    metadata
    created_at
    updated_at
    created_by
    updated_by
  }
}
    """

    def ListActionMetadataOverrides(self):
        query = gql(self._ListActionMetadataOverridesQuery)
        variables = {
        }
        operation_name = "ListActionMetadataOverrides"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
