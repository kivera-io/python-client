from gql import gql
from typing import Sequence

class listMethods:

    _ListManagedRulesQuery = """
    query ListManagedRules {
    ManagedRules{
        id
        type_id
        description
        policy
        config
        tags
        version
        risk_rating
        compliance_mappings
        Service {
            id
            GlobalService {
                id
                name
                Provider {
                    id
                    name
                }
                Services {
                    id
                    inspection
                }
            }
        }
    }
}
    """

    def ListManagedRules(self):
        query = gql(self._ListManagedRulesQuery)
        variables = {
        }
        operation_name = "ListManagedRules"
        return self.execute(query, variable_values=variables, operation_name=operation_name)
