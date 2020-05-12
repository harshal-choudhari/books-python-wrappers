#$Id$#

from books.model.Transaction import Transaction
from books.model.CreditNoteRefund import CreditNoteRefund
from books.model.VendorPayment import VendorPayment
from books.model.CustomerPayment import CustomerPayment
from books.model.Bill import Bill
from books.model.Expense import Expense
from books.model.Invoice import Invoice
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

bank_transaction_api = zoho_books.get_bank_transactions_api()

accounts_api = zoho_books.get_bank_accounts_api()
account_id = accounts_api.get_bank_accounts().get_bank_accounts()[1].get_account_id()

transaction_type = 'sales_without_invoices'
transaction_id = bank_transaction_api.get_bank_transactions().get_transactions()[0].get_transaction_id()

contact_api = zoho_books.get_contacts_api()
customer_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()

settings_api = zoho_books.get_settings_api()
currency_id = settings_api.get_currencies().get_currencies()[0].get_currency_id()

vendor_payments_api = zoho_books.get_vendor_payments_api()
payment_id = vendor_payments_api.get_vendor_payments().get_vendor_payments()[0].get_payment_id()
vendor_id = vendor_payments_api.get_vendor_payments().get_vendor_payments()[0].get_vendor_id()

bill_api = zoho_books.get_bills_api()
bill_id = bill_api.get_bills().get_bills()[1].get_bill_id()

# get transaction list

param={'account_id':account_id}
print bank_transaction_api.get_bank_transactions(param)
print bank_transaction_api.get_bank_transactions()

# get transaction
'''
print bank_transaction_api.get("71127000000224005")
'''
# Create a transaction for an account

bank_transaction=Transaction()
bank_transaction.set_from_account_id('71127000000079023')
bank_transaction.set_to_account_id('71127000000012001')
bank_transaction.set_transaction_type('transfer_fund')
bank_transaction.set_amount(10.0)
bank_transaction.set_payment_mode('cash')
bank_transaction.set_exchange_rate(10.0)
bank_transaction.set_date('2014-02-01')
bank_transaction.set_customer_id(customer_id)
bank_transaction.set_reference_number('')
bank_transaction.set_description('halo')
bank_transaction.set_currency_id(currency_id)

print bank_transaction_api.create(bank_transaction)

# update a transaction
bank_transaction=Transaction()
bank_transaction.set_from_account_id('71127000000079023')
bank_transaction.set_to_account_id('71127000000012001')
bank_transaction.set_transaction_type('transfer_fund')
bank_transaction.set_amount(10.0)
bank_transaction.set_payment_mode('cash')
bank_transaction.set_exchange_rate(100.0)
bank_transaction.set_date('2014-02-01')
bank_transaction.set_customer_id(customer_id)
bank_transaction.set_reference_number('')
bank_transaction.set_description('halo')
bank_transaction.set_currency_id(currency_id)

print bank_transaction_api.update(transaction_id,bank_transaction)

# Delete a transaction

print bank_transaction_api.delete(transaction_id)

# Get matching transactions

#param = {'transaction_type':'expense' }

print bank_transaction_api.get_matching_transactions(transaction_id)
#print bank_transaction_api.get_matching_transactions(transaction_id,param)

# Match a transaction
transactions_to_be_matched = Transaction()
transactions_to_be_matched.set_transaction_id(transaction_id)
transactions_to_be_matched.set_transaction_type(transaction_type)
transactions = []
transactions.append(transactions_to_be_matched)
print bank_transaction_api.match_a_transaction(transaction_id,transactions)
print bank_transaction_api.match_a_transaction(transaction_id,transactions, account_id)

# Unmatch a matched transaction
print bank_transaction_api.unmatch_a_matched_transaction(transaction_id) 
print bank_transaction_api.unmatch_a_matched_transaction(transaction_id,account_id)

# Get associated transaction
sort_column='statement_date'
print bank_transaction_api.get_associated_transactions(transaction_id)
print bank_transaction_api.get_associated_transactions(transaction_id,sort_column)

# Exclude a transaction
print bank_transaction_api.exclude_a_transaction(transaction_id)
print bank_transaction_api.exclude_a_transaction(transaction_id, account_id)

