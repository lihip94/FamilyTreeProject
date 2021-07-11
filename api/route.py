from flask import request, Blueprint,jsonify

from data_access.service import *

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home", methods=['GET', 'POST'])
def land():
    """Landing page"""
    return '<h1>"hello world"</h1>'


@main.route("/login", methods=['GET', 'POST'])
def login():
    """Log in page"""
    account_data = request.get_json()
    email = account_data['email']
    password = account_data['password']
    validation = valid_input(email, password)
    if validation:
        return jsonify(validation)
    return jsonify(valid_login(email, password))


@main.route("/signup", methods=['GET', 'POST'])
def signup():
    """Sign up page"""
    account_data = request.get_json()
    email = account_data['email']
    username = account_data['username']
    password = account_data['password']
    validation = valid_input(email, username, password)
    if validation:
        return jsonify(validation)
    details = {
            "username": username,
            "password": password,
            "email": email
    }
    return jsonify(valid_signup(details))


@main.route("/add_new_tree", methods=['GET', 'POST'])
def add_new_tree():
    """add new person page"""
    tree_data = request.get_json()
    tree_name = tree_data['tree_name']
    token = tree_data['token']
    validation = valid_input(tree_name, token)
    if validation:
        return jsonify(validation)
    token_validation = valid_token(token)
    if token_validation:
        return jsonify(token_validation)
    return jsonify(add_tree(tree_name, token))


@main.route("/add_new_person", methods=['GET', 'POST'])
def add_new_person():
    """add new person page"""
    person_data = request.get_json()
    person_id = person_data['person_id']
    first_name = person_data['first_name']
    last_name = person_data['last_name']
    gender = person_data['gender']
    tree_id = person_data['tree_id']
    token = person_data['token']
    validation = valid_input(person_id, first_name, last_name, gender, tree_id, token)
    if validation:
        return jsonify(validation)
    token_validation = valid_token(token)
    if token_validation:
        return jsonify(token_validation)
    details = {
        "id": person_id,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "tree_id": tree_id,
        "token": token
    }
    return jsonify(add_person(details))


@main.route("/add_new_relation", methods=['GET', 'POST'])
def add_new_relation():
    """add new person page. mother_id and father_id: at least one of the two exist"""
    relation_data = request.get_json()
    person_id = relation_data['person_id']
    mother_id = relation_data['mother_id']
    father_id = relation_data['father_id']
    token = relation_data['token']
    validation = valid_input(person_id, mother_id, father_id, token)
    if validation:
        return jsonify(validation)
    token_validation = valid_token(token)
    if token_validation:
        return jsonify(token_validation)
    details = {
        "person_id": person_id,
        "mother_id": mother_id,
        "father_id": father_id
    }
    return jsonify(add_relation(details))


@main.route("/get_tree_table", methods=['GET', 'POST'])
def get_table():
    """get table information"""
    tree_data = request.get_json()
    token = tree_data['token']
    name = tree_data['tree_name']
    validation = valid_input(token, name)
    if validation:
        return jsonify(validation)
    token_validation = valid_token(token)
    if token_validation:
        return jsonify(token_validation)
    return jsonify(get_tree_information(token, name))