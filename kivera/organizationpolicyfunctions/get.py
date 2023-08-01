
from gql import gql
from typing import Sequence

class getMethods:

    _GetOrganizationPolicyFunctionQuery = """
    query GetOrganizationPolicyFunction {
    OrganizationPolicyFunctions{
        function
        id
        organization_id
    }
}
    """

    def GetOrganizationPolicyFunction(self):
        query = gql(self._GetOrganizationPolicyFunctionQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)

    _GetOrganizationPolicyFunctionV2Query = """
    query GetOrganizationPolicyFunctionV2($id: Int!,) {
    OrganizationPolicyFunctions_by_pk(id: $id) {
        function
        id
        organization_id
    }
}
    """

    def GetOrganizationPolicyFunctionV2(self, id: int):
        query = gql(self._GetOrganizationPolicyFunctionV2Query)
        variables = {
            "id": id,
        }
        return self.execute(query, variable_values=variables)
