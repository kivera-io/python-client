# Kivera Python Client

This library generates a wrapper around the gql Client library from a set of .graphql/.gql files.

### Installation

```
pip3 install git+ssh://git@github.com/kivera-io/python-client.git
```

### Example Usage
```
import kivera
import json

creds = "/path/to/user-api-key.json"
with open(creds) as f:
  creds_json = json.load(f)
client = kivera.Client(credentials=creds_json)
print(client.ListOrganizationPolicyFunctions())
print(client.ListRulesV4())
```

# Useful Links

- [Quick Start Guide](https://docs.kivera.io/docs/quick-start-guide)
- [Generate API Keys](https://docs.kivera.io/docs/my-profile#generate-api-keys)
