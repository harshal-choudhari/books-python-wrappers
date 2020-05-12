#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.CreditNotesParser import CreditNotesParser
from os.path import basename
from json import dumps
from books.api.Api import Api

base_url = Api().base_url + 'creditnotes/'
parser = CreditNotesParser()
zoho_http_client = ZohoHttpClient()

class CreditNotesApi:
    """Creditnotes api class is used to 

    1.List Credits notes with pagination.
    2.Get details of a credit note.
    3.Create a credit note for a custoomer.
    4.Update an existing creditnote.
    5.Delete an existing creditnote.
    6.Change an existing creditnote status to open.
    7.Mark an existing creditnote as void.
    8.Email a creditnote to a customer.
    9.Get email history of a credit note.
    10.Get email content of a credit note.
    11.Update the billing address of an existing credit note.
    12.Update the shipping address of an existing credit note.
    13.Get all credit note pdf templates.
    14.Update the pdf template associated with the creditnote.
    15.List invooices to which the credit note is applied.
    16.Apply credit note to existing invoices.
    17.Delete the credits applied to an invoice.
    18.List all refunds with pagination.
    19.List all refunds of an existing credit note.
    20.Get refund of a particular credit note.
    21.Refund credit note amount.
    22.Update the refunded transaction.
    23.Delete a credit note refund.
    24.Get history and comments of a credit note.
    25.Add a comment to an existing credit note.
    26.Delete a credit note comment.

    """
      
    def __init__(self, authtoken, organization_id):
        """Initialize credit notes api using user's authtoken and organization 
            id.

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

    def get_credit_notes(self, parameter=None):
        """List all credit notes with pagination.

        Args:
            parameter(dict, optional): Filter with which the list has to be 
                displayed. Defaults to None.


        Returns:
            instance: Credit notes list object.
        
        Raises: 
            Books Exception: If status is '200' or '201'.
 
        """
        response = zoho_http_client.get(base_url, self.details, self.headers, parameter)
        return parser.creditnotes_list(response) 

    def get_credit_note(self, creditnote_id, print_pdf=None, accept=None):
        """Get details of a credit note.

        Args:
            creditnote_id(str): Credit note id.
            print_pdf(bool, optional): Export credit note pdf with default 
                option. Allowed values are true, false,on and off.

        Returns:
            instance: Credit note object.

        Raises:
            Books Exception: If status is not '200' or '201'.

        """
        url = base_url + creditnote_id
        if print_pdf is not None and accept is not None:
            query = {
                'print':str(print_pdf).lower(), 
                'accept':accept
                }
            response = zoho_http_client.getfile(url, self.details, self.headers, query)
            return response
        elif print_pdf is not None:
            query = {
                'print':str(print_pdf).lower()
                } 
            if print_pdf:
                query.update({
                    'accept':'pdf'
                    })
                response = zoho_http_client.getfile(url, self.details, self.headers, query)
                return response
            else:
                response = zoho_http_client.get(url, self.details, self.headers, query)
                return parser.get_creditnote(response) 
        elif accept is not None:
            query = {
                'accept':accept
                }
            response = zoho_http_client.getfile(url, self.details, self.headers, query)
            return response 
        else:
            response = zoho_http_client.get(url, self.details, self.headers)
            return parser.get_creditnote(response) 
  
    def create(self, credit_note, invoice_id=None, \
        ignore_auto_number_generation=None):
        """Creates a credit note.

        Args:
            credit_note(instance): Credit note object.
            invoice_id(str, optional): Invoice id for which invoice has to be 
                applied.
            ignore_auto_number_generation(bool, optional): True to ignore auto 
                number generation else False. If set True this parameter 
                becomes mandatory.
          
        Returns:
            instance: Credit note object.
 
        """
        json_object = dumps(credit_note.to_json())
        data = {
            'JSONString': json_object
            }
        if invoice_id is not None and ignore_auto_number_generation is not \
            None:
            query = {
                'invoice_id':invoice_id, 
                'ignore_auto_number_generation':ignore_auto_number_generation 
                }
        elif invoice_id is not None:
            query = {
                'invoice_id':invoice_id
                }
        elif ignore_auto_number_generation is not None:
            query = {
                'ignore_auto_number_generation':ignore_auto_number_generation
                }
        else:
            query = None
        response = zoho_http_client.post(base_url, self.details, self.headers, data, query)
        return parser.get_creditnote(response) 

    def update(self, credit_note_id, credit_note, \
        ignore_auto_number_generation=None):
        """Update an existing credit note.

        Args:
            credit_note_id(str): Credit note id.
            credit_note(instance): Credit note object.
            ignore_auto_number_generation(bool, optional): True to ignore auto 
                number generation. If this is set true then this parameter is 
                mandatory.

        Returns:
            instance: Credit note object.

        """   
        url = base_url + credit_note_id
        json_object = dumps(credit_note.to_json())
        data = {
            'JSONString': json_object
            }
        if ignore_auto_number_generation is not None:
            query = {
                'ignore_auto_number_generation':ignore_auto_number_generation
                } 
        else:
            query = None
        response = zoho_http_client.put(url, self.details, self.headers, data, query)
        return parser.get_creditnote(response)

    def delete(self, creditnote_id):
        """Delete an existing credit note.

        Args:
            creditnote_id(str): Credit note id.

        Returns: 
            str: Success message('The credit note has been deleted.').

        """
        url = base_url + creditnote_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 

    def convert_to_open(self, creditnote_id):
        """Change an existing credit note status to open.
        Args:
            creditnote_id(str): Credit note id.

        Returns: 
            str: Success message(the status of the credit note has been changed 
                to open.

        """
        url = base_url + creditnote_id  + '/status/open'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 

    def void_credit_note(self, creditnote_id):
        """Mark an existing credit note as void.

        Args:
            creditnote_id(str): Credit note id.

        Returns:
            str: Success message('The credit note has been marked as void.').

        """
        url = base_url + creditnote_id + '/status/void'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 
  
    def email_credit_note(self, creditnote_id, email, attachment=None,
                          customer_id=None):
        """Email a credit note to the customer.

        Args:
            creditnote_id(str): Creditnote id.
            email(instance): Email object.
            attachment(list of dict, optional): List of dictionary containing 
                details of the files to be attached.
            customer_id(str, optional): Id of the customer.

        Returns:
            str: Success message('Your credit note has been sent.').

        """  
        url = base_url + creditnote_id + '/email'
        json_object = dumps(email.to_json()) 
        data = {
            'JSONString': json_object
            }
        if attachment is not None and customer_id is not None:
            query = {
                'customer_id':customer_id
                }
            file_list = []
            for value in attachment:
                attachments = {
                    'attachments': {
                        'filename':basename(value),         
                        'content':open(value).read()
                        } 
                    }
                file_list.append(attachments)
        elif attachment is not None:
            file_list = []
            for value in attachment:
                attachments = {
                    'attachments': {
                        'filename':basename(value), 
                        'content':open(value).read()
                        }
                    }
                file_list.append(attachments)
            query = None
        elif customer_id is not None:
            query = {
                'customer_id': customer_id
                }
            file_list = None
        else:
            query = None
            file_list = None
        response = zoho_http_client.post(url, self.details, self.headers, data, query, 
                                         file_list)
        return parser.get_message(response) 

    def email_history(self, creditnote_id):
        """Get email history of a credit note.

        Args:
            creditnote_id(str): Credit note id.
        
        Returns: 
            instance: Email object.

        """
        url = base_url + creditnote_id + '/emailhistory'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.email_history(response) 

    def get_email_content(self, creditnote_id, email_template_id=None):
        """Get email content of a credit note.

        Args:
            creditnote_id(str): Creditnote id.
            email_template_id(str, optional): Email template id.

        Returns:
            instance): Email object.

        """
        url = base_url + creditnote_id + '/email'
        if email_template_id is not None:
            query = {
                'email_template_id': email_template_id
                }
        else:
            query = None
        response = zoho_http_client.get(url, self.details, self.headers, query)
        return parser.email(response) 
  
    def update_billing_address(self, creditnote_id, address, 
                               is_update_customer=None):
        """Update billing address.

        Args:
            creditnote_id(str): Credit note id.
            address(instance): Address object.
            is_update_customer(bool, optional): True to update customer else 
                False.

        Returns:
            instance: Address object.

        """
        url = base_url + creditnote_id + '/address/billing'
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
        return parser.get_billing_address(response)

    def update_shipping_address(self, creditnote_id, address, 
                                is_update_customer=None):
        """Update shipping address.

        Args:
            creditnote_id(str): Credit note id.
            address(instance): Address object.
            is_update_customer(bool, optional): True to update customer 
                else False.
        
        Returns:
            instance: Address object.

        """
        url = base_url + creditnote_id + '/address/shipping'
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

    def list_credit_note_template(self):
        """Get all credit note pdf templates.

        Returns:
            list of instance: List of templates object.

        """
        url = base_url + 'templates'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.list_templates(response) 
 
    def update_credit_note_template(self, creditnote_id, template_id):
        """Update credit note template.

        Args:
            creditnote_id(str): Credit note id.
            template_id(str): Template id.

        Returns:
            str: Success message('The credit note has been updated.').

        """
        url = base_url + creditnote_id + '/templates/' + template_id
        response = zoho_http_client.put(url, self.details, self.headers, '')
        return parser.get_message(response) 

#### Apply to Invoice------------------------------------------------------------------------------------------------------------

  
    def list_invoices_credited(self, creditnote_id): 
        """List invoices to which credit note is applied.

        Args:
            creditnote_id(str): Credit note id.

        Returns:
            list of instance: List of invoices credited object.
 
        Raises:
            Books Exception: If status is not '200' or '201'.

        """
        url = base_url + creditnote_id + '/invoices'  
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.list_invoices_credited(response) 
  
    def credit_to_invoice(self, creditnote_id, invoice):
        """List invoices to which the credited note is applied.

        Args:
            creditnote_id(str): Credit note id.
            invoice(instance): Invoice object.

        Returns:
            list of invoices: List of invoice objects.

        """
        url = base_url + creditnote_id + '/invoices'
        invoices = {
            'invoices': []
            }
        for value in invoice:
            data = {}
            data['invoice_id'] = value.get_invoice_id()
            data['amount_applied'] = value.get_amount_applied()
            invoices['invoices'].append(data)
        json_string = {
            'JSONString': dumps(invoices)
            }
        response = zoho_http_client.post(url, self.details, self.headers, json_string)
        return parser.credit_to_invoice(response)
      
    def delete_invoices_credited(self, creditnote_id, creditnote_invoice_id):
        """Delete the credits applied to an invoice.

        Args:
            creditnote_id(str): Credit note id.
            creditnote_invoice_id(str): Credit note invoice id.

        Returns:
            str: Success message('Credits applied to an invoice have been 
                 deleted.').

        """
        url = base_url + creditnote_id + '/invoices/' + creditnote_invoice_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 

##  REFUND-----------------------------------------------------------------------------------------------------------------------

    def list_credit_note_refunds(self, customer_id=None, sort_column=None):
        """List all refunds wiht pagination.

        Args:
            customer_id(str, optional): Customer id.
            sort_column(str, optional): Sort refund list. Allowed values are 
                refund_mode, reference_number, date, creditnote_number, 
                customer_name, amount_bcy and amount_fcy.

        Returns:
            instance: Credit notes refund list object.

        """       
        url = base_url + 'refunds'
        if customer_id is not None and sort_column is not None:
            parameter = {
                'customer_id':customer_id, 
                'sort_column':sort_column
                }
        elif sort_column is not None or customer_id is not None:
            parameter = {
                'sort_column': sort_column
                } if sort_column is not None else {
                'customer_id': customer_id
                }
        else:
            parameter = None
        response = zoho_http_client.get(url, self.details, self.headers, parameter)
        return parser.creditnote_refunds(response) 

    def list_refunds_of_credit_note(self, creditnote_id): 
        """List all refunds of an existing credit note.

        Args:
            creditnote_id(str): Credit note id.

        Returns:
            instance: Creditnotes refund list.

        """
        url = base_url + creditnote_id + '/refunds'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.creditnote_refunds(response)

    def get_credit_note_refund(self, creditnote_id, creditnote_refund_id):
        """Get credit note refund.

        Args:
            creditnote_id(str): Credit note id.
            creditnote_refund_id(str): Creditnote refund id.

        Returns:
            instance: Creditnote refund object.

        """       
        url = base_url + creditnote_id + '/refunds/' + creditnote_refund_id
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_creditnote_refund(response)
  
    def refund_credit_note(self, creditnote_id, creditnote):
        """Refund credit note amount.

        Args:
            creditnote_id(str): Credit note id.

        Returns:
            creditnote(instance): Credit note object.

        """
        url = base_url + creditnote_id + '/refunds'
        json_object = dumps(creditnote.to_json())
        data = { 
            'JSONString': json_object
            }
        response = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_creditnote_refund(response)
     
    def update_credit_note_refund(self, creditnote_id, creditnote_refund_id, 
                                  creditnote):
        """Update the refunded transaction.

        Args:
            creditnote_id(str): Credit note id.
            creditnote_refund_id(str): Credit note refund id.
            creditnote(instance): Credit note object.

        Returns:
            instance: Creditnote object.

        """
        url = base_url + creditnote_id + '/refunds/' + creditnote_refund_id
        json_object = dumps(creditnote.to_json())
        data = { 
            'JSONString': json_object
            }
        response = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_creditnote_refund(response) 

    def delete_credit_note_refund(self, creditnote_id, creditnote_refund_id): 
        """Delete a credit note refund.

        Args:
            creditnote_id(str): Credit note id.
            creditnote_refund_id(str): Credit note refund id.
  
        Returns:
            str: Success message('The refund has been successfully deleted.').

        """
        url = base_url + creditnote_id + '/refunds/' + creditnote_refund_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response)

## Comments and History----------------------------------------------------------------------------------------------------------


    def list_creditnote_comments_history(self, creditnote_id):
        """Get history and comments of a credit note.

        Args:
            creditnote_id(str): Credit note id.
 
        Returns:
            instance: Comments list object.

        """
        url = base_url + creditnote_id + '/comments'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.comments_list(response) 
  
    def add_comment(self, creditnote_id, comments):
        """Add a comment to an existing credit note.

        Args:
            creditnote_id(str): Credit note id.
            comments(instance): Comments object.

        Returns:
            instance: Comments object.

        """
        url = base_url + creditnote_id + '/comments'
        data = {}
        data['description'] = comments.get_description()
        json_string = {
            'JSONString': dumps(data)
            }
        response = zoho_http_client.post(url, self.details, self.headers, json_string)
        return parser.get_comment(response) 

    def delete_comment(self, creditnote_id, comment_id):
        """Delete a credit note comment.

        Args:
            creditnote_id(str): Credit note id.
            comment_is(str): Comment id.

        Returns:
            str: Success message('The comment has been deleted.').

        """
        url = base_url + creditnote_id + '/comments/' + comment_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 

