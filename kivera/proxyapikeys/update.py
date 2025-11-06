from gql import gql
from typing import Sequence

class updateMethods:

    _DisableProxyApiKeyQuery = """
    mutation DisableProxyApiKey($id: Int!) {
    update_ProxyApiKeys(where: {id: {_eq: $id}}, _set: {status: false}) {
        returning {
            proxy_id
            api_key
            org_client_id
            id
            status
        }
    }
}
    """

    def DisableProxyApiKey(self, id: int):
        query = gql(self._DisableProxyApiKeyQuery)
        variables = {
            "id": id,
        }
        operation_name = "DisableProxyApiKey"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )

    _DisableProxyApiKeysByProxyIdQuery = """
    mutation DisableProxyApiKeysByProxyId($proxy_id: Int!) {
    update_ProxyApiKeys(where: {proxy_id: {_eq: $proxy_id}}, _set: {status: false}) {
        returning {
            proxy_id
            api_key
            org_client_id
            id
            status
        }
    }
}
    """

    def DisableProxyApiKeysByProxyId(self, proxy_id: int):
        query = gql(self._DisableProxyApiKeysByProxyIdQuery)
        variables = {
            "proxy_id": proxy_id,
        }
        operation_name = "DisableProxyApiKeysByProxyId"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
