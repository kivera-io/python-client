
from gql import gql
from typing import Sequence

class getMethods:

    _GetRuleDependenciesByRuleIdQuery = """
    query GetRuleDependenciesByRuleId($rule_id: Int!) {
    RuleDependencies(where: {rule_id: {_eq: $rule_id}, deleted: {_eq: false}}) {
        id
        rule_id
        dependent_rule_id
        Rule {
            description
            Service {
                id
                GlobalService {
                    id
                    name
                    Provider {
                        id
                        name
                    }
                }
            }
        }
        RuleDependenciesResources {
            rule_dependencies_id
            locked
        }
    }
}
    """

    def GetRuleDependenciesByRuleId(self, rule_id: int):
        query = gql(self._GetRuleDependenciesByRuleIdQuery)
        variables = {
            "rule_id": rule_id,
        }
        return self.execute(query, variable_values=variables)
