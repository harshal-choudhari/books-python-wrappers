#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.JournalsParser import JournalsParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'journals/'
zoho_http_client = ZohoHttpClient()
parser = JournalsParser()

class JournalsApi:
    """Journals Api class is used to:
     
    1.Get journals list.
    2.Get the details of the journal.
    3.Create a journal.
    4.Updates the journal with given information.
    5.Deletes the given journal.

    """
    def __init__(self, authtoken, organization_id):
        """Initialize parameters for Journals Api.

        Args:
            authtoken(str): User's authtoken.
            organization_id(str): User's organization id.

        """        
        self.headers = {
            'Authorization': 'Zoho-oauthtoken ' + authtoken,
        }
        self.details = {
            'organization_id': organization_id
            }
  
    def get_journals(self, parameter=None):
        """Get Journals list.
 
        Args:
            parameter(dict): Filter with which the list has to be displayed.

        Returns:
            instance: Journals List object.

        """    
        resp = zoho_http_client.get(base_url, self.details, self.headers, parameter)
        return parser.get_list(resp)

    def get(self, journal_id):
        """Get details of a journal.

        Args:
            journal_id(str): Journal id.
 
        Returns:
            instance: Journals object.

        """  
        url = base_url + journal_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_journal(resp) 
  
    def create(self, journal):
        """Create a journal.
 
        Args:
            journal(instance): Journal object. 
 
        Returns:
            instance: Journal object.

        """     
        json_object = dumps(journal.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.get_journal(resp) 

    def update(self, journal_id, journal):
        """Update an existing journal.

        Args:
            journal_id(str): Journal id.
            journal(instance): Journal object.

        Returns:
            instance: Journal object.

        """
        url = base_url + journal_id
        json_object = dumps(journal.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_journal(resp) 

    def delete(self, journal_id):
        """Delete the given journal.

        Args:
            journal_id(str): Journal id.

        """
        url = base_url + journal_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

