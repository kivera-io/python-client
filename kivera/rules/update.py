from gql import gql
from typing import Sequence

class updateMethods:

    _UpdateRuleQuery = """
    mutation UpdateRule($rule_id: Int!, $description: String!, $service_id: Int!, $config: jsonb!, $enable_cfn_scan: Boolean!, $enforce: Boolean!, $log_request_body: Boolean!) {
  update_Rules_by_pk(pk_columns: {id: $rule_id}, _set: {config: $config, description: $description, service_id: $service_id, enable_cfn_scan: $enable_cfn_scan, enforce: $enforce, log_request_body: $log_request_body}) {
    id
    Service {
      id
    }
  }
}
    """

    def UpdateRule(self, rule_id: int, description: str, service_id: int, config: dict, enable_cfn_scan: bool, enforce: bool, log_request_body: bool):
        query = gql(self._UpdateRuleQuery)
        variables = {
            "rule_id": rule_id,
            "description": description,
            "service_id": service_id,
            "config": config,
            "enable_cfn_scan": enable_cfn_scan,
            "enforce": enforce,
            "log_request_body": log_request_body,
        }
        return self.execute(query, variable_values=variables)

    _UpdateRuleV4Query = """
    mutation UpdateRuleV4($id: Int!, $config: jsonb!, $dependencies_enabled: Boolean!, $description: String!, $enforce: Boolean!, $enable_cfn_scan: Boolean!, $log_request_body: Boolean!, $policy: String!,$tags: jsonb! = []) {
  update_Rules(where: {id: {_eq: $id}}, _set: {config: $config, dependencies_enabled: $dependencies_enabled, description: $description, enforce: $enforce, enable_cfn_scan: $enable_cfn_scan, log_request_body: $log_request_body,  policy: $policy, tags: $tags}) {
    returning {
      dependencies_enabled
      description
      enable_cfn_scan
      enforce
      policy
      id
      log_request_body
      tags
    }
  }
}
    """

    def UpdateRuleV4(self, id: int, config: dict, dependencies_enabled: bool, description: str, enforce: bool, enable_cfn_scan: bool, log_request_body: bool, policy: str, tags: dict = None):
        query = gql(self._UpdateRuleV4Query)
        variables = {
            "id": id,
            "config": config,
            "dependencies_enabled": dependencies_enabled,
            "description": description,
            "enforce": enforce,
            "enable_cfn_scan": enable_cfn_scan,
            "log_request_body": log_request_body,
            "policy": policy,
            "tags": tags,
        }
        return self.execute(query, variable_values=variables)
