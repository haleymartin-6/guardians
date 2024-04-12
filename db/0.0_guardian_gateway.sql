-- Create a new database called blogs
CREATE DATABASE IF NOT EXISTS gateway;

-- Show databases
SHOW DATABASES;

USE gateway;


Create TABLE IF NOT EXISTS customers  (
    customerID int PRIMARY KEY AUTO_INCREMENT,
    firstName varchar(50) NOT NULL,
    lastName varchar(50) NOT NULL,
    email1 varchar(75) UNIQUE,
    email2 varchar(75) UNIQUE,
    number varchar(50) NOT NULL,
    promotionScore int
);


Create TABLE IF NOT EXISTS retailer  (
    retailerID int PRIMARY KEY AUTO_INCREMENT,
    name varchar(50) NOT NULL
);


Create TABLE IF NOT EXISTS brand  (
    brandID int PRIMARY KEY AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    summary text
);


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


Create TABLE IF NOT EXISTS discountsLiked  (
    customerID int,
    discountLiked int,
    PRIMARY KEY (customerID, discountLiked),
    FOREIGN KEY (customerID)
         REFERENCES customers(customerID)
       ON UPDATE cascade ON DELETE restrict

);


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


