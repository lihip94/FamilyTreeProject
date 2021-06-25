from DB import FamilyTreeDB
from uuid import uuid4
import json

db = FamilyTreeDB()


def valid_login(email_address, password):
    # check in users table (select)
    data = {}
    account = db.select_specific_account(email_address, password)
    if len(account) == 1:
        status = 200
        message = "Login was successfully!"
        data = account
    else:
        status = 404
        message = "Login Failed. Something went wrong, Please try again"
    # create token (random/ hash table/ md 5)
    rand_token = uuid4()
    # save token in DB
    db.update_token(rand_token, email_address)
    result = {
        "status": status,
        "message": message,
        "data": data,
        "token": rand_token
    }
    return json.dumps(result)


def valid_signup(body):
    table_name = "account"
    if db.account_exist(body["email"], body["username"]):
        status = 404
        message = "Signup Failed. user exist in the system"
    else:
        db.add_to_table(table_name, body)
        status = 200
        message = "Signup successfully!"
    result = {
        "status": status,
        "message": message,
    }
    return result


def add_person(body):
    table_name = "person"
    if db.person_exist(body["id"]):
        status = 404
        message = "Person already exist in the tree"
    else:
        db.add_to_table(table_name, body)
        status = 200
        message = "Person added to the tree successfully!"
    result = {
        "status": status,
        "message": message,
    }
    return result


def add_relation(details):
    pass


def get_tree_information(token, name):
    # check token and get user_id
    # send user and name to get_tree
    result_from_db = FamilyTreeDB.get_table_content(name)
    # convert the result that will route
    return result_from_db


def get_table_information(token, name):
    pass
