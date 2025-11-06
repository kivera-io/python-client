from gql import gql
from typing import Sequence

class getMethods:

    _GetActiveProxyApiKeysQuery = """
    query GetActiveProxyApiKeys($proxy_id: Int!) {
  ProxyApiKeys(where: {proxy_id: {_eq: $proxy_id}, status: {_eq: true}, expiry: {_is_null: true}}) {
    proxy_id
    id
    api_key
    org_client_id
    entity_secret
    Proxy {
      id
      organization_id
      status
    }
  }
}
    """

    def GetActiveProxyApiKeys(self, proxy_id: int):
        query = gql(self._GetActiveProxyApiKeysQuery)
        variables = {
            "proxy_id": proxy_id,
        }
        operation_name = "GetActiveProxyApiKeys"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )

    _GetProxyApiKeysQuery = """
    query GetProxyApiKeys($proxy_id: Int!) {
  ProxyApiKeys(where: {proxy_id: {_eq: $proxy_id}, status: {_eq: true}}) {
    proxy_id
    id
    api_key
    org_client_id
    entity_secret
    Proxy {
      id
      organization_id
      status
    }
  }
}
    """

    def GetProxyApiKeys(self, proxy_id: int):
        query = gql(self._GetProxyApiKeysQuery)
        variables = {
            "proxy_id": proxy_id,
        }
        operation_name = "GetProxyApiKeys"
        operation_type = "read"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
