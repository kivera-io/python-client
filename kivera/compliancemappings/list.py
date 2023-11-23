from gql import gql
from typing import Sequence

class listMethods:

    _ListComplianceMappingsQuery = """
    query ListComplianceMappings {
    ComplianceMappings{
        framework
        control
    }
}
    """

    def ListComplianceMappings(self):
        query = gql(self._ListComplianceMappingsQuery)
        variables = {
        }
        operation_name = "ListComplianceMappings"
        return self.execute(query, variable_values=variables, operation_name=operation_name)
