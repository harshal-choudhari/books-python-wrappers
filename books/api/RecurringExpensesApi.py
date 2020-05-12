#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.RecurringExpensesParser import RecurringExpensesParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'recurringexpenses/'
parser = RecurringExpensesParser()
zoho_http_client = ZohoHttpClient()

class RecurringExpensesApi:
    """Recurring Expenses Api is used to 

    1.List recurring expenses with pagination .
    2.Get the details of a recurring expense.
    3.Create a recurring expense.
    4.Update an existing recurring expense.
    5.Delete an existing recurring expense.
    6.Stop an active recurring expense.
    7.Resume a stopped recurring expense.
    8.List child expenses created from recurring expense.
    9.Get history and comments of a recurring expense.

    """
    def __init__(self, authtoken, organization_id):
        """Initialize Recurring Expenses Api using user's authtoken and 
            organization id. 
     
        Args:
            authotoken(str): User's authtoken.
            organization_id(str): User's organization id.

        """
        self.headers = {
            'Authorization': 'Zoho-oauthtoken ' + authtoken,
        }
        self.details = {
            'organization_id': organization_id
            }
  
    def get_recurring_expenses(self, param=None):
        """List recurring expenses with pagination.

        Args:
            parameter(dict, optional): Filter with which the list has to be 
                displayed.

        Returns:
            instance: Recurring expenses list object.

        """
        resp = zoho_http_client.get(base_url, self.details, self.headers, param) 
        return parser.get_list(resp) 

    def get(self, recurring_expense_id):
        """Get details of a recurring expense.
   
        Args:
            recurring_expense_id: Recurring expense id.

        Returns:
            instance: Recurring expense object.

        """
        url = base_url + recurring_expense_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_recurring_expense(resp) 

    def create(self, recurring_expenses):
        """Create a recurring expense.

        Args:
            recurring_expenses(instance): Recurring expense object.

        Returns:
            instance: Recurring expense object.
 
        """
        json_object = dumps(recurring_expenses.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.get_recurring_expense(resp) 

    def update(self, recurring_expense_id, recurring_expenses):
        """Update an existing recurring expense.

        Args:
            recurring_expense_id(str): Recurring expense id.
            recurring_expenses(instance): Recurring expense object.

        Returns:
            instance: Recurring expense object.

        """ 
        url = base_url + recurring_expense_id
        json_object = dumps(recurring_expenses.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_recurring_expense(resp)
  
    def delete(self, recurring_expense_id):
        """Delete an existing recurring expense.
 
        Args:
            recurring_expense_id(str): Recurring expense id.

        Returns:
            str: Success message('The recurring expense has been deleted.').

        """
        url = base_url + recurring_expense_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
 
    def stop_recurring_expense(self, recurring_expense_id):
        """Stop an active recurring expense.

        Args:
            recurring_expense_id(str): Recurring expense id.

        Returns:
            str: Success message('The recurring expense has been stopped.').

        """
        url = base_url + recurring_expense_id + '/status/stop'
        resp = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(resp) 
  
    def resume_recurring_expense(self, recurring_expense_id):
        """Resume a stopped recurring expense.

        Args:
            recurring_expense_id(str): Recurring expense id.

        Returns:
            str: Success message('Resume a stopped recurring expense.').

        """
        url = base_url + recurring_expense_id + '/status/resume'
        resp = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(resp) 

    def list_child_expenses_created(self, recurring_expense_id, parameter=None):
        """List child expenses created.

        Args:
            recurring_expense_id(str): Recurring Expense id.
            sort_column(str, optional): Sort child expenses created. Allowed 
                values are date, account_name, vendor_name, 
                paid_through_account_name, customer_name and total.

        Returns:
            instance: Expense history object.
            
        """
        url = base_url + recurring_expense_id + '/expenses'
        if parameter is not None:
            query = {
                'sort_column': parameter
                }
        else:
            query = None 
        resp = zoho_http_client.get(url, self.details, self.headers, query)
        return parser.get_expense_history(resp) 
  
    def list_recurring_expense_comments_and_history(self, recurring_expense_id):
        """Get history and comments of recurring expense.

        Args: 
            recurring_expense_id(str): Recurring expense id.

        Returns:
            instance: Comments list object.

        """
        url = base_url + recurring_expense_id + '/comments'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_comments(resp) 

  
