#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.RecurringInvoiceParser import RecurringInvoiceParser 
from .Api import Api
from json import dumps

base_url = Api().base_url + 'recurringinvoices/'
parser = RecurringInvoiceParser()
zoho_http_client = ZohoHttpClient()

class RecurringInvoicesApi:
    """Recurring invoice api class is used:
    
    1.To list all the recurring invoices with pagination.
    2.To get details of a recurring invoice.
    3.To create a recurring invoice.
    4.To update an existing recurring invoice.
    5.To delete an existing recurring invoice.
    6.To stop an active recurring invoice.
    7.To resume a stopped recurring invoice.
    8.To update the pdf template associated with the recurring invoice.
    9.To get the complete history and comments of a recurring invoice.

    """

    def __init__(self, authtoken, organization_id):
        """Initialize Contacts Api using user's authtoken and organization id.

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

    def get_recurring_invoices(self, parameter=None): 
        """List of recurring invoices with pagination.

        Args:
            parameter(dict, optional): Filter with which the list has to be 
                displayed. Defaults to None.

        Returns:
            instance: Recurring invoice list object.

        """
        response = zoho_http_client.get(base_url, self.details, self.headers, parameter) 
        return parser.recurring_invoices(response)  
  
    def get_recurring_invoice(self, recurring_invoice_id):
        """Get recurring invoice details.
        
        Args:
            recurring_invoice_id(str): Recurring invoice id.

        Returns:
            instance: Recurring invoice object.

        """
        url = base_url + recurring_invoice_id
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.recurring_invoice(response)  

    def create(self, recurring_invoice):
        """Create recurring invoice.
        
        Args:
            recurring_invoice(instance): Recurring invoice object.

        Returns:
            instance: Recurring invoice object.

        """
        json_object = dumps(recurring_invoice.to_json())
        data = {
            'JSONString': json_object
            }
        response = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.recurring_invoice(response)  

    def update(self, recurring_invoice_id, recurring_invoice):
        """Update an existing recurring invoice.

        Args:
            recurring_invoice_id(str): Recurring invoice id.
            recurring_invoice(instance): Recurring invoice object.

        Returns:
            instance: Recurring invoice object.

        """
        url = base_url + recurring_invoice_id
        json_object = dumps(recurring_invoice.to_json())
        data = {
            'JSONString': json_object
            }
        response = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.recurring_invoice(response)  
    
    def delete(self, recurring_invoice_id): 
        """Delete an existing recurring invoice.
     
        Args:
            recurring_invoice_id(str): Recurring invoice id.
 
        Returns:
            str: Success message('The recurring invoice has been deleted.').
 
        """
        url = base_url + recurring_invoice_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 

    def stop_recurring_invoice(self, recurring_invoice_id):
        """Stop an active recurring invoice.
      
        Args: 
            recurring_invoice_id(str): Recurring invoice id.

        Returns:
            str: Success message ('The recurring invoice has been stopped.').

        """
        url = base_url + recurring_invoice_id + '/status/stop'
        response = zoho_http_client.post(url, self.details, self.headers, '') 
        return parser.get_message(response)  

    def resume_recurring_invoice(self, recurring_invoice_id):
        """Resume an active recurring invoice.
      
        Args: 
            recurring_invoice_id(str): Recurring invoice id.

        Returns:
            str: Success message ('The recurring invoice has been activated.').

        """
        url = base_url + recurring_invoice_id + '/status/resume'
        response = zoho_http_client.post(url, self.details, self.headers, '') 
        return parser.get_message(response) 

    def update_recurring_invoice_template(self, 
                                          recurring_invoice_id, template_id):
        """Update the pdf template associated with the recurring invoice.
      
        Args: 
            recurring_invoice_id(str): Recurring invoice id.
            template_id(str): Template id.

        Returns:
            str: Success message ('Recurring invoice information has been
                                  updated.').

        """
        url = base_url + recurring_invoice_id + '/templates/' + template_id
        response = zoho_http_client.put(url, self.details, self.headers, '')
        return parser.get_message(response)  
 
    def list_recurring_invoice_history(self, recurring_invoice_id):
        """List the complete history and comments of a recurring invoice.

        Args:
            recurring_invoice_id(str): Recurring invoice id.

        Returns:
            instance: Recurring invoice history and comments list object.

        """
        url = base_url + recurring_invoice_id + '/comments'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.recurring_invoice_history_list(response) 

      
      
