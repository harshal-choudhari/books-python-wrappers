#$Id$#

from books.model.Expense import Expense
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

expenses_api = zoho_books.get_expenses_api()

expense_id = expenses_api.get_expenses().get_expenses()[0].get_expense_id()

accounts_api = zoho_books.get_bank_accounts_api()
account_id = accounts_api.get_bank_accounts().get_bank_accounts()[0].get_account_id()

param = {'filter_by': 'AccountType.Expense'}
chart_of_accounts_api = zoho_books.get_chart_of_accounts_api()
expense_account_id = chart_of_accounts_api.get_chart_of_accounts(param).get_chartofaccounts()[1].get_account_id()

settings_api = zoho_books.get_settings_api()
currency_id = settings_api.get_currencies().get_currencies()[0].get_currency_id()

contact_api = zoho_books.get_contacts_api()
customer_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()

vendor_api = zoho_books.get_vendor_payments_api()
vendor_id = vendor_api.get_vendor_payments().get_vendor_payments()[0].get_vendor_id()

# List Expenses 

parameters={'filter_by':'Status.Unbilled'}
print expenses_api.get_expenses()
print expenses_api.get_expenses(parameters)

# Get an expense

print expenses_api.get(expense_id)

# Create an expense

expenses=Expense()
expenses.set_account_id(expense_account_id)
expenses.set_paid_through_account_id(account_id)
expenses.set_date("2012-12-30")
expenses.set_amount(100.0)
expenses.set_tax_id("71127000000077019")
expenses.set_is_inclusive_tax(True)
expenses.set_is_billable(True)
expenses.set_customer_id(customer_id)
expenses.set_vendor_id(vendor_id)
expenses.set_currency_id(currency_id)
#expenses.set_exchange_rate()
#expenses.set_project_id()

print expenses_api.create(expenses)
receipt="/{file_directory}/download.jpg"

print expenses_api.create(expenses,receipt) 

# Update an expense

expenses=Expense()
expenses.set_account_id(expense_account_id)
expenses.set_paid_through_account_id(account_id)
expenses.set_date("2012-12-30")
expenses.set_amount(100.0)
expenses.set_tax_id("")
expenses.set_is_inclusive_tax(True)
expenses.set_is_billable(True)
expenses.set_customer_id(customer_id)
expenses.set_vendor_id(vendor_id)
expenses.set_currency_id(currency_id)
#expenses.set_exchange_rate()
#expenses.set_project_id()

print expenses_api.update(expense_id,expenses)
receipt="/{file_directory}/download.jpg"
print  expenses_api.update(expense_id,expenses,receipt)

# Delete an expense

print expenses_api.delete(expense_id)
'''
# List expense comments and history

print expenses_api.list_comments_history(expense_id)
'''
# Receipt

#get an expense receipt

print expenses_api.get_receipt(expense_id)
print expenses_api.get_receipt(expense_id,True)

# Get an expense receipt

receipt="/{file_directory}/download.jpg"
print expenses_api.add_receipt(expense_id,receipt)

# Delete a receipt

print expenses_api.delete_receipt(expense_id)





