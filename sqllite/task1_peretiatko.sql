CREATE DATABASE workers;
USE workers;


CREATE TABLE workers
(
EmployeeID int,
EmployeeName varchar(255),
EmergencyContactName varchar(255),
PhoneNumber int,
Address varchar(255),
City varchar(255),
Country varchar(255)
);
INSERT INTO workers ( )
VALUES
(234, 'Kill', 'Olha', 56, 'Kit', 'KR', 'USA' ),
(235, 'Bil', 'Lom', 0933489180, 'NY', 'NY', 'USA' ),
(236, 'Bob', 'Kot', 0672177840, 'SW', 'Man', 'USA' );
ALTER TABLE workers
ADD BloodGroup varchar(255);
USE workers;
UPDATE workers
SET EmployeeName ='Aahana', City='Dnipro'
WHERE EmployeeID = 235;
DELETE FROM workers
WHERE EmployeeName='Bob';
SELECT * FROM workers;



