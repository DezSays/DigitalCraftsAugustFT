-- psql -U postgres db_name \i file.sql
-- Step 1. Create Database Sept2022;

--* CREATE DATABASE Sept2022;

-- Step 2. Create a table and name it students. It should contain the following information: name, website, github_username, points, gender, cohort_start_date, graduated.

--* CREATE TABLE student (
--*     name varchar,
--*     website varchar,
--*     github_username varchar,
--*     points integer,
--*     gender char(1),
--*     cohort_start_date date,
--*     graduated boolean
--* );

-- Step 3. Add three students to your table.

--* -- INSERT INTO student VALUES 
--* (
--* 'Dane', 'dane@me.com', 'dane', 30, 'M', '2022-02-07', FALSE
--* ),
--* (
--* 'chewie', 'chewie@me.com', 'chewie', 100, 'M', '2022-02-07', FALSE
--* ),
--* (
--* 'violet', 'violet@me.com', 'violet', 42, 'M', '2022-02-07', FALSE
--* );

-- Step 4. Update your table so that the student with the lowest points is given 5 more points.

--* SELECT name, MIN(points) FROM student; 
--* UPDATE student SET points = 35 WHERE name='Dane';

-- Step 5. Update the values in your table where any student who has False for their graduation is changed to True.

--* UPDATE student SET graduated = TRUE WHERE graduated = FALSE;

-- Step 6. Add two more students to your table.

--* -- INSERT INTO student VALUES 
--* (
--* 'tri', 'tri@me.com', 'tri', 100, 'M', '2022-02-07', TRUE
--* ),
--* (
--* 'gary', 'gary@me.com', 'gary', 29, 'M', '2022-02-07', FALSE
--* );

-- Step 7. Delete one student from your table. 

--* DELETE FROM student WHERE name = 'gary';

-- Step 8. Show all students with M selected as their gender. 

--* SELECT * FROM student WHERE gender='M';

-- Step 9. Show which students have graduated. 

--* SELECT * FROM student WHERE graduated=TRUE;

-- Step 10. Alter table and add city to your table.

--* ALTER TABLE student ADD city varchar;

-- Step 11: Get the average points from the table. 

--* SELECT AVG(points) FROM student;