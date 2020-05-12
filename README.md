## **ZohoBooks Python Client Library With Oauth2.0 Support**
The Python library for integrating with the Zoho Books API.
This library is forked from [books-python-wrapper](https://github.com/zoho/books-python-wrappers).

Tests are not converted to python3 yet.

## Installation
---------------
Setup file is included in code. It can be installed in your project.
        python3 setup.py install
        

## Documentation
----------------
[API Reference](https://www.zoho.com/books/api/v3/index.html)

## Usage
--------
In order to access the Zoho Books APIs, users need to have a valid Zoho account and a valid Auth Token.
 
### **Sign up for a Zoho Account:**

- - - 

For setting up a Zoho account, access the Zoho Books [Sign Up](https://www.zoho.com/books/signup) page and enter the requisite details - email address and password.
 
### **Generate Access and Refresh Tokens:**

- - -
 
To generate the Tokens, you need to send an authentication request to Zoho Accounts in a prescribed URL format. [Refer here](https://www.zoho.com/books/api/v3/index.html)


## Python Wrappers - Sample


### How to access Zoho Books APIs through Python wrapper classes?
------------------------------------------------------------------ 

Below is a sample code for accessing the Books APIs through Python wrapper classes. Please import these classes:

        from books.model.Organization import Organization
        from books.model.Address import Address
        from books.api.OrganizationsApi import OrganizationsApi
        from books.service.ZohoBooks import ZohoBooks
		
Once you're done with importing the requisite classes, you'll have to proceed to create an instance of OrganisationsAPI.

### **Create OrganisationsAPI instance:**

- - -

Now there are two ways of creating an instance of OrganisationsAPI.

 - Pass the AuthToken and create a OrganisationsAPIinstance. 

Sample code:

        organizations_api = OrganizationsApi({"access_token"}, {"organization_id"})
			
 - Pass the AuthToken and organisations id to first create an instance of ZohoBooks, and then proceed to get the instance of Organisations API. 

Sample code:
     
        zoho_books = ZohoBooks({"access_token"}, {"organization_id"})

        organizations_api = zoho_books.get_organizations_api()
			
			
### **Get the list of organizations:**

- - -
			
If you wish to get the list of all your Zoho Books organizations, you need to call the `get_organizations()` method in the format below:

        print organizations_api.get_organizations()
        
It returns the list of organizations object as a response.

### **Get details of an organization:**

- - - 

In order to get the details of a organization, you need to call the `get()` method by passing organization_id as a parameter.
    
        print organizations_api.get({"organization_id"})

### **Create a new organization:**

- - - 

Make use of the sample code below to create a new organization:
        
        organization = Organization()
        organization.set_name("ZOHO")

        address = Address()
        address.set_street_address1("9390 Research Blvd")
        address.set_street_address2("Bldg II, Suite 440")
        address.set_city("Austin")
        address.set_state("Texas")
        address.set_country("U.S.A")
        address.set_zip("78759")
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

### **Update an existing organization:**

- - - 

Proceed to update the details of an existing organization with the help of the sample code below:
 
        organization = Organization()
        organization.set_name("ZOHO")

        address = Address()
        address.set_street_address1("9390 Research Blvd")
        address.set_street_address2("Bldg II, Suite 440")
        address.set_city("Austin")
        address.set_state("Texas")
        address.set_country("U.S.A")
        address.set_zip("78759")

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

### **Get the parameters of an organization:**

- - - 

To fetch organization parameters like address, currency code etc. use the sample code below:

        organization = organizations_api.get({"organization_id"})
        currency_code = organization.get_currency_code()
        organization_address = organization.get_address()
        organization_name = organization.get_name()

### **Catch Exceptions:**

- - -

If there is any error encountered while calling the Python Wrappers of Zoho Books API, the respective class will throw the BooksException. Use the below mentioned code to catch the BooksException:

        try:
        
            organization = organizations_api.get({"organization_id"})
            
        except BooksException as b_e:
        
            print "Error Code:" + b_e.get_code() + "\nError Message:" + b_e.get_message()

For a full set of examples, click [here](../../tree/master/test).
      

