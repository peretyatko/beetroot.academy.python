SELECT first_name, last_name
FROM employees;
SELECT department_id
FROM employees;
SELECT * FROM employees
ORDER BY first_name;
SELECT MIN(salary)
FROM employees;
SELECT MAX(salary)
FROM employees;
SELECT ROUND ((salary / 12.00), 2) AS monthly_salary
FROM employees;
SELECT first_name, last_name, salary, salary * 0.12 AS PF
FROM employees;