from gql import gql
from typing import Sequence

class getMethods:

    _GetCountersAggregateQuery = """
    query GetCountersAggregate {
  Counters_aggregate {
    aggregate {
      sum {
        counter_total_request
        counter_notifies
        counter_denials
        counter_accepts
      }
    }
  }
  Proxies_aggregate {
    aggregate {
      count
    }
  }
}
    """

    def GetCountersAggregate(self):
        query = gql(self._GetCountersAggregateQuery)
        variables = {
        }
        operation_name = "GetCountersAggregate"
        return self.execute(query, variable_values=variables, operation_name=operation_name)
