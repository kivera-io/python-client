
from gql import gql
from typing import Sequence

class listMethods:

    _ListServicesQuery = """
    query ListServices {
  Services {
    id
    organization_id
    inspection
    GlobalService {
      id
      name
      title
      description
      created_at
      Provider {
        id
        name
      }
    }
  }
}
    """

    def ListServices(self):
        query = gql(self._ListServicesQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
