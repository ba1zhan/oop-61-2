import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    age INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_name TEXT,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
""")

conn.commit()

def create_student(name, age):
    cursor.execute(
        "INSERT INTO students(name, age) VALUES (?, ?)",
        (name, age)
    )
    conn.commit()

def create_course(student_id, course_name, grade):
    cursor.execute(
        "INSERT INTO courses(student_id, course_name, grade) VALUES (?, ?, ?)",
        (student_id, course_name, grade)
    )
    conn.commit()

def students_with_courses():
    cursor.execute("""
    SELECT students.name, students.age, courses.course_name, courses.grade
    FROM students
    LEFT JOIN courses ON students.id = courses.student_id
    """)
    for row in cursor.fetchall():
        print(row)

def aggregate_functions():
    cursor.execute("SELECT COUNT(*) FROM courses")
    print(cursor.fetchone()[0])

    cursor.execute("SELECT MAX(grade) FROM courses")
    print(cursor.fetchone()[0])

    cursor.execute("SELECT AVG(grade) FROM courses")
    print(cursor.fetchone()[0])

def courses_count_by_student():
    cursor.execute("""
    SELECT students.name, COUNT(courses.id)
    FROM students
    LEFT JOIN courses ON students.id = courses.student_id
    GROUP BY students.id
    """)
    for row in cursor.fetchall():
        print(row)

def students_with_python():
    cursor.execute("""
    SELECT name FROM students
    WHERE id IN (
        SELECT student_id FROM courses
        WHERE course_name = 'Python'
    )
    """)
    for row in cursor.fetchall():
        print(row)

cursor.execute("""
CREATE VIEW IF NOT EXISTS student_courses_view AS
SELECT students.name, courses.course_name, courses.grade
FROM students
JOIN courses ON students.id = courses.student_id
""")

conn.commit()

def read_view():
    cursor.execute("SELECT * FROM student_courses_view")
    for row in cursor.fetchall():
        print(row)

create_student("Байжан", 20)
create_student("Данислам", 19)

create_course(1, "Python", 95)
create_course(1, "SQLite", 90)
create_course(2, "Python", 88)

students_with_courses()
aggregate_functions()
courses_count_by_student()
students_with_python()
read_view()

conn.close()
