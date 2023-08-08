from gql import gql
from typing import Sequence

class updateMethods:

    _AttachProfilesToIdentityQuery = """
    mutation AttachProfilesToIdentity($objects: [IdentityProfiles_insert_input!]!) {
  insert_IdentityProfiles(objects: $objects, on_conflict: {constraint: identityprofiles_uniq_key, update_columns: [identity_id, deleted]}) {
    returning {
      identity_id
      deleted
      id
      profile_id
    }
  }
}
    """

    def AttachProfilesToIdentity(self, objects: Sequence[dict]):
        query = gql(self._AttachProfilesToIdentityQuery)
        variables = {
            "objects": objects,
        }
        return self.execute(query, variable_values=variables)
