#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.BillsParser import BillsParser
from books.api.Api import Api
from os.path import basename
from json import dumps

base_url = Api().base_url + 'bills/'
zoho_http_client = ZohoHttpClient()
parser = BillsParser()

class BillsApi:
    """Bills Api is used to

    1.List all bills with pagination
    2.Get the details of a bill.
    3.Create a bill received from a vendor.
    4.Update an existing bill.
    5.delete an existing bill.
    6.Mark a bill status as void.
    7.Mark a void bill as open.
    8.Update the billing address.
    9.Get the list of payments made for the bill.
    10.Apply the vendor credits from excess vendor payments to a bill. 
    11.Delete a payment made to a bill.
    12.Returns a file attached to the bill.
    13.Attach a file to a bill.
    14.Delete the file attached to a bill.
    15.Get the cmplete history and comments of a bill.
    16.Add a comment for a bill.
    17.Delete a bill comment.

    """
    def __init__(self, authtoken, organization_id):
        """Initialize Bills api using user's authtoken and organization id.

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

    def get_bills(self, parameter=None):
        """List all bills with pagination.

        Args:
            parameter(dict, optional): Filter with which the list has to be 
                displayed.

        Returns:
            instance: Bill list object.
 
        """
        resp = zoho_http_client.get(base_url, self.details, self.headers, parameter) 
        return parser.get_list(resp) 

    def get(self, bill_id):
        """Get the details of a bill.

        Args:
            bill_id(str): Bill id.

        Returns:
            instance: Bill object.

        """
        url = base_url + bill_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_bill(resp) 

    def create(self, bill, attachment=None):
        """Create a bill received from the vendor.

        Args:
            bill(instance): Bill object.
            attachment(file, optional): File to be attached with the bill. 
                Allowed extensions are gif, png, jpeg, jpg, bmp and pdf.

        Returns:
            instance: Bill object.
 
        """        
        json_object = dumps(bill.to_json())
        data = {
            'JSONString': json_object
            }
        if attachment is None:
            attachments = None
        else: 
            attachments = [{
                'attachment': {
                    'filename': basename(attachment), 
                    'content': open(attachment).read()
                    } 
                }]
        resp = zoho_http_client.post(base_url, self.details, self.headers, data, None, \
                                     attachments)
        return parser.get_bill(resp) 

    def update(self, bill_id, bill, attachment=None):
        """Update an existing bill.

        Args:
            bill_id(str): Bill id.
            bill(instance): Bill object.
            attachment(file, optional): File to be attached with the bill. 
                Allowed extensions are gif, png, jpeg, jpg, bmp and pdf.
 
        Returns:
            instance: Bill object.
 
        """
        url = base_url + bill_id
        json_object = dumps(bill.to_json())
        data = {
            'JSONString': json_object
            }
        if attachment is None:
            attachments = None
        else: 
            attachments = [{
                'attachment': {
                    'filename': basename(attachment), 
                    'content': open(attachment).read()
                    } 
                }]
        resp = zoho_http_client.put(url, self.details, self.headers, data, None, \
                                     attachments)
        return parser.get_bill(resp) 

    def delete(self, bill_id):
        """Delete an existing bill.

        Args:
            bill_id(str): Bill id.

        Returns: 
            str: Success message('The bill has been deleted.').
 
        """
        url = base_url + bill_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def void_a_bill(self, bill_id):
        """Mark a bill status as void.
 
        Args:
            bill_id(str): Bill id.

        Returns:
            str: Success message('The bill has been marked as void.').

        """
        url = base_url + bill_id + '/status/void'
        resp = zoho_http_client.post(url, self.details, self.headers, '') 
        return parser.get_message(resp) 
  
    def mark_a_bill_as_open(self, bill_id):
        """Mark a void bill as open.
 
        Args: 
            bill_id(str): Bill id.

        Returns:
            str: Success message('The status of the bill has been changed from 
                 void to open.').

        """
        url = base_url + bill_id + '/status/open'
        resp = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(resp) 
  
    def update_billing_address(self, bill_id, billing_address):
        """Update the billing address for the bill.

        Args:
            bill_id(str): Bill id.
            billing_address(instance): Billing address object.
 
        Returns:
            str: Success message('Billing address update.').

        """
        url = base_url + bill_id + '/address/billing'
        json_object = dumps(billing_address.to_json())
        data = { 
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_message(resp) 
 
    def list_bill_payments(self, bill_id):
        """Get the list of payments made for the bill.

        Args:
            bill_id(str): Bill id.

        Returns:
            instance: Payments list object.

        """
        url = base_url + bill_id + '/payments'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_payments_list(resp)
  
    def apply_credits(self, bill_id, bill_payments):
        """Apply the vendor credits from excess vendor payments to a bill.

        Args: 
            bill_id(str): Bill id.
            bill_payments(list of instance): list of payments object.

        Returns:
            str: Success message('Credits have been applied to the bill.').
 
        """ 
        url = base_url + bill_id + '/credits'
        data = {}
        bill_payments_list = []
        for value in bill_payments:
            bill_payment = {}
            bill_payment['payment_id'] = value.get_payment_id()
            bill_payment['amount_applied'] = value.get_amount_applied()
            bill_payments_list.append(bill_payment)

        data['bill_payments'] = bill_payments_list
        json_string = {
            'JSONString': dumps(data)
            }
        resp = zoho_http_client.post(url, self.details, self.headers, json_string)
        return parser.get_message(resp) 

    def delete_a_payment(self, bill_id, bill_payment_id):
        """Delete a payment made to a bill.
 
        Args:
            bill_id(str): Bill id.
            bill_payment_id(str): Bill payment id.

        Returns:
            str: Success message('The payment has been deleted.').
 
        Raises:
            Books Exception: If status is not '200' or '201'.

        """
        url = base_url + bill_id + '/payments/' + bill_payment_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def get_a_bill_attachment(self, bill_id, preview=None):
        """Get the file attached to the bill.
 
        Args:
            bill_id(str): Bill id.
            preview(bool, optional): True to get the thumbnail of the 
                attachment else False.
 
        Returns:
            file: File attached to the bill.
 
        """
        if preview is not None: 
            query = {
                'preview': preview
                }
        else:
            query = None
        url = base_url + bill_id + '/attachment'
        resp = zoho_http_client.getfile(url, self.details, self.headers, query) 
        return resp
 
    def add_attachments_to_a_bill(self, bill_id, attachment):
        """Attach a file to a bill.

        Args:
            bill_id(str): Bill id.
            attachment(file): File to attach. Allowed extensions are gif, png, 
                jpeg, jpg, bmp, pdf, xls, xlsx, doc, docx.

        Returns:
            str: Success message('The document has been deleted.').

        """
        url = base_url + bill_id + '/attachment'
        attachments = [{
                'attachment': {
                    'filename': basename(attachment), 
                    'content': open(attachment).read()
                    } 
                }] 
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data, None, attachments)
        return parser.get_message(resp) 

    def delete_an_attachment(self, bill_id):
        """Delete the file attached to a bill.
        
        Args:
            bill_id(str): Bill id.
 
        Returns:
            str: Success message('The attachment has been deleted.').
  
        """
        url = base_url + bill_id + '/attachment'
        resp = zoho_http_client.delete(url, self.details, self.headers) 
        return parser.get_message(resp) 

    def list_bill_comments_and_history(self, bill_id):
        """Get the complete history and comments of a bill.
  
        Args:
            bill_id(str): Bill id.

        Returns: 
            instance: Comments list object.

        """
        url = base_url + bill_id + '/comments'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_comments(resp) 

    def add_comment(self, bill_id, description):
        """Add a comment for a bill.

        Args:
            bill_id(str): Bill id.
            description(str): Description.
 
        Returns:
            str: Success message('Comments added.').

        """
        url = base_url + bill_id + '/comments'
        data = {
            'description': description 
            }
        json_string = {
            'JSONString': dumps(data)
            }
        resp = zoho_http_client.post(url, self.details, self.headers, json_string)
        return parser.get_comment(resp) 

    def delete_a_comment(self, bill_id, comment_id):
        """Delete a bill comment.

        Args:
            bill_id(str): Bill id.
            comment_id(str): Comment id.
 
        Returns: 
            str: Success message('The comment has been deleted.').
 
        Raises: 
            Books Exception: If status is '200' or '201'.

        """
        url = base_url + bill_id + '/comments/' + comment_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
  
