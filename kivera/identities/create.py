from gql import gql
from typing import Sequence

class createMethods:

    _CreateAwsTenantIdentityQuery = """
    mutation CreateAwsTenantIdentity($name: String!, $description: String!, $organization_id: Int!, $tags: jsonb! = [], $type_id: Int!, $identity_type: identity_type!, $profiles: [IdentityProfiles_insert_input!] = []) {
  insert_Identities(objects: {
    name: $name,
    description: $description,
    organization_id: $organization_id,
    type_id: $type_id,
    tags: $tags,
    identity_type: $identity_type,
    IdentityProfiles: {data: $profiles},
    AwsTenants: {data: {}},
  }){
    returning {
      id
      name
      description
      organization_id
      type_id
      status
      tags
      identity_type
      AwsTenants {
        id
        account_id
        unique_id
        verified
        identity_id
        provider_id
        role_arn
      }
    }
  }
}
    """

    def CreateAwsTenantIdentity(self, name: str, description: str, organization_id: int, type_id: int, identity_type: dict, tags: dict = None, profiles: Sequence[dict] = None):
        query = gql(self._CreateAwsTenantIdentityQuery)
        variables = {
            "name": name,
            "description": description,
            "organization_id": organization_id,
            "tags": tags,
            "type_id": type_id,
            "identity_type": identity_type,
            "profiles": profiles,
        }
        return self.execute(query, variable_values=variables)

    _CreateIdentityQuery = """
    mutation CreateIdentity($name: String!, $description: String!, $config: jsonb!, $organization_id: Int!, $tags: jsonb!, $type_id: Int!, $identity_type: identity_type!, $profiles: [IdentityProfiles_insert_input!] = []) {
  insert_Identities(objects: {
    name: $name,
    config: $config,
    description: $description,
    organization_id: $organization_id,
    type_id: $type_id,
    status: true,
    tags: $tags,
    identity_type: $identity_type,
    IdentityProfiles: {data: $profiles}}) {
    returning {
      description
      organization_id
      status
      config
      id
      name
      type_id
      tags
    }
  }
}
    """

    def CreateIdentity(self, name: str, description: str, config: dict, organization_id: int, tags: dict, type_id: int, identity_type: dict, profiles: Sequence[dict] = None):
        query = gql(self._CreateIdentityQuery)
        variables = {
            "name": name,
            "description": description,
            "config": config,
            "organization_id": organization_id,
            "tags": tags,
            "type_id": type_id,
            "identity_type": identity_type,
            "profiles": profiles,
        }
        return self.execute(query, variable_values=variables)
