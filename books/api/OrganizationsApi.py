#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.SettingsParser import SettingsParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'organizations/'
zoho_http_client = ZohoHttpClient()
parser = SettingsParser()

class OrganizationsApi:
    """Organization api is used to

    1.List organizations.
    2.Get the details of an organization.
    3.Create an organization.
    4.Update an organization.
    
    """
    def __init__(self, authtoken, organization_id):
        """Initialize Settings Api using authtoken and organization id.

        Args:
            authtoken(str): User's Authtoken.
            organization_id(str): User's Organization id.

        """
        self.headers = {
            'Authorization': 'Zoho-oauthtoken ' + authtoken,
        }
        self.details = {
            'organization_id': organization_id
            }

    def get_organizations(self):
        """Get list of all organizations.

        Returns:
            instance: Organizations list object.

        """
        resp = zoho_http_client.get(base_url, self.details, self.headers) 
        return parser.get_organizations(resp) 
 
    def get(self, organization_id):
        """Get organization id.

        Args:
            organization_id(str): Organization id.

        Returns:
            instance: Organization object.

        """
        url = base_url + organization_id
        resp = zoho_http_client.get(url, self.details, self.headers) 
        return parser.get_organization(resp) 

    def create(self, organization):
        """Create an organization.

        Args:
            organization(instance): Organization object.

        Returns:
            instance: Organization object.

        """
        json_obj = dumps(organization.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.get_organization(resp)

    def update(self, organization_id, organization):
        """Update organization.

        Args:
            organization_id(str): ORganization id.
            organization(instance): Organization object.

        Returns:
            instance: Organization object.

        """
        url = base_url +  organization_id
        json_obj = dumps(organization.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_organization(resp) 
