import mysql.connector
from tables import *

FAMILY_TREE_DB = "familytreedb"


class FamilyTreeDB:
    def __init__(self):
        # singleton function or connection pool
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="RRROOOTTT12345",
            database="familytreedb"
        )
        self.cursor = self.db.cursor()
        self.account = Account()
        self.person = Person()
        self.relation = Relation()
        self.tree = Tree()
        self.root = Root()
        self.connection = Connection()

    def create_tables(self):
        create_command = "CREATE TABLE IF NOT EXISTS {} ({}, {})"
        # create users table
        self.cursor.execute(
            create_command.format(self.account.name, self.account.attr_with_types(), self.account.primary)
        )

        # create person table
        self.cursor.execute(
            create_command.format(self.person.name, self.person.attr_with_types(), self.person.primary)
        )

        # create person-parents-relation table
        self.cursor.execute(
            create_command.format(self.relation.name, self.relation.attr_with_types(), self.relation.primary)
        )

        # create tree table ( the name of the the is the last name of the family members )
        self.cursor.execute(
            create_command.format(self.tree.name, self.tree.attr_with_types(), self.tree.primary)
        )

        # create tree-person-relation table
        self.cursor.execute(
            create_command.format(self.root.name, self.root.attr_with_types(), self.root.primary)
        )

        # create tree-user-relation table
        self.cursor.execute(
            create_command.format(self.connection.name, self.connection.attr_with_types(), self.connection.primary)
        )

        self.db.commit()

    def find_table(self, table_name):
        if table_name == self.users:
            return self.users
        elif table_name == self.person:
            return self.person
        elif table_name == self.relation:
            return self.relation
        elif table_name == self.tree:
            return self.tree
        elif table_name == self.root:
            return self.root
        elif table_name == self.connection:
            return self.connection

    def add_to_table(self, table_name, body):
        add_command = "INSERT INTO {} ({}) VALUES ({})"
        table = self.find_table(table_name)
        self.cursor.execute(add_command.format(table.name, table.attr_with_types(), table.num_of_attr()), body)
        self.db.commit()

    def delete_from_table(self, table_name):
        pass

    def get_table_content(self, table_name):
        self.cursor.execute("SELECT * " + table_name)

    def select_specific_from_table(self, table_name):
        self.cursor.execute("select username from user where username=%s", a.username)


def main():
    db = FamilyTreeDB()
    db.create_tables()
    #db.add_user("Liat", 2345)
    # db.cursor.execute("SELECT * FROM users")
    # for x in db.cursor:
    #     print(x)


if __name__ == "__main__":
    main()
