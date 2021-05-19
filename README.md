Project for akvelon internship

TASK №1
Description

Imagine you are to implement a tool for managing personal finances for money planning. You would need to build a REST API for storing user and transactions information. 
The user entity represents an agent who is adding transactions and contains following fields:
●id
●first name
●last name
●email

The second entity is a transaction - either income or withdrawal. Each transaction needs to have a reference to some user. The Transaction entity contains:
●id
●user_id
●amount - the sum of a transaction
●date

Functional requirements:
●Ability to create / view / edit / delete information about user
●Ability to create / view / edit / delete transactions information
●Ability to view all customer’s payments
●Ability to view sum of income/outcome grouped by dates (say, an array of {“date”: “2021-05-11”, “sum”: 2543.50} jsons, so that as a user I know how much I’ve spent/received each day). Will be a plus if you also add start date and end date filter to it.
●To view customers, and payments you need to provide various filtering methods (by payment date, type of transaction (either income or outcome, based on the sign of amount)) and sorting (by date, by amount)


TASK №2
Description
Implement a function which will return n’th number of Fibonacci sequence. The function would be called as:
fibonacci(0) = 0
fibonacci(7) = 13
	
Functional requirements:
In the same project which contains your solution for Task #1 create utils.py file in a convenient place (or just use existing if you already have it). Define fibonacci function in this utils file and show examples of usage.

Technology Requirements
Tasks should be completed:
●On Django or Flask Web framework (or other, like Tornado)
●With any DBMS (PostgreSQL, MySQL)
●With Swagger (https://swagger.io)
●Uploaded to the GitHub
●Using English to write comments and descriptions of classes, fields, etc
