import random
import string
from datetime import datetime
import mysql.connector


class Student:
    def __init__(self, name, surname, age, joiningYear):
        self.student_id = self.generate_student_id(name)
        self.name = name
        self.surname = surname
        self.age = age
        self.joiningYear = joiningYear

    def generate_student_id(self, name):
        random_suffix = ''.join(random.choices(string.digits, k=4))
        name_without_spaces = name.replace(" ", "").lower()
        student_id = name_without_spaces[:3] + random_suffix
        return student_id

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Age:", self.age)
        print("Joining Year:", self.joiningYear)
        print()

def name_checker(name):
    if name.isalpha():
        return True
    else:
        return False

def number_checker(age):
    try:
        float(age)
        return True
    except ValueError:
        return False

def create_student():
    print("You are about to create a student.")
    name = input("Enter student's name: ")
    while not name_checker(name) or len(name) > 15:
        print("Invalid input. Please enter letters only and a maximum of 15 characters.")
        name = input("Enter student's name: ")

    surname = input("Enter student's surname: ")
    while not name_checker(surname) or len(surname) > 15:
        print("Invalid input. Please enter letters only and a maximum of 15 characters.")
        surname = input("Enter student's surname: ")

    age = input("Enter student's age: ")
    while not number_checker(age) or not 11 <= int(age) <= 17:
        print("Invalid input. Please enter numbers only between 11 and 17.")
        age = input("Enter student's age: ")

    joining_year = input("Enter school start date (YYYY-MM-DD): ")
    while True:
        try:
            joining_year = datetime.strptime(joining_year, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the specified format.")
            joining_year = input("Enter school start date (YYYY-MM-DD): ")

    student = Student(name, surname, age, joining_year)
    save_to_database(student)  # Call the function to save the student data to the database
    return student

def save_to_database(student):
    # Establish a connection to the MariaDB database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Panajot",
        database="studentdatabase"
    )

    cursor = conn.cursor()   #what tells the database what you wanna do --> always use the cursor

    # Prepare the SQL query to insert the student data into the database
    query = "INSERT INTO students (student_id, name, surname, age, joining_year) VALUES (%s, %s, %s, %s, %s)"
    values = (student.student_id, student.name, student.surname, student.age, student.joiningYear)

    # Execute the query
    cursor.execute(query, values)

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()



def delete_student_by_name():
    name = input("Enter the name of the student to delete: ")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Panajot",
        database="studentdatabase"
    )
    cursor = conn.cursor()

    # Prepare the SQL query to delete the student by name
    query = "DELETE FROM students WHERE name = %s"
    values = (name,)

    # Execute the query
    cursor.execute(query, values)

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()



def delete_student_by_id():
    # Establish a connection to the MariaDB database
    student_id = input("Enter the ID of the student to delete: ")
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Panajot",
        database="studentdatabase"
    )
    cursor = conn.cursor()

    # Prepare the SQL query to delete the student by ID
    query = "DELETE FROM students WHERE student_id = %s"
    values = (student_id,)

    # Execute the query
    cursor.execute(query, values)

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()


def modify_student():
    student_id = input("Enter the ID of the student to modify: ")

    # Establish a connection to the MariaDB database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Panajot",
        database="studentdatabase"
    )
    
    cursor = conn.cursor()

    query = "SELECT * FROM students WHERE student_id = %s"
    values = (student_id,)
    cursor.execute(query, values)
    student = cursor.fetchone()

    if student is None:
        print("Student not found.")
    else:
        print("Current details:")
        print("Name:", student[1])
        print("Surname:", student[2])
        print("Age:", student[3])
        print("Joining Year:", student[4])

        # Prompt the user for updated details
        name = input("Enter the new name of the student: ")
        surname = input("Enter the new surname of the student: ")
        age = input("Enter the new age of the student: ")
        joining_year = input("Enter the new joining year of the student (YYYY-MM-DD): ")

        # Prepare the SQL query to update the student's details
        query = "UPDATE students SET name = %s, surname = %s, age = %s, joining_year = %s WHERE student_id = %s"
        values = (name, surname, age, joining_year, student_id)

        # Execute the query
        cursor.execute(query, values)

        # Commit the changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()

