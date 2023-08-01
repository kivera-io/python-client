
from gql import gql
from typing import Sequence

class createMethods:

    _CreateRuleQuery = """
    mutation CreateRule($config: jsonb!,$description: String!, $service_id: Int!, $enable_cfn_scan: Boolean!, $enforce: Boolean!, $log_request_body: Boolean!) {
  insert_Rules_one(object: {config: $config, description: $description, service_id: $service_id, enable_cfn_scan: $enable_cfn_scan, enforce: $enforce, log_request_body: $log_request_body}) {
    config
    description
    id
    service_id
  }
}
    """

    def CreateRule(self, config: dict, description: str, service_id: int, enable_cfn_scan: bool, enforce: bool, log_request_body: bool):
        query = gql(self._CreateRuleQuery)
        variables = {
            "config": config,
            "description": description,
            "service_id": service_id,
            "enable_cfn_scan": enable_cfn_scan,
            "enforce": enforce,
            "log_request_body": log_request_body,
        }
        return self.execute(query, variable_values=variables)

    _CreateRuleV4Query = """
    mutation CreateRuleV4($config: jsonb = "", $description: String!, $service_id: Int!, $enable_cfn_scan: Boolean = false, $enforce: Boolean = true, $log_request_body: Boolean = true, $dependencies_enabled: Boolean = false, $tags: jsonb! = [], $rule_dependencies: [RuleDependencies_insert_input!] = [], $policy: String!) {
  insert_Rules(objects: {config: $config, description: $description, service_id: $service_id, enable_cfn_scan: $enable_cfn_scan, enforce: $enforce,  log_request_body: $log_request_body, dependencies_enabled: $dependencies_enabled,  tags: $tags,  RuleDependencies: {data: $rule_dependencies}, policy: $policy }) {
    returning {
      id
      log_request_body
      enforce
      enable_cfn_scan
      description
      dependencies_enabled
      service_id
      tags
      policy
      RuleDependencies {
        dependent_rule_id
        deleted
      }
      Service {
        GlobalService {
          provider_id
        }
      }
    }
  }
}
    """

    def CreateRuleV4(self, description: str, service_id: int, policy: str, config: dict = None, enable_cfn_scan: dict = None, enforce: dict = None, log_request_body: dict = None, dependencies_enabled: dict = None, tags: dict = None, rule_dependencies: Sequence[dict] = None):
        query = gql(self._CreateRuleV4Query)
        variables = {
            "config": config,
            "description": description,
            "service_id": service_id,
            "enable_cfn_scan": enable_cfn_scan,
            "enforce": enforce,
            "log_request_body": log_request_body,
            "dependencies_enabled": dependencies_enabled,
            "tags": tags,
            "rule_dependencies": rule_dependencies,
            "policy": policy,
        }
        return self.execute(query, variable_values=variables)

    _CreateRulesV4Query = """
    mutation CreateRulesV4($objects: [Rules_insert_input!]!) {
  insert_Rules(objects: $objects) {
    returning {
      config
      description
      id
      service_id
      enforce
      enable_cfn_scan
      log_request_body
      tags
      policy
    }
  }
}
    """

    def CreateRulesV4(self, objects: Sequence[dict]):
        query = gql(self._CreateRulesV4Query)
        variables = {
            "objects": objects,
        }
        return self.execute(query, variable_values=variables)