# Restore a transaction
#print bank_transaction_api.restore_a_transaction(transaction_id)
print bank_transaction_api.restore_a_transaction(transaction_id, account_id)
'''
#------------------------------------------------------------------------
#Categorize
'''
credit_notes_api = zoho_books.get_creditnotes_api()
credit_note_id = credit_notes_api.get_credit_notes(param).get_creditnotes()[0].get_creditnote_id()

# Categorize an uncategorized transaction
categorize_a_transaction = Transaction()

categorize_a_transaction.set_from_account_id('71127000000079023')
categorize_a_transaction.set_to_account_id('71127000000012001')
categorize_a_transaction.set_transaction_type('transfer_fund')
categorize_a_transaction.set_amount(10.0)
categorize_a_transaction.set_payment_mode('cash')
categorize_a_transaction.set_exchange_rate(1.0)
categorize_a_transaction.set_date('2014-04-29')
categorize_a_transaction.set_customer_id(customer_id)
categorize_a_transaction.set_reference_number('2')
categorize_a_transaction.set_description('transafer')
categorize_a_transaction.set_currency_id(currency_id)

print bank_transaction_api.categorize_an_uncategorized_transaction(transaction_id,categorize_a_transaction)

# Categorize as credit note refund
refund = CreditNoteRefund()
refund.set_creditnote_id(credit_note_id)
refund.set_date('2014-01-01')
refund.set_refund_mode('cash')
refund.set_reference_number('')
refund.set_exchange_rate(1.0)
refund.set_from_account_id(account_id)
refund.set_description('credit not categorize')

print bank_transaction_api.categorize_as_credit_note_refunds(transaction_id,refund)

# Categorize as vendor payments
vendor_payment = VendorPayment()
vendor_payment.set_vendor_id(vendor_id)
bills=Bill()
bills.set_bill_id(bill_id)
bills.set_amount_applied(10.0)
vendor_payment.set_bills(bills)
vendor_payment.set_payment_mode('cash')
vendor_payment.set_description('vendor payments')
vendor_payment.set_date('2014-04-29')
vendor_payment.set_reference_number('2')
vendor_payment.set_exchange_rate(1.0)
vendor_payment.set_amount(20.0)
vendor_payment.set_paid_through_account_id('')

print bank_transaction_api.categorize_as_vendor_payment(transaction_id,vendor_payment)

# Categorize as customer payment
invoice_api = zoho_books.get_invoices_api()
invoice_id = invoice_api.get_invoices().get_invoices()[0].get_invoice_id()

customer_payments = CustomerPayment()
customer_payments.set_customer_id(customer_id)
invoice = Invoice()
invoice.set_invoice_id(invoice_id)
invoice.set_amount_applied(20.0)
invoice.set_tax_amount_withheld(4.0)
invoices = [invoice]
customer_payments.set_invoices(invoices)
customer_payments.set_payment_mode('cash')
customer_payments.set_description('')
customer_payments.set_date('2014-04-28')
customer_payments.set_reference_number('')
customer_payments.set_exchange_rate(1.0)
customer_payments.set_amount(10.0)
customer_payments.set_bank_charges(0.0)
customer_payments.set_tax_account_id('')
customer_payments.set_account_id(account_id)

contact_ids = contact_api.get_contacts().get_contacts()[1].get_contact_id()

print bank_transaction_api.categorize_as_customer_payment(transaction_id,customer_payments)
print bank_transaction_api.categorize_as_customer_payment(transaction_id,customer_payments,contact_ids)

# Categorize as expense

expense = Expense()
expense.set_account_id(account_id)
expense.set_paid_through_account_id('')
expense.set_amount(200.0)
expense.set_date('2014-04-28')
expense.set_is_inclusive_tax(False)
expense.set_is_billable(True)
expense.set_reference_number('2')
expense.set_description('')
expense.set_customer_id(customer_id)
expense.set_vendor_id(vendor_id)
expense.set_currency_id('currency_id)
expense.set_exchange_rate(20.0)
expense.set_project_id('')
receipt = '/{file_directory}/download.jpg'
print bank_transaction_api.categorize_as_expense(transaction_id,expense)
print bank_transaction_api.categorize_as_expense(transaction_id,expense,receipt)

# Uncategorize a categorized transaction

print bank_transaction_api.uncategorize_a_categorized_transaction(transaction_id)


