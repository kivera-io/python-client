from gql import gql
from typing import Sequence

class createMethods:

    _CreateProxyQuery = """
    mutation CreateProxy($description: String!, $name: String!, $organization_id: Int!, $debug: Boolean!, $proxy_mode: String!, $default_identity_id: Int, $provider_data: [ProxyProviders_insert_input!]!, $allow_noncloud_traffic: Boolean!, $default_mode: proxysettings_default_mode_type!) {
  insert_Proxies_one(object: {description: $description, name: $name, organization_id: $organization_id, ProxySettings: {data: {proxy_mode: $proxy_mode, debug: $debug, default_identity_id: $default_identity_id, allow_noncloud_traffic: $allow_noncloud_traffic, default_mode: $default_mode}}, ProxyProviders: {data: $provider_data}}) {
    name
    organization_id
    status
    id
    ProxySettings {
      id
      default_identity_id
      debug
      proxy_mode
      default_mode
      allow_noncloud_traffic
    }
    ProxyProviders {
      id
      provider_id
    }
  }
}
    """

    def CreateProxy(self, description: str, name: str, organization_id: int, debug: bool, proxy_mode: str, provider_data: Sequence[dict], allow_noncloud_traffic: bool, default_mode: dict, default_identity_id: int = None):
        query = gql(self._CreateProxyQuery)
        variables = {
            "description": description,
            "name": name,
            "organization_id": organization_id,
            "debug": debug,
            "proxy_mode": proxy_mode,
            "default_identity_id": default_identity_id,
            "provider_data": provider_data,
            "allow_noncloud_traffic": allow_noncloud_traffic,
            "default_mode": default_mode,
        }
        return self.execute(query, variable_values=variables)

    _CreateProxyV2Query = """
    mutation CreateProxyV2(
  $name: String!,
  $description: String!,
  $organization_id: Int!,
  $debug: Boolean = false,
  $proxy_mode: String = "HYBRID",
  $default_mode: proxysettings_default_mode_type!,
  # @genqlient(pointer: true)
  $default_identity_id: Int = null,
  $allow_noncloud_traffic: Boolean = false,
  $tags: jsonb! = [],
  $providers: [ProxyProviders_insert_input!] = [],
  $identities: [ProxyIdentities_insert_input!] = [],
) {
  insert_Proxies(objects: {description: $description, name: $name, organization_id: $organization_id, tags: $tags, ProxySettings: {data: {proxy_mode: $proxy_mode, debug: $debug, default_identity_id: $default_identity_id, allow_noncloud_traffic: $allow_noncloud_traffic, default_mode: $default_mode}}, ProxyProviders: {data: $providers}, ProxyIdentities: {data: $identities}}) {
    returning {
      id
      description
      name
      organization_id
      status
      tags
      ProxySettings {
        id
        debug
        proxy_mode
        default_mode
        default_identity_id
        allow_noncloud_traffic
      }
      ProxyProviders {
        id
        provider_id
        enabled
      }
      ProxyIdentities {
        deleted
        id
        identity_id
        proxy_id
      }
    }
  }
}
    """

    def CreateProxyV2(self):
        query = gql(self._CreateProxyV2Query)
        variables = {
        }
        return self.execute(query, variable_values=variables)
