#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.BankRulesParser import BankRulesParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'bankaccounts/rules/'
zoho_http_client = ZohoHttpClient()
parser = BankRulesParser()

class BankRulesApi:
    """This class is used to 

    1.Fetch all the rules created for a specified bank or credit card account.
    2.Get details of a specific rule.
    3.Create a rule.
    4.Update an existing rule.
    5.Delete a rule.

    """
    def __init__(self, authtoken, organization_id):
        """Initialize Bank rules Api using user's authtoken and organization 
            id.

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
    
    def get_rules(self, account_id):
        """Get list of rules.

        Args:
            account_id(str): Account id for which the rules have to be listed.
        
        Returns: 
            instance: Bank rules list object.

        """
        param = {
            'account_id': account_id
            }
        resp = zoho_http_client.get(base_url, self.details, self.headers, param)
        return parser.get_rules(resp) 

    def get(self, rule_id):
        """Get details of a rule.
 
        Args:
            rule_id(str): Rule id.

        Returns:
            instance: Bank rules object.

        """
        url = base_url + rule_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_rule(resp) 

    def create(self, rule):
        """Create a rule.

        Args:
            rule(instance): Bank rule object.

        Returns:
            instance: Bank rule object.

        """
        json_object = dumps(rule.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.get_rule(resp)
   
    def update(self, rule_id, rule):
        """Update an existing rule.

        Args:
            rule_id(str): Rule id.

        Returns:
            instance: Bank rule object.

        """
        url = base_url + rule_id
        json_object = dumps(rule.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_rule(resp) 

    def delete(self, rule_id):
        """Delete an existing rule.

        Args:
            rule_id(str): Rule id.

        Returns:
            str: Success message('The rule has been deleted.').

        """
        url = base_url + rule_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
      
