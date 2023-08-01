
from gql import gql
from typing import Sequence

class listMethods:

    _ListOrganizationQuery = """
    query ListOrganization {
    Organizations {
        billing_contact
        company_name
        domain
        email_domain
        id
        max_total_request_count
        Memberships {
            MembershipRoles {
                Role {
                    id
                    role_name
                }
            }
        }
    }
}
    """

    def ListOrganization(self):
        query = gql(self._ListOrganizationQuery)
        variables = {
        }
        return self.execute(query, variable_values=variables)
