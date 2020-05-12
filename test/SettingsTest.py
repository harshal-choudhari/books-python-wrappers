#$Id$#

from books.model.Preference import Preference
from books.model.Organization import Organization
from books.model.Address import Address
from books.model.User import User
from books.model.Item import Item
from books.model.InvoiceSetting import InvoiceSetting
from books.model.NotesAndTerms import NotesAndTerms
from books.model.EstimateSetting import EstimateSetting
from books.model.CreditnoteSetting import CreditnoteSetting
from books.model.Currency import Currency
from books.model.ExchangeRate import ExchangeRate
from books.model.Tax import Tax
from books.model.OpeningBalance import OpeningBalance
from books.model.Account import Account
from books.model.Autoreminder import Autoreminder
from books.model.ManualReminder import ManualReminder
from books.model.TaxGroup import TaxGroup
from books.service.ZohoBooks import ZohoBooks
import os

access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

settings_api = zoho_books.get_settings_api()
organizations_api = zoho_books.get_organizations_api()
users_api = zoho_books.get_users_api()
items_api = zoho_books.get_items_api()

currency_id = settings_api.get_currencies().get_currencies()[0].get_currency_id()
#List preferences

print settings_api.list_preferences()

#Update preference

preference = Preference()
preference.set_convert_to_invoice(False)
preference.set_notify_me_on_online_payment(True)
preference.set_send_payment_receipt_acknowledgement("")
preference.set_auto_notify_recurring_invoice("")
preference.set_snail_mail_include_payment_stub("")
preference.set_is_show_powered_by(True)
preference.set_attach_expense_receipt_to_invoice("")
preference.set_allow_auto_categorize("")

print settings_api.update_preferences(preference)

# Create a unit

print settings_api.create_unit("m")

#Delete unit
unit_id = "71127000000179031"

print settings_api.delete_unit(unit_id)


#Organization
organization_id = organizations_api.get_organizations()[0].get_organization_id()

# List organizations.

print organizations_api.get_organizations()

#Get organization

print organizations_api.get(organization_id)

#Create organization

organization = Organization()
organization.set_name("Jony and co")
address = Address()
address.set_street_address1("2/65")
address.set_street_address2("vignesh plaza")
address.set_city("MDU")
address.set_state("TN")
address.set_country("India")
address.set_zip("322")
organization.set_address(address)
organization.set_industry_type("")
organization.set_industry_size("")
organization.set_fiscal_year_start_month("january")
organization.set_currency_code("USD")
organization.set_time_zone("Asia/Calcutta")
organization.set_date_format("dd MMM yyyy")
organization.set_field_separator("")
organization.set_language_code("en")
organization.set_tax_basis("accrual")
organization.set_tax_type("tax")
organization.set_org_address("")
organization.set_remit_to_address("")
print organizations_api.create(organization)

#Update organization

organization = Organization()
organization.set_name("Jony and co")
address = Address()
address.set_street_address1("2/65")
address.set_street_address2("vignesh plaza")
address.set_city("MDU")
address.set_state("TN")
address.set_country("India")
address.set_zip("322")
organization.set_address(address)
organization.set_industry_type("")
organization.set_industry_size("")
organization.set_fiscal_year_start_month("january")
organization.set_currency_code("INR")
organization.set_time_zone("Asia/Calcutta")
organization.set_date_format("dd MMM yyyy")
organization.set_field_separator("")
organization.set_language_code("en")
organization.set_tax_basis("accrual")
organization.set_tax_type("tax")
organization.set_org_address("")
organization.set_remit_to_address("")
print organizations_api.update(organization_id, organization)


# User

user_id = users_api.get_users().get_users()[0].get_user_id()
#List user

print users_api.get_users()
param = {'filter_by': 'Status.All'}
print users_api.get_users(param)

# Get user

print users_api.get(user_id)

# current user

print users_api.current_user()

#Create user

user = User()
user.set_name("karanya")
user.set_email("lek1000@d.com")
user.set_user_role("staff")
print users_api.create(user)

#update user
user = User()
user.set_name("vakaa")
user.set_email("lekha10@d.com")
user.set_user_role("staff")
print users_api.update(user_id, user)

#delete user

print users_api.delete(user_id)

#Invite user

print users_api.invite_user(user_id)

#Mark user as active

print users_api.mark_user_as_active(user_id)

#Mark user as inactive

print users_api.mark_user_as_inactive(user_id)


# Item
item_id = items_api.list_items().get_items()[0].get_item_id()
# List items.

print items_api.list_items()

# Get an item

print items_api.get(item_id)

# Create item

item = Item()
item.set_name("Item 2")
item.set_description("Item")
item.set_rate(10.0)
item.set_account_id("")
item.set_tax_id("")

print items_api.create(item)

