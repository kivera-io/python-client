from gql import gql
from typing import Sequence

class listMethods:

    _ListRolesQuery = """
    query ListRoles {
    Roles {
        id
        role_name
    }
}
    """

    def ListRoles(self):
        query = gql(self._ListRolesQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
