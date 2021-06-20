from DB import FamilyTreeDB
from uuid import uuid4
import json


def login(email_address, password):
    # check in users table (select)
    data = {}
    account = FamilyTreeDB.select_specific_account(email_address, password)
    if len(account) == 1:
        status = "Passed"
        message = "Login was successfully!"
        data = account
    else:
        status = "Failed"
        message = "Login Failed. Something went wrong, Please try again"
    # create token (random/ hash table/ md 5)
    rand_token = uuid4()
    # save token in DB
    FamilyTreeDB.update_token(rand_token, email_address)
    result = {
        "status": status,
        "message": message,
        "data": data,
        "token": rand_token
    }
    return json.dumps(result)


def get_tree_information(token, name):
    # check token and get user_id
    # send user and name to get_tree
    result_from_db = FamilyTreeDB.get_table_content(name)
    # convert the result that will route
    return result_from_db


def get_table_information(token, name):
    pass


def add_person(details):
    pass


def signup(body):
    pass


def is_login(username):
    pass
