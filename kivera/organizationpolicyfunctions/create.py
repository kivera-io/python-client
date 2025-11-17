from gql import gql
from typing import Sequence

class createMethods:

    _CreateAndUpdateOrganizationPolicyFunctionQuery = """
    mutation CreateAndUpdateOrganizationPolicyFunction(
    $org_id: Int!,
    $function: String!,
    # @genqlient(omitempty: true)
    $name: String,
    # @genqlient(omitempty: true)
    $rego_version: String
) {
    insert_OrganizationPolicyFunctions_one(object: {
        organization_id: $org_id,
        function: $function,
        name: $name,
        rego_version: $rego_version
    }, on_conflict: {constraint: organizationpolicyfunctions_uniq_key, update_columns: [function, name, rego_version]}) {
        organization_id
        id
        function
        rego_version
    }
}
    """

    def CreateAndUpdateOrganizationPolicyFunction(self):
        query = gql(self._CreateAndUpdateOrganizationPolicyFunctionQuery)
        variables = {
        }
        operation_name = "CreateAndUpdateOrganizationPolicyFunction"
        operation_type = "write"
        return self.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
            operation_type=operation_type,
        )
