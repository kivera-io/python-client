from gql import gql
from typing import Sequence

class getMethods:

    _GetActiveUserApiKeysQuery = """
    query GetActiveUserApiKeys($user_id: String!, $org_id: Int!) {
    UserApiKeys(where: {user_id: {_eq: $user_id}, org_id: {_eq: $org_id}, status: {_eq: true}, expiry: {_is_null: true}}) {
        client_id
        org_client_id
        id
        org_id
        status
        user_id
        created
        expiry
    }
}
    """

    def GetActiveUserApiKeys(self, user_id: str, org_id: int):
        query = gql(self._GetActiveUserApiKeysQuery)
        variables = {
            "user_id": user_id,
            "org_id": org_id,
        }
        operation_name = "GetActiveUserApiKeys"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )

    _GetUserApiKeysQuery = """
    query GetUserApiKeys($user_id: String!, $org_id: Int!) {
    UserApiKeys(where: {user_id: {_eq: $user_id}, org_id: {_eq: $org_id}, status: {_eq: true}}) {
        client_id
        org_client_id
        id
        org_id
        status
        user_id
        created
        expiry
    }
}
    """

    def GetUserApiKeys(self, user_id: str, org_id: int):
        query = gql(self._GetUserApiKeysQuery)
        variables = {
            "user_id": user_id,
            "org_id": org_id,
        }
        operation_name = "GetUserApiKeys"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
