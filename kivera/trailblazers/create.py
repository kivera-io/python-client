
from gql import gql
from typing import Sequence

class createMethods:

    _CreateTrailBlazerQuery = """
    mutation CreateTrailBlazer($name: String!, $description: String!, $organization_id: Int!, $debug: Boolean = false,
  $trailblazer_mode: String = "HYBRID",  $identities: [TrailBlazerIdentities_insert_input!] = [], $tags: jsonb!, $status: String = "CREATING") {
  insert_TrailBlazers(objects: {
    name: $name,
    org_id: $organization_id,
    tags: $tags,
    description: $description,
    status: $status,
    TrailBlazerSettings: {
      data: {
        debug: $debug,
        trailblazer_mode: $trailblazer_mode
      }
    },
    TrailBlazerIdentities: {data: $identities}}) {
    affected_rows
    returning {
      id
    }
  }
}
    """

    def CreateTrailBlazer(self):
        query = gql(self._CreateTrailBlazerQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
