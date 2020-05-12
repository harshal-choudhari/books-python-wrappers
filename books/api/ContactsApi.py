#$Id$#

from os.path import basename
from json import dumps
from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.ContactParser import ContactParser
from .Api import Api

base_url = Api().base_url + 'contacts/'
parser = ContactParser()
zoho_http_client = ZohoHttpClient()

class ContactsApi:
    """ContactsApi class is used:

    1.To get the list of contacts for a particular organization.
    2.To get details of particular contact.
    3.To create a new contact for an organization.
    4.To update a contact.
    5.To delete a contact.
    6.To mark a contact as active.
    7.To mark a contact as inactive.
    8.To enable payment reminders for a contact
    9.To disable payment reminders for a contact.
    10.To send email statement to a contact.
    11.To get the statement mail content
    12.To send email to a contact.
    13.To list recent activities of a contact.
    14.To list the refund history of a contact.
    15.To track a contact for 1099 reporting.
    16.To untrack a contact for 1099 reporting.

    """
    def __init__(self, authtoken, organization_id):
        """Initialize Contacts Api using user's authtoken and organization id.

        Args:
            authtoken(str): User's authtoken.
            organization_id(str): User's organization id.

        """
        self.headers = {
            'Authorization': 'Zoho-oauthtoken ' + authtoken,
        }
        self.details={
            'organization_id': organization_id
            }
  
    def get_contacts(self, parameter=None):   
        """List of contacts with pagination for a particular organization.

        Args:
            parameter(dict, optional): Filter with which the list has to be 
                displayed. Defaults to None.

        Returns:
            instance: List of contact objects with pagination.

        """
        response = zoho_http_client.get(base_url, self.details, self.headers, parameter)
        return parser.get_contacts(response) 

    def get(self, contact_id):
        """Get details of a contact.

        Args:
            contact_id(str): Contact_id of a particular contact.

        Returns:
            instance: Contact object.

        """
        url = base_url + contact_id
        response = zoho_http_client.get(url, self.details, self.headers, None)
        return parser.get_contact(response) 

    def create(self, contact):
        """Create a contact.

        Args:
            contact(instance): Contact object.

        Returns:
            instance: Contact object.

        """
        data = contact.to_json()
        field = {
                'JSONString':dumps(data)
                } 
        response = zoho_http_client.post(base_url, self.details, self.headers, field, None)
        return parser.get_contact(response)
   
    def update(self, contact_id, contact):
        """Update a contact with the given information.

        Args:
            contact_id(str): Contact_id of the contact that has to be updated.
            contact(instance): Contact object which has the information that 
                has to be updated.

        Returns:
            instance: Contact object.

        Raises:
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id
        data = contact.to_json()
        field = {
                'JSONString':dumps(data)
                } 
        response = zoho_http_client.put(url, self.details, self.headers, field, None)
        return parser.get_contact(response) 
 
    def delete(self, contact_id):
        """Delete a particular contact.

        Args:
            contact_id(str): Contact id of the contact to be deleted.

        Returns:
            str: Success message('The contact has been deleted').

        Raises: 
            Books exception: If status is not '200' or '201'.

        """ 
        url = base_url +  contact_id
        response = zoho_http_client.delete(url, self.details,self.headers)
        return parser.get_message(response) 

    def mark_active(self, contact_id):
        """Mark a contact as active.

        Args:
            contact_id(str): Contact id of the contact.

        Returns:
            str: Success message('The contact has been marked as active').

        Raises:
            Books exception: If status is not '200' or '201'.

        """
        url= base_url + contact_id + '/active'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 

    def mark_inactive(self, contact_id):
        """Mark a contact as inactive.

        Args:
            contact_id(str): Contact id of the contact.

        Returns:
            str: Success message('The contact has been marked as inactive').

        Raises:
            Books exception: If status is not '200' or '201'.

        """         
        url = base_url + contact_id + '/inactive'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response) 

    def enable_payment_reminder(self, contact_id):
        """Enable automated payment reminders for a contact.

        Args:
            contact_id(str): Contact id of the contact.

        Returns:
            str: Success message('All reminders associated with this contact 
                have been enabled').

        Raises:
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id + '/paymentreminder/enable'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response)
 
    def disable_payment_reminder(self, contact_id):
        """Disable automated payment reminders for a contact.

        Args:
            contact_id(str): Contact id of the contact.

        Returns:
            str: Success message('All reminders associated with this contact 
                have been disabled').

        Raises:
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id + '/paymentreminder/disable'
        response = zoho_http_client.post(url, self.details, self.headers,'')
        return parser.get_message(response) 

    def email_statement(self, contact_id, email,start_date=None, end_date=None, 
                        attachments=None):
        """Email statement to the contact. If JSONString is not inputted, mail 
            will be sent with the default mail content.

        Args:
            contact_id(str): Contact id of the contact.
            email(instance): Email.
            start_date(str, optional): Starting date of the statement. 
                Default to None.
            end_date(str, optional): Ending date of the statement. 
                Default to None.
                If starting date and ending date is not given current month's 
                    statement will be sent to the contact.
            attachments(list): List of files to be attached.

        Returns:
            str: Success message('Statement has to been sent to the customer').

        Raises:
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id + '/statements/email'
        data = {}
        data = email.to_json()
        if start_date is not None and end_date is not None:
            data['start_date'] = start_date
            data['end_date'] = end_date
        fields = {
            'JSONString': dumps(data)
                }
        if attachments is None:
            response = zoho_http_client.post(url, self.details, self.headers, fields)
        else:
            file_list = []

            for value in attachments:
                attachment = {
                    'attachments': {
                        'filename': basename(value), 
                        'content': open(value).read()
                        }
                    }
                file_list.append(attachment)
            
            response = zoho_http_client.post(url, self.details, self.headers, fields, None, file_list)
        return parser.get_message(response) 

    def get_statement_mail_content(self, contact_id, start_date, end_date):
        """Get the statement mail content.

        Args:
            start_date(str): Start date for statement.
            end_date(str): End date for statement.

        Returns:
            instance: Email object.

        Raises: 
            Books exception:if status is not '200' or '201'.

        """ 
        url = base_url + contact_id + '/statements/email'
        query_string = {
            'start_date': start_date,
            'end_date': end_date
            }
        response = zoho_http_client.get(url, self.details, self.headers, query_string)
        return parser.get_mail_content(response) 
 
    def email_contact(self, contact_id, email, attachments=None, 
                      send_customer_statement=None):
        """Send email to contact.

        Args:
            contact_id(str): Contact id of the contact.
            email(instance): Email object.
            attachments(list, optional): List of files to be attached. 
                Default to None.
            send_customer_statement(bool, optional): Send customer statement 
                pdf with email. Default to None.

        Returns:
            str: Success message('Email has been sent').

        Raises:
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id + '/email'

        json_object = dumps(email.to_json())
        data = {
            'JSONString': json_object
            }
        if attachments is not None and send_customer_statement is not None:
            file_list = []

            for value in attachments:
                attachment = {
                    'attachments': {
                        'filename': basename(value), 
                        'content': open(value).read()
                        }
                    }
                file_list.append(attachment)

            parameter = {
                'send_customer_statement': send_customer_statement
                }
            response = zoho_http_client.post(url, self.details, self.headers, data, parameter, file_list)

        elif attachments is not None:
            file_list = []

            for value in attachments:
                attachment = {
                    'attachments': {
                        'filename': basename(value), 
                        'content': open(value).read()
                        }
                    }
                file_list.append(attachment)

            response = zoho_http_client.post(url, self.details, self.headers, data, None, file_list)

        elif send_customer_statement is not None:
            parameter = { 
                'send_customer_statement': send_customer_statement
                }
            response = zoho_http_client.post(url, self.details, self.headers, data, parameter)

        else:
            response = zoho_http_client.post(url, self.details, self.headers, data)

        return parser.get_message(response)

    def list_comments(self, contact_id):
        """List recent activities of a contact with pagination.

        Args:
            contact_id(str): Contact id of the contact.

        Returns:
            instance: Comments list object.

        Raises:
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id + '/comments'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_comment_list(response) 

    def get_comments(self, contact_id):
        """List recent activities of a contact.

        Args:
            contact_id(str): Contact id of the contact.

        Returns:
            list: List of comments object.

        Raises:
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id + '/comments'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_comment_list(response).get_comments()
     
    def list_refunds(self, contact_id):
        """List the refund history of a contact with pagination.

        Args: 
            contact_id(str): Contact id of the contact.

        Returns:
            instance: Refunds list object.

        Raises:
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id + '/refunds'
        response = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_refund_list(response) 
 
    def get_refunds(self, contact_id): 
        """List the refund history of a contact.

        Args: 
            contact_id(str): Contact id of the contact.

        Returns:
            list: List of refunds object.

        Raises:
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id + '/refunds'
        response = zoho_http_client.get(url, self.details)
        return parser.get_refund_list(response).get_creditnote_refunds() 
    
    def track_1099(self, contact_id):
        """Track a contact for 1099 reporting.

        Args:
            contact_id(str): Contact id of the contact.

        Returns:
            str: Success message('1099 tracking is enabled').

        Raises: 
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id + '/track1099'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response)   

    def untrack_1099(self, contact_id):
        """Track a contact for 1099 reporting.

        Args:
            contact_id(str): Contact id of the contact.

        Returns:
            str: Success message('1099 tracking is enabled').

        Raises: 
            Books exception: If status is not '200' or '201'.

        """
        url = base_url + contact_id + '/untrack1099'
        response = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(response)
