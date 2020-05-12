#$Id$#

from os.path import basename
from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.EstimatesParser import EstimatesParser
from .Api import Api
from json import dumps

base_url = Api().base_url + 'estimates/'
parser = EstimatesParser()
zoho_http_client = ZohoHttpClient()

class EstimatesApi:
    """Estimates Api class is used to:
   
    1.List all estimates with pagination.
    2.Get the details of an estimate.
    3.Create an estimate.
    4.Update an existing estimate.
    5.Delete an existing estimate.
    6.Mark a draft estimate as sent.
    7.Mark a sent estimate as accepted.
    8.Mark a sent estimate as declined.
    9.Email an estimate to the customer.
    10.Send estimates to your customer by email.
    11.Get the email content of an estimate.
    12.Export maximum of 25 pdfs as single pdf.
    13.Export estimates as pdf and print them.
    14.Update the billing address for the estimate.
    15.Update the shipping address for the estimate.
    16.Get all estimate pdf templates.
    17.Update the pdf template associated with the template.
    18.Get the complete history and comments of an estimate.
    19.Add a comment for an estimate.
    20.Update an existing comment of an estimate.
    21.Delete an estimate comment.

    """
    def __init__(self, authtoken, organization_id):
        """Initialize Estimates api using user's authtoken and 
            organization id.

        Args:
            authtoken(str): Authtoken(str): User's authtoken.
            organization_id(str): User's organization id.

        """
        self.headers = {
            'Authorization': 'Zoho-oauthtoken ' + authtoken,
        }
        self.details = {
            'organization_id': organization_id
            }
  
    def get_estimates(self, parameter=None):
        """Get list of estimates with pagination.

        Args:
            parameter(dict, optional): Filter with which the list has to be 
                dispalyed.

        Returns:
            instance: Invoice list object.

        """  
        response = zoho_http_client.get(base_url, self.details, self.headers, parameter)
        return parser.get_list(response) 

    def get(self, estimate_id, print_pdf=None, accept=None):   
        """Get details of an estimate.
 
        Args:
            estimate_id(str): Estimate id.
            print_pdf(bool, None): True to print pdf else False.
            accept(str, None): Get the details in particular format such as 
                json/pdf/html. Default format is json. Allowed values are json,
                pdf and html.

        Returns: 
            instance: Estimate object.
        
        """
        url = base_url + estimate_id
        query = {}
        if print_pdf is not None and accept is not None:
            query = {
                'print':print_pdf, 
                'accept':accept
                }
            resp = zoho_http_client.getfile(url, self.details, self.headers, query)
            return resp
        elif print_pdf is True:
            query = {
                'print':print_pdf, 
                'accept':'pdf'
                } 
            resp = zoho_http_client.getfile(url, self.details, self.headers, query)
            return resp
        elif accept is not None:
            query = {
                'accept':accept
                }
            resp = zoho_http_client.getfile(url, self.details, self.headers, query)
            return resp 
        else:
            response = zoho_http_client.get(url, self.details, self.headers)
            return parser.get_estimate(response) 

    def create(self, estimate, send=None, ignore_auto_number_generation=None):
        """Create an estimate.

        Args:
            estimate(instance): Estimate object.
            send(bool, optional): True to send estimate to the contact persons 
                associated with the estimate. Allowed values are true and false.
            ignore_auto_number_generation(bool, optional): True to ignore auto 
                estimate number generation for this estimate. Allowed values 
                are true and false.

        Returns:
            instance: Invoice object.

        """
        query = {}
        if send is not None and ignore_auto_number_generation is not None:
           query = {
               'send':send,  
               'ignore_auto_number_generation':ignore_auto_number_generation
               }
        elif send is not None or ignore_auto_number_generation is not None:
             query = {
                 'send': send
                 } if send is not None else {
                 'ignore_auto_number_generation': ignore_auto_number_generation
                 }
        else:
            query = None
        json_object = dumps(estimate.to_json())
        data = {
            'JSONString': json_object
            }
        response = zoho_http_client.post(base_url, self.details, self.headers, data, query)
        return parser.get_estimate(response)     

    def update(self, estimate_id, estimate, 
               ignore_auto_number_generation=None):
        """Update an existing estimate.
 
        Args:
            estimate_id(str): Estiamte id.
            estiamte(instance): Estiamte object.
            ignore_auto_number_generation(bool, optional): True to ignore auto 
                estimate number generation for this estimate. Allowed values 
                are true and false.

        Returns:
            instance: Estimates object.

        """
        url = base_url + estimate_id   
        query = {}
        if ignore_auto_number_generation is not None:
            query = {
                'ignore_auto_number_generation': ignore_auto_number_generation
                }
        else:
            query = None
        json_object = dumps(estimate.to_json())
        data = {
            'JSONString': json_object
            }
        response = zoho_http_client.put(url, self.details, self.headers, data) 
        return parser.get_estimate(response)
    
    def delete(self, estimate_id):
        """Delete an existing estimate.

        Args:
            estimate_id(str): Estimate id.

        Returns:
            str: Success message('The estimate has been deleted.').

        """ 
        url = base_url + estimate_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response)

    def mark_an_estimate_as_sent(self, estimate_id):
        """Mark a draft estimate as sent.

        Args:
            estimate_id(str): Estimate id.

        Returns:
            str: Success message('Estimate status has been changed to Sent.').

        """
        url = base_url + estimate_id + '/status/sent'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 

    def mark_an_estimate_as_accepted(self, estimate_id):
        """Mark a sent estimate as accepted.

        Args: 
            estimate_id(str): Estimate id.

        Returns:
            str: Success message('Estimate status has been changed to sent.').
 
        """
        url = base_url + estimate_id + '/status/accepted'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 
   
    def mark_an_estimate_as_declined(self, estimate_id):
        """Mark a sent estimate as declined.

        Args:
            estimate_id(str): Estiamte id.

        Returns:
            str: Success message('Estimate status has been changed to 
                accepted.').

        """
        url = base_url + estimate_id + '/status/declined'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 
  
    def email_an_estimate(self, estimate_id, email, attachment=None):
        """Email an estimate to the customer.

        Args:
            estimate_id(str): Estimate id.
            email(instance): Email object. 
            attachment(list of dict): List of dictionary containing details 
                about files to be attached.

        Returns:
            instance: Email object.

        """
        url = base_url + estimate_id + '/email'
        json_object = dumps(email.to_json())
        data = {
            'JSONString': json_object
            }
        if attachment is not None:
            file_list = []
            for value in attachment:
                attachments = {
                    'attachments': {
                        'filename': basename(value), 
                        'content':open(value).read()
                        } 
                }
                file_list.append(attachments)
        else:
            file_list = None
        response = zoho_http_client.post(url, self.details, self.headers, data, None, \
                   file_list) 
        return parser.get_message(response) 
  
    def email_estimates(self, estimate_id):
        """Email estimates to the customer.

        Args: 
            estimate_id(str): Estimate id.

        Returns: 
            str: Success message('Mission accomplished.').

        """
        url = base_url + 'email'
        estimate_ids = {
            'estimate_ids': estimate_id
            }
        response = zoho_http_client.post(url, self.details, self.headers, '', \
                   estimate_ids)
        return parser.get_message(response) 

    def get_estimate_email_content(self, estimate_id, email_template_id=None):
        """Get estimate email content.

        Args:
            estiamte_id(str): Estiamte id.
            email_template_id(str): Email template id.

        Returns:
            instance: Email object.

        """
        url = base_url + estimate_id + '/email'
        query = {}
        if email_template_id is not None:
            query = {
                'email_template_id':email_template_id
                }
        else:
            query = None
        response = zoho_http_client.get(url, self.details, self.headers, query)
        return parser.get_email_content(response) 
 
    def bulk_export_estimates(self, estimate_id):
        """Export maximum of 25 estimates as pdf.

        Args:
            estimate_id(str): Estimate id.

        Returns:
            file: Pdf containing details of estimate.

        """
        url = base_url + 'pdf'
        query = {
            'estimate_ids': estimate_id
            }
        response = zoho_http_client.getfile(url, self.details, self.headers, query)
        return response 
  
    def bulk_print_estimates(self, estimate_ids):
        """Export estimates as pdf and print them.

        Args: 
            estimate_ids(str): Estimate ids.

        Returns:
            file: Pdf containing details of estimate.

        """
        url = base_url + 'print'
        query = {
            'estimate_ids': estimate_ids
            }
        response = zoho_http_client.getfile(url, self.details, self.headers, query)
        return response

   
    def update_billing_address(self, estimate_id, address, 
                               is_update_customer=None):
        """Update billing address.

        Args:
            estimate_id(str): Estiamte id.
            address(instance): Address object.
            is_update_customer(bool, optional): True to update customer.

        Returns:
            instance: Address object.

        """
        url = base_url + estimate_id + '/address/billing' 
        json_object = dumps(address.to_json())
        data = {
            'JSONString': json_object
            }
        if is_update_customer is not None:
            query = {
                'is_update_customer':is_update_customer
                }
        else: 
            query = None
        response = zoho_http_client.put(url, self.details, self.headers, data, query)
        return parser.get_billing_address(response) 

    def update_shipping_address(self, estimate_id, address, 
                                is_update_customer=None):
        """Update shipping address.

        Args: 
            estimate_id(str): Estimate id.
            address(instance): Address object.
            is_update_customer(bool, optional): True to update customer 
                else False.

        Returns:
            instance: Address object.

        """
        url = base_url + estimate_id + '/address/shipping'
        json_object = dumps(address.to_json())
        data = {
            'JSONString': json_object
            }
        if is_update_customer is not None:
            query = {
                'is_update_customer': is_update_customer
                }
        else:
            query = None
        response = zoho_http_client.put(url, self.details, self.headers, data, query)
        return parser.get_shipping_address(response)
 
    def list_estimate_template(self):
        """List all estimate pdf templates.

        Returns:
            instance: Template list object.

        """
        url = base_url + 'templates'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.estimate_template_list(response)
  
    def update_estimate_template(self, estimate_id, template_id):
        """Update estimate template.

        Args:
            estimate_id(str): Estimate id.
            template_id(str): Template id.

        Returns:
            str: Success message('Estimate information has been updated.').
        
        """
        url = base_url + estimate_id + '/templates/' + template_id
        response = zoho_http_client.put(url, self.details, self.headers, '')
        return parser.get_message(response)

