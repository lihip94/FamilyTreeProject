from flask import Flask, render_template, url_for, request, redirect

from service import *

app = Flask(__name__)


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def land():
    """Landing page"""
    pass


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Log in page"""
    email = request.form.get('email')
    password = request.form.get('password')
    validation = valid_input(email, password)
    if validation:
        return validation
    return valid_login(email, password)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    """Sign in page"""
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    validation = valid_input(email, username, password)
    if validation:
        return validation
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
    token = request.form.get('token')
    validation = valid_input(tree_name, token)
    if validation:
        return validation
    token_validation = valid_token(token)
    if token_validation:
        return token_validation
    return add_tree(tree_name, token)


@app.route("/add_new_person", methods=['GET', 'POST'])
def add_new_person():
    """add new person page"""
    person_id = request.form.get('person_id')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    gender = request.form.get('gender')
    tree_id = request.form.get('tree_id')
    token = request.form.get('token')
    validation = valid_input(person_id, first_name, last_name, gender, tree_id, token)
    if validation:
        return validation
    token_validation = valid_token(token)
    if token_validation:
        return token_validation
    details = {
        "id": person_id,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "tree_id": tree_id,
        "token": token
    }
    return add_person(details)


@app.route("/add_new_relation", methods=['GET', 'POST'])
def add_new_relation():
    """add new person page. mother_id and father_id: at least one of the two in mandatory"""
    person_id = request.form.get('person_id')
    mother_id = request.form.get('mother_id')
    father_id = request.form.get('father_id')
    token = request.form.get('token')
    validation = valid_input(person_id, mother_id, father_id, token)
    if validation:
        return validation
    token_validation = valid_token(token)
    if token_validation:
        return token_validation
    details = {
        "person_id": person_id,
        "mother_id": mother_id,
        "father_id": father_id
    }
    return add_relation(details)


@app.route("/get_tree_table", methods=['GET', 'POST'])
def get_table():
    """get table information"""
    token = request.form['token']
    name = request.form['tree_name']
    validation = valid_input(token, name)
    if validation:
        return validation
    token_validation = valid_token(token)
    if token_validation:
        return token_validation
    return get_tree_information(token, name)


if __name__ == "__main__":
    app.run()
