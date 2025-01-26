import sqlite3
import os


def add_courses():
    manycourses: int = int(input("How many courses u want to add?"))
    for _ in range (manycourses):
        topic: str = str(input("Whats the name of the topic?"))
        hours: int = int(input("How many hours is the topic?"))
        tup = (topic , hours)
        cursor.execute("INSERT INTO courses (topic , hours) VALUES (?, ?)", tup)
        conn.commit()

def add_students():
    manystudents: int = int(input("How many students u want to add?"))
    for _ in range(manystudents):
        name:str = str(input("enter the name of the student"))
        email:str = str(input("enter the email of the student"))
        tup1 = (name , email)
        cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", tup1)
        conn.commit()

def add_grade():
    manygrades: int = int(input("How many courses u want to add?"))
    for _ in range(manygrades):
        student_id: int = int(input("Enter student id"))
        course_id: int = int(input("Enter course id"))
        grade: int = int(input("Enter student grade"))
        tup2: tuple = (student_id , course_id , grade)
        cursor.execute("INSERT INTO grades (student_id , course_id , grade) VALUES (? , ? , ?) " , tup2)
        conn.commit()

db_name: str = "dsf.db"
if os.path.exists(db_name):
    print("there is an gets removed")
    os.remove(db_name)

conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("CREATE TABLE courses (course_id INTEGER PRIMARY KEY Autoincrement, topic TEXT NOT NULL UNIQUE , hours INTEGER NOT NULL)")
cursor.execute("CREATE TABLE grades (student_id INTEGER NOT NULL, course_id INTEGER NOT NULL , grade INTEGER CHECK (grade BETWEEN 0 AND 100) , PRIMARY KEY (student_id , course_id) FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id))")
cursor.execute("CREATE TABLE students (student_id INTEGER PRIMARY KEY Autoincrement, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)")

cursor.execute("SELECT courses.topic, AVG(grades.grade) AS average_grade FROM courses LEFT JOIN grades ON grades.course_id = courses.course_id GROUP BY courses.course_id")
cursor.execute("SELECT topic FROM courses")

##### i did task 5 in add_grade def
#hetgar

def add_course_check():
    topic: str = str(input("What is the course topic?"))
    hours: int = int(input("How much hours is the course?"))
    cursor.execute("SELECT * FROM courses WHERE topic like ?" , (topic,))
    has_or_no = cursor.fetchone()
    if has_or_no:
        print("theres already a course about this subject")
    else:
        cursor.execute("INSERT INTO courses (topic , hours) VALUES (? , ?) ", (topic, hours))
        conn.commit()
        print("Course added")