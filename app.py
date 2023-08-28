from flask import Flask, render_template, request, redirect, url_for, flash, session, get_flashed_messages, jsonify
import random
import string
from datetime import datetime

app = Flask(__name__)

app.secret_key = 'VerySecret'  # Replace with your own secret key

# User login details
users = {
    'admin': 'password',
    'user1': 'pass123',
    'user2': 'pass456'
}

Students = []


@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))


@app.route("/studentCreate", methods=["POST"])
def studentCreate():
    # Get data from the form using request.form.get
    name = request.form.get("name")
    surname = request.form.get("surname")
    age = request.form.get("age")
    joiningYear = request.form.get("joiningYear")

    if name_checker(name) and name_checker(surname) and number_checker(age) and date_checker(joiningYear):
        student = Student(name, surname, age, joiningYear)
        Students.append(student)
        response_message = (f"Received: {name} {surname}, Age: {age}, Joining Year: {joiningYear},"
                            f" Student ID: {student.student_id}")
        return "Student record created successfully. " + response_message
    else:
        return "Invalid input. Please try again. Stop hacking my website lol."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate username and password
        if username in users and users[username] == password:
            session['username'] = username  # Store username in session
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'error')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    with app.test_request_context():  # Create a temporary request context
        # Clear all flash messages
        flashes = list(get_flashed_messages())
        for message in flashes:
            flash(message, 'message')

    flash('Logged out successfully!', 'success')  # Add flash message for successful logout
    return redirect(url_for('login'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html'), 404


# student
class Student:
    def __init__(self, name, surname, age, joiningYear):
        self.student_id = generate_student_id(name)
        self.name = name
        self.surname = surname
        self.age = age
        self.joiningYear = joiningYear


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


def generate_student_id(name):
    random_suffix = ''.join(random.choices(string.digits, k=4))
    name_without_spaces = name.replace(" ", "").lower()
    student_id = name_without_spaces[:3] + random_suffix
    return student_id

def date_checker(joiningYear):
    try:
        joiningYear = datetime.strptime(joiningYear, "%Y-%m-%d").date()
        return True
    except ValueError:
        return False


# def create_student(name, surname, age, joiningYear):
#     while not name_checker(name) or len(name) > 15:
#         invalid_Name = "Invalid input. Please enter letters only and a maximum of 15 characters."
#         name = input("Enter student's name: ")
#
#     while not name_checker(surname) or len(surname) > 15:
#         print("Invalid input. Please enter letters only and a maximum of 15 characters.")
#         surname = input("Enter student's surname: ")
#
#     while not number_checker(age) or not 11 <= int(age) <= 17:
#         print("Invalid input. Please enter numbers only between 11 and 17.")
#         age = input("Enter student's age: ")
#
#     while True:
#         try:
#             joiningYear = datetime.strptime(joiningYear, "%Y-%m-%d").date()
#             break
#         except ValueError:
#             print("Invalid date format. Please enter the date in the specified format.")
#             joiningYear = input("Enter school start date (YYYY-MM-DD): ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# if __name__ == '__main__':
#     app.run(ssl_context=('certificate.pem', 'private_key.pem'), host='0.0.0.0', port=443)
