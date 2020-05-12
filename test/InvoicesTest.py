#$Id$#

from books.model.Invoice import Invoice
from books.model.Address import Address
from books.model.Email import Email
from books.model.LineItem import LineItem
from books.model.PaymentGateway import PaymentGateway
from books.model.CustomField import CustomField
from books.model.PaymentAndCredit import PaymentAndCredit
from books.model.InvoicePayment import InvoicePayment
from books.model.InvoiceCredited import InvoiceCredited
from books.model.Comment import Comment

from books.service.ZohoBooks import ZohoBooks
import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

invoice_api = zoho_books.get_invoices_api()
#invoice_id = invoice_api.get_invoices().get_invoices()[0].get_invoice_id()

contact_api = zoho_books.get_contacts_api()
customer_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()

contact_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()
invoice_ids = invoice_api.get_invoices().get_invoices()[0].get_invoice_id() + ',' + invoice_api.get_invoices().get_invoices()[1].get_invoice_id()
'''
template_id = invoice_api.list_invoice_templates().get_templates()[0].get_template_id()
'''
items_api = zoho_books.get_items_api()
item_id = items_api.list_items().get_items()[0].get_item_id()

attachment = ['/{file_directory}/fil1.txt', '/{file_directory}/fil2.txt']

# to list invoices

parameter = {'status':'sent'}
print invoice_api.get_invoices()
print invoice_api.get_invoices(parameter)

#to get an invoice

print invoice_api.get(invoice_id)
print invoice_api.get(invoice_id, True, 'json')

#create invoice

#invoice_num =  'INV-000001'
date = '2014-01-27'
payment_terms = 15
payment_terms_label = 'Net 15'
due_date = '2014-03-27'
discount = 1.0
discount_type = 'item_level'
exc_rate = 2.0
reccuring_invoice_id = ""
invoiced_estimate_id = ""
contact_person_id = []
salesperson_name = 'bob'

invoice = Invoice()
invoice.set_customer_id(customer_id)

invoice.set_contact_persons(contact_person_id)
invoice.set_reference_number('1354444444445')
invoice.set_template_id(template_id)
invoice.set_date(date)
invoice.set_payment_terms(payment_terms)
invoice.set_payment_terms_label(payment_terms_label)
invoice.set_due_date(due_date)
invoice.set_discount(discount)
invoice.set_is_discount_before_tax(True)
invoice.set_discount_type(discount_type)
invoice.set_exchange_rate(exc_rate)
invoice.set_recurring_invoice_id(reccuring_invoice_id)
invoice.set_invoiced_estimate_id(invoiced_estimate_id)
invoice.set_salesperson_name(salesperson_name)

custom_field = CustomField()
#custom_field.set_index(1)
custom_field.set_value('2 days')

invoice.set_custom_fields(custom_field)

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
#line_items.set_tax_id('')

invoice.set_line_items(line_items)

payment_gateway = PaymentGateway()
payment_gateway.set_gateway_name('paypal')

payment_gateway.set_additional_field1('standard')
invoice.set_payment_options(payment_gateway)

invoice.set_allow_partial_payments(True)
invoice.set_custom_body('')
invoice.set_custom_subject('')
invoice.set_notes('notes')
invoice.set_terms('terms')
invoice.set_shipping_charge(7.50)
invoice.set_adjustment(15.5)
invoice.set_adjustment_description('adjustment')
print invoice_api.create(invoice)
#print invoice_api.create(invoice, False)
#invoice.set_invoice_number('25')
#print invoice_api.create(invoice, True, True)
#print invoice_api.create(invoice, True, None)
#print invoice_api.create(invoice, None, False)

# update invoice

date = '2014-01-27'
payment_terms = 15
payment_terms_label = 'Net 15'
due_date = '2014-03-27'
discount = 1.0
discount_type = 'item_level'
exc_rate = 2.0
reccuring_invoice_id = ""
invoiced_estimate_id = ""
contact_person_id = []
salesperson_name = 'bob'

invoice = Invoice()
invoice.set_customer_id(customer_id)

