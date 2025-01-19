#1

#SELECT exam_year , AVG(grade)  FROM grades
#GROUP BY exam_year

#2

#SELECT student_name , AVG(grade)  FROM grades
#GROUP BY student_name

#3

#SELECT exam_year , MAX(grade) AS "MAX" , MIN(grade) as "MIN" FROM grades
#GROUP BY exam_year

#4

#SELECT exam_year , subject_name , COUNT(subject_name) FROM grades
#GROUP BY subject_name

#5

#SELECT subject_name , AVG(grade) FROM grades
#HAVING AVG(grade) > 85

#6

#SELECT grade , count(grade) as times FROM grades
#WHERE grade > 90
#GROUP BY grade