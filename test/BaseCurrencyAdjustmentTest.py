#$Id$#

from books.model.BaseCurrencyAdjustment import BaseCurrencyAdjustment
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

base_currency_adjustment_api = zoho_books.get_base_currency_adjustment_api()

base_currency_adjustment_id = base_currency_adjustment_api.get_base_currency_adjustments().get_base_currency_adjustments()[0].get_base_currency_adjustment_id()

#List base currency adjustment

parameter = { 'filter_by': 'Date.All',
              'sort_column': 'adjustment_date'}

print base_currency_adjustment_api.get_base_currency_adjustments()
print base_currency_adjustment_api.get_base_currency_adjustments(parameter)

#Get a base currency adjustment
print base_currency_adjustment_api.get(base_currency_adjustment_id)

# List account details for base currency adjustments
settings_api = zoho_books.get_settings_api()
currency_id = settings_api.get_currencies().get_currencies()[0].get_currency_id()

parameter = {'currency_id': currency_id,
             'adjustment_date': '2014-04-21',
             'exchange_rate': 20.0,
             'notes': 'sdfs'}
            
print base_currency_adjustment_api.list_account_details(parameter)

# Create a base currency adjustment 
account_ids = '71127000000000367'
base_currency_adjustment = BaseCurrencyAdjustment()
base_currency_adjustment.set_currency_id('71127000000000105')
base_currency_adjustment.set_adjustment_date('2014-04-21')
base_currency_adjustment.set_exchange_rate(20.0)
base_currency_adjustment.set_notes('hello')
print base_currency_adjustment_api.create(base_currency_adjustment, account_ids)

#Delete a base currency adjustment

print base_currency_adjustment_api.delete(base_currency_adjustment_id)

