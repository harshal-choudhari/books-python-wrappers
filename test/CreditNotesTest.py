#$Id$#

from books.model.CreditNote import CreditNote
from books.model.Address import Address
from books.model.Email import Email
from books.model.LineItem import LineItem
from books.model.CreditNoteRefund import CreditNoteRefund
from books.model.Comment import Comment
from books.model.Invoice import Invoice
from books.service.ZohoBooks import ZohoBooks
import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

credit_notes_api = zoho_books.get_creditnotes_api()

contact_api = zoho_books.get_contacts_api()
customer_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()
param = {'status': 'open'}
credit_note_id = credit_notes_api.get_credit_notes(param).get_creditnotes()[0].get_creditnote_id()

contact_api = zoho_books.get_contacts_api()
contact_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()
contact_person_api = zoho_books.get_contact_persons_api()
contact_persons_id = contact_person_api.get_contact_persons(contact_id).get_contact_persons()[0].get_contact_person_id()

invoice_api = zoho_books.get_invoices_api()
invoice_id = invoice_api.get_invoices().get_invoices()[0].get_invoice_id()

items_api = zoho_books.get_items_api()
item_id = items_api.list_items().get_items()[0].get_item_id()

template_id = credit_notes_api.list_credit_note_template()[0].get_template_id()
email_template_id='71127000000000085'

# List credit notes
print credit_notes_api.get_credit_notes()

# Get credit note

print credit_notes_api.get_credit_note(credit_note_id)
print credit_notes_api.get_credit_note(credit_note_id,True,'pdf')
print credit_notes_api.get_credit_note(credit_note_id,False,'json')

# Create credit note

credit_notes=CreditNote()
credit_notes.set_customer_id(customer_id)
credit_notes.set_contact_persons(contact_persons_id)
credit_notes.set_reference_number("")
credit_notes.set_template_id(template_id)
credit_notes.set_date('2014-01-01')
credit_notes.set_exchange_rate(8.0)

line_items=LineItem()
line_items.set_item_id(item_id)
line_items.set_account_id('')
line_items.set_name('drive')
line_items.set_description('500 gb hard disk drive')
line_items.set_rate(388)
line_items.set_unit('nos')
line_items.set_quantity(3.00)
credit_notes.set_line_items(line_items)
credit_notes.set_notes('Thank u')
credit_notes.set_terms('Conditions Apply')

#print credit_notes_api.create(credit_notes)
#credit_notes.set_creditnote_number('12')
#print credit_notes_api.create(credit_notes,invoice_id,True)
#print credit_notes_api.create(credit_notes,None,True)
print credit_notes_api.create(credit_notes,invoice_id)

# Update credit note

credit_notes=CreditNote()
credit_notes.set_customer_id(customer_id)
credit_notes.set_contact_persons(contact_persons_id)
credit_notes.set_reference_number('')
credit_notes.set_template_id(template_id)
credit_notes.set_date('2014-01-01')
credit_notes.set_exchange_rate(8.0)

line_items=LineItem()
line_items.set_item_id(item_id)
line_items.set_account_id('')
line_items.set_name('Disk')
line_items.set_description('disk drive')
line_items.set_rate(388)
line_items.set_unit('nos')
line_items.set_quantity(3.00)
credit_notes.set_line_items(line_items)
credit_notes.set_notes('Thank u')
credit_notes.set_terms('Conditions Apply')

print credit_notes_api.update(credit_note_id,credit_notes)
credit_notes.set_creditnote_number('10')
print credit_notes_api.update(credit_note_id,credit_notes,True)

# Delete credit note

print credit_notes_api.delete(credit_note_id)

# Convert to open

print credit_notes_api.convert_to_open(credit_note_id)

# Void credit note

print credit_notes_api.void_credit_note(credit_note_id)

# Email credit note

email=Email()
to_mailid=['example@gmail.com','example@zohocorp.com']
email.set_to_mail_ids(to_mailid)
email.set_subject('Statement of transactions')
email.set_body('welcome') 

attachments=['/{file_directory}/new1.pdf']

print credit_notes_api.email_credit_note(credit_note_id,email)
print credit_notes_api.email_credit_note(credit_note_id,email,None,customer_id)
print credit_notes_api.email_credit_note(credit_note_id,email,attachments,customer_id)

# Email History

print credit_notes_api.email_history(credit_note_id)

