#$Id$#

from books.model.Estimate import Estimate
from books.model.Address import Address
from books.model.Email import Email
from books.model.ContactPerson import ContactPerson
from books.model.LineItem import LineItem
from books.model.CustomField import CustomField

from books.service.ZohoBooks import ZohoBooks
import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

estimate_api = zoho_books.get_estimates_api()

estimate_id = estimate_api.get_estimates().get_estimates()[0].get_estimate_id()
estimate_ids = estimate_api.get_estimates().get_estimates()[0].get_estimate_id() + ',' + estimate_api.get_estimates().get_estimates()[1].get_estimate_id()

contact_api = zoho_books.get_contacts_api()
customer_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()

items_api = zoho_books.get_items_api()
item_id = items_api.list_items().get_items()[0].get_item_id()

template_id  = estimate_api.list_estimate_template().get_templates()[0].get_template_id()

# to list Estimates

print estimate_api.get_estimates()

# to get an estimate

#print estimate_api.get(estimate_id)
#print estimate_api.get(estimate_id, True)
#print estimate_api.get(estimate_id, False)
#print estimate_api.get(estimate_id, True, 'json')
print estimate_api.get(estimate_id, None, 'html')

#to create an estimate

ref_num = 'QRT-123456'
date = '2013-10-03'
expiry_date = '2013-10-17'
exchange_rate = 1.0
discount = 0.0
discount_type = 'item_level'
salesperson_name = 'Billu'
name = 'at'
description = 'building'

estimate = Estimate()
estimate.set_customer_id(customer_id)
contact_person = []

estimate.set_contact_persons(contact_person)

estimate.set_template_id(template_id)
estimate.set_reference_number(ref_num)
estimate.set_date(date)
estimate.set_expiry_date(expiry_date)
estimate.set_exchange_rate(exchange_rate)
estimate.set_discount(discount)
estimate.set_is_discount_before_tax(True)
estimate.set_discount_type(discount_type)
estimate.set_salesperson_name(salesperson_name)

line_items = LineItem()
line_items.set_item_id(item_id)
line_items.set_name(name)
line_items.set_description(description)
estimate.set_line_items(line_items)

line_items1 = LineItem()
line_items1.set_item_id(item_id)
line_items1.set_name('at')
line_items1.set_description('build')
estimate.set_line_items(line_items1) 

custom_field = CustomField()
custom_field.set_index('')
custom_field.set_value('custom')
estimate.set_custom_fields(custom_field)

estimate.set_notes('looking forward for your business')
estimate.set_terms('terms and conditions apply')
estimate.set_shipping_charge(0.0)
estimate.set_adjustment(0.0)
estimate.set_adjustment_description('Adjustment')


#print estimate_api.create(estimate)
#print estimate_api.create(estimate, False)
#estimate.set_estimate_number('35')
#print estimate_api.create(estimate, True, True)
#print estimate_api.create(estimate, None, False)
print estimate_api.create(estimate, True, None)

# update an estimate

ref_num = 'QRT-123456'
date = '2013-10-03'
expiry_date = '2013-10-17'
exchange_rate = 1.0
discount = 0.0
discount_type = 'item_level'
salesperson_name = 'Bob'
name = 'at'
description = 'building'

estimate = Estimate()
estimate.set_customer_id(customer_id)

contact_person = []

estimate.set_contact_persons(contact_person)

estimate.set_template_id(template_id)
estimate.set_reference_number(ref_num)
estimate.set_date(date)
estimate.set_expiry_date(expiry_date)
estimate.set_exchange_rate(exchange_rate)
estimate.set_discount(discount)
estimate.set_is_discount_before_tax(True)
estimate.set_discount_type(discount_type)
estimate.set_salesperson_name(salesperson_name)

line_items = LineItem()
line_items.set_item_id(item_id)
line_items.set_name(name)
line_items.set_description(description)
estimate.set_line_items(line_items)

line_items1 = LineItem()
line_items1.set_item_id(item_id)
line_items1.set_name('at')
line_items1.set_description('build')
estimate.set_line_items(line_items1) 
custom_field = CustomField()
custom_field.set_index('')
custom_field.set_value('custom')
estimate.set_custom_fields(custom_field)

estimate.set_notes('looking forward for your business')
estimate.set_terms('terms and conditions apply')
estimate.set_shipping_charge(0.0)
estimate.set_adjustment(0.0)
estimate.set_adjustment_description('Adjustment')

#print estimate_api.update(estimate_id, estimate)
print estimate_api.update(estimate_id, estimate, False)

# delete an estimate

print estimate_api.delete(estimate_id)

# mark an estimate as sent

print estimate_api.mark_an_estimate_as_sent(estimate_id)

# mark an estimate as accepted 

print estimate_api.mark_an_estimate_as_accepted(estimate_id)

# mark an estimate as declined

print estimate_api.mark_an_estimate_as_declined(estimate_id)

# email an estimate

email = Email()
to_mailid = ['example@gmail.com', 'example@zohocorp.com']
email.set_to_mail_ids(to_mailid)
email.set_subject('Statement of transactions')
email.set_body('welcome') 

print estimate_api.email_an_estimate(estimate_id, email)

#email an estimate (attach a file)
email = Email()
to_mailid = ['example@gmail.com', 'example@zohocorp.com']
email.set_to_mail_ids(to_mailid)
email.set_subject('Statement of transactions')
email.set_body('welcome') 
email.set_file_name('new1.pdf')

attachment = ['/{file_directory}/fil1.txt', '/{file_directory}/fil2.txt']
print estimate_api.email_an_estimate(estimate_id, email, attachment)

# email estimates

print estimate_api.email_estimates(estimate_ids) #check whether email success message has to be modelled!

# Get estimate email content

print estimate_api.get_estimate_email_content(estimate_id)
print estimate_api.get_estimate_email_content(estimate_id, template_id)

# Bulk export estimates

print estimate_api.bulk_export_estimates(estimate_ids)

#bulk print estimates

print estimate_api.bulk_print_estimates(estimate_ids)

#update billing address

billing_address = Address()
billing_address.set_address('43,  Km street')
billing_address.set_city('Chennai')
billing_address.set_state('TamilNadu')
billing_address.set_zip('3344')
billing_address.set_country('India')
billing_address.set_fax('67899')

print estimate_api.update_billing_address(estimate_id, billing_address)
print estimate_api.update_billing_address(estimate_id, billing_address, True)

# update shipping address

shipping_address = Address()
shipping_address.set_address('43,  Km street')
shipping_address.set_city('Chennai')
shipping_address.set_state('TamilNadu')
shipping_address.set_zip('3344')
shipping_address.set_country('India')
shipping_address.set_fax('67899')

print estimate_api.update_shipping_address(estimate_id, shipping_address)
print estimate_api.update_shipping_address(estimate_id, shipping_address, False)

#list estimate template

print estimate_api.list_estimate_template()

#update estimate template

print estimate_api.update_estimate_template(estimate_id, template_id)

#------------------------------------------------------------------------------------------------------------------------------------------

# Comments and history 


comment_id = estimate_api.list_comments_history(estimate_id).get_comments()[0].get_comment_id()

#list estimate comments & history

print estimate_api.list_comments_history(estimate_id)

#Add Comment

print estimate_api.add_comment(estimate_id, 'is description', True)

# Update Comment

print estimate_api.update_comment(estimate_id, comment_id, 'is a description', False)

#delete Comment

print estimate_api.delete_comment(estimate_id, comment_id)

