#$Id$#

from os.path import basename
from json import dumps
from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.InvoicesParser import InvoicesParser
from .Api import Api

base_url = Api().base_url + 'invoices/'
parser = InvoicesParser()
zoho_http_client = ZohoHttpClient()

class InvoicesApi:
    """Invoice Api class is used to:
    
    1.List all invoices with pagination.
    2.Get the details of an invoice.
    3.Create an invoice.
    4.Update an existing invoice.
    5.Delete an existing invoice.
    6.Mark a draft invoice as sent.
    7.Mark an invoice status as void.
    8.Mark a voided invoice as draft.
    9.Email an invoice to the customer.
    10.Send invoices to your customer by email.
    11.Get the email content of an email.
    12.Remind the customer about an unpaid invoice by email.
    13.Remind the customer abount unpaid invoices by email.
    14.Get the mail content of the payment reminder.
    15.Export maximum of 25 invoices as pdf.
    16.Export invoices as pdf and print them.
    17.Disable automated payment reminders for an invoice.
    18.Enable automated payment reminders for an invoice.
    19.Write off the invoice balance amount of an invoice.
    20.Cancel the write off amount of an invoice.
    21.Update the billing address for an existing invoice.
    22.Update the shipping address for an existing invoice.
    23.Get all invoice pdf templates.
    24.Update the pdf template associated with the invoice.
    25.Get the list of payments made for an invoice.
    26.Get the list of credits applied for an invoice.
    27.Apply the customer credits to an invoice.
    28.Delete a payment made to an invoice.
    29.Delete a particular credit applied to an invoice.
    30.Return a file attached to an invoice.
    31.Attach a file to an invoice.
    32.Send attachment while emailing the invoice.
    33.Delete the file attached to the invoice.
    34.Delete an expense receipt attached to an invoice.
    35.Get the complete history and comments of an invoice.
    36.Add a comment for an invoice.
    37.Update an existing comment of an invoice.
    38.Delete an invoice comment.

    """
    def __init__(self, authtoken, organization_id):
        """Initialize Invoice api using user's authtoken and organization 
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

    def get_invoices(self, parameter=None):
        """Get list of all invoices with pagination.

        Args:
            parameter(dict, optional): Filter with which the list has to be 
                displayed.
   
        Returns:
            instance: Invoice list instance.
 
        """
        response = zoho_http_client.get(base_url, self.details, self.headers, parameter)
        return parser.get_list(response)   
  
    def get(self, invoice_id, print_pdf=None, accept=None):
        """Get details of an invoice.
 
        Args: 
            invoice_id(str): Inovice id.
            print_pdf(bool): True to print invoice as pdf else False.
            accept(str): Format in which the invoice details has to be 
                downloaded. Default value is json. Allowed value is json, 
                pdf and html.

        Returns:
            instance or file: If accept is None invoice object is returned 
                else File containing invoice details is returned.
        
        """            
        url = base_url + invoice_id
        query = {}
        if print_pdf is not None and accept is not None:
            query = {
                'print': print_pdf, 
                'accept': accept
                }
            resp = zoho_http_client.getfile(url, self.details, self.headers, query)
            return resp
        elif print_pdf is not None:
             query = {'print': print_pdf} 
             if print_pdf is True:
                 query.update({'accept':'pdf'})
                 resp = zoho_http_client.getfile(url, self.details, self.headers, query)
                 return  resp
             else:
                 response = zoho_http_client.get(url, self.details, self.headers, query)
                 return parser.get(response) 
        elif accept is not None:
            query = {
                'accept': accept
                }
            resp = zoho_http_client.getfile(url, self.details, self.headers, query)
            return resp 
        else:
            response = zoho_http_client.get(url, self.details, self.headers)
            return parser.get(response)
   
    def create(self, invoice, send=None, ignore_auto_number_generation=None):
        """Creat an invoice.

        Args:
            invoice(instance): Invoice object.
            send(bool, optional): To send invoice to the cocntact persons 
                associated with the invoice. Allowed values are true and false.
            ignore_auto_number_generation(bool, optional): Ignore auto invoice 
                number generation for the invoice. This mandates the invoice 
                number. Allowed values are true and false.

        Returns:
            instance: Invoice object.

        """
        json_object = dumps(invoice.to_json())
        data = { 
            'JSONString': json_object
            }
        query = {}
        if send is not None and ignore_auto_number_generation is not None:
            query = {
                'send':send, 
                'ignore_auto_number_generation': ignore_auto_number_generation
                }         
        elif send is not None or ignore_auto_number_generation is not None:
            query = {
                'send': send
                } if send is not None else {
                    'ignore_auto_number_generation': \
                    ignore_auto_number_generation
                    }
        else: 
            query = None
        response = zoho_http_client.post(base_url, self.details, self.headers, data, query)
        return parser.get(response)  

    def update(self, invoice_id, invoice, ignore_auto_number_generation=None):
        """Update an existing invoice.

        Args:
            invoie_id(str): Invoice id.
            invoice(instance): Invoice object.
            ignore_auto_number_generation(bool, optional): Ignore auto invoice 
                number generation for the invoice. This mandates the invoice 
                number. Allowed values are true and false.

        Returns:
            instance: Invoice object.

        """
        url = base_url + invoice_id
        json_object = dumps(invoice.to_json())
        data = { 
            'JSONString': json_object
            }
        if ignore_auto_number_generation is not None:
            query = {
                'ignore_auto_number_generation': ignore_auto_number_generation
                }
        else:
            query = None
        response = zoho_http_client.put(url, self.details, self.headers, data, query)
        return parser.get(response) 
      
    def delete(self, invoice_id):
        """Delete an existing invoice.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            str: Success message('The invoice has been deleted.').

        """
        url = base_url + invoice_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 
   
    def mark_an_invoice_as_sent(self, invoice_id):
        """Mark an invoice as sent.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            str: Success message('Inovice status has been changed to sent.').
        
        """
        url = base_url + invoice_id + '/status/sent'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response)  

    def void_an_invoice(self, invoice_id): 
        """Mark an invoice as void.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            str: Success message('Invoice status has been changed to void.').
        
        """
        url = base_url + invoice_id + '/status/void'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response)   

    def mark_as_draft(self, invoice_id):
        """Mark a voided invoice as draft.

        Args: 
            invoice_id(str): Invoice id.

        Returns:
            str: Success message('Status of invoice changed form void to  
                    draft.').
 
        """
        url = base_url + invoice_id + '/status/draft/'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response)    

    def email_an_invoice(self, invoice_id, email, attachment=None, \
        send_customer_statement=None, send_attachment=None):
        """Email an invoice to the customer.

        Args:
            invoice_id(str): Invoice id.
            email(instance): Email object.
            attachment(list of dict, optional): List of dictionary objects 
                containing details of files to be attached.
            send_customer_statement(bool, optional): True to send customer 
                statement pdf with email else False.
            send_attachment(bool, optional): True to send the attachment with 
                mail else False.

        Returns:
            str: Success message('Your invoice has been sent.').

        """
        url = base_url + invoice_id + '/email'
        json_object = dumps(email.to_json())
        data = { 
            'JSONString': json_object
            }
        if attachment is not None and send_customer_statement is not None and \
            send_attachment is not None:
            query = {
                'send_customer_statement': send_customer_statement, 
                'send_attachment': send_attachment
                }
            file_list = []
            for value in attachment:
                attachments = {
                    'attachments': {
                        'filename': basename(value), 
                        'content':open(value).read()
                        }
                }
                file_list.append(attachments)
        elif attachment is not None and send_customer_statement is not None:
            query = {
                'send_customer_statement':send_customer_statement, 
                }
            file_list = []
            for value in attachment:
                attachments = {
                    'attachments': {
                        'filename': basename(value),
                        'content': open(value).read()
                        } 
                    }
                file_list.append(attachments)
        elif attachment is not None and send_attachment is not None:
            query = {
                'send_attachment':send_attachment
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
        elif send_customer_statement is not None and send_attachment is not None:
            query = {
                'send_customer_statement':send_customer_statement, 
                'send_attachment':send_attachment
                }
            file_list = None
        elif attachment is not None:
            file_list = []
            for value in attachment:
                attachments = {
                    'attachments': {
                        'filename': basename(value), 
                        'content':open(value).read()
                        }
                    }
                file_list.append(attachments)
            query = None
        elif send_customer_statement is not None:
            query = {
                'send_customer_statement':send_customer_statement, 
                }
            file_list = None
        elif send_attachment is not None:
            query = {
                'send_attachment':send_attachment
                }
            file_list = None
        else:
            query = None
            file_list = None
        response = zoho_http_client.post(url, self.details, self.headers, data, query, file_list)
        return parser.get_message(response) 

    def email_invoices(self, contact_id, invoice_ids, email=None, \
        snail_mail=None):
        """Send invoice to customers by email.

        Args:
            contact_id(list of str): List of Contact ids.
            invoice_ids(str): Comma separated Invoice ids which are to 
                be emailed.
            email(bool, optional): True to send via email.
            snail_mail(bool, optional): True to send via snail mail.

        Returns:
            str: Success message('Mission accomplished! We've sent all 
                the invoices.').

        """
        query = {
            'invoice_ids': invoice_ids
            }
        url = base_url + 'email'
        data = {}
        data['contacts'] = []
        for value in contact_id:
            contacts = {
                'contact_id':value, 
                'email':True, 
                'snail_mail': False
                }
            if (email is not None) and (snail_mail is not None):
                contacts = {
                    'contact_id':value, 
                    'email':email, 
                    'snail_mail':snail_mail
                    }
            data['contacts'].append(contacts)
        fields = {
            'JSONString': dumps(data)
            }    
        response = zoho_http_client.post(url, self.details, self.headers, fields, query)
        return parser.get_message(response) 

    def get_email_content(self, invoice_id, email_template_id=None):
        """Get the email content of an invoice.
 
        Args:
            invoice_id(str): Invoice id.
            email_template_id(str, optional): Email template id. If None 
                 default template id will be inputted.

        Returns:
            instance: Email object.

        """
        url = base_url + invoice_id + '/email'
        if email_template_id is not None:
            query = {
                'email_template_id':email_template_id
                }
        else:
            query = None
        response = zoho_http_client.get(url, self.details, self.headers, query)
        return parser.get_content(response) 

    def remind_customer(self, invoice_id, email, attachment=None, \
        send_customer_statement=None):      
        """Remind customers abount unpaid invoices.
      
        Args:
            invoice_id(str): Invoice id.
            email(instance): Email object.
            attachment(list of dict, optional): List of dictionary objects 
                containing details of files to be attached.
            send_customer_statement(bool, optional): True to send customer 
                statement along with email else False.
  
        Returns:
            str: Success message('Your payment reminder has been sent.').
 
        """
        url = base_url + invoice_id + '/paymentreminder'
        json_object = dumps(email.to_json())
        data = {
            'JSONString': json_object
            }
        if send_customer_statement is not None and attachment is not None:
           query = {
               'send_customer_statement':send_customer_statement
               }
           file_list = []
           for value in attachment:
               attachments = {
                   'attachments': {
                       'filename': basename(value), 
                       'content':open(value).read()
                       }
                   }
               file_list.append(attachments)
        elif send_customer_statement is not None:
            query = {
                'send_customer_statement':send_customer_statement
                }
            file_list = None
        elif attachment is not None:
            file_list = []
            for value in attachment:
                attachments = {
                    'attachments': {
                        'filename': basename(value), 
                        'content':open(value).read()
                        }
                    }
                file_list.append(attachments)
            query = None
        else:
            query = None
            file_list = None
        response = zoho_http_client.post(url, self.details, self.headers, data, query, file_list)
        return parser.get_message(response)  

    def bulk_invoice_reminder(self, invoice_id):
        """Remind customers about unpaid invoices.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            str: Success message('Success! All reminders have been sent.').

        """
        url = base_url + 'paymentreminder'
        invoice_ids = {
            'invoice_ids': invoice_id
            }
        response = zoho_http_client.post(url, self.details, self.headers, '', invoice_ids)
        return parser.get_message(response) 
 
    def get_payment_reminder_mail_content(self, invoice_id):
        """Get the mail content of the payment reminder.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            instance: Email object.

        """
        url = base_url + invoice_id + '/paymentreminder'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.payment_reminder_mail_content(response) 
 
    def bulk_export_invoices(self, invoice_id):
        """Export maximum of 25 invoices as pdf.
 
        Args:
            invoice_id(str): Comma separated invoice ids which are to be 
                exported as pdfs.
 
        Returns:
            file: Pdf file containing invoice details.
     
        """
        url = base_url + 'pdf'
        query = {
            'invoice_ids': invoice_id
            }
        response = zoho_http_client.getfile(url, self.details, self.headers, query)
        return response 
   
    def bulk_print_invoices(self, invoice_id):
        """Export invoices as pdf and print them.
 
        Args:
            invoice_id(str): Invoice id.

        Returns:
            file: File that has to be printed.

        """
        url = base_url + 'pdf'
        invoice_ids = {
            'invoice_ids': invoice_id
            }
        response = zoho_http_client.getfile(url, self.details, self.headers, invoice_ids)
        return response 
    
    def disable_payment_reminder(self, invoice_id):
        """Disable payment reminer.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            str: Success message('Reminders stopped.').

        """
        url = base_url + invoice_id + '/paymentreminder/disable'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 

    def enable_payment_reminder(self, invoice_id):
        """Enable payment reminder.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            str: Success message('Reminders enabled.').

        """
        url = base_url + invoice_id + '/paymentreminder/enable'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response)        
      
    def write_off_invoice(self, invoice_id):
        """Write off the invoice balance amount of an invoice.

        Args:
            invoice_id(str): Invoice id.
  
        Returns:
            str: Success message('Invoice has been written off.').

        """
        url = base_url + invoice_id + '/writeoff'  
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 
 
    def cancel_write_off(self, invoice_id):
        """Cancel the write off amount of an invoice.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            str: Success message('The writeoff done for this invoice 
                has been cancelled.').

        """
        url = base_url + invoice_id + '/writeoff/cancel'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 

    def update_billing_address(self, invoice_id, address, \
        is_update_customer=None):
        """Update billing address for the invoice.

        Args:
            invoice_id(str): Invoice id.
            address(instance): Address object.
            is_update_customer(bool, optional): True to update the address
                for all draft, unpaid invoice and future invoices.

        Returns:
            instance: Address object.

        """
        url = base_url + invoice_id + '/address/billing'
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

    def update_shipping_address(self, invoice_id, address, \
        is_update_customer=None):
        """Update shipping address for the invoice.

        Args:
            invoice_id(str): Invoice id.
            address(instance): Address object.
            is_update_customer(bool, optional): True to update the address 
                for all draft, unpaid invoice and future invoices.

        Returns:
            instance: Address object.

        """
        url = base_url + invoice_id + '/address/shipping'
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

    def list_invoice_templates(self):
        """Get all invoice pdf templates.

        Returns: 
            instance: Invoice template list object.

        """
        url = base_url + 'templates'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.invoice_template_list(response) 

    def update_invoice_template(self, invoice_id, template_id):
        """Update the pdf template associated with the invoice.

        Args:
            invoice_id(str): Invoice id.
            template_id(str): Tempalte id.
 
        Returns:
            str: Success message('Invoice information has been updated.').
        
        """
        url = base_url + invoice_id + '/templates/' + template_id
        response = zoho_http_client.put(url, self.details, self.headers, '')
        return parser.get_message(response) 

## Payments and Credits--------------------------------------------------------

    def list_invoice_payments(self, invoice_id):
        """List the payments made for an invoice.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            list of payments instance: List of Invoice payments list object.

        """
        url = base_url + invoice_id + '/payments'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.payments_list(response) 

    def list_credits_applied(self, invoice_id):
        """Get the list of credits applied for an invoice.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            list of credits instance: List of credits object.

        """
        url = base_url + invoice_id + '/creditsapplied'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.credits_list(response) 

    def apply_credits(self, invoice_id, payments_and_credits):
        """Apply the customer credits either from credit notes or 
            excess customer payments to an invoice.
 
        Args:
            invoice_id(str): Invoice id.
            payments_and_credits(instance): Payments object.

        Returns:
            instance: Payments and credits object.
 
        """
        url = base_url + invoice_id + '/credits'
        data = {}
        invoice_payments = []
        apply_credits = []
        for value in payments_and_credits.invoice_payments:
            payments = {}
            payments['payment_id'] = value.get_payment_id()
            payments['amount_applied'] = value.get_amount_applied()
            invoice_payments.append(payments)
        for value in payments_and_credits.apply_creditnotes:
            credits = {}
            credits['creditnote_id'] = value.get_creditnote_id()
            credits['amount_applied'] = value.get_amount_applied()
            apply_credits.append(credits)
        data['invoice_payments'] = invoice_payments
        data['apply_creditnotes'] = apply_credits
        json_string = {
            'JSONString': dumps(data)
            }
        response = zoho_http_client.post(url, self.details, self.headers, json_string)
        return parser.apply_credits(response) 

    def delete_payment(self, invoice_id, invoice_payment_id):
        """Delete a payment made to an invoice.

        Args:
            invoice_id(str): Invoice id.
            invoice_payment_id(str): Invoice payment id.

        Returns:
            str: Success message('The payment has been deleted.').
         
        """
        url = base_url + invoice_id + '/payments/' + invoice_payment_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 

    def delete_applied_credit(self, invoice_id, creditnotes_invoice_id):
        """Delete a particular credit applied to an invoice.

        Args:
            invoice_id(str): Invoice id.
            creditnotes_invoice_id(str): Creditnotes invoice id.
      
        Returns:
            str: Success message('Credits applied to an invoice have been 
                deleted.').

        """
        url = base_url + invoice_id + '/creditsapplied/' + \
              creditnotes_invoice_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 
        
## Attachment------------------------------------------------------------------

    def get_an_invoice_attachment(self, invoice_id, preview = None):
        """Get an invoice attachment.

        Args:
            invoice_id(str): Invoice id
            preview(bool): True to get the thumbnail of the attachment.
        Returns:
            file: File attached to the invoice.
 
        """
        url = base_url + invoice_id + '/attachment'
        query_string = {
                'preview': str(preview)
                } if preview is not None else None     
        response = zoho_http_client.getfile(url, self.details, self.headers, query_string)
        return response  

    def add_attachment_to_an_invoice(self, invoice_id, attachment, \
        can_send_in_mail=None):
        """Add a file to an invoice.

        Args:
            invoice_id(str): Invoice id.
            attachment(list of dict): List of dict containing details of the 
                files to be attached.
            can_send_in_mail(bool, optional): True to send the attachment with 
                the invoice when emailed.

        Returns:
            str: Success message('Your file has been successfully attached to 
                the invoice.').

        """
        url = base_url + invoice_id + '/attachment'
        file_list = []
        for value in attachment:
            attachments = {
                'attachment': {
                    'filename':basename(value), 
                    'content':open(value).read()
                    }
                }
            file_list.append(attachments)
            if can_send_in_mail is not None:
                query = {
                    'can_send_in_mail':can_send_in_mail
                    }
            else:
                query = None
        data = {
            'JSONString': ''
            }
        response = zoho_http_client.post(url, self.details, self.headers, data, query, \
                                         file_list)
        return parser.get_message(response) 

    def update_attachment_preference(self, invoice_id, can_send_in_mail):
        """Update whether to send attached file while emailing the invoice.
        
        Args:
            invoice_id(str): Invoice id.
            can_send_in_mail(bool): Boolean to send attachment with the 
                invoice when emailed.
        
        Returns:
            str: Success message('Invoice information has been updated.').
        
        """     
        url = base_url + invoice_id + '/attachment'
        query = {
            'can_send_in_mail':can_send_in_mail, 
            }
        data = {
            'JSONString': ''
            }
        response = zoho_http_client.put(url, self.details, self.headers, data, query)
        return parser.get_message(response) 

    def delete_an_attachment(self, invoice_id):
        """Delete the file attached to the invoice.

        Args:
            invoice_id(str): Invoice id.

        Returns:
            str: Success message('Your file is no longer attached 
                to the invoice.').

        """
        url = base_url + invoice_id + '/attachment'
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 
 
    def delete_expense_receipt(self, expense_id):
        """Delete the expense receipts attached to an invoice which 
            is raised from an expense.

        Args:
            expense_id: Expense id.
            
        Returns:
            str: Success message('The attached expense receipt has 
                been deleted.').
  
        """
        url = base_url + 'expenses/' + expense_id + '/receipt'
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 

  
#### Comments and History -----------------------------------------------------



    def list_invoice_comments_history(self, invoice_id):
        """Get the complete history and comments of an invoice.

        Args:
            invoice_id(str): Invoice_id.
         
        Returns:
            instance: Comments list object.

        """ 
        url = base_url + invoice_id + '/comments'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.comments_list(response) 
  
    def add_comment(self, invoice_id, comments):
        """Add comment for an invoice.
 
        Args:
            invoice_id(str): Invoice id.
            comments(instance): Comments object.
 
        Returns:
            str: Success message('Comments added.').

        """
        url = base_url + invoice_id + '/comments'
        data = {}
        data['payment_expected_date'] = comments.get_payment_expected_date()
        data['description'] = comments.get_description()
        data['show_comment_to_clients'] = \
        comments.get_show_comment_to_clients()
        json_string = {
            'JSONString': dumps(data)
            }
        response = zoho_http_client.post(url, self.details, self.headers, json_string)
        return parser.get_comment(response) 

    def update_comment(self, invoice_id, comment_id, comments):
        """Update an existing comment of an invoice.

        Args:
            invoice_id(str): Invoice id.
            comment_id(str): Comment id.
            comments(instance): Comments object.
        
        Returns:
            instance: Comments object.

        """
        url = base_url + invoice_id + '/comments/' + comment_id
        data = {}
        data['description'] = comments.get_description()
        data['show_comment_to_clients'] = \
        comments.get_show_comment_to_clients()
        json_string = {
            'JSONString': dumps(data)
            }
        response = zoho_http_client.put(url, self.details, self.headers, json_string)
        return parser.get_comment(response) 
  
    def delete_comment(self, invoice_id, comment_id):
        """Delete an invoice comment.

        Args:
            invoice_id(str): Invoice id.
            comment_id(str): Comment id.

        Returns:
            str: Success message.('The comment has been deleted.').

        """
        url = base_url + invoice_id + '/comments/' + comment_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response) 
   
 
