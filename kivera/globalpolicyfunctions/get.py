
from gql import gql
from typing import Sequence

class getMethods:

    _GetGlobalPolicyFunctionQuery = """
    query GetGlobalPolicyFunction($gpfn: String!) {
  GlobalPolicyFunctions(where: {name: {_eq: $gpfn}}) {
    name
    function
    id
  }
}
    """

    def GetGlobalPolicyFunction(self, gpfn: str):
        query = gql(self._GetGlobalPolicyFunctionQuery)
        variables = {
            "gpfn": gpfn,
        }
        return self.execute(query, variable_values=variables)
