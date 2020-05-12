#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.ContactParser import ContactParser
from .Api import Api
from json import dumps

base_url = Api().base_url + 'contacts/'
parser = ContactParser()
zoho_http_client = zoho_http_client = ZohoHttpClient()

class ContactPersonsApi:
    """ContactPersonsApi class is used to:

    1.To get the list of contact persons of a contact with pagination.
    2.To get the details of a contact person.
    3.To create a contact person for a contact.
    4.To update an existing contact person.
    5.To delete a contact person.
    6.To mark a contact person as primary for the contact.

    """
 
    def __init__(self, authtoken, organization_id):
        """Initialize ContactPersons Api using user's authtoken and 
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

    def get_contact_persons(self, contact_id):
        """List contact persons of a contact with pagination.

        Args:
            contact_id(str): Contact id of a contact.

        Returns:
            instance: Contact Persons list object.

        """ 
        url = base_url + contact_id + '/contactpersons'
        response=zoho_http_client.get(url, self.details, self.headers)
        return parser.get_contact_persons(response) 

    def get(self, contact_person_id):
        """Get the contact persons details.

        Args:
            contact_id(str): Contact id of a contact.

        Returns:
            instance: Contact Person object.

        """
        url = base_url + 'contactpersons/' + contact_person_id
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_contact_person(response) 
  
    def create(self, contact_person):
        """Create a contact person for contact.

        Args:
            contact_id(str): Contact_id of a contact.

        Returns:
            instance: Contact person object.

        """
        url = base_url + 'contactpersons'
        json_object = dumps(contact_person.to_json())
        data = {
            'JSONString': json_object
            }
        response = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_contact_person(response)
   
    def update(self, contact_person_id, contact_person):
        """Update an existing contact person.

        Args:
            contact_id(str): Contact_id of a contact.
            contact_person(instance): Contact person object.

        Returns:
            instance: Contact person object.

        """
        url = base_url + 'contactpersons/' + contact_person_id
        json_object = dumps(contact_person.to_json())
        data = {
            'JSONString': json_object
            }
        response = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_contact_person(response) 

    def delete(self, contact_person_id):
        """Delete a contact person.
        
        Args:
            contact_person_id(str): Contact person id of a contact person.
    
        Returns:
            str: Success message('The contact person has been deleted').
 
        """
        url = base_url + 'contactpersons/' + contact_person_id
        response = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(response)
      
    def mark_as_primary_contact(self, contact_person_id):
        """Mark a contact person as primary for the contact.
        
        Args:
            contact_person_id(str): Contact person id of a contact person.
       
        Returns:
            str: Success message('This contact person has been marked as 
                your primary contact person.').
      
        """
        url = base_url + 'contactpersons/' + contact_person_id + '/primary'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 
    
  
   