# Get email content

print credit_notes_api.get_email_content(credit_note_id)
print credit_notes_api.get_email_content(credit_note_id,email_template_id)

# Update billing address

billing_address=Address()
billing_address.set_address('43, Km street')
billing_address.set_city('Chennai')
billing_address.set_state('TamilNadu')
billing_address.set_zip('3344')
billing_address.set_country('India')
billing_address.set_fax('67899')

print credit_notes_api.update_billing_address(credit_note_id,billing_address)
print credit_notes_api.update_billing_address(credit_note_id,billing_address,True)

# Update shipping Address

shipping_address=Address()
shipping_address.set_address('35,srinagar')
shipping_address.set_city('Mumbai')
shipping_address.set_state('TamilNadu')
shipping_address.set_zip('9877')
shipping_address.set_country('India')
shipping_address.set_fax('63003')

print credit_notes_api.update_shipping_address(credit_note_id,shipping_address)
print credit_notes_api.update_shipping_address(credit_note_id,shipping_address,True)

# List credit note template

print credit_notes_api.list_credit_note_template()

# Update credit note template

print credit_notes_api.update_credit_note_template(credit_note_id,template_id)

'''
#----------------------------------------------------------------------------------------
# Apply to invoices

invoice_id = credit_notes_api.list_invoices_credited(credit_note_id).get_invoices_credited()[0].get_invoice_id()
'''
creditnote_invoice_id = credit_notes_api.list_invoices_credited(credit_note_id)[0].get_creditnotes_invoice_id()

# List invoices credited

print credit_notes_api.list_invoices_credited(credit_note_id)

# Credit to an invoice

invoices=[]
invoice=Invoice()
invoice.set_invoice_id(invoice_id)
invoice.set_amount_applied(10.0)
invoices.append(invoice)

print credit_notes_api.credit_to_invoice(credit_note_id,invoices) 

# Delete invoice credited
print credit_notes_api.delete_invoices_credited(credit_note_id,creditnote_invoice_id)
'''
#-----------------------------------------------------------------------------------------
'''
# Refund
credit_note_id = credit_notes_api.list_credit_note_refunds().get_creditnote_refunds()[0].get_creditnote_id()
creditnote_refund_id = credit_notes_api.list_refunds_of_credit_note(credit_note_id).get_creditnote_refunds()[0].get_creditnote_refund_id()
# List credit note refunds

sort_column='refund_mode'
print credit_notes_api.list_credit_note_refunds()
#print credit_notes_api.list_credit_note_refunds(customer_id)
#print credit_notes_api.list_credit_note_refunds(None,sort_column)
#print credit_notes_api.list_credit_note_refunds(customer_id,sort_column)

# List refunds of a credit note

print credit_notes_api.list_refunds_of_credit_note(credit_note_id)

# Get credit note refund

print credit_notes_api.get_credit_note_refund(credit_note_id,creditnote_refund_id)

# Refund credit note

refund=CreditNoteRefund()
refund.set_date('2014-01-01')
refund.set_refund_mode('Cash')
refund.set_reference_number('')
refund.set_amount(20.0)
refund.set_exchange_rate(8.0)
refund.set_from_account_id('71127000000000361')
refund.set_description('Refunded amt')
print credit_notes_api.refund_credit_note(credit_note_id,refund)

# Update credit note refund

refund=CreditNoteRefund()
refund.set_date('2014-01-01')
refund.set_refund_mode('')
refund.set_reference_number('')
refund.set_amount(20.0)
refund.set_exchange_rate(8.0)
refund.set_from_account_id('71127000000000361')
refund.set_description('')
print credit_notes_api.update_credit_note_refund(credit_note_id,creditnote_refund_id,refund)

# Delete credit note refund

print credit_notes_api.delete_credit_note_refund(credit_note_id,creditnote_refund_id)


#---------------------------------------------------------------------------

# Comments and History
comment_id = credit_notes_api.list_creditnote_comments_history(credit_note_id).get_comments()[0].get_comment_id()

# list credit note comment and history

print credit_notes_api.list_creditnote_comments_history(credit_note_id)

# Add Comment

comment=Comment()
comment.set_description('credits applied')
print credit_notes_api.add_comment(creditnote_id,comment)

# Delete a comment

print credit_notes_api.delete_comment(creditnote_id,comment_id)


