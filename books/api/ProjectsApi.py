#$Id$#

from books.util.ZohoHttpClient import ZohoHttpClient
from books.parser.ProjectsParser import ProjectsParser
from books.api.Api import Api
from json import dumps

base_url = Api().base_url + 'projects/'
zoho_http_client = ZohoHttpClient()
parser = ProjectsParser()

class ProjectsApi:
    """This class is used to 
 
    1. List all projects with pagination.
    2.Get details of a project.
    3.Create a new project.
    4.Update an existing project.
    5.Delete an existing project.
    6.Mark a project as active.
    7.Mark a project as inactive.
    8.Clone a project.
    9.Get list of tasks added to a project.
    10.Get details of a task.
    11.Add task to a project.
    12.Update details of a task.
    13.Delete a task added to a project.
    14.Get list of users associated with a project.
    15.Get details of a user in a project.
    16.Assign users to a project.
    17.Invite and add user to the project.
    18.Update details of a user.
    19.Remove user from the project.
    20.List all time entries with pagination.
    21.Get details of a time entry.
    22.Logging time entries.
    23.Update logged time entry.
    24.Deleting logged time entry.
    25.Deleting time entries.
    26.Get current running timer.
    27.Start tracking time spent.
    28.Stop tracking time.
    29.Get comments for a project.
    30.Post comment to a project.
    31.Delete a comment from a project.
    32.List invoices created for this project.

    """

    def __init__(self, authtoken, organization_id):
        """Initialize Projects api using user's authtoken and organization id.

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
        
    def get_projects(self, parameters=None): 
        """List all projects with pagination.

        Args:
            parameters(dict, optional): Filter with which the list has to be 
                displayed.

        Returns:
            instance: Projects list object.

        """
        resp = zoho_http_client.get(base_url, self.details, self.headers, parameters) 
        return parser.get_projects_list(resp)
 
    def get_project(self, project_id):
        """Get details of a project.

        Args:
            project_id(str): Project id.

        Returns:
            instance: Project object.

        """
        url = base_url + project_id
        resp = zoho_http_client.get(url, self.details, self.headers) 
        return parser.get_project(resp) 

    def create_project(self, project):
        """Create a new project.

        Args:
            project(instance): Project object.

        Returns:
            instance: Projects object

        """
        json_object = dumps(project.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(base_url, self.details, self.headers, data) 
        return parser.get_project(resp) 

    def update_project(self, project_id, project):
        """Update an existing project.

        Args:
            project_id(str): Project id.
            project(instance): Project object.

        Returns: 
            instance: Project object.

        """
        url = base_url + project_id
        json_object = dumps(project.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data) 
        return parser.get_project(resp) 

    def delete_project(self, project_id):
        """Delete an existing project.

        Args:
            project_id(str): Project id.

        Returns:
            str: Success message('The project has been deleted.').

        """
        url = base_url + project_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def activate_project(self, project_id):
        """Mark project as active.

        Args:
            project_id(str): Project id.

        Returns: 
            str: Success message('The selected project have been marked as 
                active.').

        """
        url = base_url + project_id + '/active'
        resp = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(resp) 

    def inactivate_project(self, project_id):
        """Mark project as inactive.

        Args:
            project_id(str): Project id.

        Returns:
            str: Success message('The selected project have been marked as 
                inactive.').

        """
        url = base_url + project_id + '/inactive'
        resp = zoho_http_client.post(url, self.details, self.headers, '')
        return parser.get_message(resp) 

    def clone_project(self, project_id, project):
        """Cloning a project.

        Args:
            project_id(str): Project id.

        Returns:
            instance: Project object.

        """
        url = base_url + project_id +  '/clone'
        json_object = dumps(project.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_project(resp) 

    def get_tasks(self, project_id, sort_column=None):
        """Get list of tasks added to a project.

        Args:
            project_id(str): Project id.
            sort_column(str): Sort column. Allowed Values: task_name, 
                billed_hours, log_time and un_billed_hours.

        Returns: 
            instance: Task list object.

        """  
        url = base_url + project_id + '/tasks'
        if sort_column is not None:
            parameter = {
                'sort_column': sort_column
                }       
        else:
            parameter = None
        resp = zoho_http_client.get(url, self.details, self.headers, parameter)
        return parser.get_tasks_list(resp) 

    def get_task(self, project_id, task_id):
        """Get details of a task.

        Args: 
            project_id(str): Project id.
            task_id(str): Task id.

        Returns:
            instance: Task object.

        """
        url = base_url + project_id + '/tasks/' + task_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_task(resp) 
     
    def add_task(self, project_id, task):
        """Add task to project.

        Args:
            project_id(str): Project id.
            task(instance): Task object.

        Returns:
            instance: Task object.

        """
        url = base_url + project_id + '/tasks'
        json_object = dumps(task.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_task(resp) 

    def update_task(self, project_id, task_id, task):
        """Update details of a task.

        Args: 
            project_id(str): Project id.
            task_id(str): Task id.

        Returns:
            instance: Task object.

        """
        url = base_url + project_id + '/tasks/' + task_id
        json_object = dumps(task.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_task(resp) 

    def delete_task(self, project_id, task_id):
        """Delete task added to a project.

        Args:
            project_id(str): Project id.
            task_id(str): Task id.

        Returns:
            str: Success message('The task has been deleted.').

        """
        url = base_url + project_id + '/tasks/' + task_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def get_users(self, project_id):
        """Get list of users associated with a project.

        Args:
            project_id(str): Project id.

        Returns:
            instance: Users list object.

        """
        url = base_url + project_id + '/users'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_users(resp) 

    def get_user(self, project_id, user_id):
        """Get details of a user in a project.

        Args:
            project_id(str): Project id.
            user_id(str): User id.

        Returns:
            instance: USer object.

        Raises:
            Books Exception: If status is not '200' or '201'.

        """
        url = base_url + project_id + '/users/' + user_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_user(resp) 

    def assign_users(self, project_id, users):
        """Assign users to a project.
 
        Args:
            project_id(str): Project id.
            users(list of instance): List of users object.

        Returns:
            instance: Users list object.

        """
        url = base_url + project_id + '/users'
        users_obj = {
            'users': [] 
            }
        for value in users:
            user = value.to_json()
            users_obj['users'].append(user)
        json_object = dumps(users_obj)
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_users(resp) 

    def invite_user(self, project_id, user):
        """Invite and add user to the project.

        Args:
            project_id(str): Project id.
            user(instance): User object.

        Returns:
            instance: User object.

        """
        url = base_url + project_id + '/users/invite'
        json_object = dumps(user.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_user(resp) 
 
    def update_user(self, project_id, user_id, user):
        """Update details of a user.

        Args:
            project_id(str): Project id.
            user_id(str): User id.
            user(instance): User object.

        Returns:
            instance: User object.

        """
        url = base_url + project_id + '/users/' +user_id
        json_object = dumps(user.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_user(resp)  

    def delete_user(self, project_id, user_id):
        """Remove user from the project.

        Args:
            project_id(str): Project id.
            user_id(str): User id.

        Returns:
            str: Success message('The staff has been removed.').

        """
        url = base_url + project_id + '/users/' + user_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def get_time_entries(self, parameters=None):
        """List all time entries with pagination.

        Args:
            parameters(dict, optional): Filter with which the list has to be 
                displayed.

        Returns:
            instance: Time entries list object.

        """
        url = base_url + 'timeentries'
        resp = zoho_http_client.get(url, self.details, self.headers, parameters) 
        return parser.get_time_entries_list(resp) 

    def get_time_entry(self, time_entry_id):
        """Get details of time entry.

        Args:
            time_entry_id(str): Time entry id.

        Returns:
            instance: Time entry object.

        """
        url = base_url + 'timeentries/' + time_entry_id
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_time_entry(resp) 

    def log_time_entries(self, time_entry):
        """Logging time entries.

        Args:
            time_entry(instance): Time entry object.

        Returns:
            instance: Time entry.

        """
        url = base_url + 'timeentries'
        json_object = dumps(time_entry.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_time_entry(resp) 

    def update_time_entry(self, time_entry_id, time_entry):
        """Update logged time entry.

        Args:
            time_entry_id(str): Time entry id.
            time_entry(instance): Time entry object.

        Returns:
            instance: Time entry object.

        """
        url = base_url + 'timeentries/' + time_entry_id
        json_object = dumps(time_entry.to_json())
        data = {
            'JSONString': json_object
            }
        resp = zoho_http_client.put(url, self.details, self.headers, data)
        return parser.get_time_entry(resp) 

    def delete_time_entry(self, time_entry_id):
        """Delete time entry.

        Args:
            time_entry_id(str): Time entry id.

        Returns:
            str: Success message('The time entry has been deleted.').

        """
        url = base_url + 'timeentries/' + time_entry_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def delete_time_entries(self, time_entry_ids):
        """Delete time entries.

        Args:
            time_entry_ids(str): Id of the time entries to be deleted.

        Returns:
            str: Success message('The selected timesheet entries have been 
                deleted.').

        """
        url = base_url + 'timeentries'
        param = {
            'time_entry_ids': time_entry_ids
            }
        resp = zoho_http_client.delete(url, self.details, self.headers, param) 
        return parser.get_message(resp) 

    def get_timer(self):
        """Get current running timer.

        Returns: 
            instance: Time entry object.

        Raises:
            Books Exception: If status is not '200' or '201'.

        """
        url = base_url + 'timeentries/runningtimer/me'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_time_entry(resp) 
 
    def start_timer(self, timer_entry_id):
        """Start tracking time spent.

        Args: 
            timer_entry_id(str): Timer entry id.

        Returns: 
            instance: Time entry object.

        """
        url = base_url + 'timeentries/' + timer_entry_id + '/timer/start'
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_time_entry(resp)

    def stop_timer(self): 
        """Stop tracking time.

        Returns:
            instance: Time entry object.

        """
        url = base_url + 'timeentries/timer/stop'
        data = {
            'JSONString': ''
            }
        resp = zoho_http_client.post(url, self.details, self.headers, data)
        return parser.get_time_entry(resp)

    def get_comments(self, project_id):
        """Get list of comments for a project.

        Args:
            project_id(str): Project id.
         
        Returns:
            instance: Comments list object.

        """
        url = base_url + project_id + '/comments'
        resp = zoho_http_client.get(url, self.details, self.headers)
        return parser.get_comments(resp) 

    def post_comment(self, project_id, comment):
        """Post comment to a project.

        Args:
            project_id(str): Project id.
            comment(instance): Comment object.

        Returns:
            instance: Comment object.

        """
        url = base_url + project_id + '/comments'
        data = { 
            'description': comment.get_description()
            }
        json_string = {
            'JSONString': dumps(data)
            }
        resp = zoho_http_client.post(url, self.details, self.headers, json_string)
        return parser.get_comment(resp) 
     
    def delete_comment(self, project_id, comment_id):
        """Delete an existing comment.

        Args:
            project_id(str): Project id.
            comment_id(str): comment id. 

        Returns: 
            str: Success message('The comment has been deleted.').
 
        """
        url = base_url + project_id + '/comments/' + comment_id
        resp = zoho_http_client.delete(url, self.details, self.headers)
        return parser.get_message(resp) 

    def get_invoices(self, project_id, sort_column=None):
        """List invoices created for this project.
  
        Args:
            project_id(str): Project id.

        Returns:
            instance: Invoices list object.

        """
        url = base_url + project_id + '/invoices'
        if sort_column is not None:
            param = {
                'sort_column': sort_column
                } 
        else:
            param = None
        resp = zoho_http_client.get(url, self.details, self.headers, param)
        return parser.get_invoice_list(resp) 
        
            
          
  
           
