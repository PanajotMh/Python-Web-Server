from flask import Flask, render_template, request, redirect, url_for, flash, session, get_flashed_messages
from flask_sslify import SSLify
import os
import multiprocessing


app = Flask(__name__)
app.secret_key = 'secretKey'  # Session management
sslify = SSLify(app)



# Mock user credentials for demonstration purposes

users = {
    'admin': 'password',
    'user1': 'pass123',
    'user2': 'pass456'
}


@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))
    
@app.route("/studentCreate", methods=["POST"])
def studentCreate():
    name = request.form.get("name")
    surname = request.form.get("surname")
    age = request.form.get("age")
    joining_year = request.form.get("joiningYear")

    #add actions later

    response_message = f"Received: {name} {surname}, Age: {age}, Joining Year: {joining_year}"
    return response_message


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

from flask import flash

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




# if __name__ == '__main__':
#     app.run(ssl_context=('certificate.pem', 'private_key.pem'), host='0.0.0.0', port=443)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)


app = Flask(__name__)
app2 = Flask(__name__)

def run_app():
    app.run(ssl_context=('certificate.pem', 'private_key.pem'), host='0.0.0.0', port=443)

def run_app2():
    app2.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=run_app)
    # process2 = multiprocessing.Process(target=run_app2)
    
    process1.start()
    # process2.start()
    
    process1.join()
    # process2.join()
    # lol