#$Id$#

from books.model.Journal import Journal
from books.model.LineItem import LineItem
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

journal_api = zoho_books.get_journals_api()
journal_id = journal_api.get_journals().get_journals()[0].get_journal_id()

param = {'filter_by': 'AccountType.Expense'}
chart_of_accounts_api = zoho_books.get_chart_of_accounts_api()
expense_account_id = chart_of_accounts_api.get_chart_of_accounts(param).get_chartofaccounts()[1].get_account_id()

# get journal list

parameter = {'total_less_than':100.0}
#print journal_api.get_journals()
print journal_api.get_journals(parameter)

# get journal

print journal_api.get(journal_id)

#create a journal

journal = Journal()
journal.set_journal_date('2014-06-10')
journal.set_reference_number('')
journal.set_notes('loan')
line_items = LineItem()
line_items.set_account_id(expense_account_id)
line_items.set_description('')
line_items.set_tax_id('')
line_items.set_amount(20.0)
line_items.set_debit_or_credit('credit')
journal.set_line_items(line_items)
item = LineItem()
item.set_account_id(expense_account_id)
item.set_description('')
item.set_tax_id('')
item.set_amount(20.0)
item.set_debit_or_credit('debit')
journal.set_line_items(item)
print journal_api.create(journal)

# update a journal

journal = Journal()
journal.set_journal_date('2014-04-21')
journal.set_reference_number('')
journal.set_notes('loan')
line_items = LineItem()
line_items.set_account_id(expense_account_id)
line_items.set_description('')
line_items.set_tax_id('')
line_items.set_amount(20.0)
line_items.set_debit_or_credit('credit')
journal.set_line_items(line_items)
item = LineItem()
item.set_account_id(expense_account_id)
item.set_description('')
item.set_tax_id('')
item.set_amount(20.0)
item.set_debit_or_credit('debit')
journal.set_line_items(item)
print journal_api.update(journal_id,journal)

# Delete a journal

print journal_api.delete(journal_id)

