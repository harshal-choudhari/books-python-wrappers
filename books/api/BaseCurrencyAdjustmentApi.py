#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.BaseCurrencyAdjustmentParser import BaseCurrencyAdjustmentParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'basecurrencyadjustment/'
zoho_http_client = ZohoHttpClient()
parser = BaseCurrencyAdjustmentParser()

class BaseCurrencyAdjustmentApi:
    """Base Currency Adjsutment Api is used to:
    
    1.List base currency adjustment.
    2.Get base currency adjustment details.
    3.List account details for base currency adjustment.
    4.Creates a base currency adjustment.
    5.Deletes a base currency adjustment.

    """
 
    def __init__(self, authtoken, organization_id):
        """Initialize parameters for Base currency adjustment api.

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

    def get_base_currency_adjustments(self, parameters=None):
        """List base currency adjustment.

        Args:
            parameters(dict, optional): Filter with whichj the list has to 
                be displayed. Defaults to None.

        Returns:
            instance: Base currency adjustment list object.

        """
        resp = zoho_http_client.get(base_url, self.details, self.headers, parameters) 
        return parser.get_list(resp) 

    def get(self, base_currency_adjustment_id):
        """Get base currency adjustment details.

        Args:
            base_currency_adjustment_id(str): Base currency adjustment id.

        Returns: 
            instance: Base currency adjustment object.

        """
        url = base_url + base_currency_adjustment_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_base_currency_adjustment(resp) 

    def list_account_details(self, parameters):
        """List account details for base currency adjustments.

        Args:
            parameters(dict): Parameters with which the list has to be 
                displayed.

        Returns:
            instance: Base currency adjustment object.

        """
        url = base_url + 'accounts'
        resp = zoho_http_client.get(url, self.details, self.headers, parameters)
        return parser.list_account_details(resp)

    def create(self, base_currency_adjustment, account_id): 
        """Create base currency adjustment.

        Args: 
            base_currency_adjustment(instance): Base currency adjustment 
                object.
            account_ids(str): Account ids.

        Returns:
            instance: Base currency adjustment object.

        """
        json_object = dumps(base_currency_adjustment.to_json())
        data = {
            'JSONString': json_object
            }
        account_ids = {
            'account_ids': account_id
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data, account_ids)
        return parser.get_base_currency_adjustment(resp) 

    def delete(self, base_currency_adjustment_id):
        """Delete an existing base currency adjustment.

        Args:
            base_currency_adjustment_id(str): Base currency adjustment id.

        Returns:
            str: Success message('The selected base currency adjustment has 
                been deleted.').
 
        """
        url = base_url + base_currency_adjustment_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp)