#Update item

item = Item()
item.set_name("item 1")
item.set_description("Item")
item.set_rate(100.0)
item.set_account_id("")
item.set_tax_id("")

print items_api.update(item_id, item)

#Delete item

print items_api.delete_item(item_id)

#Mark item as active

print items_api.mark_item_as_active(item_id)

#Mark item as inactive

print items_api.mark_item_as_inactive(item_id)


#Invoice Settings
#Get invoice settings

print settings_api.get_invoice_settings()

#update invoice settings

invoice_settings = InvoiceSetting()
invoice_settings.set_auto_generate(True)
invoice_settings.set_prefix_string("INV")
invoice_settings.set_start_at(1)
invoice_settings.set_next_number("43")
invoice_settings.set_quantity_precision(2)
#invoice_settings.set_discount_enabled(False)
invoice_settings.set_reference_text("")
#invoice_settings.set_default_template_id("")
invoice_settings.set_notes("Hai")
invoice_settings.set_terms("")
invoice_settings.set_is_shipping_charge_required(True)
invoice_settings.set_is_adjustment_required(True)
invoice_settings.set_invoice_item_type("")
invoice_settings.set_discount_type("item_level")
invoice_settings.set_warn_convert_to_open(True)
invoice_settings.set_warn_create_creditnotes(True)
invoice_settings.set_is_open_invoice_editable(True)
invoice_settings.set_is_sales_person_required(True)
print settings_api.update_invoice_settings(invoice_settings)

#Get invoice notes and terms

print settings_api.get_invoice_notes_and_terms()

#Update invoice notes and terms
notes_and_terms = NotesAndTerms()
notes_and_terms.set_notes("Thanks")
notes_and_terms.set_terms("")
print settings_api.update_invoice_notes_and_terms(notes_and_terms)

"""
#Estimates

#Get estimates settings.
"""
print settings_api.get_estimate_settings()

#update estimate settings

estimate_settings = EstimateSetting()
estimate_settings.set_auto_generate(True)
estimate_settings.set_prefix_string("EST-")
estimate_settings.set_start_at(2)
estimate_settings.set_next_number("041")
estimate_settings.set_quantity_precision(2)
estimate_settings.set_discount_type("item_level")
estimate_settings.set_reference_text("")
estimate_settings.set_notes("Hai")
estimate_settings.set_terms("")
estimate_settings.set_terms_to_invoice(True)
estimate_settings.set_notes_to_invoice(True)
estimate_settings.set_warn_estimate_to_invoice(True)
estimate_settings.set_is_sales_person_required(True)
print settings_api.update_estimate_settings(estimate_settings)

#Get estimates notes and terms.

print settings_api.get_estimates_notes_and_terms()

#update estimate notes and terms

notes_and_terms = NotesAndTerms()
notes_and_terms.set_notes("Thanks")
notes_and_terms.set_terms("")
print settings_api.update_estimates_notes_and_terms(notes_and_terms)
"""
#Creditnotes

#List credit note
"""
print settings_api.list_creditnote_settings()

#Update creditnotes settings

creditnote_settings = CreditnoteSetting()
creditnote_settings.set_auto_generate(True)
creditnote_settings.set_prefix_string("CN-")
creditnote_settings.set_reference_text("")
creditnote_settings.set_next_number("0027")
creditnote_settings.set_notes("Thank you")
creditnote_settings.set_terms("Conditions Apply")
print settings_api.update_creditnote_settings(creditnote_settings)

#Get creditnote notes and terms

print settings_api.get_creditnote_notes_and_terms()

#update creditnote notes and terms

notes_and_terms = NotesAndTerms()
notes_and_terms.set_notes("Thanks")
notes_and_terms.set_terms("")
print settings_api.update_creditnote_notes_and_terms(notes_and_terms)

"""
#Currency and exchange rate

#List currencies

"""
print settings_api.get_currencies()

#Get a currency

print settings_api.get_currency(currency_id)

#Create a currency

currency = Currency()
currency.set_currency_code("NPR")
currency.set_currency_symbol("")
currency.set_price_precision(1)
currency.set_currency_format("1,234,567.89")
print settings_api.create_currency(currency)

#Update currency
currency = Currency()
currency.set_currency_code("NPR")
currency.set_currency_symbol("")
currency.set_price_precision(1)
currency.set_currency_format("1,234,567.89")
print settings_api.update_currency(currency_id , currency)

#Delete currency

print settings_api.delete_currency(currency_id)
"""
#List exchange rates
exchange_rate_id = settings_api.list_exchange_rates(currency_id).get_exchange_rates()[0].get_exchange_rate_id()
"""
print settings_api.list_exchange_rates(currency_id)

#Get exchange rate 

print settings_api.get_exchange_rate(currency_id, exchange_rate_id)

