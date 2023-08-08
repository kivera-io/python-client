from gql import gql
from typing import Sequence

class listMethods:

    _ListGlobalServicesQuery = """
    query ListGlobalServices {
  GlobalServices {
    id
    name
    title
    description
    created_at
    Provider {
      name
      id
    }
  }
}
    """

    def ListGlobalServices(self):
        query = gql(self._ListGlobalServicesQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)

    _ListGlobalServicesForProviderQuery = """
    query ListGlobalServicesForProvider($provider: String!) {
  GlobalServices(where: {Provider: {name: {_eq: $provider}}}) {
    id
    name
    title
    description
  }
}
    """

    def ListGlobalServicesForProvider(self, provider: str):
        query = gql(self._ListGlobalServicesForProviderQuery)
        variables = {
            "provider": provider,
        }
        return self.execute(query, variable_values=variables)
