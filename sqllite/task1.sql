INSERT INTO hr ( )
VALUES
(234, 'Kill', 'Olha', 56, 'Kit', 'KR', 'USA' ),
(235, 'Bil', 'Lom', 0933489180, 'NY', 'NY', 'USA' ),
(236, 'Bob', 'Kot', 0672177840, 'SW', 'Man', 'USA' );
ALTER TABLE hr
ADD BloodGroup varchar(255);
USE hr;
UPDATE hr
SET EmployeeName ='Aahana', City='Dnipro'
WHERE EmployeeID = 235;
DELETE FROM hr
WHERE EmployeeName='Bob';
SELECT * FROM hr;
