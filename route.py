from flask import Flask, render_template, url_for, request, redirect

from service import *

app = Flask(__name__)


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def land():
    """Landing page"""
    return "<h1>Landing page<h1>"


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Log in page"""
    email = request.form.get('email')
    password = request.form.get('password')
    return valid_login(email, password)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    """Sign in page"""
    "<h1>Signup page<h1>"
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    # if email is None or username is None or password is None:
    #     return {
    #         "status": 404,
    #         "message": "some values are missing"
    #     }
    details = {
            "username": username,
            "password": password,
            "email": email
    }
    return valid_signup(details)


@app.route("/add_new_tree", methods=['GET', 'POST'])
def add_new_tree():
    """add new person page"""
    tree_name = request.form.get('tree_name')
    token = request.form.get['token']
    return add_tree(tree_name, token)


@app.route("/add_new_person", methods=['GET', 'POST'])
def add_new_person():
    """add new person page"""
    person_id = request.form.get('person_id')
    first_name = request.form.get('first_name')
    last_name = request.form('last_name')
    gender = request.form.get('gender')
    tree_id = request.form.get('tree_id')
    details = {
        "id": person_id,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "tree_id": tree_id
    }
    return add_person(details)


@app.route("/add_new_relation", methods=['GET', 'POST'])
def add_new_relation():
    """add new person page. mother_id and father_id: at least one of the two in mandatory"""
    person_id = request.form.get('person_id')
    mother_id = request.form.get('mother_id')
    father_id = request.form.get('father_id')
    details = {
        "person_id": person_id,
        "mother_id": mother_id,
        "father_id": father_id
    }
    return add_relation(details)


@app.route("/get_table", methods=['GET', 'POST'])
def get_table():
    """get table information"""
    token = request.form['token']
    name = request.form['tree_name']
    return get_tree_information(token, name)


@app.route("/get_tree", methods=['GET', 'POST'])
def get_tree():
    """get tree information"""
    token = request.form['token']
    tree_name = request.form['tree_name']
    return get_tree_information(token, tree_name)


if __name__ == "__main__":
    app.run()
