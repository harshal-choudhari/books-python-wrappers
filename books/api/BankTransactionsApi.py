#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.BankTransactionsParser import BankTransactionsParser
from books.api.Api import Api
from os.path import basename
from json import dumps

base_url = Api().base_url + 'banktransactions/'
zoho_http_client = ZohoHttpClient()
parser = BankTransactionsParser()

class BankTransactionsApi:
    """Bank Transactions Api class is used to 

    1.Get all the transaction details involved in an account.
    2.Get the details of a transaction.
    3.Create a bank transaction based on allowed transaction types.
    4.Update an existing bank transaction.
    5.Delete a transaction from an account.
    6.Get matching transactions.
    7.Match an uncategorized transaction with an existing transaction in the 
      account.
    8.Unmatch a transaction that was previously matched and make it 
      uncategorized.
    9.Get a list of all the associated that were matched or categorized to the 
      given imported transaction.
    10.Exclude a transaction from your bank or credit card account.
    11.Restore an excluded transaction in your account.
    12.Categorize an uncategorized transaction by creating a new transaction.
    13.Categorize an uncategorized transaction as a refund from credit note.
    14.Categorize an uncategorized transaction as vendor payment.
    15.Categorize an uncategorized transaction as customer payment.
    16.categorize an uncategorized transaction as Expense.
    17.Revert a categorized transaction as uncategorized.

    """ 
    def __init__(self, authtoken, organization_id):
        """Initialize Bank transaction api using user's authtoken and 
            organization id.

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
  
    def get_bank_transactions(self, parameter=None): 
        """Get all transaction details involved in an account.

        Args:
            parameter: Filter with which the list has to be displayed.

        Returns:
            instance: Bank transaction list object.
   
        """
        resp = zoho_http_client.get(base_url, self.details, self.headers, parameter)
        return parser.get_list(resp)

    def get(self, transaction_id):
        """Get bank transaction details.

        Args:
            transaction_id(str): Transaction id.

        Returns:
            instance: Bank transaction object.

        """
        url = base_url + transaction_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_transaction(resp) 
 
    def create(self, transaction):
        """Create a bank transaction for an account.

        Args:
            transaction(instance): Bank Transaction object.

        Returns:
            instance: Bank transaction object.

        """
        json_object = dumps(transaction.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.get_transaction(resp) 

    def update(self, bank_transaction_id, transaction):
        """Update an existing transaction.

        Args:
            bank_transaction_id(str): Bank transaction id.
            transaction(instance): Bank transaction object.

        Returns: 
            instance: Bank transaction object.

        """   
        url = base_url + bank_transaction_id
        json_object = dumps(transaction.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_transaction(resp) 

    def delete(self, transaction_id): 
        """Delete an existing transaction.

        Args:
            transaction_id(str): Transaction id.

        Returns: 
            str: Success message('The transaction has been deleted.').
 
        """
        url = base_url + transaction_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
  
    def get_matching_transactions(self, bank_transaction_id, parameters=None): 
        """Provide criteria to search for matching uncategorized transactions.

        Args:
            bank_transaction_id(str): Bank transaction id.
            parameters(dict, optional): Filter with which matching transactions
             has to be displayed.

        Returns: 
            instance: Transactions list object.

        """
        url = base_url + 'uncategorized/' + bank_transaction_id + \
              '/match'
        resp = zoho_http_client.get(url, self.details, self.headers, parameters) 
        return parser.get_matching_transaction(resp) 
  
    def match_a_transaction(self, transaction_id, transactions, 
                            account_id=None):
        """Match an uncategorized transaction with an existing transaction in 
            the account.
 
        Args:
            transaction_id(str): Transaction id.
            transactions(list of instance): List of transactions object.
            account_id(str): Account id.
 
        Returns:
            str: Success message('The Uncategorized transaction is linked to 
                 the selected transaction(s) in Zoho Books.').
 
        """
        url = base_url + 'uncategorized/' + transaction_id + '/match'
        data = {
            'transactions_to_be_matched': []
            }
        for value in transactions:
            transactions_to_be_matched = {}
            transactions_to_be_matched['transaction_id'] = \
            value.get_transaction_id()
            transactions_to_be_matched['transaction_type'] = \
            value.get_transaction_type()
            data['transactions_to_be_matched'].append(\
            transactions_to_be_matched) 
        if account_id is None: 
            query = None
        else:
             query = {
                'account_id': account_id
                }
        json_string = {
            'JSONString': dumps(data)
            }
        resp = zoho_http_client.post(url, self.details, self.headers, json_string, query)
        return parser.get_message(resp) 

    def unmatch_a_matched_transaction(self, transaction_id, account_id=None):
        """Unmatch a transaction that was previously matched and make it 
            uncategorized.
 
        Args:
            transaction_id(str): Transaction id.
            account_id(str): Account id.

        Returns:
            str: Success message('The transaction has been unmatched.').
 
        """
        url = base_url + transaction_id + '/unmatch'
        if account_id is None:
            parameter = None
        else:
            parameter = {
                'account_id': account_id
                }
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data, parameter)
        return parser.get_message(resp) 

    def get_associated_transactions(self, transaction_id, sort_column=None):
        """Get a list of all the transactions that were matched or categorized 
            to the given imported transaction.
   
        Args:
            transaction_id(str): Transaction id.
            sort_column(str): Param description. Allowed values are statement 
                date. Defaults to None.
         
        Returns:
            instance: Transaction list object.

        """ 
        url = base_url + transaction_id + '/associated'
        if sort_column is None:
            param = None
        else:
            param = {
                'sort_column': sort_column
                }
        resp = zoho_http_client.get(url, self.details, self.headers, param) 
        return parser.get_associated_transaction(resp) 

    def exclude_a_transaction(self, transaction_id, account_id=None):
        """Exclude a transaction from your bank or credit card account.

        Args:
            transaction_id(str): Transaction id.
            account_id(str, optional): Account id.

        Returns:
            str:  Success message('The transaction has been excluded.').

        """
        url = base_url + 'uncategorized/' + transaction_id + '/exclude'
        if account_id is None:
            param = None
        else:
            param = {
                'account_id': account_id
                }
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data, param)
        return parser.get_message(resp) 

    def restore_a_transaction(self, transaction_id, account_id=None):
        """Restore a transaction.

        Args:
            transaction_id(str): Transaction id.
            account_id(str,optional): Account id.

        Returns:
            str: Success message('The excluded transactions has been 
                 restored.').

        Raises: 
            Books Exception: If status is not '200' or '201'.

        """
        url = base_url + 'uncategorized/' + transaction_id + '/restore'
        if account_id is None:
            param = None
        else:
            param = {
                'account_id': account_id
                }
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data, param)
        return parser.get_message(resp) 

    def categorize_an_uncategorized_transaction(self, transaction_id, \
        transaction):
        """Categorize an uncategorized transaction by creating a new 
            transaction.

        Args: 
            transaction_id(str): Transaction id.
            transaction(instance): Bank transaction object.

        Returns:
            str: Success message('The transaction is now categorized.').

        """
        url = base_url + 'uncategorized/' + transaction_id + '/categorize'
        json_object = dumps(transaction.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp) 

    def categorize_as_credit_note_refunds(self, transaction_id, credit_note):
        """Categorize an uncategorized transaction as a refund from a credit 
            note.

        Args:
            transaction_id(str): Transaction id.
            credit_note(instance): Credit note object.

        Returns:
            str: Success message('The transaction is now categorized.').

        """
        url = base_url + 'uncategorized/' + transaction_id + \
              '/categorize/creditnoterefunds'
        json_object = dumps(credit_note.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp)

    def categorize_as_vendor_payment(self, transaction_id, vendor_payment):
        """Categorize an uncategorized transaction as Vendor payment.

        Args:
            transaction_id(str): Transaction id.
            vendor_payment(instance): Vendor payment object.

        Returns:
            str: Success message('The transaction is now categorized.').

        """  
        url = base_url + 'uncategorized/' + transaction_id + \
              '/categorize/vendorpayments'
        json_object = dumps(vendor_payment.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp) 
  
    def categorize_as_customer_payment(self, transaction_id, customer_payment, \
        contact_ids=None):
        """Categorize an uncategorized transaction as Customer Payment.

        Args:
            transaction_id(str): Transaction id.
            customer_payment(instance): Customer payment object.
            contact_ids(str, optional): Contact ids. Defaults to None.

        Returns:
            str: Success message('The transaction is now categorized.').

        """
        url = base_url + 'uncategorized/' + transaction_id + \
              '/categorize/customerpayments'
        json_object = dumps(customer_payment.to_json())
        data = {
            'JSONString': json_object
            }
        if contact_ids is None:
            param = None
        else:
            param = {
                'contact_ids': contact_ids
                }
        resp = zoho_http_client.post(url, self.details, self.headers, data, param)
        return parser.get_message(resp) 

    def categorize_as_expense(self, transaction_id, expense, receipt=None):
        """Categorize an uncategorized transaction as expense.

        Args:
            transaction_id(str): Transaction id.
            expense(instance): Expense object.
            receipt(file, optional): File to be attached. Allowed Extensions 
                are gif, png, jpeg, jpg, bmp and pdf.

        Returns:
            str: Success message('The transaction is now categorized.').

        """ 
        url = base_url + 'uncategorized/' + transaction_id + \
              '/categorize/expense'  
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
        resp = zoho_http_client.post(url, self.details, self.headers, data, None, attachments)
        return parser.get_message(resp) 

    def uncategorize_a_categorized_transaction(self, transaction_id, 
                                               account_id=None):
        """Revert a categorized transaction as uncategorized.

        Args:
            transaction_id(str): Transaction id.
            account_id(str, optional): Account id. Defaults to None.

        Returns:
            str: Success message('The transaction has been uncategorized.').

        """  
        url = base_url + transaction_id + '/uncategorize'
        if account_id is None:
            query = None
        else:
            query = {
                'account_id': account_id
                }
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data,  query)
        return parser.get_message(resp) 

