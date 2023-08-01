
from gql import gql
from typing import Sequence

class getMethods:

    _GetProviderQuery = """
    query GetProvider($provider: String!) {
  Providers(where: {name: {_eq: $provider}}) {
    name
    id
  }
}
    """

    def GetProvider(self, provider: str):
        query = gql(self._GetProviderQuery)
        variables = {
            "provider": provider,
        }
        return self.execute(query, variable_values=variables)

    _GetProvidersQuery = """
    query GetProviders {
  Providers {
    name
    id
    ProviderDomains {
      domain_regex
    }
  }
}
    """

    def GetProviders(self):
        query = gql(self._GetProvidersQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
