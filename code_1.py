# import mysql.connector    # provides a Python interface for working with MariaDB/MySQL databases
import time
import random
import string
from datetime import datetime

class Student:                                              #define a student class
    def __init__(self, student_id, name, surname, age, joiningYear):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.age = age
        self.joiningYear = joiningYear

# def save(self):
#         # Establish a connection to the MariaDB database
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="your_username",
#             password="your_password",
#             database="your_database"
#         )
#         cursor = conn.cursor()


def nameChecker(name):   #Check if a given input only contains names (letters).
    if name.isalpha(): #handle alphabetic characters from various languages as long as they are supported by the Unicode character database.
        return True
    else:
        return False
    
def numberChecker(age): #Check if a digit is entered, doesn't accept decimal values.
    try:
        float(age)
        return True
    except ValueError:
        return False

def generate_student_id(name):   #create a random student ID 
    random_suffix = ''.join(random.choices(string.digits, k=4))  # Generate a random 4-digit suffix
    name_without_spaces = name.replace(" ", "").lower()  # Remove spaces and convert name to lowercase
    student_id = name_without_spaces[:3] + random_suffix  # Combine first 3 characters of name with the suffix
    return student_id   #the student's name is at least 3 letters long




def createStudent():                                #Function that creates a student.
    print("You are about to create a student.")
    time.sleep(1)

    while True:
        name = input("Enter student's name: ")
        if nameChecker(name) and len(name) <= 15:
            break
        else:
            print("Invalid input. Please enter letters only.")

    while True:
        surname = input("Enter student's surname: ")
        if nameChecker(surname) and len(surname) <= 15:
            break
        else:
            print("Invalid input. Please enter letters only.")


    while True:
        age = int(input("Enter a number: "))
        if numberChecker(age) and (age >= 11 and age<=17):  #assuming this is a secondary school
            break
        else:
            print("Invalid input. Please enter numbers only.")

    student_id = generate_student_id(name)
    print("Unique Student ID:", student_id)

    while True:
        joiningYear = input("Enter school start date (YYYY-MM-DD): ")
        try:
            joiningYear = datetime.strptime(joiningYear, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the specified format.")
    student = Student(student_id, name, surname, age, joiningYear)
    return student

student = createStudent()


print("Student ID:", student.student_id)
print("Name:", student.name)
print("Surname:", student.surname)
print("Age:", student.age)
print("Joining Year:", student.joiningYear)

print("Testing if this will show in Github")

