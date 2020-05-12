#$Id$#

from books.model.ChartOfAccount import ChartOfAccount
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

chart_of_accounts_api = zoho_books.get_chart_of_accounts_api()

account_id = chart_of_accounts_api.get_chart_of_accounts().get_chartofaccounts()[0].get_account_id()

# list chart of accounts


parameters = {'filter_by':'AccountType.Active'}
print chart_of_accounts_api.get_chart_of_accounts()
print chart_of_accounts_api.get_chart_of_accounts(parameters)

# Get an Account

print chart_of_accounts_api.get(account_id)

# Create an account
account = ChartOfAccount()
account.set_account_name('DD1')
account.set_account_type('other_asset')
account.set_currency_id('')
account.set_description('Fixed Deposit')

print chart_of_accounts_api.create(account)

# Update an account
account = ChartOfAccount()
account.set_account_name('SD1')
account.set_account_type('other_asset')
#account.set_currency_id('')
account.set_description('Fixed Deposit')
print chart_of_accounts_api.update("71127000000165001", account)

#Delete an account

print chart_of_accounts_api.delete(account_id)

#Mark an account as active

print chart_of_accounts_api.mark_an_account_as_active(account_id)

# Mark an account as inactive

print chart_of_accounts_api.mark_an_account_as_inactive(account_id)

# List of transactions for an account

#account_id = 
param = {'amount.less_than':100.0, 
      #'account_id':account_id, 
       'filter_by':'TransactionType.Invoice'}

print chart_of_accounts_api.list_of_transactions()
print chart_of_accounts_api.list_of_transactions(param).get_transactions()

# Delete a transaction

transaction_id = chart_of_accounts_api.list_of_transactions(param).get_transactions()[0].get_transaction_id()

print chart_of_accounts_api.delete_a_transaction("71127000000165001")

