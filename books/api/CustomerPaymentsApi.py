#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.CustomerPaymentsParser import CustomerPaymentsParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'customerpayments/'
parser = CustomerPaymentsParser()
zoho_http_client = ZohoHttpClient()

class CustomerPaymentsApi:
    """CustomerPaymentsApi class is used:
     
    1.To list all the payments made by the customer.
    2.To get the details of the customer payment.
    3.To create a payment made by the customer.
    4.To update a payment made by the customer.
    5.To delete an existing customer payment.

    """

    def __init__(self, authtoken, organization_id):
        """Initialize Customer payment's api using user's authtoken 
               and organization id.
        
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
 
    def get_customer_payments(self, parameter=None):
        """List all customer payments with pagination.
 
        Args:
            parameter(dict, optional): Filter with which the list has 
                to be displayed. Default to None.

        Returns:
            instance: Customer payments list object.
        
        """
        response = zoho_http_client.get(base_url, self.details, self.headers, parameter) 
        return parser.customer_payments(response) 
  
    def get(self, payment_id):
        """Get details of a customer payment.

        Args:
            payment_id(str): Payment id of the customer.
 
        Returns:
            instance: Customer payment object.
        
        """
        url = base_url + payment_id
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_customer_payment(response) 
  
    def create(self, customer_payment):
        """Create a payment made by the customer.

        Args:
            customer_payment(instance): customer payment object.

        Returns:
            instance: customer payment object.

        """
        json_object = dumps(customer_payment.to_json())
        data = {
            'JSONString': json_object
            }
        response = zoho_http_client.post(base_url,self.details, self.headers,data)
        return parser.get_customer_payment(response) 
  
    def update(self, payment_id, customer_payment):
        """Update a payment made by a customer.
        
        Args:
            payment_id(str): Payment id.
            customer_payment(instance): Customer payment object.
       
        Returns:
            instance: Customer payment object.
 
        """
        url = base_url + payment_id
        json_object = dumps(customer_payment.to_json())
        data = {
            'JSONString': json_object
            }
        response = zoho_http_client.put(url,self.details, self.headers,data)
        return parser.get_customer_payment(response) 

    def delete(self, payment_id):
        """Delete an existing customer payment.

        Args:
            payment_id(str): Payment id.
 
        Returns:
            str: Success message ('The payment has been deleted.')
      
        """
        url = base_url + payment_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 

