
SELECT first_name, last_name, departments.department_id, departments.depart_name
FROM departments
JOIN employees ON departments.department_id = employees.department_id;

SELECT first_name, last_name, departments.depart_name, locations.city, locations.state_province
FROM departments
JOIN employees ON departments.department_id = employees.department_id 
JOIN locations ON departments.location_id = locations.location_id;

SELECT first_name, last_name, departments.department_id, departments.depart_name
FROM departments
JOIN employees ON departments.department_id = employees.department_id 
WHERE departments.department_id=80 OR departments.department_id = 40;

SELECT *FROM departments;

SELECT employees_worker.first_name AS manadger, employees_manadger.first_name AS worker
FROM employees AS employees_worker
JOIN employees AS employees_manadger ON employees_manadger.manager_id = employees_worker.employee_id;

SELECT jobs.job_title, (employees.first_name || employees.last_name) AS full_name, jobs.max_salary - employees.salary
FROM jobs
JOIN employees ON jobs.job_id=employees.job_id;

SELECT job_title, SUM(salary)/COUNT(job_title) AS average_salary
FROM jobs
JOIN employees ON jobs.job_id = employees.job_id
GROUP BY job_title;

SELECT city,(employees.first_name || employees.last_name) AS full_name, salary
FROM departments
JOIN locations ON locations.location_id = departments.location_id
JOIN employees ON departments.department_id = employees.department_id 
WHERE locations.city = "London";

SELECT depart_name, COUNT(employees.department_id)
FROM departments
JOIN employees ON departments.department_id = employees.department_id 
GROUP BY depart_name;

