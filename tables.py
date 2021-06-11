
class Table:
    def __init__(self):
        self.name = "Table"
        self.attr = []

    def attr_to_string(self):
        return ', '.join(self.attr)

    def num_of_attr(self):
        num = len(self.attr)
        return '%s' * num


class TableName:
    USERS_TABLE = "users"
    PERSON_TABLE = "person"
    RELATION_TABLE = "relation"
    TREE_TABLE = "tree"
    ROOT_TABLE = "root"
    CONNECTION_TABLE = "connection"


class Users(Table):
    def __init__(self):
        self.name = TableName.USERS_TABLE
        self.attr = ["id int PRIMARY KEY AUTO_INCREMENT", "name VARCHAR(50)", "password int"]


class Person(Table):
    def __init__(self):
        self.name = TableName.PERSON_TABLE
        self.attr = ["id int PRIMARY KEY", "first_name VARCHAR(50)", "last_name VARCHAR(50)", "gender ENUM('M', 'F')"]


class Relation(Table):
    def __init__(self):
        self.name = TableName.RELATION_TABLE
        self.attr = ["person_id int PRIMARY KEY", "mother_id int", "father_id int"]


class Tree(Table):
    def __init__(self):
        self.name = TableName.TREE_TABLE
        self.attr = ["id int PRIMARY KEY AUTO_INCREMENT", "name VARCHAR(50)"]


class Root(Table):
    def __init__(self):
        self.name = TableName.ROOT_TABLE
        self.attr = ["tree_id int PRIMARY KEY", "person_id int"]


class Connection(Table):
    def __init__(self):
        self.name = TableName.CONNECTION_TABLE
        self.attr = ["tree_id int PRIMARY KEY", "user_id int"]