# Comments and History

    def list_comments_history(self, estimate_id):
        """Get complete history and comments.

        Args:
            estiamte_id(str): Estimate id.

        Returns:
            list of instance: list of comments object.
 
        """ 
        url = base_url + estimate_id + '/comments'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_comments(resp)
  
    def add_comment(self, estimate_id, description, show_comment_to_clients):
        """Add a comment for an estimate.

        Args:
            estimate_id(str): Estimate id.
            description(str): Description.
            show_comment_to_clients(bool): True to show comment to clients.

        Returns:
            instance: Comments object.

        """
        url = base_url + estimate_id + '/comments'
        data = {}
        data['description'] = description
        data['show_comment_to_clients'] = show_comment_to_clients
        field = {
            'JSONString': dumps(data)
            }
        resp = zoho_http_client.post(url, self.details, self.headers, field)
        return parser.get_comment(resp)

    def update_comment(self, estimate_id, comment_id, description, 
                       show_comment_to_clients):
        """Update an existing comment.

        Args:
            estimate_id(str): Estimate id.
            comment_id(str): Comment id.
            description(str): Description.
            show_comments_to_clients(bool): True to show comments to clients.
         
        Returns:
            instance: Comments object.
       
        """
        url = base_url +estimate_id + '/comments/' + comment_id
        data = {} 
        data['description'] = description
        data['show_comment_to_clients'] = show_comment_to_clients
        field = {
            'JSONString': dumps(data)
            }
        resp = zoho_http_client.put(url, self.details, self.headers, field)
        return parser.get_comment(resp) 
  
    def delete_comment(self, estimate_id, comment_id):
        """Delete an existing comment.

        Args:
            comment_id(str): Comment id.

        Returns:
            str: Success message('The comment has been deleted.').
       
        """
        url = base_url + estimate_id + '/comments/' + comment_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
   
   