invoice.set_contact_persons(contact_person_id)
invoice.set_reference_number('1354444444445')
invoice.set_template_id(template_id)
invoice.set_date(date)
invoice.set_payment_terms(payment_terms)
invoice.set_payment_terms_label(payment_terms_label)
invoice.set_due_date(due_date)
invoice.set_discount(discount)
invoice.set_is_discount_before_tax(True)
invoice.set_discount_type(discount_type)
invoice.set_exchange_rate(exc_rate)
invoice.set_recurring_invoice_id(reccuring_invoice_id)
invoice.set_invoiced_estimate_id(invoiced_estimate_id)
invoice.set_salesperson_name(salesperson_name)

custom_field = CustomField()
#custom_field.set_index(1)
custom_field.set_value('2 days')

invoice.set_custom_fields(custom_field)

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
#line_items.set_tax_id('')

invoice.set_line_items(line_items)

payment_gateway = PaymentGateway()
payment_gateway.set_gateway_name('paypal')

payment_gateway.set_additional_field1('standard')
invoice.set_payment_options(payment_gateway)

invoice.set_allow_partial_payments(True)
invoice.set_custom_body('')
invoice.set_custom_subject('')
invoice.set_notes('notes')
invoice.set_terms('terms')
invoice.set_shipping_charge(7.50)
invoice.set_adjustment(15.5)
invoice.set_adjustment_description('adjustment')

print invoice_api.update(invoice_id, invoice)
invoice.set_invoice_number('26')
print invoice_api.update(invoice_id, invoice, True)

# delete invoice

print invoice_api.delete(invoice_id)

#mark an invoice as sent

print invoice_api.mark_an_invoice_as_sent(invoice_id)

# void an invoice

print invoice_api.void_an_invoice(invoice_id)

#mark as draft

print invoice_api.mark_as_draft(invoice_id)

#email an invoice

email = Email()
to_mailid = ['example@gmail.com', 'example@zohocorp.com']
email.set_to_mail_ids(to_mailid)
email.set_cc_mail_ids(['example@gmail.com'])
email.set_subject('Statement of transactions')
email.set_body('welcome') 

print invoice_api.email_an_invoice(invoice_id, email)
print invoice_api.email_an_invoice(invoice_id, email, None, True, False)
print invoice_api.email_an_invoice(invoice_id, email, None, True)
print invoice_api.email_an_invoice(invoice_id, email, attachment, True, True)

#email invoices

contacts_id = [contact_api.get_contacts().get_contacts()[0].get_contact_id(), contact_api.get_contacts().get_contacts()[1].get_contact_id()]
print invoice_api.email_invoices(contacts_id, invoice_ids)

#invoice_email_content

email_template_id = '71127000000000061'
print invoice_api.get_email_content(invoice_id)
print invoice_api.get_email_content(invoice_id, email_template_id)

#remind customer

email = Email()
to_mail_id = ['example@zohocorp.com']
email.set_to_mail_ids(to_mail_id)
email.set_subject('Statement of transactions')
email.set_body('welcome to zoho books') 
email.set_send_from_org_email_id = True
send_customer_statement = False

print invoice_api.remind_customer(invoice_id, email, None, send_customer_statement)
print invoice_api.remind_customer(invoice_id, email, attachment, send_customer_statement)

#bulk invoice reminder

print invoice_api.bulk_invoice_reminder(invoice_ids)

#get payment reminder mail content

print invoice_api.get_payment_reminder_mail_content(invoice_id).get_deprecated_placeholders_used()

#bulk export invoices

print invoice_api.bulk_export_invoices(invoice_ids)

#bulk print invoices

print invoice_api.bulk_print_invoices(invoice_ids)

#disable payment reminder

print invoice_api.disable_payment_reminder(invoice_id)

#enable payment reminder

print invoice_api.enable_payment_reminder(invoice_id)

#write off invoice

print invoice_api.write_off_invoice(invoice_id)

#cancel write off

print invoice_api.cancel_write_off(invoice_id)

#update billing address

billing_address = Address()
billing_address.set_address('43,  Km street')
billing_address.set_city('Chennai')
billing_address.set_state('TamilNadu')
billing_address.set_zip('3344')
billing_address.set_country('India')
billing_address.set_fax('67899')

