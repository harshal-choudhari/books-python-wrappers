#$Id$#

from books.model.ContactPerson import ContactPerson
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

contact_person_api = zoho_books.get_contact_persons_api()

contact_api = zoho_books.get_contacts_api()
contact_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()

contact_person_id = contact_person_api.get_contact_persons(contact_id).get_contact_persons()[0].get_contact_person_id()

#list contact persons

print contact_person_api.get_contact_persons(contact_id)

#get contact person details

print contact_person_api.get(contact_person_id)

# create contact person

d = ContactPerson()
d.set_salutation('Mr')
d.set_first_name('bata')
d.set_last_name('kumar')
d.set_email('example@gmail.com')
d.set_phone('999887')
d.set_mobile('9998887766')
d.set_contact_id(contact_id)

print contact_person_api.create(d)

# update contact person

d.set_salutation('Ms')
d.set_first_name('anuja')
d.set_last_name('kavya')
d.set_email('kavya.anu@yzx.com')
d.set_phone('999887')
d.set_mobile('9998887766')
d.set_contact_id(contact_id)

print contact_person_api.update(contact_person_id, d)

#delete contact person

print contact_person_api.delete(contact_person_id)

#mark as primary contact

print contact_person_api.mark_as_primary_contact(contact_person_id)


