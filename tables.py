
class Table:
    def __init__(self):
        self.name = "Table"
        self.attr = []
        self.primary = ""

    def attr_with_types(self):
        return ', '.join(self.attr)

    def only_attr(self):
        return ', '.join(attr.split()[0] for attr in self.attr)

    def num_of_attr(self):
        num = len(self.attr)
        return '%s, ' * (num-1) + '%s'


class TableName:
    ACCOUNT_TABLE = "account"
    PERSON_TABLE = "person"
    RELATION_TABLE = "relation"
    TREE_TABLE = "tree"
    ROOT_TABLE = "root"
    CONNECTION_TABLE = "connection"


class Account(Table):
    def __init__(self):
        self.name = TableName.ACCOUNT_TABLE
        self.attr = [
            "username VARCHAR(50) NOT NULL",
            "password VARCHAR(255) NOT NULL",
            "email VARCHAR(25) NOT NULL",
            "token VARCHAR(64) NOT NULL",
        ]
        self.primary = "PRIMARY KEY (token)"


class Person(Table):
    def __init__(self):
        self.name = TableName.PERSON_TABLE
        self.attr = [
            "id int(11) NOT NULL",
            "first_name VARCHAR(50) NOT NULL",
            "last_name VARCHAR(50)",
            "gender ENUM('M', 'F')"
        ]
        self.primary = "PRIMARY KEY (id)"


class Relation(Table):
    def __init__(self):
        self.name = TableName.RELATION_TABLE
        self.attr = [
            "id int(11) NOT NULL",
            "mother_id int(11)",
            "father_id int(11)"
        ]
        self.primary = "PRIMARY KEY (id)"


class Tree(Table):
    def __init__(self):
        self.name = TableName.TREE_TABLE
        self.attr = [
            "id int(5) NOT NULL AUTO_INCREMENT",
            "name VARCHAR(50) NOT NULL"
        ]
        self.primary = "PRIMARY KEY (id)"


class Root(Table):
    def __init__(self):
        self.name = TableName.ROOT_TABLE
        self.attr = [
            "tree_id int(5) NOT NULL",
            "person_id int(11) NOT NULL"
        ]


class Connection(Table):
    def __init__(self):
        self.name = TableName.CONNECTION_TABLE
        self.attr = [
            "tree_id int(5) NOT NULL",
            "email int(11) NOT NULL"
        ]
