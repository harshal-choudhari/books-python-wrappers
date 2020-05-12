#$Id$#

from books.model.BankRule import BankRule
from books.model.Criteria import Criteria
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

bank_rules_api = zoho_books.get_bank_rules_api()

accounts_api = zoho_books.get_bank_accounts_api()
account_id = accounts_api.get_bank_accounts().get_bank_accounts()[0].get_account_id()
target_account_id = accounts_api.get_bank_accounts().get_bank_accounts()[1].get_account_id()

rule_id = bank_rules_api.get_rules(account_id).get_bank_rules()[0].get_rule_id()

contact_api = zoho_books.get_contacts_api()
customer_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()

# get rules list

print bank_rules_api.get_rules(account_id)

# get a rule

print bank_rules_api.get(rule_id)

#create a rule

rule=BankRule()
rule.set_rule_name('rule 9')
rule.set_target_account_id(target_account_id)
rule.set_apply_to('deposits')
rule.set_criteria_type('and')
criteria = Criteria()
criteria.set_field('payee')
criteria.set_comparator('is')
criteria.set_value('dfd')
rule.set_criterion(criteria)
rule.set_record_as('sales_without_invoices')
rule.set_account_id(account_id)
rule.set_tax_id('')
rule.set_reference_number('from_statement')
rule.set_customer_id(customer_id)

print bank_rules_api.create(rule)

# update a rule
rule=BankRule()
rule.set_rule_name('rule 8')
rule.set_target_account_id(target_account_id)
rule.set_apply_to('deposits')
rule.set_criteria_type('and')
criteria = Criteria()
criteria.set_field('payee')
criteria.set_comparator('is')
criteria.set_value('dfd')
rule.set_criterion(criteria)
rule.set_record_as('sales_without_invoices')
rule.set_account_id(account_id)
rule.set_tax_id('')
rule.set_reference_number('from_statement')
rule.set_customer_id(customer_id)

print bank_rules_api.update(rule_id,rule)

# Delete a rule

print bank_rules_api.delete(rule_id)

