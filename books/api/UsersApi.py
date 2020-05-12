#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.SettingsParser import SettingsParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'users/'
zoho_http_client = ZohoHttpClient()
parser = SettingsParser()

class UsersApi:
    """Uses Api class is used to 
 
    1.List of all users in an organization.
    2.10.Get the details of an user.
    3.Get the details of the current user.
    4.Create an user for an organization.
    5.Update the details of an existing user.
    6.Delete an existing user.
    7.Send invitation email to a user.
    8.Mark an inactive user as active.
    9.Mark an active user as inactive.
    
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
        
    def get_users(self, parameters=None):
        """Get the list of users in the organization.

        Args:
            parameters(dict, optional): Filter with which the list has to be 
                displayed.

        Returns: 
            instance: Users list object.

        """
        resp = zoho_http_client.get(base_url, self.details, self.headers, parameters)
        return parser.get_users(resp) 

    def get(self, user_id):
        """Get the details of a user.

        Args:
            user_id(str): User id.
  
        Returns:
            instance: User object.

        """
        url = base_url + user_id
        resp = zoho_http_client.get(url, self.details, self.headers) 
        return parser.get_user(resp) 

    def current_user(self):
        """Get details of a user.

        Returns:
            instance: User object.

        """
        url = base_url + 'me'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_user(resp) 

    def create(self, user):
        """Create a user for your organization.

        Args:
            user(instance): User object.

        Returns: 
            instance: User object.

        """
        json_obj = dumps(user.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.get_user(resp) 

    def update(self, user_id, user):
        """Update the details of an user.

        Args:
            user_id(str): User id.
            user(instance): User object.

        Returns:
            instance: User object.

        """
        url = base_url + user_id
        json_obj = dumps(user.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_user(resp) 

    def delete(self, user_id):
        """Delete a user associated to the organization.

        Args:
            user_id(str): User id.

        Returns:
            str: Success message('The user has been removed from your 
                organization.').

        """
        url = base_url + user_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def invite_user(self, user_id):
        """Send invitation email to a user.

        Args:
            user_id(str): User id.

        Returns:
            str: Success message('Your invitation has been sent.').
 
        """
        url = base_url + user_id + '/invite'
        data = { 
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp) 

    def mark_user_as_active(self, user_id):
        """Mark an inactive user as active.

        Args:
            user_id(str): User id.

        Returns:
            str: Success message('The user has been marked as active.').
 
        """
        url = base_url + user_id + '/active'
        data = { 
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp) 
 
    def mark_user_as_inactive(self, user_id):
        """Mark an active user as inactive.

        Args:
            user_id(str): User id.
 
        Returns:
            str: Success message('The user has been marked as inactive.').
      
        """
        url = base_url + user_id + '/inactive'
        resp = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(resp) 
