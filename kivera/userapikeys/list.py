
from gql import gql
from typing import Sequence

class listMethods:

    _ListUserApiKeysQuery = """
    query ListUserApiKeys {
    UserApiKeys {
        client_id
        id
        org_id
        status
        user_id
        created
        Organization {
            domain
            company_name
        }
    }
}
    """

    def ListUserApiKeys(self):
        query = gql(self._ListUserApiKeysQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
