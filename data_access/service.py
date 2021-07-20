from database.DB import FamilyTreeDB
from uuid import uuid4

from database.tables import TableName

db = FamilyTreeDB()


def valid_input(*args):
    result = {}
    if list(filter(lambda arg: not arg, args)):
        result = {
            "status": 404,
            "message": "some values are missing"
        }
    return result


def valid_token(token):
    result = {}
    if not db.token_exist(token):
        result = {
            "status": 404,
            "message": "invalid user"
        }
    return result


def valid_login(email_address, password):
    data = ""
    if db.account_exist(email_address, password):
        status = 200
        message = "Login was successfully!"
        rand_token = str(uuid4())
        db.update_token(rand_token, email_address)
        data = db.select_specific_account(email_address, password)
    else:
        status = 404
        message = "Login Failed. Something went wrong, Please try again"
    result = {
        "status": status,
        "message": message,
        "data": data
    }
    return result


def valid_signup(body):
    if db.email_exist(body["email"]):
        status = 400
        message = "Signup Failed. user exist in the system"
    else:
        rand_token = str(uuid4())
        body["rand_token"] = rand_token
        values_to_add = tuple([value for value in body.values()])
        db.add_to_table(TableName.ACCOUNT_TABLE, values_to_add)
        status = 200
        message = "Signup successfully!"
    result = {
        "status": status,
        "message": message
    }
    return result


def add_tree(tree_name, token):
    tree_id = db.get_tree_id(tree_name)
    email = db.get_email(token)
    if db.connection_exist(tree_id, email):
        status = 404
        message = "user already have tree with this name"
    else:
        db.add_to_table(TableName.TREE_TABLE, ("0", tree_name))
        tree_id = db.get_tree_id(tree_name)
        db.add_to_table(TableName.CONNECTION_TABLE, (tree_id, email))
        status = 200
        message = "tree add successfully"
    result = {
        "status": status,
        "message": message,
    }
    return result


def add_person(body):
    if db.tree_not_connect_to_user(body["tree_id"], body["token"]):
        status = 400
        message = "user doesn't have access to tree."
    elif db.person_exist(TableName.PERSON_TABLE, body["id"]):
        status = 400
        message = "Person already exist in the tree."
    else:
        person_body = (body["id"], body["first_name"], body["last_name"], body["gender"])
        root_body = (body["tree_id"], body["id"])
        db.add_to_table(TableName.PERSON_TABLE, person_body)
        db.add_to_table(TableName.ROOT_TABLE, root_body)
        status = 200
        message = "Person added to the person table successfully!"
    result = {
        "status": status,
        "message": message,
    }
    return result


def add_relation(body):
    if db.person_exist(TableName.RELATION_TABLE, body["person_id"]):
        status = 404
        message = "Person relation exist."
    elif not db.person_exist(TableName.PERSON_TABLE, body["person_id"]):
        status = 404
        message = "First add person than add relation"
    else:
        values_to_add = tuple([value for value in body.values()])
        db.add_to_table(TableName.RELATION_TABLE, values_to_add)
        status = 200
        message = "Person relation added to the tree successfully!"
    result = {
        "status": status,
        "message": message,
    }
    return result


def get_tree_information(token, tree_name):
    email = db.get_email(token)
    tree_id = db.get_tree_id(tree_name)
    tree_data = {}
    if not email:
        message = "invalid user"
        status = 404
    elif not tree_id:
        message = "tree name is not valid"
        status = 404
    elif not db.connection_exist(tree_id, email):
        message = "user doesn't have permit to see tree detail"
        status = 400
    else:
        tree_data = db.get_tree_persons(tree_id)
        message = "Success"
        status = 200
    result = {
        "status": status,
        "message": message,
        "data": tree_data
    }
    return result


def main():
    db.create_tables()


if __name__ == "__main__":
    main()
