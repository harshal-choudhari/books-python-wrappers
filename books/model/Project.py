#$Id$

class Project: 
    """This class is used to create object for Projects."""
    def __init__(self): 
        """Initialize the parameters for projects object."""
        self.project_id = ''
        self.project_name = ''
        self.customer_id = ''
        self.customer_name = ''
        self.currency_code = '' 
        self.description = ''
        self.status = ''
        self.billing_type = ''
        self.rate = 0.0
        self.budget_type = ''
        self.budget_hours = 0
        self.budget_amount = 0.0
        self.total_hours = ''
        self.billed_hours = ''
        self.un_billed_hours = ''
        self.created_time = ''
        self.tasks = []
        self.users = []

    def set_project_id(self, project_id):
        """Set project_id.

        Args:
            project_id(str): Project id.

        """
        self.project_id = project_id

    def get_project_id(self):
        """Get project id.

        Returns:
            str: Project id.
 
        """
        return self.project_id

    def set_project_name(self, project_name):
        """Set project name.

        Args:
            project_name(str): Project name.

        """
        self.project_name = project_name

    def get_project_name(self):
        """Get project name.

        Returns: 
            str: Project name.

        """
        return self.project_name

    def set_customer_id(self, customer_id):
        """Set customer id.

        Args:
            customer_id(str): Customer id.

        """
        self.customer_id = customer_id

    def get_customer_id(self):
        """Get customer id.

        Returns:
            str: Customer id.

        """
        return self.customer_id

    def set_customer_name(self, customer_name):
        """Set customer name.

        Args:
            customer_name(str): Customer name.
 
        """
        self.customer_name = customer_name

    def get_customer_name(self):
        """Get customer name.

        Returns:
            str: Customer name.

        """
        return self.customer_name

    def set_currency_code(self, currency_code):
        """Set currency code.

        Args:
            currency_code(str): Currency code.

        """
        self.currency_code = currency_code

    def get_currency_code(self): 
        """Get currency_code.

        Returns: 
            str: Currency code.

        """
        return self.currency_code

    def set_description(self, description):
        """Set description.

        Args:
            description(str): Description.

        """ 
        self.description = description

    def get_description(self):
        """Get description.

        Returns:
            str: Description.

        """
        return self.description

    def set_status(self, status):
        """Set status.

        Args:
            status(str): Status.

        """
        self.status = status

    def get_status(self):
        """Get status.

        Returns:
            str: Status.

        """
        return self.status

    def set_billing_type(self, billing_type):
        """Set billing type.

        Args:
            billing_type(str): Billing type.

        """
        self.billing_type = billing_type

    def get_billing_type(self):
        """Get billing type.

        Returns:
            str: Billing type.

        """
        return self.billing_type

    def set_budget_type(self, budget_type):
        """Set budget type.

        Args:
            budget_type(str): Budget type.

        """
        self.budget_type = budget_type

    def get_budget_type(self):
        """Get budget type.

        Returns:
            str: Budget type.

        """
        return self.budget_type

    def set_total_hours(self, total_hours):
        """Set total hours.

        Args:
            total_hours(str): Total hours.

        """
        self.total_hours = total_hours

    def get_total_hours(self):
        """Get total hours.

        Returns:
            str: Total hours.

        """
        return self.total_hours

    def set_billed_hours(self, billed_hours):
        """Set billed hours.

        Args:
            billed_hours(str): Billed hours.

        """
        self.billed_hours = billed_hours

    def get_billed_hours(self):
        """Get billed hours.

        Returns:
            str: Billed hours.

        """
        return self.billed_hours

    def set_un_billed_hours(self, un_billed_hours): 
        """Set unbilled hours.

        Args:
            un_billed_hours(str): Unbilled hours.

        """
        self.un_billed_hours = un_billed_hours

    def get_un_billed_hours(self):
        """Get unbilled hours.

        Returns:
            str: Unbilled hours.

        """
        return self.un_billed_hours

    def set_created_time(self, created_time):
        """Set created time.

        Args:
            created_time(str): Created time.

        """
        self.created_time = created_time

    def get_created_time(self):
        """Get created time.

        Returns:
            str: Created time.

        """
        return self.created_time

    def set_tasks(self, task):
        """Set task.

        Args:
            task(instance): Task object.

        """
        self.tasks.append(task)

    def get_tasks(self):
        """Get tasks.

        Returns:
            list of instance: List of task object.

        """
        return self.tasks

    def set_users(self, user):
        """Set User.

        Args:
            user(instance): User object.

        """
        self.users.append(user)

    def get_users(self):
        """Get user.

        Returns:
            list of object: User object.

        """
        return self.users

    def set_rate(self, rate):
        """Set rate.

        Args:
            rate(float): Rate.

        """
        self.rate = rate

    def get_rate(self):
        """Get rate.

        Returns:
            float: Rate.

        """
        return self.rate

    def set_budget_hours(self, budget_hours):
        """Set budget hours.

        Args:
            budget_hours(str): Budget hours.

        """
        self.budget_hours = budget_hours

    def get_budget_hours(self):
        """Get budget hours.

        Returns:
            str: Budget hours.

        """
        return self.budget_hours

    def set_budget_amount(self, budget_amount):
        """Set budget amount.

        Args:
            budget_amount(float): Budget amount.

        """
        self.budget_amount = budget_amount

    def get_budget_amount(self):
        """Get budget amount.

        Returns:
            float: Budget amount.

        """
        return self.budget_amount

    def to_json(self):
        """This method is used to convert projects object to json format.

        Returns:
            dict: Dictionary containing json for projects.

        """
        data = {}
        if self.project_name != '':
            data['project_name'] = self.project_name
        if self.customer_id != '':
            data['customer_id'] = self.customer_id
        if self.description != '':
            data['description'] = self.description
        if self.billing_type != '':
            data['billing_type'] = self.billing_type
        if self.rate > 0:
            data['rate'] = self.rate
        if self.budget_type != '':
            data['budget_type'] = self.budget_type
        if self.budget_hours != '':
            data['budget_hours'] = self.budget_hours
        if self.budget_amount > 0:
            data['budget_amount'] = self.budget_amount
        if self.users:
            data['users'] = []
            for value in self.users:
                user = value.to_json()
                data['users'].append(user)
        if self.tasks:
            data['tasks'] = []
            for value in self.tasks:
                task = value.to_json()
                data['tasks'].append(task)
        return data
