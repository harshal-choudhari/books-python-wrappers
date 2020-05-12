#$Id$#

from books.model.Project import Project
from books.model.User import User
from books.model.Task import Task
from books.model.TimeEntry import TimeEntry
from books.model.Comment import Comment
from books.service.ZohoBooks import ZohoBooks

import os
access_token = os.environ.get('ACCESS_TOKEN')
organization_id = os.environ.get('ORGANIZATION_ID')
zoho_books = ZohoBooks(access_token, organization_id)

projects_api = zoho_books.get_projects_api()

project_id = projects_api.get_projects().get_projects()[0].get_project_id()

contact_api = zoho_books.get_contacts_api()
customer_id = contact_api.get_contacts().get_contacts()[0].get_contact_id()
task_id = projects_api.get_tasks(project_id).get_tasks()[0].get_task_id()
user_id = projects_api.get_users(project_id).get_users()[0].get_user_id()
time_entry_id = projects_api.get_time_entries().get_time_entries()[0].get_time_entry_id()

#Projects

#List Projects

param = {'filter_by': 'Status.All'}
print projects_api.get_projects(param)
print projects_api.get_projects()

# Get project

print projects_api.get_project(project_id)

#Create project

project = Project()
project.set_project_name('pro 14')
project.set_customer_id(customer_id)
project.set_description("")
project.set_billing_type('based_on_staff_hours')
project.set_rate(0.0)
project.set_budget_type("total_project_cost")
project.set_budget_hours(0)
project.set_budget_amount(10.0)
users = []
user = User()
user.set_user_id(user_id)
user.set_rate(10.0)
user.set_budget_hours(1)
users.append(user)
project.set_users(users)
tasks = []
task = Task()
task.set_task_name('task 1')
task.set_description('')
task.set_rate(10.0)
task.set_budget_hours(1)
tasks.append(task)
project.set_tasks(task)

print projects_api.create_project(project)

# Update a project

project = Project()
project.set_project_name('pro 15')
project.set_customer_id(customer_id)
project.set_description("")
project.set_billing_type('based_on_staff_hours')
project.set_rate(0.0)
project.set_budget_type("total_project_cost")
project.set_budget_hours(0)
project.set_budget_amount(10.0)
users = []
user = User()
user.set_user_id(user_id)
user.set_rate(10.0)
user.set_budget_hours(1)
users.append(user)
project.set_users(users)
tasks = []
task = Task()
task.set_task_name('task 1')
task.set_description('')
task.set_rate(10.0)
task.set_budget_hours(1)
tasks.append(task)
project.set_tasks(task)

print projects_api.update_project(project_id, project)

#Delete project
project_id = "71127000000207015"
print projects_api.delete_project(project_id)

#Activate project

print projects_api.activate_project(project_id)

# Inactivate project

print projects_api.inactivate_project(project_id)

#Clone project

project = Project()
project.set_project_name('pro 16')
project.set_description("cloned project")

print projects_api.clone_project(project_id, project)
'''
# TASKS
'''
#List tasks
sort_column = 'task_name'
print projects_api.get_tasks(project_id,sort_column)
print projects_api.get_tasks(project_id)

#Get task

print projects_api.get_task(project_id, task_id)

#Add task

task = Task()
task.set_task_name('task 6')
task.set_description('sub Task')
task.set_rate(0)
task.set_budget_hours(0)

print projects_api.add_task(project_id, task)

#Update task

task = Task()
task.set_task_name('task 6')
task.set_description('sub Task')
task.set_rate(0)
task.set_budget_hours(0)

print projects_api.update_task(project_id, task_id,task)

#Delete task
task_id = "71127000000210001"
print projects_api.delete_task(project_id, task_id)

'''
#Users

# List users 
'''
print projects_api.get_users(project_id)

# Get user

print projects_api.get_user(project_id,user_id)

#Assign user

user = User()
user.set_user_id(user_id)
user.set_rate(0)
user.set_budget_hours(0)
users = []
users.append(user)
print projects_api.assign_users(project_id,users)

# Invite user
user = User()
user.set_user_name('johny')
user.set_email('example@gmail.com')
user.set_user_role('staff')
user.set_rate(0)
user.set_budget_hours(0)

print projects_api.invite_user(project_id,user)

#Update user
project_id = "71127000000179001"
user_id = "71127000000179007"
user = User()
user.set_user_name('user 1')
user.set_user_role('staff')
user.set_rate(0.0)
user.set_budget_hours(0)
print projects_api.update_user(project_id, user_id,user)

#Delete user
print projects_api.delete_user(project_id,user_id)

'''
## Time entry

# List time entry
'''
print projects_api.get_time_entries()
param = {'filter_by': 'Date.All'}
print projects_api.get_time_entries(param)

#Get a time entry

print projects_api.get_time_entry(time_entry_id)

#Log time entries

time_entry = TimeEntry()
time_entry.set_project_id(project_id)
time_entry.set_task_id(task_id)
time_entry.set_user_id(user_id)
time_entry.set_log_date('2014-05-21')
time_entry.set_begin_time("10:00")
time_entry.set_end_time("10:01")
time_entry.set_log_time("10:00")
time_entry.set_start_timer(True)

print projects_api.log_time_entries(time_entry)

#Update time entry

time_entry = TimeEntry()
time_entry.set_project_id(project_id)
time_entry.set_task_id(task_id)
time_entry.set_user_id(user_id)
time_entry.set_log_date('2014-05-12')
time_entry.set_begin_time("10:00")
time_entry.set_end_time("10:01")
time_entry.set_log_time("10:00")
time_entry.set_start_timer(False)

print projects_api.update_time_entry(time_entry_id, time_entry)

#Delete time entry

print projects_api.delete_time_entry(time_entry_id)

#Delete time entries

time_entry_ids = time_entry_id
print projects_api.delete_time_entries(time_entry_ids)

#get timer

print projects_api.get_timer()

#start timer

print projects_api.start_timer(time_entry_id)

#Stop timer

print projects_api.stop_timer()
'''
#List comments

print projects_api.get_comments(project_id)
'''
#Post comments

comment = Comment()
comment.set_description("Based on hours")
print projects_api.post_comment(project_id, comment)

#Delete comments
comment_id = projects_api.get_comments(project_id).get_comments()[0].get_comment_id()

print projects_api.delete_comment(project_id,comment_id)

# List Invoices

print projects_api.get_invoices(project_id)

