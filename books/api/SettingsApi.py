#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.SettingsParser import SettingsParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'settings/'
zoho_http_client = ZohoHttpClient()
parser = SettingsParser()

class SettingsApi:
    """This class is used to 
 
    1.List preferences that are configured.
    2.Update the preferences that has been configured.
    3.Create a unit that can be associated to a line item.
    4.Delete a unit that has been associated to a line item.
    5.Get the details of invoice settings.
    6.Update the settings information of invoice.
    7.Get the details of notes and terms.
    8.Update invoice notes and terms.
    9.Get estimate settings.
    10.Update estimate settings.
    11.Get estimate notes and terms.
    12.Update estimate notes and terms.
    13.List creditnotes settings.
    14.Update creditnotes settings.
    15.Get creditnote notes and term
    16.Update creditnote notes and terms.
    17.List currencies.
    18.Get details of a currency.
    19.Create a currency.
    20.Update a currency.
    21.Delete a currency.
    22.List exchange rates.
    23.Get an exchange rate.
    24.Create an exchange rate.
    25.Update an exchange rate.
    26.Delete an exchange rate.
    27.List taxes.
    28.Get details of a tax.
    29.Create a tax.
    30.Update a tax.
    31.Delete a tax.
    32.Get a tax group.
    33.Create a tax group.
    34.Update a tax group.
    35.Delete a tax group.
    36.Get Opening balance.
    37.Create opening balance.
    38.Update opening balance.
    39.Delete opening balance.
    40.List auto payment reminder.
    41.Get an auto payment reminder.
    42.Enable auto reminder.
    43.Disable auto reminder.
    44.Update an auto reminder.
    45.List manual reminders.
    46.Get a manual reminder.
    47.Update a manual reminder. 

    """

    def __init__(self, authtoken, organization_id):
        """Initialize Settings Api using authtoken and organization id.

        Args:
            authtoken(str): User's Authtoken.
            organization_id(str): User's Organization id.

        """
        self.headers = {
            'Authorization': 'Zoho-oauthtoken ' + authtoken,
        }
        self.details = {
            'organization_id': organization_id 
            }
    
    def list_preferences(self):
        """List of preferences that are configured.

        Returns: 
            instance: Preference list object.

        """
        url = base_url + 'preferences'
        resp = zoho_http_client.get(url, self.details, self.headers) 
        return parser.preference_list(resp) 

    def update_preferences(self, preference):
        """Update preference.

        Args:
            preference(instance): Preference object.

        Returns:
            str: Success message('Preferences have been saved.').
 
        """
        url = base_url + 'preferences'
        json_object = dumps(preference.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, data, self.headers)
        return parser.get_message(resp) 

    def create_unit(self, unit):
        """Create a unit that can be associated to a line item.

        Args:
            unit(str): Unit. Eg: Kg. 
   
        Returns:
            str: Success message('Unit added.').

        """
        url = base_url + 'units'
        data = { 
            'unit': unit
            }
        json_string = {
            'JSONString': dumps(data)
            }
        resp = zoho_http_client.post(url, self.details, self.headers, json_string)
        return parser.get_message(resp) 
        
    def delete_unit(self, unit_id):
        """Delete a unit that has been associated to an item.

        Args:
            unit_id(str): Unit id.

        Returns:
            str: Success message('You have successfully deleted the unit.').

        """
        url = base_url + 'units/' + unit_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
    
    def get_invoice_settings(self):
        """Get the details of invoice settings.
 
        Returns:
            instance: Invoice settings object.
 
        """
        url = base_url + 'invoices'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_invoice_settings(resp) 

    def update_invoice_settings(self, invoice_settings):
        """Update the settings information for invoices.

        Args:
            invoice_settings(instance): Invoice settings.

        Returns:
            instance: Invoice settings object.

        """
        url = base_url + 'invoices'
        json_object = dumps(invoice_settings.to_json())
        data = { 
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_invoice_settings(resp)

    def get_invoice_notes_and_terms(self):
        """Get the details of invoce notes and terms.

        Returns:
            instance: Notes and terms object.

        """
        url = base_url + 'invoices/notesandterms'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_notes_and_terms(resp) 

    def update_invoice_notes_and_terms(self, invoice_notes_and_terms):
        """Update the notes and terms for an invoice.

        Args:
            invoice_notes_and_terms(instance): Invoice notes and terms object.

        Returns:
            instance: Invoice notes and terms object.

        """
        url = base_url + 'invoices/notesandterms'
        json_object = dumps(invoice_notes_and_terms.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_notes_and_terms(resp) 

    def get_estimate_settings(self):
        """Get estimate settings.

        Returns:
            instance: Estimate settings.

        """
        url = base_url + 'estimates'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_estimate_settings(resp) 

    def update_estimate_settings(self, estimate_setting):
        """Update estimate settings.

        Args:
            estimate_setting(instance): Estimate setting object.

        Returns:
            instance: Estiamte setting object.
 
        """
        url = base_url + 'estimates'
        json_object = dumps(estimate_setting.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_estimate_settings(resp) 

    def get_estimates_notes_and_terms(self): 
        """Get estimates notes and terms.

        Returns:   
            instance: notes and terms object.

        """
        url = base_url + 'estimates/notesandterms'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_notes_and_terms(resp) 

    def update_estimates_notes_and_terms(self, notes_and_terms):
        """Update estimate notes and terms.

        Args:
            notes_and_terms(instance): Notes and terms object.
 
        Returns:
            instance: Estimates notes and terms.
  
        """
        url = base_url + 'estimates/notesandterms'
        json_object = dumps(notes_and_terms.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data) 
        return parser.get_notes_and_terms(resp) 

    def list_creditnote_settings(self):
        """List creditnotes settings.

        Returns:
            instance: creditnotes settings.

        """
        url = base_url + 'creditnotes'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_creditnote_settings(resp) 

    def update_creditnote_settings(self, creditnotes_settings):
        """Update creditnotes settings.

        Args:
            creditnotes_settings(instance): Creditnotes settings object.

        Returns:
            instance: Creditnotes settings object.

        """
        url = base_url + 'creditnotes'
        json_object = dumps(creditnotes_settings.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_creditnote_settings(resp) 

    def get_creditnote_notes_and_terms(self):
        """Get creditnotes notes and terms.

        Returns:
            instance: Creditnotes settings object.

        """
        url = base_url + 'creditnotes/notesandterms'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_notes_and_terms(resp)

    def update_creditnote_notes_and_terms(self, notes_and_terms):
        """Update creditnotes notes and terms.

        Args:
            notes_and_terms(instance): Notes and terms object.

        Returns:
            instance: Notes and terms object.

        """
        url = base_url + 'creditnotes/notesandterms'
        json_object = dumps(notes_and_terms.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data) 
        return parser.get_notes_and_terms(resp) 

    def get_currencies(self, param=None):
        """List of configured currencies with pagination.

        Args:
            param(dict, optional): Filter with which the list has to be 
                 displayed.

        Returns:
            instance: Currency list object.

        """
        url = base_url + 'currencies'
        if param is not None:
            data = {
                'filter_by': param
                }
        else:
            data = None
        resp = zoho_http_client.get(url, self.details, self.headers, data)
        return parser.get_currencies(resp) 

    def get_currency(self, currency_id):
        """Get the details of a currency.

        Args:
            currency_id(str): Currency id.

        Returns:
            instance: Currency object.

        """
        url = base_url + 'currencies/' + currency_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_currency(resp) 

    def create_currency(self, currency):
        """Create a currency for transactions.

        Args:
            currency(instance): Currency object.

        Returns: 
            instance: Currency object.

        """
        url = base_url + 'currencies'
        json_obj = dumps(currency.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_currency(resp) 
    
    def update_currency(self, currency_id, currency):
        """Update the details of currency.

        Args:
            currency_id(str): Currency id.
            currency(instance): Currency object.

        Returns:     
            instance: Currecny object.

        """
        url = base_url + 'currencies/' + currency_id 
        json_obj = dumps(currency.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_currency(resp) 
     
    def delete_currency(self, currency_id):
        """Delete currency.

        Args:
            currency_id(str): Currency id.

        Returns:
            str: Success message('The currency has been deleted.').
 
        """
        url = base_url + 'currencies/' + currency_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def list_exchange_rates(self, currency_id, param=None):
        """List of exchange rates configured for the currency.

        Args:
            param(dict, optional): Filter with which the list has to be 
                displayed.

        Returns:
            instance: Exchange rate list object.

        """
        url = base_url + 'currencies/' + currency_id + '/exchangerates'
        resp = zoho_http_client.get(url, self.details, self.headers, param)
        return parser.get_exchange_rates(resp) 

    def get_exchange_rate(self, currency_id, exchange_rate_id):
        """Get details of an exchange rate that has been associated to the 
            currency.

        Args:
            currency_id(str): Currency id.
            exchange_rate_id(str): Exchange rate id.

        Returns:
            instance: Exchange rate object.

        """ 
        url = base_url + 'currencies/' + currency_id + '/exchangerates/' + \
              exchange_rate_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_exchange_rate(resp) 

    def create_exchange_rate(self, exchange_rate):
        """Create an exchange rate for the specified currency.

        Args:
            currency_id(str): Currency id.
            exchange_rate(instance): Exchange rate object.

        Returns:
            instance: Exchange rate object.

        """
        url = base_url + 'currencies/' + exchange_rate.get_currency_id() + \
              '/exchangerates'
        json_obj = dumps(exchange_rate.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_exchange_rate(resp) 
 
    def update_exchange_rate(self, exchange_rate):
        """Update the details of exchange rate currency.

        Args: 
            exchange_rate(instance): Exchnage rate object.
           
        Returns:
            str: Success message('The exchange rate has been update.').
      
        """
        url = base_url + 'currencies/' + exchange_rate.get_currency_id() + \
              '/exchangerates/' + exchange_rate.get_exchange_rate_id()
        json_obj = dumps(exchange_rate.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_message(resp) 

    def delete_exchange_rate(self, currency_id, exchange_rate_id):
        """Delete an exchnage rate for the specified currency.

        Args:
            currency_id(str): Currency id.
            exchange_rate_id(str): Exchange rate id.

        Returns:
            str: Success message('Exchange rate successfully deleted.').
 
        """
        url = base_url + 'currencies/' + currency_id + '/exchangerates/' + \
              exchange_rate_id
        resp = zoho_http_client.delete(url, self.details, self.headers) 
        return parser.get_message(resp) 

    def get_taxes(self):
        """List of taxes with pagination.

        Returns:
            instance: Tax list object.

        """
        url = base_url + 'taxes'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_taxes(resp) 

    def get_tax(self, tax_id):
        """Get details of a tax.

        Args:
            tax_id(str): Tax id.

        Returns:
            instance: Tax object.

        """
        url = base_url + 'taxes/' + tax_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_tax(resp) 
    
    def create_tax(self, tax):
        """Create tax.

        Args:
            tax(instance): Tax object.

        Returns:
            instance: Tax object.

        """
        url = base_url + 'taxes'
        json_obj = dumps(tax.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_tax(resp) 
 
    def update_tax(self, tax_id, tax):
        """Update the details of tax.

        Args:
            tax_id(str): Tax id.
            tax(instance): Tax object.

        Returns:
            instance: Tax object.

        """
        url = base_url + 'taxes/' + tax_id
        json_obj = dumps(tax.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_tax(resp) 
            
    def delete_tax(self, tax_id):
        """Delete tax.

        Args:
            tax_id(str): Tax id.

        Returns:
            str: Success message('The record has been deleted.').

        """
        url = base_url + 'taxes/' + tax_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
   
    def get_tax_group(self, tax_group_id):
        """Get details of a tax group with associated taxes.

        Args:
            tax_group_id(str): Tax group id.

        Returns:
            instance: Tax group object.

        """
        url = base_url + 'taxgroups/' + tax_group_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_tax_group(resp)

    def create_tax_group(self, tax_group):
        """Create a tax group associating multiple taxes.

        Args:
            tax_group_name(str): Tax group name.
            taxes(str): List of tax ids associated to the tax group.

        Returns:
            instance: Tax group object.
 
        """
        url = base_url + 'taxgroups'
        json_obj = dumps(tax_group.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_tax_group(resp) 

    def update_tax_group(self, tax_group):
        """Update tax group.

        Args:
            tax_group_id(str): Tax group id.
            tax_group_name(str): Tax group name.
            taxes(str): List of tax ids associated to that tax group.

        Returns:
            instance: Tax group object.

        """
        url = base_url + 'taxgroups/' + tax_group.get_tax_group_id()
        json_obj = dumps(tax_group.to_json())
        data = {
            'JSONString': json_obj
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_message(resp) 
 
    def delete_tax_group(self, tax_group_id): 
        """Delete tax group.

        Args:
            tax_group_id(str): Tax group id.

        Returns:
            str: Success message('The tax group has been deleted.'). 
   
        """
        url = base_url + 'taxgroups/' + tax_group_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def get_opening_balance(self):
        """Get opening balance.

        Returns:
            instance: Opening balance object.

        """
        url = base_url + 'openingbalances'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_opening_balance(resp) 

    def create_opening_balance(self, opening_balance):
        """Create opening balance.

        Args:
            opening_balance(instance): Opening balance object.

        Returns:
            instance: Opening balance object.

        """
        url = base_url + 'openingbalances'
        json_object = dumps(opening_balance.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_opening_balance(resp) 

    def update_opening_balance(self, opening_balance):
        """Update opening balance.

        Args:
            opening_balance(instance): Opening balance object.

        Returns:
            instance: Opening balance object.

        """
        url = base_url + 'openingbalances'
        json_object = dumps(opening_balance.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_opening_balance(resp) 

    def delete_opening_balance(self):
        """Delete the entered opening balance.

        Returns:
            str: Success message('The entered opening balance has been 
                deleted.').

        """
        url = base_url + 'openingbalances'
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 
                 
    def list_auto_payment_reminder(self):
        """List auto payment reminder.

        Returns:
            instance: Autoreminders list object.

        """
        url = base_url + 'autoreminders'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_autoreminders(resp) 

    def get_auto_payment_reminder(self, reminder_id):
        """Get auto payment reminder.
 
        Args:
            reminder_id(str): Reminder id.

        Returns:
            instance: Auto payment reminder object.

        """
        url = base_url + 'autoreminders/' + reminder_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_autoreminder(resp) 

    def enable_auto_reminder(self, reminder_id):
        """Enable automated payment reminder.

        Args:
            reminder_id(str): Reminder id.

        Returns:
            str: Success message('Payment reminder has been enabled.').

        """
        url = base_url + 'autoreminders/' + reminder_id + '/enable'
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp) 

    def disable_auto_reminder(self, reminder_id):
        """Disable automated payment reminder.

        Args:
            reminder_id(str): Reminder id.

        Returns:
            str: Success message('Payment reminder has been disabled.').

        """
        url = base_url + 'autoreminders/' + reminder_id + '/disable'
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_message(resp) 

    def update_auto_reminder(self, reminder_id, autoreminder):
        """Update an auto reminder.

        Args: 
            reminder_id(str): Reminder id.
            autoreminder(instance): Auto reminder object.

        Returns:
            str: Success message('Your payment reminder preferences have 
                been saved.').

        """
        url = base_url + 'autoreminders/' + reminder_id 
        json_obj = autoreminder.to_json()
        data = { 
            'JSONString': json_obj
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_message(resp) 

    def list_manual_reminders(self, type_of_reminder=None):
        """List of manual reminders.

        Args:
            type_of_reminder(str): Type to select between open or overdue 
                reminder.

        Returns:
            instance: Manual reminder list object.

        """
        url = base_url + 'manualreminders'
        if type_of_reminder is not None:
           param = {
                'type': type_of_reminder
                }
        else:
            param = None
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_manual_reminders(resp) 

    def get_manual_reminder(self, reminder_id):
        """Get the details of a manual reminder.

        Args:
            manual_reminder(instance): Manual reminder object.

        Returns:
            instance: Manual reminder object.

        """
        url = base_url + 'manualreminders/' + reminder_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_manual_reminder(resp) 

    def update_manual_reminder(self, reminder_id, manual_reminder):
        """Update manual reminder.

        Args:
            reminder_id(str): Reminder id.
            manual_reminder(instance): Manual reminder.

        Returns:
            instance: Manual reminder.

        """
        url = base_url + 'manualreminders/' + reminder_id
        json_obj = dumps(manual_reminder.to_json())
        data = { 
            'JSONString': json_obj
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_message(resp) 
 



       