print invoice_api.update_billing_address(invoice_id, billing_address)
print invoice_api.update_billing_address(invoice_id, billing_address, True)

# update shipping address

shipping_address = Address()
shipping_address.set_address('43,  Km street')
shipping_address.set_city('Chennai')
shipping_address.set_state('TamilNadu')
shipping_address.set_zip('3344')
shipping_address.set_country('India')
shipping_address.set_fax('67899')

print invoice_api.update_shipping_address(invoice_id, shipping_address)
print invoice_api.update_shipping_address(invoice_id, shipping_address, True)

# list invoice templates
'''
print invoice_api.list_invoice_templates()
'''
# update invoice template

print invoice_api.update_invoice_template(invoice_id, template_id)
'''
#----------------------------------------------------------------------------------------------------------------------------------------

# Payments and Credits
'''
param = {'status': 'partially_paid'}
invoice_id = invoice_api.get_invoices(param).get_invoices()[2].get_invoice_id()
invoice_payment_id = invoice_api.list_invoice_payments(invoice_id).get_payments()[0].get_invoice_payment_id()
creditnotes_invoice_id = invoice_api.list_credits_applied(invoice_id).get_invoices_credited()[0].get_creditnotes_invoice_id()

payment_id = invoice_api.list_invoice_payments(invoice_id).get_payments()[0].get_payment_id()
creditnote_id = invoice_api.list_credits_applied(invoice_id).get_invoices_credited()[0].get_creditnote_id()

# to list invoice payments

print invoice_api.list_invoice_payments(invoice_id).get_payments()

# to list credits applied

print invoice_api.list_credits_applied(invoice_id)

# apply credits
payments_and_credits = PaymentAndCredit()
credits = InvoiceCredited()
credits.set_creditnote_id(creditnote_id)
credits.set_amount_applied(3.0)
payments_and_credits.set_apply_creditnotes(credits)
payments = InvoicePayment()
payments.set_payment_id(payment_id)
payments.set_amount_applied(0.0)
payments_and_credits.set_payments(payments)
print invoice_api.apply_credits(invoice_id, payments_and_credits)

#to delete payment
print invoice_api.delete_payment(invoice_id, invoice_payment_id)

#to delete applied credit

print invoice_api.delete_applied_credit(invoice_id, creditnotes_invoice_id)

'''
#-----------------------------------------------------------------------------------------------------------------------------------------

# Attachment
'''
expense_api = zoho_books.get_expenses_api()
expense_id = expense_api.get_expenses().get_expenses()[0].get_expense_id()

# Get an invoice attachment
preview = False
print invoice_api.get_an_invoice_attachment(invoice_id)
print invoice_api.get_an_invoice_attachment(invoice_id, preview)

# add attachment to an invoice

print invoice_api.add_attachment_to_an_invoice(invoice_id, ['/{file_directory}/download.jpg'])  
print invoice_api.add_attachment_to_an_invoice(invoice_id, ['/{file_directory}/download.jpg'], True)

# update attachment preference

print invoice_api.update_attachment_preference(invoice_id, True)

# delete an attachment

print invoice_api.delete_an_attachment(invoice_id)

# delete expense receipt

print invoice_api.delete_expense_receipt(expense_id)
'''
#------------------------------------------------------------------------------------------------------------------------------------------

# Comments and History
'''
comment_id = invoice_api.list_invoice_comments_history(invoice_id).get_comments()[0].get_comment_id()
#list invoice comments & history

print invoice_api.list_invoice_comments_history(invoice_id)

#Add Comment

comments = Comment()
comments.set_description('this is a comment')
comments.set_show_comment_to_clients(False)
comments.set_payment_expected_date('')
print invoice_api.add_comment(invoice_id, comments)

# Update Comment
comments = Comment()
comments.set_description('Invoice marked as sent')
comments.set_show_comment_to_clients(False)
print invoice_api.update_comment(invoice_id, comment_id, comments)

#delete Comment

print invoice_api.delete_comment(invoice_id, comment_id)

 
