
from gql import gql
from typing import Sequence

class listMethods:

    _ListProxyProviderVersionsQuery = """
    query ListProxyProviderVersions {
    ProviderVersions {
        id
        provider_id
        version_name
        hash
        url
        created
        Provider {
            name
        }
    }
}
    """

    def ListProxyProviderVersions(self):
        query = gql(self._ListProxyProviderVersionsQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