#Create an exchange rate
exchange_rate = ExchangeRate()
exchange_rate.set_currency_id(currency_id)
exchange_rate.set_currency_code("NPR")
exchange_rate.set_effective_date("2014-05-08")
exchange_rate.set_rate(25.0)
print settings_api.create_exchange_rate(exchange_rate)

#Update an exchange rate

exchange_rate = ExchangeRate()
exchange_rate.set_exchange_rate_id(exchange_rate_id)
exchange_rate.set_currency_id(currency_id)
exchange_rate.set_currency_code("EUR")
exchange_rate.set_effective_date("2014-05-08")
exchange_rate.set_rate(25.0)
print settings_api.update_exchange_rate(exchange_rate)

#Delete an exchange rate

print settings_api.delete_exchange_rate(currency_id, exchange_rate_id)

"""
#Tax and Tax group
tax_id = settings_api.get_taxes().get_taxes()[0].get_tax_id()
tax_group_id = "71127000000184003"
#List taxes
"""
print settings_api.get_taxes()

#Get a tax

print settings_api.get_tax(tax_id)

#Create tax

tax = Tax()
tax.set_tax_name("tax-1")
tax.set_tax_percentage(10.5)
tax.set_tax_type("tax")
print settings_api.create_tax(tax)

#update tax
tax = Tax()
tax.set_tax_name("Shipping_tax1")
tax.set_tax_percentage(10.5)
tax.set_tax_type("tax")
print settings_api.update_tax(tax_id, tax)

#Delete tax
print settings_api.delete_tax(tax_id)

#Get tax group
print settings_api.get_tax_group(tax_group_id)

#Create tax group
tax_group = TaxGroup()
tax_group.set_tax_group_name("group_taxes")
taxes = "71127000000183009,71127000000191007"
tax_group.set_taxes(taxes)
print settings_api.create_tax_group(tax_group)

#update tax group

tax_group = TaxGroup()
tax_group.set_tax_group_name("group_taxes")
taxes = "71127000000185001,71127000000183007"
tax_group.set_taxes(taxes)
tax_group.set_tax_group_id(tax_group_id)
print settings_api.update_tax_group(tax_group)

#Delete tax group
tax_group_id = "711270"
print settings_api.delete_tax_group(tax_group_id)
"""
#Opening balance
#Get opening balance
"""
print settings_api.get_opening_balance()

#Create opening balance

account_id="71127000000170302"
opening_balance = OpeningBalance()
opening_balance.set_date('2014-05-09')
accounts = Account()
accounts.set_account_id(account_id)
accounts.set_debit_or_credit("debit")
accounts.set_exchange_rate(1.0)
accounts.set_currency_id(currency_id)
accounts.set_amount(200.0)
opening_balance.set_accounts(accounts)
print settings_api.create_opening_balance(opening_balance)

#Update opening balance

account_id="71127000000170302"
opening_balance = OpeningBalance()
opening_balance.set_opening_balance_id("71127000000186001")
opening_balance.set_date('2014-05-09')
accounts = Account()
accounts.set_account_id(account_id)
accounts.set_debit_or_credit("debit")
accounts.set_exchange_rate(1.0)
accounts.set_currency_id("71127000000000099")
accounts.set_amount(2000.0)
opening_balance.set_accounts(accounts)
print settings_api.update_opening_balance(opening_balance)

#Delete opening balance

print settings_api.delete_opening_balance()
"""

#Auto payment reminder
auto_payment_reminder_id = settings_api.list_auto_payment_reminder().get_auto_reminders()[0].get_autoreminder_id()
#List auto payment reminder
"""
print settings_api.list_auto_payment_reminder()
"""
#Get an auto payment reminder
print settings_api.get_auto_payment_reminder(auto_payment_reminder_id)
"""
#Update an auto reminder
autoreminder = Autoreminder()
autoreminder.set_is_enabled(True)
autoreminder.set_notification_type('days_after_due_date')
autoreminder.set_address_type('remind_me')
autoreminder.set_number_of_days(3)
autoreminder.set_subject('hai')
autoreminder.set_body('Reminder')
print settings_api.update_auto_reminder(reminder_id, autoreminder)

"""
#List manual reminders
reminder_id = settings_api.list_manual_reminders().get_manual_reminders()[0].get_manualreminder_id()
"""
print settings_api.list_manual_reminders()
"""
#Get a manual reminder

print settings_api.get_manual_reminder(reminder_id)
"""
#Update a manual reminder

manual_reminder = ManualReminder()
manual_reminder.set_subject("Hello")
manual_reminder.set_body("Manual reminder")
manual_reminder.set_cc_me(False)
print settings_api.update_manual_reminder(reminder_id, manual_reminder)

"""
