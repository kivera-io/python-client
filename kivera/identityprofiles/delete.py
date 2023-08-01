
from gql import gql
from typing import Sequence

class deleteMethods:

    _DeleteIdentityProfileQuery = """
    mutation DeleteIdentityProfile($id: Int!) {
  update_IdentityProfiles(where: {id: {_eq: $id}}, _set: {deleted: false}) {
    returning {
      deleted
      id
      identity_id
      profile_id
    }
  }
}
    """

    def DeleteIdentityProfile(self, id: int):
        query = gql(self._DeleteIdentityProfileQuery)
        variables = {
            "id": id,
        }
        return self.execute(query, variable_values=variables)
