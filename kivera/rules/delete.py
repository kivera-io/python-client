from gql import gql
from typing import Sequence

class deleteMethods:

    _DeleteRuleQuery = """
    mutation DeleteRule($rule_id: Int!) {
  delete_Rules(where: {id: {_eq: $rule_id}}) {
    affected_rows
  }
}
    """

    def DeleteRule(self, rule_id: int):
        query = gql(self._DeleteRuleQuery)
        variables = {
            "rule_id": rule_id,
        }
        return self.execute(query, variable_values=variables)

    _DeleteRulesQuery = """
    mutation DeleteRules($ids: [Int!]!) {
  delete_ProfileRules(where: {rule_id: {_in: $ids}}) {
    affected_rows
  }
  delete_Rules(where: {id: {_in: $ids}}) {
    affected_rows
  }
}
    """

    def DeleteRules(self, ids: Sequence[int]):
        query = gql(self._DeleteRulesQuery)
        variables = {
            "ids": ids,
        }
        return self.execute(query, variable_values=variables)
