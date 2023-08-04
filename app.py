from flask import Flask, render_template, request, redirect, url_for, flash, session, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'secretKey'  # Session management

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




if __name__ == '__main__':
    app.run(debug=True)
