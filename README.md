This is my first project with python and tkinter library.
Every bar needs a management system to work correctly and legally. The Bar Management System (BMS) provides ability for Employees (Bartenders and Waiters) to update the customer orders, for Hall Managers to control Bartenders and Waiters working process, and for Managers to update products in system and to manage the entire working process. The system will be developed as a MVC using Tkinter as front-end, and JSON file persistence technologies.

The main user roles (actors) are:
•	Employee – every employee of the bar can create an work account. Employees can open new order, can see all already opened orders and can update them without removing products from them, and also can close orders and issues a cash receipt.
•	Hall Manager – to get account from this type you must create a work account and Manager must change your role to a “Hall Manager”. As a Hall Manager you have all Employee rights, but you can also make revision of products, see cash receipts history and have full permissions to update customer orders (you can remove products from order if product is added by mistake or something else).
•	Manager – system allow with a specific admin password to create a manager account. Manager can do anything that Employees and Hall Managager can, they also have permissions to add products in the system, change products attributes (ingredients, quantity, price and etc.), and to manage accounts.

The project is not fully completed :) !
