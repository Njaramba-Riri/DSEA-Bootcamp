CREATE TABLE EmployeeDepartment(
    employee_id int NOT NULL UNIQUE PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL,
    job VARCHAR(255),
    manager_id int NOT NULL,
    salary int
);

INSERT INTO EmployeeDEpartment 
VALUES('7032','John Clark','Sales Person','2341','40,000');

INSERT INTO EmployeeDepartment
VALUES('7033','Mary Njeri','HR','2341','65,000');

INSERT INTO EmployeeDepartment
VALUES('7034','James Riri','Data Engineer','2322','320,000');

INSERT INTO EmployeeDepartment
VALUES('7035','Lucy Kimani','Receptionist','2320','35,000');

INSERT INTO EmployeeDepartment
VALUES('7036','Peter Ndirangu','C.E.O','2300','350,000');


SELECT SUM(salary), MIN(salary), MAX(salary) FROM EmployeeDepartment;
