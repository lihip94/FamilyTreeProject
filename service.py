from DB import FamilyTreeDB
from uuid import uuid4
import json

db = FamilyTreeDB()


def valid_login(email_address, password):
    # check in users table (select)
    data = {}
    if email_address is None or password is None:
        status = 404,
        message = "some values are missing"
    elif len(db.select_specific_account(email_address, password)) == 1:
        status = 200
        message = "Login was successfully!"
        rand_token = uuid4().int
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
    return json.dumps(result)


def valid_signup(body):
    table_name = "account"
    if body["email"] is None or body["username"] is None or body["password"] is None:
        status = 404,
        message = "some values are missing"
    elif db.account_exist(body["email"]):
        status = 400
        message = "Signup Failed. user exist in the system"
    else:
        rand_token = uuid4().int
        body["rand_token"] = rand_token
        values_to_add = ()
        for value in body.values():
            values_to_add += (value,)
        db.add_to_table(table_name, values_to_add)
        status = 200
        message = "Signup successfully!"
    result = {
        "status": status,
        "message": message,
    }
    return result


def add_tree(tree_name, token):
    if not db.token_exist(token):
        message = "invalid user"
        status = 404
    else:
        db.add_to_table("tree", tree_name)
        message = "tree add successfully"
        status = 200
    result = {
        "status": status,
        "message": message,
    }
    return result


def add_person(body):
    person_table = "person"
    if body["id"] is None or body["first_name"] is None or body["last_name"] is None or body["gender"] is None:
        status = 404,
        message = "some values are missing"
    elif db.person_exist(person_table, body["id"]):
        status = 400
        message = "Person already exist in the tree."
    else:
        person_body = (body["id"], body["first_name"], body["last_name"], body["gender"])
        root_body = (body["tree_id"], body["id"])
        db.add_to_table(person_table, person_body)
        db.add_to_table("root", root_body)
        status = 200
        message = "Person added to the tree successfully!"
    result = {
        "status": status,
        "message": message,
    }
    return result


def add_relation(body):
    table_name = "relation"
    if body["person_id"] is None or (body["mother_id"] is None or body["father_id"] is None):
        status = 400
        message = "some values are missing"
    elif db.person_exist(table_name, body["person_id"]):
        status = 404
        message = "Person relation exist."
    else:
        db.add_to_table(table_name, body)
        status = 200
        message = "Person added to the tree successfully!"
    result = {
        "status": status,
        "message": message,
    }
    return result


def get_tree_information(token, tree_name):
    if not db.token_exist(token):
        message = "invalid user"
        status = 404
    email = db.get_email(token)
    tree_id = db.get_tree_id(tree_name)
    if len(tree_id) <= 0:
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
    # details = {
    #         "username": "user1",
    #         "password": 123456,
    #         "email": "user1@gmail.com"
    # }
    # print(valid_signup(details))
    # print(valid_login("user1@gmail.com", 123456))
    # print(valid_login("user1@gmail.com", 1236))
    # body = {
    #     "id": 203043,
    #     "first_name": "Chen",
    #     "last_name": "Yosi",
    #     "gender": "F",
    #     "tree_id": 1
    # }
    # print(add_person(body))
    # db.cursor.execute("SELECT * FROM account")
    # for x in db.cursor:
    #     print(x)


if __name__ == "__main__":
    main()
