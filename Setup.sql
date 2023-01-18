-- Create Database food_management;
use food_management;
-- create table food_items (Food_no INT Primary Key, Food_name Varchar(32), Food_price INT);
-- create table customers (Customer_Name VARCHAR(32) , Customer_Mobile_No char(10), Customer_address VARCHAR(64),Primary Key(Customer_Name,Customer_Mobile_No));
-- create table orders (Food_no INT ,Customer_Name VARCHAR(32) , Customer_Mobile_No Varchar(10),Order_time datetime, FOREIGN KEY(Food_no) REFERENCES food_items(Food_no),FOREIGN KEY(Customer_Name,Customer_Mobile_No) REFERENCES customers(Customer_Name,Customer_Mobile_No));
-- insert into food_items values(1,"Rajma Chawal",199)
-- insert into food_items values(2,"Dal Chawal",199)
