#$Id$#

from books.model.RecurringInvoice import RecurringInvoice
from books.model.PaymentGateway import PaymentGateway
from books.model.LineItem import LineItem

from books.service.ZohoBooks import ZohoBooks
import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

recurring_invoice_api = zoho_books.get_recurring_invoices_api()
recurring_invoice_id = recurring_invoice_api.get_recurring_invoices().get_recurring_invoices()[0].get_recurring_invoice_id()

contact_api = zoho_books.get_contacts_api()
customer_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()

items_api = zoho_books.get_items_api()
item_id = items_api.list_items().get_items()[0].get_item_id()

# to list recurring invoices

print recurring_invoice_api.get_recurring_invoices()

# get a recurring invoice

print recurring_invoice_api.get_recurring_invoice(recurring_invoice_id)

# create a recurring invoice

recurring_invoice = RecurringInvoice()
recurring_invoice.set_recurrence_name('Venkat')
recurring_invoice.set_customer_id(customer_id)
recurring_invoice.set_contact_persons([])
recurring_invoice.set_template_id('')
recurring_invoice.set_start_date('2014-01-01')
recurring_invoice.set_end_date('2014-01-25')
recurring_invoice.set_recurrence_frequency('weeks')#allowed i/p = days, weeks, months, years
recurring_invoice.set_repeat_every(1)
recurring_invoice.set_payment_terms(15)
recurring_invoice.set_payment_terms_label('')
recurring_invoice.set_exchange_rate(0.0)

payment_gateway = PaymentGateway()
payment_gateway.set_gateway_name('paypal')
payment_gateway.set_additional_field1('standard')
recurring_invoice.set_payment_options(payment_gateway)
recurring_invoice.set_discount(0.00)
recurring_invoice.set_is_discount_before_tax(True)
recurring_invoice.set_discount_type('item_level')

line_items = LineItem()
line_items.set_item_id(item_id)
line_items.set_project_id('')
line_items.set_expense_id('')
line_items.set_name('drive')
line_items.set_description('500 gb hard disk drive')
line_items.set_item_order(1)
line_items.set_rate(388)
line_items.set_unit('nos')
line_items.set_quantity(3.00)
line_items.set_discount(0.00)
line_items.set_tax_id('')
recurring_invoice.set_line_items(line_items)
recurring_invoice.set_notes('Thank u')
recurring_invoice.set_terms('welcome')
recurring_invoice.set_salesperson_name('Bob')
recurring_invoice.set_shipping_charge(0.0)
recurring_invoice.set_adjustment(0.0)
recurring_invoice.set_adjustment_description('rounding off')

print recurring_invoice_api.create(recurring_invoice)

# Update recurring invoice

recurring_invoice = RecurringInvoice()
recurring_invoice.set_recurrence_name('maata')
recurring_invoice.set_customer_id(customer_id)
recurring_invoice.set_contact_persons([])
recurring_invoice.set_template_id('')
recurring_invoice.set_start_date('2014-01-01')
recurring_invoice.set_end_date('2014-01-25')
recurring_invoice.set_recurrence_frequency('weeks')#allowed ip = days, weeks, months, years
recurring_invoice.set_repeat_every(1)
recurring_invoice.set_payment_terms(15)
recurring_invoice.set_payment_terms_label('')
recurring_invoice.set_exchange_rate(0.0)

payment_gateway = PaymentGateway()
payment_gateway.set_gateway_name('paypal')
payment_gateway.set_additional_field1('standard')
recurring_invoice.set_payment_options(payment_gateway)
recurring_invoice.set_discount(0.00)
recurring_invoice.set_is_discount_before_tax(True)
recurring_invoice.set_discount_type('item_level')

line_items = LineItem()
line_items.set_item_id(item_id)
line_items.set_project_id('')
line_items.set_expense_id('')
line_items.set_name('drive')
line_items.set_description('500 gb hard disk drive')
line_items.set_item_order(1)
line_items.set_rate(388)
line_items.set_unit('nos')
line_items.set_quantity(3.00)
line_items.set_discount(0.00)
line_items.set_tax_id('')
recurring_invoice.set_line_items(line_items)
recurring_invoice.set_notes('Thank u')
recurring_invoice.set_terms('welcome')
recurring_invoice.set_salesperson_name('Bob')
recurring_invoice.set_shipping_charge(0.0)
recurring_invoice.set_adjustment(0.0)
recurring_invoice.set_adjustment_description('rounding off')

print recurring_invoice_api.update(recurring_invoice_id, recurring_invoice)

# Delete recurring invoice

print recurring_invoice_api.delete(recurring_invoice_id)

# Stop recurring invoice

print recurring_invoice_api.stop_recurring_invoice(recurring_invoice_id)

# Resume recurring invoice
print recurring_invoice_api.resume_recurring_invoice(recurring_invoice_id)

# update recurring invoice

template_id = "71127000000017001"
print recurring_invoice_api.update_recurring_invoice_template(recurring_invoice_id, template_id)

# list recurring invoice history

print recurring_invoice_api.list_recurring_invoice_history(recurring_invoice_id)


