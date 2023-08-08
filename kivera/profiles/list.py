from gql import gql
from typing import Sequence

class listMethods:

    _ListProfilesQuery = """
    query ListProfiles {
  Profiles {
    description
    id
    name
    organization_id
    tags
    ProfileRules(where: {deleted: {_eq: false}}) {
      rule_id
    }
    IdentityProfiles_aggregate(where: {deleted: {_eq: false}}) {
      aggregate {
        count
      }
    }
    ProfileRules_aggregate(where: {deleted: {_eq: false}}) {
      aggregate {
        count
      }
    }
  }
}
    """

    def ListProfiles(self):
        query = gql(self._ListProfilesQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
