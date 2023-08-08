from gql import gql
from typing import Sequence

class listMethods:

    _ListIdentityTypesQuery = """
    query ListIdentityTypes{
  IdentityTypes{
    config
    id
    identity_type
  }
}
    """

    def ListIdentityTypes(self):
        query = gql(self._ListIdentityTypesQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
