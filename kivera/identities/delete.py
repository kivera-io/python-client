from gql import gql
from typing import Sequence

class deleteMethods:

    _DeleteIdentitiesQuery = """
    mutation DeleteIdentities($ids: [Int!]!) {
  update_Identities(where: {id: {_in: $ids}}, _set: {status: false}) {
    returning {
      id
      status
    }
  }
  update_IdentityProfiles(where: {identity_id: {_in: $ids}}, _set: {deleted: true}) {
    affected_rows
  }
}
    """

    def DeleteIdentities(self, ids: Sequence[int]):
        query = gql(self._DeleteIdentitiesQuery)
        variables = {
            "ids": ids,
        }
        return self.execute(query, variable_values=variables)

    _DeleteIdentityQuery = """
    mutation DeleteIdentity($id: Int!) {
  update_Identities(where: {id: {_eq: $id}}, _set: {status: false}) {
    returning {
      config
      description
      id
      name
      organization_id
      status
      tags
      type_id
    }
  }
  update_IdentityProfiles(where: {identity_id: {_eq: $id}}, _set: {deleted: true}) {
    affected_rows
  }
}
    """

    def DeleteIdentity(self, id: int):
        query = gql(self._DeleteIdentityQuery)
        variables = {
            "id": id,
        }
        return self.execute(query, variable_values=variables)
