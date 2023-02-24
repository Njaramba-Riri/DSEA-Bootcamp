/*creating table students*/
CREATE TABLE students(
    names varchar2(20),
    Reg_no varchar2(20),
    course varchar2(20),
    mobile_no varchar2(12),
    school varchar2(20),
    reg_date date,
    grad_date date
);

/*Adding data into students*/
INSERT INTO students VALUES('James Riri', 'SCPP/00824/2023', 'Machine Learning','075743993','SCIT','01-jan-2023','18-Dec-2026');

INSERT INTO students VALUES('Mary Wanjiku','SDDP/2320/2021','Statistics','074563928','Mathematics','13-01-2021','23-12-2025');

INSERT INTO students VALUES('Abdi Hassan','SPPS/2093/2018','Civil Engineering','079364728','Engineering','07-09-2018','17-04-2023');

INSERT INTO students VALUES('Mary Wanjiku','SBMS/0834/2022','Bsc Commerce','0738273646','Mathematics','27-04-2022','18-12-2026');


/*SELECT- retrieving data USING SQL SELECT statement*/
SELECT * FROM students;

SELECT names, Reg_no, course FROM students;

/*Renaming columns using SSELECT Statement*/
SELECT name "Full name",Reg_no"Registration Number",reg_date "Registration Date", grad_date"Graduation date" FROM students;

/*Checking for Duplicate Rows/records*/
SELECT DISTINCT names from students;

/*WHERE clause*/
SELECT Reg_no "Registration Number", course FROM students 
WHERE names='Mary Wanjiku';

SELECT names,grad_date FROM students 
WHERE mobile_no=NULL;

/*ORDER BY Clause*/
SELECT names
FROM students
ORDER BY reg_date ASC;/*Ascending order*/

SELECT names
FROM students
ORDER BY grad_date DESC;/*Descending order*/

/*UPDATE Command*/
UPDATE students
SET name='Maureen Wanjiru'
WHERE reg_no='SBMS/0834/2022';

/*Creating a copy of the table*/
/*CREATE TABLE students2
AS (SELECT* FROM students);

CREATE  TABLE students 
AS (SELECT * FROM students);

/*Creating a table using a subsubquery*/
CREATE TABLE students4
AS (SELECT names,Reg_no,course, grad_date
WHERE school='Mathematics');

/*Working with Dates*/
SELECT names, Reg_no FROM students
WHERE reg_date<'01-04-2023';

/*Reporting grouped data
grouped funtions:-
avg
count
max
min
stddev
sum
variance
*/
SELECT min(reg_date), max(grad_date) FROM students;

/*SQL Constraints*/
/*NOT NULL*/
CREATE TABLE Sales(
    sale_id int NOT NULL,
    sale_amount int NOT NULL,
    Vendor_name varchar(255) NOT NULL,
    sale_date date,
    profit int NOT NULL,
);

/*UNIQUE Constraint*/
CREATE TABLE Sales(
    sale_id int NOT NULL,
    sale_amount int NOT NULL,
    vendor_name varchar(255) NOT NULL,
    sale_date date,
    profit int,
    UNIQUE(sale_id)
);

/*Adding UNIQUE CONSTRAINTS when a the table already exists*/
ALTER TABLE Sales
ADD CONSTRAINT UC_sales UNIQUE(sale_id, sale_amount);

/*Dropping a UNIQUE Constraint*/
ALTER TABLE Sales
DROP CONSTRAINT UC_sales;

/*CHECK Constraint*/
CREATE TABLE Sales(
    sale_id int NOT NULL UNIQUE,
    sale_amount int NOT NULL,
    vendor_name varchar(255),
    sale_date date,
    profit int,
CHECK(vendor_name<>'Riri')
);

/*For multiple columns*/
CREATE TABLE Sales(
    sale_id int NOT NULL UNIQUE,
    SALE_AMOUNT int NOT NULL,
    vendor_name varchar(255),
    sale_date date,
    profit int,
CONSTRAINT chk_sales CHECK (vendor_name<>'Riri' and profit>500)
);

/*Deleteing &adding to an existing table*/
ALTER TABLE Sales
ADD CONSTRAINT chk_sales CHECK(vendor_name<>'Riri' and profit>500);

ALTER TABLE Sales
DROP CONSTRAINT chk_sales;

/*PRIMARY KEY CONSTRAINT*/
CREATE TABLE Sales(
    sale_id int NOT NULL,
    sale_amount int NOT NULL,
    vendor_name varchar(250),
    sale_date date,
    profit int,
    PRIMARY KEY(sale_id)
);

/*Defining primary key in multiple columns*/
CREATE TABLE Sales(
    sale_id int NOT NULL,
    sale_amount int NOT NULL,
    vendor_name varchar(255),
    sale_date date,
    profit int,
    CONSTRAINT pk_sales PRIMARY KEY(sale_id, sale_amount)
);

/*Adding or deleting a primary key*/
ALTER TABLE Sales
ADD PRIMARY KEY(sale_id);

ALTER TABLE Sales
ADD CONSTRAINT pk_sales PRIMARY KEY(sale_id, sale_amount);

ALTER TABLE Sales
DROP CONSTRAINT pk_sales;

/*FOREIGN KEY CONSTRAINT*/
CREATE TABLE Sales_person(
    sales_person_id int NOT NULL,
    sales_person_name varchar(255),
    sales_person_location varchar(255),
    sale_id int NOT NULL,
    PRIMARY KEY(sales_person_id),
    FOREIGN KEY(sale_id) REFERENCES Sales(sale_id)
);

/*On multiple lines*/
CREATE TABLE Sales_Person (
    Sales_Person_Id int NOT NULL,
    Sales_Person_Name varchar(255),
    Sales_Person_Location varchar(255),
    Sale_Id int NOT NULL,
    PRIMARY KEY (Sales_Person_Id),
    CONSTRAINT fk_Sales_Sales_Person FOREIGN KEY (Sale_Id) REFERENCES Sales (Sale_Id)
);

/*Adding or dropping a foreign key constraint*/
ALTER TABLE Sales_person
ADD FOREIGN KEY(Sale_id) REFERENCES Sales(sale_id);

ALTER TABLE Sales_person
ADD CONSTRAINT fk_sales_sales_person
FOREIGN KEY(Sale_id) REFERENCES Sales(Sale_Id);

/*Dropping*/
ALTER TABLE Sales_Person
DROP CONSTRAINT fk_Sales_Sales_Person;

