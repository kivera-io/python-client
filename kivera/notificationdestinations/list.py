
from gql import gql
from typing import Sequence

class listMethods:

    _ListNotificationDestinationsQuery = """
    query ListNotificationDestinations {
  NotificationDestinations {
    id
    name
    destination_type
    org_id
    config
    description
    NotificationMonitorDestinations {
      id
      monitor_id
    }
  }
}
    """

    def ListNotificationDestinations(self):
        query = gql(self._ListNotificationDestinationsQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
