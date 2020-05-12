#$Id$#

from books.model.CustomerPayment import CustomerPayment
from books.model.Invoice import Invoice
from books.service.ZohoBooks import ZohoBooks
import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

customer_payments_api = zoho_books.get_customer_payments_api()

payment_id = customer_payments_api.get_customer_payments().get_customer_payments()[0].get_payment_id()
customer_id = customer_payments_api.get_customer_payments().get_customer_payments()[0].get_customer_id()

invoice_api = zoho_books.get_invoices_api()
invoice_id = invoice_api.get_invoices().get_invoices()[0].get_invoice_id()

accounts_api = zoho_books.get_bank_accounts_api()
account_id = accounts_api.get_bank_accounts().get_bank_accounts()[0].get_account_id()

# List customer payments

print customer_payments_api.get_customer_payments()

# Get a customer payment

print customer_payments_api.get(payment_id)

# Create a payment_customer

customer_payments = CustomerPayment()
customer_payments.set_customer_id(customer_id)
invoices = []
invoice = Invoice()
invoice.set_invoice_id(invoice_id)
invoice.set_amount_applied(20.0)
invoice.set_tax_amount_withheld(4.0)
invoices.append(invoice)
customer_payments.set_invoices(invoices)
customer_payments.set_payment_mode('Cash')
customer_payments.set_description('')
customer_payments.set_date('2014-01-01')
customer_payments.set_reference_number('')
customer_payments.set_exchange_rate(30.0)
customer_payments.set_amount(300.0)
customer_payments.set_bank_charges(4.0)
customer_payments.set_tax_account_id('')
customer_payments.set_account_id(account_id)

print customer_payments_api.create(customer_payments)

# Update a payment customer

customer_payments = CustomerPayment()
customer_payments.set_customer_id(customer_id)
invoices = []
invoice = Invoice()
invoice.set_invoice_id('71127000000121041')
invoice.set_amount_applied(20.0)
invoice.set_tax_amount_withheld(4.0)
invoices.append(invoice)
customer_payments.set_invoices(invoices)
customer_payments.set_payment_mode('Cash')
customer_payments.set_description('')
customer_payments.set_date('2014-01-01')
customer_payments.set_reference_number('')
customer_payments.set_exchange_rate(30.0)
customer_payments.set_amount(300.0)
customer_payments.set_bank_charges(4.0)
customer_payments.set_tax_account_id('')
customer_payments.set_account_id('71127000000081061')

print customer_payments_api.update(payment_id,customer_payments)

# Delete a customer payment

print customer_payments_api.delete(payment_id)


