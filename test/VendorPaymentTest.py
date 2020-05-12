#$Id$#

from books.model.VendorPayment import VendorPayment
from books.model.Bill import Bill
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

vendor_payments_api = zoho_books.get_vendor_payments_api()
payment_id = vendor_payments_api.get_vendor_payments().get_vendor_payments()[0].get_payment_id()
vendor_id = vendor_payments_api.get_vendor_payments().get_vendor_payments()[0].get_vendor_id()
accounts_api = zoho_books.get_bank_accounts_api()
account_id = accounts_api.get_bank_accounts().get_bank_accounts()[0].get_account_id()

bill_api = zoho_books.get_bills_api()
bill_id = bill_api.get_bills().get_bills()[0].get_bill_id()

# list vendor payments

parameter={'filter_by':'PaymentMode.Cash'}
#print vendor_payments_api.get_vendor_payments(parameter)
print vendor_payments_api.get_vendor_payments()

# Get a vendor payment

print vendor_payments_api.get(payment_id)

# Create a vendor payment

vendor_payment = VendorPayment()
vendor_payment.set_vendor_id(vendor_id)
vendor_payment.set_payment_mode('Stripe')
vendor_payment.set_description('')
vendor_payment.set_date('2014-05-10')
vendor_payment.set_reference_number('1')
vendor_payment.set_exchange_rate(0.0)
vendor_payment.set_amount(20.0)
vendor_payment.set_paid_through_account_id(account_id)

bills = Bill()
bills.set_bill_id(bill_id)
bills.set_amount_applied(0.0)
vendor_payment.set_bills(bills)

print vendor_payments_api.create(vendor_payment)

# Update a vendor payment
vendor_payment = VendorPayment()
vendor_payment.set_vendor_id(vendor_id)
vendor_payment.set_payment_mode('')
vendor_payment.set_description('')
vendor_payment.set_date('2014-02-02')
vendor_payment.set_reference_number('')
vendor_payment.set_exchange_rate(0.0)
vendor_payment.set_amount(20.0)
vendor_payment.set_paid_through_account_id(account_id)

bills = Bill()
bills.set_bill_id(bill_id)
bills.set_amount_applied(0.0)
vendor_payment.set_bills(bills)

print vendor_payments_api.update(payment_id,vendor_payment)

# Delete a vendor payment

print vendor_payments_api.delete(payment_id)

