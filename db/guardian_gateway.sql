-- Create a new database called blogs
CREATE DATABASE IF NOT EXISTS gateway;

-- Show databases
SHOW DATABASES;

USE gateway;

DROP TABLE IF EXISTS customers;
Create TABLE IF NOT EXISTS customers  (
    customerID int PRIMARY KEY AUTO_INCREMENT,
    firstName varchar(50) NOT NULL,
    lastName varchar(50) NOT NULL,
    email1 varchar(75) UNIQUE,
    email2 varchar(75) UNIQUE,
    number varchar(50) NOT NULL,
    promotionScore int
);

DROP TABLE IF EXISTS retailer;
Create TABLE IF NOT EXISTS retailer  (
    retailerID int PRIMARY KEY AUTO_INCREMENT,
    name varchar(50) NOT NULL
);

DROP TABLE IF EXISTS brand;
Create TABLE IF NOT EXISTS brand  (
    brandID int PRIMARY KEY AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    summary text
);

DROP TABLE IF EXISTS discounts;
Create TABLE IF NOT EXISTS discounts  (
    discountID int PRIMARY KEY AUTO_INCREMENT,
    amount float,
    addedDate datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
    likes bool,
    referralCode varchar(75) UNIQUE,
    expirationDate datetime,
    retailerID int,
    brandID int,
    FOREIGN KEY (retailerId)
       REFERENCES retailer(retailerID)
       ON UPDATE restrict ON DELETE restrict,
    FOREIGN KEY (brandID)
       REFERENCES brand(brandID)
       ON UPDATE restrict ON DELETE restrict
);

DROP TABLE IF EXISTS customerDiscounts;
Create TABLE IF NOT EXISTS customerDiscounts  (
    customerID int,
    discountID int,
    PRIMARY KEY (customerID, discountID),
    FOREIGN KEY (customerID)
         REFERENCES customers(customerID)
       ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (discountID)
         REFERENCES discounts(discountID)
       ON UPDATE cascade ON DELETE cascade
);

DROP TABLE IF EXISTS discountsLiked;
Create TABLE IF NOT EXISTS discountsLiked  (
    customerID int,
    discountLiked int,
    PRIMARY KEY (customerID, discountLiked),
    FOREIGN KEY (customerID)
         REFERENCES customers(customerID)
       ON UPDATE cascade ON DELETE restrict

);

DROP TABLE IF EXISTS notifications;
Create TABLE IF NOT EXISTS notifications  (
    notificationID int AUTO_INCREMENT,
    discountID int,
    text text,
    status bool,
    dateTime datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY(notificationID, discountID),
    FOREIGN KEY (discountID)
         REFERENCES discounts(discountID)
       ON UPDATE cascade ON DELETE restrict

);

DROP TABLE IF EXISTS products;
Create TABLE IF NOT EXISTS products (
    productID int AUTO_INCREMENT,
    brandID int,
    name varchar(128) NOT NULL,
    cost float NOT NULL,
    tutorial text,
    productType varchar(50),
    PRIMARY KEY (productID, brandID),
    FOREIGN KEY (brandID)
         REFERENCES brand(brandID)
       ON UPDATE cascade ON DELETE restrict,
    INDEX idx_cost (cost)
);


#User Persona 1
SELECT * FROM products WHERE productType = 'technology';
INSERT INTO products(brandID, name, cost, tutorial, productType)
VALUES (1,'TechCrunch', 70, 'Coding help', 'technology');

SELECT * FROM discounts d JOIN brand b ON d.brandID = b.brandID JOIN products p ON p.brandID = b.brandID WHERE p.productType = 'technology';
INSERT INTO discounts(amount, addedDate, likes, referralCode, expirationDate, retailerID, brandID)
VALUES (50.0, '2024-06-30 23:23:12', true, 'techCode10', '2025-06-30 23:23:12', 1, 1);

INSERT INTO notifications (discountID, text, status)
VALUES (1, 'Notification message about promotions if enough members use code', true);

INSERT INTO notifications (discountID, text, status)
VALUES (2, 'Notification message about new, exclusive promotions from emerging tech brands.', true);

SELECT n.* FROM notifications n JOIN discounts d ON n.discountID = d.discountID JOIN brand b ON d.brandID = b.brandID JOIN products p ON p.brandID = b.brandID WHERE p.productType = 'technology';

#User Persona 2
SELECT * FROM products WHERE productType = 'education';
INSERT INTO products(brandID, name, cost, tutorial, productType)
VALUES (2,'Reading Rainbow', 20, 'Learning to read', 'education');

SELECT * FROM products WHERE productType = 'communication_services';
INSERT INTO products(brandID, name, cost, tutorial, productType)
VALUES (3,'Mint Mobile', 30, 'Cheap Mobile Communications', 'communication_services');

SELECT * FROM products WHERE productType = 'technology' OR productType = 'children';
INSERT INTO products(brandID, name, cost, tutorial, productType)
VALUES (4,'Toddler Toys', 10, 'Toys for your toddler at half price', 'children');

SELECT * FROM products WHERE productType = 'skill_development';
INSERT INTO products(brandID, name, cost, tutorial, productType)
VALUES (5,'edX', 50, 'Learning any skill at a professional level', 'skill_development');

INSERT INTO notifications (discountID, text, status)
VALUES (2, 'Notification message about new promotions from emerging household brands.', true);

#User Persona 3
SELECT * FROM discounts WHERE brandID = 5;

INSERT INTO discounts (amount, likes, referralCode, expirationDate, retailerID, brandID)
VALUES (10.0, true, 'emma15', '2024-06-30 23:23:12', 1, 1);

SELECT * FROM discounts WHERE referralCode = 'emma15';
INSERT INTO discounts(amount, addedDate, likes, referralCode, expirationDate, retailerID, brandID)
VALUES (100.0, '2024-07-30 23:23:12', true, 'emma15', '2025-07-30 23:23:12', 2, 1);

INSERT INTO notifications (discountID, text, status)
VALUES (3, 'Notification message about new, exclusive promotions from TechCrunch.', true);

INSERT INTO customers(customerID, firstName, lastName, email1, email2, number, promotionScore)
VALUES (1,'Emma', 'Monroe', 'emmamonroe@gmail.com', '', '(855)643-2852', 32);
SELECT promotionScore FROM customers WHERE customerID = '1';

#User Persona 4
SELECT * FROM products WHERE productType = 'technology';
INSERT INTO products(brandID, name, cost, tutorial, productType)
VALUES (6,'TechTime', 80, 'External coding tool', 'technology');

SELECT * FROM discounts d JOIN brand b ON d.brandID = b.brandID JOIN products p ON p.brandID = b.brandID WHERE p.productType = 'technology' AND d.amount < 50.0;

INSERT INTO notifications (discountID, text, status)
VALUES (4, 'Notification message about promotions if enough members use code', true);

SELECT * FROM products WHERE productType = 'skill_development';
INSERT INTO products(brandID, name, cost, tutorial, productType)
VALUES (7,'Arman Coding Tutorials', 20, 'Learning any skill at a professional level', 'skill_development');

INSERT INTO notifications (discountID, text, status)
VALUES (5, 'Notification message about new promotions from emerging tech brands.', true);





