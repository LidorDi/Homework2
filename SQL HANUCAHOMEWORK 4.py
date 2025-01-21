#########################1

#1

#SELECT Lecturers.name , Courses.name FROM Lecturers
#INNER JOIN Courses ON Courses.lecturer_id = Lecturers.lecturer_id

#2

#SELECT Lecturers.name , Courses.name FROM Courses
#LEFT JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id

#3

#SELECT Lecturers.name , Courses.name FROM Lecturers
#LEFT JOIN Courses ON Courses.lecturer_id = Lecturers.lecturer_id

#4

#SELECT Lecturers.name , Courses.name FROM Courses
#LEFT JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
#WHERE Courses.lecturer_id IS NULL

#5

#SELECT Lecturers.name , Courses.name FROM Lecturers
#LEFT JOIN Courses ON Courses.lecturer_id = Lecturers.lecturer_id
#WHERE Courses.lecturer_id IS NOT NULL






#########################2
#15

#SELECT Employees.* , Departments.name , Departments.building , Departments.budget FROM Employees
#INNER JOIN Departments ON Employees.department_id = Departments.department_id;

#16

#SELECT Employees.employee_id , Employees.name as "Employees", Departments.name as "Departments" FROM Employees
#LEFT JOIN Departments ON Employees.department_id = Departments.department_id

#17

#SELECT Employees.employee_id, Employees.name, Employees.email, Employees.salary, Employees.seniority
#FROM Employees
#LEFT JOIN Departments ON Employees.department_id = Departments.department_id
#WHERE Employees.department_id IS NULL;

#18

#SELECT COUNT(employee_id) as "EMPLOYEES COUNT" FROM Employees

#20

#SELECT Employees.employee_id, Employees.name, Departments.name, MAX(salary) AS best_salary
#FROM Employees
#RIGHT JOIN Departments ON Employees.department_id = Departments.department_id
#GROUP BY Departments.name;