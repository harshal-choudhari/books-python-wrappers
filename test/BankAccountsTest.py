#$Id$#

from books.model.BankAccount import BankAccount
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

bank_accounts_api = zoho_books.get_bank_accounts_api()

account_id = bank_accounts_api.get_bank_accounts().get_bank_accounts()[0].get_account_id()

statement_id = bank_accounts_api.get_last_imported_statement(account_id).get_statement_id()

# list view of accounts

param = {'filter_by':'Status.Active'}
print bank_accounts_api.get_bank_accounts()
print bank_accounts_api.get_bank_accounts(param)

# Get account details

print bank_accounts_api.get(account_id)

# Create a bank account

bank_account = BankAccount()
bank_account.set_account_name('account 1')
bank_account.set_account_type('bank')
bank_account.set_currency_id('')
bank_account.set_description('thanks')
bank_account.set_bank_name('')
bank_account.set_routing_number('')
bank_account.set_is_primary_account(False)
bank_account.set_is_paypal_account(False)
bank_account.set_paypal_type('')
bank_account.set_paypal_email_address('')

print bank_accounts_api.create(bank_account)

# update bank account

bank_account = BankAccount()
bank_account.set_account_name('account 2')
bank_account.set_account_type('bank')
bank_account.set_currency_id('')
bank_account.set_description('thanks')
bank_account.set_bank_name('')
bank_account.set_routing_number('')
bank_account.set_is_primary_account(False)
bank_account.set_is_paypal_account(False)
bank_account.set_paypal_type('')
bank_account.set_paypal_email_address('')

print bank_accounts_api.update(account_id,bank_account)

# Delete bank account

print bank_accounts_api.delete(account_id)

# Deactivate account

print bank_accounts_api.deactivate_account(account_id)

# Activate account

print bank_accounts_api.activate_account(account_id)

# Get last imported

print bank_accounts_api.get_last_imported_statement(account_id)

# Delete last imported statement

print bank_accounts_api.delete_last_imported_statement(account_id, statement_id)


