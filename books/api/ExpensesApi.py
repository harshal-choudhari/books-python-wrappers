#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.ExpensesParser import ExpensesParser
from os.path import basename
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'expenses/'
parser = ExpensesParser()
zoho_http_client = ZohoHttpClient()

class ExpensesApi:
    """Expenses Api is used to:
    
    1.List expenses with pagination.
    2.Get the details of an expense.
    3.Create a billable or non-billable expense.
    4.Update an existing expense.
    5.Delete an expense.
    6.Get history and comments of an expense.
    7.Returns the receipt attached to an expense.
    8.Attach a receipt to an expense.
    9.Delete the receipt attached to the expense.

    """
    def __init__(self, authtoken, organization_id):
        """Initialize Expenses Api using user's authtoken and organization 
            id.
 
        Args: 
            authtoken(str): User's Authtoken.
            organization_id(str): User's organization id.

        """
        self.headers = {
            'Authorization': 'Zoho-oauthtoken ' + authtoken,
        }
        self.details = {
            'organization_id': organization_id
            }
  
    def get_expenses(self, parameter=None): 
        """List expenses with pagination.
 
        Args:
            parameter(dict, optional): Filter with which expenses list has to 
                be displayed. Defaults to None.

        Returns:
            instance: Expenses list object.

        """
        resp = zoho_http_client.get(base_url, self.details, self.headers, parameter)
        return parser.get_list(resp) 
  
    def get(self, expense_id):
        """Get details of an expense.

        Args:
            expense_id(str): Expense id.

        Returns:
            instance: Expense object.

        """
        url = base_url + expense_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_expense(resp) 

    def create(self, expense, receipt=None):
        """Create an expense.

        Args:
            expense(instance): Expense object.
            receipt(file, optional): Expense receipt file to attach.Allowed 
                Extensions: gif, png, jpeg, jpg, bmp and pdf.

        Returns:
            instance: Expense object.

        """
        json_object = dumps(expense.to_json())
        data = {
            'JSONString': json_object
            }
        if receipt is not None:
            attachments = [{
                'receipt': {
                    'filename': basename(receipt),
                    'content': open(receipt).read()
                    }
                }]
        else:
            attachments = None
        resp = zoho_http_client.post(base_url, self.details, self.headers, data, None, \
                                     attachments)
        return parser.get_expense(resp) 

    def update(self, expense_id, expense, receipt=None):
        """Update an existing expense.

        Args:
            expense_id(str): Expense id.
            expense(instance): Expense object.
            receipt(file): Expense receipt file to attach. Allowed Extensions: 
                gif, png, jpeg, jpg, bmp and pdf.

        Returns:
            instance: Expense object.

        """
        url = base_url + expense_id
        json_object = dumps(expense.to_json())
        data = {
            'JSONString': json_object
            }
        if receipt is None:
            attachments = None
        else:
            attachments = [{
                'receipt': {
                    'filename': basename(receipt),
                    'content': open(receipt).read()
                    }
                }]
        resp = zoho_http_client.put(url, self.details, self.headers, data, None,
                                     attachments)
        return parser.get_expense(resp) 
  
    def delete(self, expense_id):
        """Delete an existing expense.

        Args:
            expense_id(str): Expense id.

        Returns:
            str: Success message('The expense has been deleted.').

        """
        url = base_url + expense_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
  
    def list_comments_history(self, expense_id):
        """Get history and comments of an expense.

        Args:
            expense_id(str): Expense id.

        Returns:
            instance: comments list object.
 
        """
        url = base_url + expense_id + '/comments'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_comments(resp) 

    def get_receipt(self, expense_id, preview=None):
        """Get the receipt attached to an expense.

        Args:
            expense_id(str): Expense id.
            preview(bool, optional): True to get the thumbnail of the receipt.

        Returns:
            file: Returns the receipt attached to the expense.
 
        """
        url = base_url + expense_id + '/receipt'
        if preview is not None:
            query = {
                'preview': preview
                }
        else:
            query = None
        resp = zoho_http_client.getfile(url, self.details, self.headers, query)
        return resp 

    def add_receipt(self, expense_id, receipt):
        """Attach a receipt to an expense.

        Args:
            expense_id(str): Expense id.
            receipt(file): Receipt to be attached.Allowed Extensions: gif, png,
             jpeg, jpg, bmp, pdf, xls, xlsx, doc and docx.

        Returns:
            str: Success message('The expense receipt has been attached.').

        """
        url = base_url + expense_id + '/receipt'
        attachments = [{
                'receipt': {
                    'filename': basename(receipt),
                    'content': open(receipt).read()
                    }
                }]
        data = { 
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data, None, attachments)
        return parser.get_message(resp) 

    def delete_receipt(self, expense_id):
        """Delete the receipt attached to the expense.
 
        Args:
            expense_id(str): Expense id.

        Returns:
            str: Success message('The attached expense receipt has been 
                deleted.').

        """
        url = base_url + expense_id + '/receipt'
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
  
