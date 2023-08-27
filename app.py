from flask import Flask, current_app, request, make_response

app = Flask(__name__)

session = []


@app.get('/')
def home():
    return current_app.send_static_file('home.html')


@app.post("/studentCreate")
def create():
    data = request.form
    name = data.get("name")

    print(name)

    if name not in session:
        session.append(name)
        return make_response({"custom_response": "user logged in!"}, 200)

    return make_response({"custom_response": "user already logged in!"}, 403)


@app.post("/studentRemove")
def delete():
    data = request.form
    name = data.get("name")

    if name in session:
        session.remove(name)
        return make_response({"custom_response": "user logged out!"}, 200)

    return make_response({"custom_response": "user already logged out!"}, 403)
