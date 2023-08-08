from gql import gql
from typing import Sequence

class listMethods:

    _ListProvidersQuery = """
    query ListProviders {
    Providers(order_by: {id: asc}) {
        name
        id
    }
}
    """

    def ListProviders(self):
        query = gql(self._ListProvidersQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
