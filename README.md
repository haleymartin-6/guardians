# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

# Project Information
Guardians is an application with the goal to provide deals and discounts to consumers on technology that is out of the mainstream large corporations. Within our design, we have Customers, Discounts, Notifications, and Products, all with the appropriate fields attributed to each one. Each customer has a first name, last name, email(s), phone number, and a promotion score. This promotional score is important because when a customer uses another customer's promo code, their promotion score increases. Each discount has the amount, the added date, the amount of likes (customers can like a discount to save it for later or emphasize the usefulness of it), the referral code, the expiration date, the retailer id, and the brand id. Notifications have a discount id for the discount it is associated with, the text of what the notification is actually saying, the status, and the date and time at which the notification is posted.The products have a name, cost, tutorial (this is for our users who may be less familiar with technology and need some guides on how/when this product could be used), product type (i.e. Computer, Phone, GPS, etc.), and brand id.

# Group Members & Their Contributions
Shoutout to Haley, Shruthi, and Kyle for writing the SQL files. Grace added some things to the python files (discounts.py, customers.py, products.py) and is also writing the readme. Snehit did a lot of brainstorming our project idea and coming up with Guardians as a whole. We used Shruthi's computer for all of the AppSmith files, with Haley and Shruthi focused on the functionality of the AppSmith pages while Grace focused on the UI design.


