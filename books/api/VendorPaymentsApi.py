#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.VendorPaymentsParser import VendorPaymentsParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'vendorpayments/'
parser = VendorPaymentsParser()
zoho_http_client = ZohoHttpClient()

class VendorPaymentsApi:
    """Vendor Payaments Api is used to

    1.List all the paymnets made to your vendor.
    2.Get the details of a vendor payment.
    3.Create a payment made to the vendor.
    4.Update an existing vendor payment.
    5.Delete an existing vendor payment.

    """
    def __init__(self, authtoken, organization_id):
        """Initialize Vendor payments api using user's authtoken and 
            organization id.

        Args: 
            authtoken(str): User's authtoken.
            organization_id(str): User's organization id.

        """
        self.headers = {
            'Authorization': 'Zoho-oauthtoken ' + authtoken,
        }
        self.details = {
            'organization_id': organization_id
            }
   
    def get_vendor_payments(self, parameter=None):
        """List all the payments made to the vendor.

        Args:
            parameter(dict, optional): Filter with which the list has to be 
                displayed.

        Returns:
            instance: Vendor payments list object.

        """
        resp = zoho_http_client.get(base_url, self.details, self.headers, parameter)
        return parser.get_list(resp) 

    def get(self, payment_id):
        """Get the details of vendor payment.
 
        Args:
            payment_id(str): Payment id.
 
        Returns:
            instance: Vendor payments object.

        """
        url = base_url + payment_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_vendor_payment(resp) 

    def create(self, vendor_payments):
        """Create a payment made to vendor.

        Args:
            vendor_payments(instance): Vendor payments object.

        Returns:
            instance: Vendor payments object.

        """
        json_object = dumps(vendor_payments.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data)
        return parser.get_vendor_payment(resp) 

    def update(self, payment_id, vendor_payments):
        """Update an existing vendor payment.
      
        Args:
            payment_id(str): Payment id.
            vendor_payments(instance): Vendor payments object.

        Returns:
            instance: Vendor payments object.
 
        """
        url = base_url + payment_id
        json_object = dumps(vendor_payments.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_vendor_payment(resp) 

    def delete(self, payment_id):
        """Delete an existing vendor payment.
 
        Args:
            payment_id(str): Payment id.

        Returns:
            str: Success message('The paymenet has been deleted.').

        """
        url = base_url + payment_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 




