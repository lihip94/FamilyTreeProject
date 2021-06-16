from flask import Flask, render_template, url_for, request, redirect

from service import *

app = Flask(__name__)


@app.route("/")
def land():
    """Landing page"""
    return "<h1>Landing page<h1>"


@app.route("/home", methods=['GET'])
def home():
    """Home page"""
    if request.method == 'GET':
        return is_login(request.form['username'])


@app.route("/login", methods=['POST'])
def login():
    """Log in page"""
    if request.method == 'POST':
        return login(request.form['email'], request.form['password'])


@app.route("/signup", methods=['POST'])
def signup():
    """Sign in page"""
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['last_name']
    details = [email, first_name, last_name, password]
    if request.method == 'POST':
        return signup(details)


@app.route("/add_new_person", methods=['POST'])
def add_new_person():
    """add new person page"""
    person_id = request.form['person_id']
    mother_id = request.form['mother_id']
    father_id = request.form['father_id']
    details = [person_id, mother_id, father_id]
    if request.method == 'POST':
        return add_person(details)


@app.route("/get_table", methods=['GET'])
def get_table():
    """get table information"""
    token = request.form['token']
    name = request.form['tree_name']
    if request.method == 'GET':
        return get_table_information(token, name)


@app.route("/get_tree", methods=['GET'])
def get_tree():
    """get tree information"""
    token = request.form['token']
    name = request.form['tree_name']
    if request.method == 'GET':
        return get_tree_information(token, name)


if __name__ == "__main__":
    app.run()
