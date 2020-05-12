#$Id$#

from books.model.Bill import Bill
from books.model.LineItem import LineItem
from books.model.Address import Address
from books.model.PaymentAndCredit import PaymentAndCredit
from books.model.BillPayment import BillPayment
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

bill_api = zoho_books.get_bills_api()
bill_id = bill_api.get_bills().get_bills()[1].get_bill_id()

vendor_api = zoho_books.get_vendor_payments_api()
vendor_id = vendor_api.get_vendor_payments().get_vendor_payments()[0].get_vendor_id()
param = {'filter_by': 'AccountType.Expense'}
chart_of_accounts_api = zoho_books.get_chart_of_accounts_api()
account_id = chart_of_accounts_api.get_chart_of_accounts(param).get_chartofaccounts()[1].get_account_id()

attachment = '/{file_directory}/emp.pdf'

# List bills
parameter = {'status':'open'}
print bill_api.get_bills()
print bill_api.get_bills(parameter)

# Get a bill

print bill_api.get(bill_id)

# Create a bill

bill = Bill()
bill.set_vendor_id(vendor_id)
bill.set_bill_number('38')
bill.set_date('2014-05-12')
bill.set_due_date('2014-05-13')
bill.set_exchange_rate(1)
bill.set_reference_number("2")

line_items = LineItem() 
line_items.set_account_id(account_id)
line_items.set_description('table')
line_items.set_rate("1000.0")
line_items.set_quantity("4")
line_items.set_item_order("0")
bill.set_line_items(line_items)
bill.set_notes("before due")
bill.set_terms('conditions Apply')

print bill_api.create(bill)
#print bill_api.create(bill,attachment)

# Update a bill

bill = Bill()
bill.set_vendor_id(vendor_id)
bill.set_bill_number('38')
bill.set_date('2014-05-12')
bill.set_due_date('2014-05-13')
bill.set_exchange_rate(1)
bill.set_reference_number("2")

line_items = LineItem() 
line_items.set_account_id(account_id)
line_items.set_description('table')
line_items.set_rate("1000.0")
line_items.set_quantity("4")
line_items.set_tax_id("")
line_items.set_item_order("0")

bill.set_line_items(line_items)
bill.set_notes("before due")
bill.set_terms('conditions Apply')


#print bill_api.update(bill_id,bill)
print bill_api.update(bill_id,bill,attachment)

# Delete a bill

print bill_api.delete(bill_id)

# Void a bill

print bill_api.void_a_bill(bill_id)

# Mark a bill as open

print bill_api.mark_a_bill_as_open(bill_id)

# Update billing_ address

billing_address=Address()
billing_address.set_address('no. 2 kumaran streeet')
billing_address.set_city('chennai')
billing_address.set_state('Tamilnadu')
billing_address.set_zip('908')
billing_address.set_country('India')

print bill_api.update_billing_address(bill_id,billing_address)
'''
'''
param = {'status': 'paid'}
bill_id = bill_api.get_bills(param).get_bills()[0].get_bill_id()
payment_id = bill_api.list_bill_payments(bill_id)[0].get_payment_id()
bill_payment_id = bill_api.list_bill_payments(bill_id)[0].get_bill_payment_id()

# List bill payment

print bill_api.list_bill_payments(bill_id)

# Apply credits

bill_payments = BillPayment()
bill_payments.set_payment_id(payment_id)
bill_payments.set_amount_applied(0.0)
print bill_api.apply_credits(bill_id,[bill_payments])

# Delete a payment

print bill_api.delete_a_payment(bill_id,bill_payment_id)

'''
# Get a bill attachment
'''
print bill_api.get_a_bill_attachment(bill_id)
#print bill_api.get_a_bill_attachment("71127000000080017",True)

# Add attachment to a bill
attachment='/{file_directory}/download.jpg'
print bill_api.add_attachments_to_a_bill(bill_id,attachment)

# Delete an attachment

print bill_api.delete_an_attachment(bill_id)

# List bill comments and history
comment_id = bill_api.list_bill_comments_and_history(bill_id).get_comments()[0].get_comment_id()

print bill_api.list_bill_comments_and_history(bill_id)

# Add Comment
description="Welcome"
print bill_api.add_comment(bill_id,description)

# Delete a comment
comment_id = "71127000000204442"
print bill_api.delete_a_comment(bill_id,comment_id)



