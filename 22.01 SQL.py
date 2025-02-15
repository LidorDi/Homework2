#a

# SELECT courses.course_name , lecturers.first_name FROM courses
# INNER JOIN lecturers ON courses.lecturer_id = lecturers.lecturer_id

#b

#SELECT courses.course_name FROM courses
# WHERE courses.lecturer_id IS NULL

#C

#SELECT courses.course_name , lecturers.first_name FROM courses
# LEFT JOIN lecturers ON lecturers.lecturer_id = courses.lecturer_id

#D

#SELECT courses.course_name , lecturers.first_name FROM courses
# INNER JOIN lecturers ON lecturers.lecturer_id = courses.lecturer_id

# SAME QUESTION LIKE A ?

#E

# SELECT lecturers.first_name FROM courses
# RIGHT JOIN lecturers ON lecturers.lecturer_id = courses.lecturer_id
# WHERE courses.lecturer_id IS NULL

#F

# SELECT courses.course_name , lecturers.first_name FROM courses
# RIGHT JOIN lecturers ON lecturers.lecturer_id = courses.lecturer_id

#G

# SELECT courses.course_name , lecturers.first_name FROM courses
# FULL JOIN lecturers ON lecturers.lecturer_id = courses.lecturer_id

#H

# SELECT lecturers.first_name, lecturers.last_name, courses.course_name FROM LECTURERS
# CROSS JOIN  courses;


