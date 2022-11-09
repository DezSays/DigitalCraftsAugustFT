-- psql -U postgres db_name \i file.sql
-- Step 1. Create a database named mockcompany.

--* CREATE DATABASE mockcompany;

-- Step 2. Create a table named employee, and have the following columns: name, position, currently_employed, years_employed, gender, salary, id.

--* CREATE TABLE employee (
--*     name varchar,
--*     position varchar,
--*     currently_employed boolean,
--*     years_employed integer,
--*     gender char(1),
--*     salary integer,
--*     id integer
--* );

-- Step 3. Add five employees to your table, 3 that are currently employed and two that are not.

--* -- INSERT INTO employee VALUES 
--* (
--* 'Dane', 'Customer Service', FALSE , 30, 'M', 65000, 1
--* ),
--* (
--* 'Angela', 'IT', FALSE , 30, 'F', 45000, 2
--* ),
--* (
--* 'Veronica', 'Manager', TRUE , 30, 'F', 95000, 3
--* ),
--* (
--* 'Felipe', 'Customer Service', TRUE , 30, 'M', 65000, 4
--* ),
--* (
--* 'James', 'IT', TRUE , 30, 'F', 85000, 5
--* );


-- Step 4. Display only the names and corresponding id numbers from your table.

--* SELECT name, id FROM employee;

-- Step 5. Display only the names and corresponding id numbers of employees that are currently employed.

--* SELECT name, id FROM employee WHERE currently_employed='yes';

-- Step 6. Display only the names, corresponding id numbers, and salaries of employees that have been working for more than 5 years.

--* SELECT name, id, salary FROM employee WHERE currently_employed=TRUE;

-- Step 7. Display only the names, corresponding id numbers, and years employed of those who have salaries higher than 75k.

--* SELECT name, id, years_employed FROM employee WHERE salary > 75000;

-- Step 8: Display only the names of employees that have a d, upper or lower case, somewhere in their name.

--* SELECT name FROM employee WHERE name ilike '%d%';

-- Step 9. Display only the names of employees that have an upper case T in their name.

--* SELECT name FROM employee WHERE name like '%A%';

-- Step 10. Take out the gender column from the table.

--* ALTER TABLE employee DROP COLUMN gender;

-- Step 11. Figure out how many records you have in your database.

--* SELECT COUNT(name) FROM employee;

-- Step 12. Display the and salary of the highest paid employee.

--* SELECT MAX(salary) FROM employee;

-- Step 13. Display all employees, sorted in ascending order by name.

--*-- SELECT * FROM employee ORDER BY name ASC;

-- Step 14. Display all employees, sorted in descending order by salary.

--*-- SELECT * FROM employee ORDER BY salary DESC;

-- Step 15. Display the names and salaries of the top three highest paid employees in descending order.

--* SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 3;

-- Step 16. Display the name and corresponding id number of the second highest paid employee. 

--* SELECT name, id FROM employee ORDER BY salary LIMIT 1 OFFSET 1;