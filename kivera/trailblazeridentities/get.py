from gql import gql
from typing import Sequence

class getMethods:

    _GetTrailBlazerIdentityQuery = """
    query GetTrailBlazerIdentity($id: Int!) {
  TrailBlazerIdentities_by_pk(id: $id) {
    deleted
    id
    identity_id
    trailblazer_id
  }
}
    """

    def GetTrailBlazerIdentity(self, id: int):
        query = gql(self._GetTrailBlazerIdentityQuery)
        variables = {
            "id": id,
        }
        return self.execute(query, variable_values=variables)
