import random
import string
from datetime import datetime


class Student:  # define a student class
    def __init__(self, student_id, name, surname, age, joining_year):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.age = age
        self.joining_year = joining_year


def name_checker(name):  # Check if a given input only contains names (letters).
    if name.isalpha():  # handle alphabetic characters from various languages as long as they are supported by the
        # Unicode character database.
        return True
    else:
        return False


def generate_student_id(name):  # create a random student ID
    random_suffix = ''.join(random.choices(string.digits, k=4))  # Generate a random 4-digit suffix
    name_without_spaces = name.replace(" ", "").lower()  # Remove spaces and convert name to lowercase
    student_id = name_without_spaces[:3] + random_suffix  # Combine first 3 characters of name with the suffix
    return student_id  # the student's name is at least 3 letters long


def create_student():  # Function that creates a student.
    while True:
        name = input("Enter student's name: ")
        if name_checker(name) and len(name) <= 15:
            break
        else:
            print("Invalid input. Please enter letters only.")

    while True:
        surname = input("Enter student's surname: ")
        if name_checker(surname) and len(surname) <= 15:
            break
        else:
            print("Invalid input. Please enter letters only.")

    while True:
        age = input("Enter a number: ")
        if not name_checker(age):
            if 11 <= int(age) <= 17:  # assuming this is a secondary school
                break
        else:
            print("Invalid input. Please enter numbers only.")

    student_id = generate_student_id(name)
    print("Unique Student ID:", student_id)

    while True:
        joining_year = input("Enter school start date (YYYY-MM-DD): ")
        try:
            joining_year = datetime.strptime(joining_year, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the specified format.")

    return Student(student_id, name, surname, age, joining_year)


student = create_student()

print("Student ID:", student.student_id)
print("Name:", student.name)
print("Surname:", student.surname)
print("Age:", student.age)
print("Joining Year:", student.joining_year)

print("Testing if this will show in Github")
