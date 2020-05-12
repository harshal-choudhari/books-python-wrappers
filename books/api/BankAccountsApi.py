#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.BankAccountsParser import BankAccountsParser 
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'bankaccounts/'
zoho_http_client  =  ZohoHttpClient()
parser  =  BankAccountsParser()

class BankAccountsApi:
    """Bank Accounts Api is used to 
    
    1.List all bank and credit card accounts of the organization.
    2.Get detailed look of a specified account.
    3.Create a bank account or a credit card account for an organization.
    4.Modify an existing account.
    5.Delete an existing bank account from an organization.
    6.Make an account inactive.
    7.Make an account active.
    8.Get the details of last imported statement.
    9.Delete the statement that was imported lastly.

    """
    def __init__(self, authtoken, organization_id):
        """Initialize Bank accounts api using user's authtoken and 
            organization id.
        
        Args: 
            authotoken(str): Authtoken.
            organization id(str): Organization id.

        """
        self.headers = {
            'Authorization': 'Zoho-oauthtoken ' + authtoken,
        }
        self.details = {
            'organization_id': organization_id
            }
  
    def get_bank_accounts(self, parameter=None):
        """List all bank and credit accounts of an organization.
       
        Args:
            parameter(dict, optional): Filter with which the list has to be
                displayed. Defaults to None.

        Returns:
            instance: Bank accounts list object.

        """
        resp = zoho_http_client.get(base_url, self.details, self.headers, parameter)
        return parser.get_list(resp) 

    def get(self, account_id):
        """Get bank account details.

        Args:
            account_id(str): Account id.

        Returns:
            instance: Bank accouts object.

        """
        url = base_url + account_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_account_details(resp) 

    def create(self, bank_account):
        """Create a bank account.
 
        Args: 
            bank_account(instance): Bank accounts object.
 
        Returns:
            instance: Bank accounts object.

        """
        json_object = dumps(bank_account.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.get_account_details(resp) 

    def update(self, account_id, bank_account):
        """Update an existing bank account.

        Args:
            account_id(str): Account id.
            bank_account(instance): Bank account object.

        Returns:
            instance: Bank account object.

        """
        url = base_url + account_id
        json_object = dumps(bank_account.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_account_details(resp)     

    def delete(self, account_id):
        """Delete an existing bank account.
 
        Args:
            account_id(str): Account id.

        Returns:
            str: Success message('The account has been deleted.').

        """
        url = base_url + account_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def deactivate_account(self, account_id):
        """Deactivate a bank account.

        Args:
            account_id(str): Account id.
 
        Returns:
            str: Success message('The account has been marked as inactive.').
         
        """
        url = base_url + account_id + '/inactive'
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp) 

    def activate_account(self, account_id):
        """Activate a bank account.

        Args:
            account_id(str): Account id.

            str: Success message('The account has been marked as active.').

        """
        url = base_url + account_id + '/active'
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp) 

    def get_last_imported_statement(self, account_id):
        """Get the details of previously imported statement for the account.

        Args: 
            account_id(str): Account id.

        Returns:
            instance: Statement object.

        """ 
        url = base_url + account_id + '/statement/lastimported'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_statement(resp) 
   
    def delete_last_imported_statement(self, account_id, statement_id):
        """Delete the statement that was previously imported.

        Args:
            account_id(str): Account id.
            statement_id(str): Statement id.

        Returns:
            str: Success message('You have successfully deleted the last imported 
                 statement.').

        Raises:
            Books Exception: If status is not '200' or '201'.

        """
        url = base_url + account_id + '/statement/' + statement_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

 
  
