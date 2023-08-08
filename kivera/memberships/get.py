from gql import gql
from typing import Sequence

class getMethods:

    _GetMembershipsQuery = """
    query GetMemberships($user_id: String!) {
    Users(where: {id: {_eq: $user_id }}) {
        id
        active_org_id
        Memberships {
            id
            org_id
        }
    }
}
    """

    def GetMemberships(self, user_id: str):
        query = gql(self._GetMembershipsQuery)
        variables = {
            "user_id": user_id,
        }
        return self.execute(query, variable_values=variables)
