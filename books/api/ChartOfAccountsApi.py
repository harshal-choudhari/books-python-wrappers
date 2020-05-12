#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.ChartOfAccountsParser import ChartOfAccountsParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'chartofaccounts/'
parser = ChartOfAccountsParser()
zoho_http_client = ZohoHttpClient()

class ChartOfAccountsApi:
    """Chart of Accounts Api is used to:
     
    1.List chart of Accounts.
    2.Get the details of an account.
    3.Creates an account with the given account type.
    4.Updates an existing account.
    5.Delete an existing account.
    6.Update the account status as active.
    7.Update the account status as inactive.
    8.List all invoices transactions for the given account.
    9.Deletes the transaction.

    """
    
    def __init__(self, authtoken, organization_id):
        """Initilaize Chart of accounts api using user's authtoken and 
            organization id.

        Args: 
            authotoken(str): User's Authtoken.
            organization id(str): User's Organization id.

        """
        self.headers = {
            'Authorization': 'Zoho-oauthtoken ' + authtoken,
        }
        self.details = {
            'organization_id': organization_id
            }

    def get_chart_of_accounts(self, parameters=None):
        """Get list of chart of accounts.

        Args:
            parameters(dict, optional): Filter with which the list has to be 
                displayed.

        Returns:
            instance: Chart of accounts list object.

        """
        resp = zoho_http_client.get(base_url, self.details, self.headers, parameters) 
        return parser.get_list(resp) 
  
    def get(self, account_id):    
        """Get details of an account.
 
        Args:
            account_id(str): Account id.

        Returns:
            instance: Chart of accounts object.

        """
        url = base_url + account_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_account(resp) 

    def create(self, account):
        """Create an account.

        Args:
            account(instance): Chart of accounts object.

        Returns:
            instance: Chart of accounts object.

        """
        json_object = dumps(account.to_json())
        data = { 
            'JSONString': json_object
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.get_account(resp) 
  
    def update(self, account_id, account):
        """Update an account.

        Args: 
            account_id(str): Account id.
            account(instance): Chart of accounts object.

        Returns:
            instance: Chart of accounts object.

        """
        url = base_url + account_id
        json_object = dumps(account.to_json())
        data = { 
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_account(resp) 

    def delete(self, account_id):
        """Delete an account.

        Args:
            account_id(str): Account id.

        Returns:
            str: Success message('The account has been deleted.').

        """
        url = base_url + account_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
  
    def mark_an_account_as_active(self, account_id):
        """Mark an account as active.

        Args: 
            account_id(str): Account id.

        Returns: 
            str: Success message('The account has been marked as active.').

        """
        data = {
            'JSONString': ''
            }
        url = base_url + account_id + '/active'
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp)
 
    def mark_an_account_as_inactive(self, account_id):
        """Mark an account as inactive.
        
        Args:
            account_id(str): Account id.

        Returns:
            str: Success message('The account has been marked as inactive.').

        """
        data = {
            'JSONString': ''
            }
        url = base_url + account_id + '/inactive'
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp)

    def list_of_transactions(self, parameters=None):
        """List all involved transactions for a given account.

        Args:
            parameters(dict): Dictionary containing values for account id, date amount 
                filter_by, transaction type and sort column. 

        Returns:
            instance: Transaction list object.

        """
        url = base_url + 'transactions'
        resp = zoho_http_client.get(url, self.details, self.headers, parameters) 
        return parser.get_transactions_list(resp) 

    def delete_a_transaction(self, transaction_id):
        """Delete the transaction.

        Args:
            transaction_id(str): Transaction id.

        Returns: 
            str: Success message('The transaction has been deleted.').

        """
        url = base_url + 'transactions/' + transaction_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

