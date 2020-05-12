#$Id$#

import os
from books.model.Contact import Contact
from books.model.Email import Email
from books.model.Address import Address
from books.model.ContactPerson import ContactPerson
from books.service.ZohoBooks import ZohoBooks

access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

contact_api = zoho_books.get_contacts_api()
contact_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()

settings_api = zoho_books.get_settings_api()
currency_id = settings_api.get_currencies().get_currencies()[0].get_currency_id()

# to list contacts

parameter = {'sort_column':'last_name'}
print(contact_api.get_contacts(parameter))

# to get a contact

print(contact_api.get(contact_id))

# to create contact

contact = Contact()
contact.set_contact_name('anin')
contact.set_payment_terms(15)
contact.set_payment_terms_label('Net 15')
contact.set_currency_id(currency_id)
contact.set_notes('thank you')
con_per = []
cp = ContactPerson()
cp.set_first_name('nivetha')
cp.set_salutation('ms')

con_per.append(cp)

v = ContactPerson()
v.set_first_name('varunaa')
v.set_salutation('mr')
v.set_is_primary_contact(True)
con_per.append(v)

contact.set_contact_persons(con_per)

baddress = Address()
baddress.set_address('45, suite street')
baddress.set_city('California')
baddress.set_state('CA')
baddress.set_zip('9876')
baddress.set_fax('+1-925-924-9600')
#contact.set_billing_address(baddress)

saddress = Address()
saddress.set_address('45, suite street')
saddress.set_city('California')
saddress.set_state('CA')
saddress.set_zip('9876')
saddress.set_fax('+1-925-924-9600')
contact.set_shipping_address(saddress)

contact.set_notes('Payment option: Through check' )

print(contact_api.create(contact))

# to update a contact 

contact = Contact()
contact.set_contact_name('rath')
contact.set_payment_terms(15)
contact.set_payment_terms_label('Net 15')
contact.set_currency_id(currency_id)

con_per = []
cp = ContactPerson()
cp.set_first_name('nivetha')
cp.set_salutation('ms')

con_per.append(cp)

v = ContactPerson()
v.set_first_name('varun')
v.set_salutation('mr')
v.set_is_primary_contact(True)
con_per.append(v)

contact.set_contact_persons(con_per)


baddress = Address()
baddress.set_address('45, suite street')
baddress.set_city('California')
baddress.set_state('CA')
baddress.set_zip('9876')
baddress.set_fax('+1-925-924-9600')
contact.set_billing_address(baddress)

saddress = Address()
saddress.set_address('45, suite street')
saddress.set_city('California')
saddress.set_state('CA')
saddress.set_zip('9876')
saddress.set_fax('+1-925-924-9600')
contact.set_shipping_address(saddress)

contact.set_notes('Payment option : Through check' )

print(contact_api.update(contact_id, contact))

# to delete a contact

print(contact_api.delete(contact_id))

#mark as active

print(contact_api.mark_active(contact_id))

#mark as inactive
 
print(contact_api.mark_inactive(contact_id))

#enable payment reminder

print(contact_api.enable_payment_reminder(contact_id))

#disable payment reminder

print(contact_api.disable_payment_reminder(contact_id))

#send email statement (current month's statement will be sent to contact)

email = Email()
to_mailid = ['example@zohocorp.com', 'example@gmail.com', 'example@gmail.com']
email.set_to_mail_ids(to_mailid)
email.set_subject('Statement of transactions')
email.set_body('welcome') 
#print(contact_api.email_statement(contact_id, email))

#send email statement (mentioned date statement will be sent to contact)
start_date = '2014-01-01'
end_date = '2014-01-20'
#print(contact_api.email_statement(contact_id, email, start_date, end_date))

#send email statement with attachment 
attachment = ['/{file_directory}/fil1.txt', '/{file_directory}/fil2.txt']
print(contact_api.email_statement(contact_id, email, start_date, end_date, attachment))

# get email statement

print(contact_api.get_statement_mail_content(contact_id, '2014-01-01', '2014-01-15'))

#send email to contact

email = Email()
to_mailid = ['example@zohocorp.com', 'example@gmail.com']
email.set_to_mail_ids(to_mailid)
email.set_subject('Statement of transactions')
email.set_body('welcome') 
attachment = ['/{file_directory}/n1.png', '/{file_directory}/new1.pdf']
#print(contact_api.email_contact(contact_id, email)
print(contact_api.email_contact(contact_id, email, None, True))
print(contact_api.email_contact(contact_id, email, attachment))
print(contact_api.email_contact(contact_id, email, attachment, True))

# list comments

print(contact_api.list_comments(contact_id))
print(contact_api.get_comments(contact_id))

#list refunds

print(contact_api.list_refunds(contact_id))
print(contact_api.get_refunds(contact_id))

#track 1099

print(contact_api.track_1099(contact_id))

# untrack 1099

print(contact_api.untrack_1099(contact_id))

