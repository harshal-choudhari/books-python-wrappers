#$Id$#

from books.model.RecurringExpense import RecurringExpense
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

recurring_expenses_api = zoho_books.get_recurring_expenses_api()

recurring_expense_id = recurring_expenses_api.get_recurring_expenses().get_recurring_expenses()[0].get_recurring_expense_id()

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

# list recurring expenses

print recurring_expenses_api.get_recurring_expenses()

# get a recurring expense

print recurring_expenses_api.get(recurring_expense_id)

# create a recurring expense

recurring_expense=RecurringExpense()
recurring_expense.set_account_id(expense_account_id)
recurring_expense.set_paid_through_account_id(account_id)
recurring_expense.set_recurrence_name('prabu')
recurring_expense.set_start_date('2014-01-10')
recurring_expense.set_end_date('')
recurring_expense.set_recurrence_frequency('weeks')
recurring_expense.set_repeat_every(2)
recurring_expense.set_amount(100.0)
recurring_expense.set_tax_id("")
recurring_expense.set_is_inclusive_tax(True)
#recurring_expense.set_is_billable()
recurring_expense.set_customer_id(customer_id)
recurring_expense.set_vendor_id(vendor_id)
recurring_expense.set_project_id('')
recurring_expense.set_currency_id(currency_id)
recurring_expense.set_exchange_rate(1)

print recurring_expenses_api.create(recurring_expense)

# Update a recurring expense

recurring_expense=RecurringExpense()
recurring_expense.set_account_id(expense_account_id)
recurring_expense.set_paid_through_account_id(account_id)
recurring_expense.set_recurrence_name('vintu')
recurring_expense.set_start_date('2014-01-10')
recurring_expense.set_end_date('')
recurring_expense.set_recurrence_frequency('weeks')
recurring_expense.set_repeat_every(2)
recurring_expense.set_amount(100.0)
recurring_expense.set_tax_id("")
recurring_expense.set_is_inclusive_tax(True)
#recurring_expense.set_is_billable()
recurring_expense.set_customer_id(customer_id)
recurring_expense.set_vendor_id(vendor_id)
recurring_expense.set_project_id('')
recurring_expense.set_currency_id(currency_id)
recurring_expense.set_exchange_rate(1)

print recurring_expenses_api.update(recurring_expense_id,recurring_expense)

# Delete a recurring expense

print recurring_expenses_api.delete(recurring_expense_id)

# Stop a recurring expense

print recurring_expenses_api.stop_recurring_expense(recurring_expense_id)

# Resume a recurring expense

print recurring_expenses_api.resume_recurring_expense(recurring_expense_id)

# list child expenses created
date='date'
print recurring_expenses_api.list_child_expenses_created(recurring_expense_id)
print recurring_expenses_api.list_child_expenses_created(recurring_expense_id,date)

# list recurring expense comments and history

print recurring_expenses_api.list_recurring_expense_comments_and_history(recurring_expense_id)


