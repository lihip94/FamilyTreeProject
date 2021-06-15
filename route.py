from flask import Flask, render_template, url_for, request, redirect

from service import *

app = Flask(__name__)


@app.route("/")
def land():
    """Landing page"""
    return "<h1>Landing page<h1>"


@app.route("/home", methods=['POST', 'GET'])
def home():
    """Home page"""
    if request.method == 'POST':
        if user_login(request.form['username']):
            return render_template('home.html')
    return render_template('login.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    """Log in page"""
    if request.method == 'POST':
        if valid_login(request.form['email'], request.form['password']):
            return redirect("home")
        else:
            return render_template('error.html')
    else:
        return render_template('login.html')


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    """Sign in page"""
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['last_name']
    details = [email, first_name, last_name, password]
    if request.method == 'POST':
        if success_signup(details):
            pass
    return render_template('signup.html')


@app.route("/add_new_person", methods=['POST', 'GET'])
def add_new_person():
    """add new person page"""
    person_id = request.form['person_id']
    mother_id = request.form['mother_id']
    father_id = request.form['father_id']
    details = [person_id, mother_id, father_id]
    if request.method == 'POST':
        # later change to try and catch
        if add_person(details):
            pass
    return render_template('person.html')


@app.route("/get_table", methods=['GET'])
def get_table():
    """get table information"""
    token = request.form['token']
    name = request.form['tree_name']
    return get_table_information(token, name)


@app.route("/get_tree", methods=['GET'])
def get_tree():
    """get tree information"""
    token = request.form['token']
    name = request.form['tree_name']
    return get_tree_information(token, name)


if __name__ == "__main__":
    app.run()
