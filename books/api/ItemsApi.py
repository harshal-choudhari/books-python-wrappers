#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.SettingsParser import SettingsParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'items/'
zoho_http_client = ZohoHttpClient()
parser = SettingsParser()

class ItemsApi:
    """Items Api class is used to 

    1.List items.
    2.Get an item.
    3.Create an item.
    4.Update an item.
    5.Delete an item.
    6.Mark item as active.
    7.Mark item as inactive.
     
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
        
    def list_items(self): 
        """Get the list of all active items with pagination.

        Returns: 
            instance: Items list object.

        """
        resp = zoho_http_client.get(base_url, self.details, self.headers)
        return parser.get_items(resp) 

    def get(self, item_id):
        """Get details of an item.

        Args:
            item_id(str): Item id.

        Returns:
            instance: Item object.

        """
        url = base_url + item_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_item(resp) 
    
    def create(self, item):
        """Create a new item.

        Args:
            item(instance): Item object.

        Returns:
            instance: Item object.

        """
        json_obj = dumps(item.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.get_item(resp) 

    def update(self, item_id, item):
        """Update an existing item.

        Args:
            item_id(str): Item id.
            item(instance): Item object.

        Returns:
            instance: Item object.
 
        """
        url = base_url + item_id 
        json_obj = dumps(item.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data) 
        return parser.get_item(resp) 

    def delete_item(self, item_id):
        """Delete an item.

        Args:
            item_id(str): Item id.

        Returns:
            str: Success message('The item has been deleted.').

        """ 
        url = base_url + item_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
    
    def mark_item_as_active(self, item_id):
        """Mark an item as active.

        Args:
            item_id(str): Item id.
 
        Returns:
            str: Success message('The item has been marked as active.').
   
        """
        url = base_url + item_id + '/active'
        data = { 
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp) 

    def mark_item_as_inactive(self, item_id):
        """Mark an item as inactive.

        Args:
            item_id(str): Item id.

        Returns:
            str: Success message('The item has been marked as inactive.').

        """
        url = base_url + item_id + '/inactive'
        data = { 
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp) 
