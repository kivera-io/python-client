
from gql import gql
from typing import Sequence

class updateMethods:

    _DisableUserApiKeyQuery = """
    mutation DisableUserApiKey($client_id: String!) {
    update_UserApiKeys(where: {client_id: {_eq: $client_id}}, _set: {status: false}) {
        returning {
            client_id
            created
            id
            org_id
            status
            user_id
        }
    }
}
    """

    def DisableUserApiKey(self, client_id: str):
        query = gql(self._DisableUserApiKeyQuery)
        variables = {
            "client_id": client_id,
        }
        return self.execute(query, variable_values=variables)

    _DisableUserApiKeysForOrgQuery = """
    mutation DisableUserApiKeysForOrg($user_id: String!, $org_id: Int!) {
    update_UserApiKeys(where: {user_id: {_eq: $user_id}, org_id: {_eq: $org_id}, status: {_eq: true}}, _set: {status: false}) {
        returning {
            client_id
            created
            id
            org_id
            status
            user_id
        }
    }
}
    """

    def DisableUserApiKeysForOrg(self, user_id: str, org_id: int):
        query = gql(self._DisableUserApiKeysForOrgQuery)
        variables = {
            "user_id": user_id,
            "org_id": org_id,
        }
        return self.execute(query, variable_values=variables)

    _UpdateUserApiKeysQuery = """
    mutation UpdateUserApiKeys($user_id: String!, $org_id: Int!, $status: Boolean!) {
    update_UserApiKeys(where: {user_id: {_eq: $user_id}, org_id: {_eq: $org_id}}, _set: {status: $status}) {
        returning {
            client_id
            created
            id
            org_id
            status
            user_id
        }
    }
}
    """

    def UpdateUserApiKeys(self, user_id: str, org_id: int, status: bool):
        query = gql(self._UpdateUserApiKeysQuery)
        variables = {
            "user_id": user_id,
            "org_id": org_id,
            "status": status,
        }
        return self.execute(query, variable_values=variables)
