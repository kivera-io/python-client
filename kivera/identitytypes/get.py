
from gql import gql
from typing import Sequence

class getMethods:

    _GetIdentityTypeQuery = """
    query GetIdentityType($id: Int!){
  IdentityTypes_by_pk(id: $id) {
    config
    id
    identity_type
  }
}
    """

    def GetIdentityType(self, id: int):
        query = gql(self._GetIdentityTypeQuery)
        variables = {
            "id": id,
        }
        return self.execute(query, variable_values=variables)
