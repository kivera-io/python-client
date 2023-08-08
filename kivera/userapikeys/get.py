from gql import gql
from typing import Sequence

class getMethods:

    _GetUserApiKeyQuery = """
    query GetUserApiKey($user_id: String!, $org_id: Int!) {
    UserApiKeys(where: {user_id: {_eq: $user_id}, org_id: {_eq: $org_id}, status: {_eq: true}}) {
        client_id
        id
        org_id
        status
        user_id
        created
    }
}
    """

    def GetUserApiKey(self, user_id: str, org_id: int):
        query = gql(self._GetUserApiKeyQuery)
        variables = {
            "user_id": user_id,
            "org_id": org_id,
        }
        return self.execute(query, variable_values=variables)
