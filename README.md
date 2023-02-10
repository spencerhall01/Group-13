# Group-13
CSE 4214 Introduction to Software Engineering

Project:
E-Commerce Website

Description:
This is a project for Dr. Charan Gudla's Introduction to Software Engineering class (CSE 4214-501) at Mississippi State University (CSE 4214)

Objective:
The objective of this project is to design and develope an e-commerce  platform that will have a number of functionalities 
based on the customer (TA) expectations


Features:


Team Members:

Spencer Hall (jsh278)
spencerhall01 (spencerhall01@gmail.com)
Group leader and contributer

George Anim (gba37@msstate.edu)
Role: Contributor 

Kyana Conway
KyanaConway
Role: contributing to e-commerce platform project
Languages: Python, SQL, Databases


Features of E-commerce platform
3.	System Features
3.1	System Feature 1 – Login based on role
3.1.1	Description and Priority
At the login page, new users will have the option to sign up for an account based on role. The roles available are Buyer, Seller and Admin. After a user creates an account based on role, they will be able to sign in the next time they visit the application using the credentials they created. This feature is a high priority for this application.
3.1.2	Stimulus/Response Sequences
	Stimulus		Response
	New user clicks sign up		Application opens a page that new user inputs information to sign up based on role
	Returning user click logon		Application allows user to input logon credentials and grants them access after authentication
	User clicks logout		Application must close page and end user session
	
3.1.3	Functional Requirements
REQ-1: Application should display logon page where a new user can create an account, or a returning user can login using registered credentials.	
REQ-2: Application should end user session when the user clicks logout.
	
3.2	System Feature 2 – Buyer Activities
3.2.1	Description and Priority
At the buyer page, the buyer should be able to search for items, compare, buy and return items.
3.2.2	Stimulus/Response Sequences
	Stimulus		Response
	Buyer should be able to search for items based on some requirement.		Application should display items based on specified requirements by buyer
	Buyer should be able to compare items based on some requirement.		Application should display compared items based on specified requirements by buyer
	Buyer should be able to buy items		Application should process buy request of buyer
	Buyer should be able to return items		Application should process buy request of buyer
	
3.2.3	Functional Requirements
REQ-1: Application should display items based on specified requirements by buye	
REQ-2: Application should display compared items based on specified requirements by buyer
REQ-3: Application should process buy request of buyer
REQ-4: Application should process buy request of buyer

3.3	System Feature 3 – Seller Activities
3.3.1	Description and Priority
At the seller page, the seller should be able to add, sell and receive payments for items sold.
3.3.2	Stimulus/Response Sequences
	Stimulus		Response
	Seller should be able to list items		Application should display items listed by seller for sale
	Seller should be able to add items to listed items for sale		Application should allow seller add items to already listed items for sale
	Seller should be able to receive payments for items sold		Application should charge buyers for items bought and credit seller account with money received.
	
3.3.3	Functional Requirements
REQ-1: Application should display items listed by seller for sale
REQ-2: Application should allow seller add items to already listed items for sale
REQ-3: Application should charge buyers for items bought and credit seller account with money received.

3.4	System Feature 3 – Admin Activities
3.4.1	Description and Priority
The admin should be able to approve/block new user accounts and products and oversee different user actions.
3.4.2	Stimulus/Response Sequences
	Stimulus		Response
	Admin should approve/block new user accounts and products		Application should display a page and provide admin ability to approve/block new user accounts and products
	
3.4.3	Functional Requirements
REQ-1: Application should display a page and provide admin ability to approve/block new user accounts and products 

