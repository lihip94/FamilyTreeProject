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
    return is_login(request.form['username'])


@app.route("/login", methods=['POST'])
def login():
    """Log in page"""
    email = request.form.get['email']
    password = request.form.get['password']
    if email is None or password is None:
        return {
            "status": 404,
            "message": "some values are missing"
        }
    return valid_login(email, password)


@app.route("/signup", methods=['POST'])
def signup():
    """Sign in page"""
    email = request.form.get['email']
    username = request.form.get['username']
    password = request.form.get['password']
    if email is None or username is None or password is None:
        return {
            "status": 404,
            "message": "some values are missing"
        }
    details = {
            "email": email,
            "username": username,
            "password": password
    }
    return valid_signup(details)


@app.route("/add_new_person", methods=['POST'])
def add_new_person():
    """add new person page"""
    person_id = request.form['person_id']
    mother_id = request.form['mother_id']
    father_id = request.form['father_id']
    details = [person_id, mother_id, father_id]
    return add_person(details)


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
