-- Consider a simple database with one tables: BankAccount 
create database Bank; 
use Bank; 

create table BankAccount(account_id int  not null Primary Key, 
account_holder_name varchar(20) not null ,
account_balance int not null );

-- Task 1: Insert Data
-- Write an SQL INSERT statement to insert data into the BankAccount table. 

insert into BankAccount values 
(101,'VARUN',25000),
(102,'RAJ',23000),
(103,'HEMA',50000),
(104,'RIYA',35000),
(105,'KAMAL',65000),
(106,'VARUN',3000);

-- Task 2: Retrieving Data
-- Write an SQL SELECT statement to retrieve the account_holder_name and account_balance of all account holders from the BankAccount table.

select account_holder_name , account_balance from BankAccount;

-- Task 3: Filtering Data
-- Write an SQL SELECT statement to retrieve the account_holder_name and account_balance where the account_balance is more than 30,000.

select account_holder_name , account_balance from BankAccount 
where 
account_balance > 30000 ;

-- Task 4: Updating Data
-- Write an SQL UPDATE statement to change the account_balance of the account holder whose ID is 101.

update  BankAccount set account_balance = 31000 
where
account_id = 101;

-- Retrieve modify data

select * from BankAccount;



