import mysql.connector
from database.tables import *
import json


class FamilyTreeDB:
    def __init__(self):
        # singleton function or connection pool
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="RRROOOTTT12345",
            database="familytree"
        )
        self.cursor = self.db.cursor(buffered=True)
        self.account = Account()
        self.person = Person()
        self.relation = Relation()
        self.tree = Tree()
        self.root = Root()
        self.connection = Connection()

    def create_tables(self):
        create_command = "CREATE TABLE IF NOT EXISTS {} ({}, {})"
        create_command_without_primary = "CREATE TABLE IF NOT EXISTS {} ({})"
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
            create_command_without_primary.format(self.root.name, self.root.attr_with_types())
        )

        # create tree-user-relation table
        self.cursor.execute(
            create_command_without_primary.format(self.connection.name, self.connection.attr_with_types())
        )

        self.db.commit()

    def find_table(self, table_name):
        if table_name == self.account.name:
            return self.account
        elif table_name == self.person.name:
            return self.person
        elif table_name == self.relation.name:
            return self.relation
        elif table_name == self.tree.name:
            return self.tree
        elif table_name == self.root.name:
            return self.root
        elif table_name == self.connection.name:
            return self.connection

    def add_to_table(self, table_name, body):
        add_command = "INSERT INTO {} ({}) VALUES ({})"
        table = self.find_table(table_name)
        self.cursor.execute(add_command.format(table.name, table.only_attr(), table.num_of_attr()), body)
        self.db.commit()

    def add_to_tree(self, table_name, body):
        add_command = "INSERT INTO {} ({}) VALUES ({})"
        self.cursor.execute(add_command.format(TableName.TREE_TABLE, "name", "%s"), body)
        self.db.commit()

    def delete_from_table(self, table_name):
        pass

    def get_table_content(self, table_name):
        self.cursor.execute("SELECT * " + table_name)

    def get_col_names(self, table_name):
        print(self.cursor.description)
        self.cursor.execute("SELECT * " + table_name)

    def select_specific_account(self, email_address, password):
        self.cursor.execute("SELECT * FROM " + self.account.name + " WHERE email = %s AND password = %s",
                            (email_address, password))
        col_values = (self.cursor.fetchall())[0]
        col_names = [column[0] for column in self.cursor.description]
        account_data = {}
        for i in range(len(col_names)):
            account_data[str(col_names[i])] = col_values[i]
        return account_data

    def email_exist(self, email_address):
        self.cursor.execute("SELECT * FROM " + self.account.name + " WHERE email = %s", (email_address,))
        account_row_count = self.cursor.rowcount
        if account_row_count >= 1:
            return True
        return False

    def account_exist(self, email_address, password):
        self.cursor.execute("SELECT * FROM " + self.account.name + " WHERE email = %s AND password = %s",
                            (email_address, password))
        account_row_count = self.cursor.rowcount
        if account_row_count >= 1:
            return True
        return False

    def person_exist(self, table_name, person_id):
        self.cursor.execute("SELECT * FROM " + table_name + " WHERE id = %s", (person_id,))
        person_row_count = self.cursor.rowcount
        if person_row_count >= 1:
            return True
        return False

    def connection_exist(self, tree_id, email):
        self.cursor.execute("SELECT * FROM connection WHERE tree_id = %s AND email = %s", (tree_id, email))
        connection_row_count = self.cursor.rowcount
        if connection_row_count > 0:
            return True
        return False

    def update_token(self, token, email_address):
        self.cursor.execute("UPDATE " + self.account.name + " SET token = %s WHERE email = %s", (token, email_address))
        self.db.commit()

    def token_exist(self, token):
        self.cursor.execute("SELECT * FROM account WHERE token = %s", (token,))
        token_row_count = self.cursor.rowcount
        if token_row_count == 1:
            return True
        return False

    def tree_exist(self, tree_name):
        self.cursor.execute("SELECT * FROM tree WHERE name = %s", (tree_name,))
        tree_row_count = self.cursor.rowcount
        if tree_row_count >= 1:
            return True
        return False

    def get_email(self, token):
        self.cursor.execute("SELECT email FROM account WHERE token = %s", (token,))
        return self.cursor.fetchone()

    def get_tree_id(self, tree_name):
        self.cursor.execute("SELECT id FROM tree WHERE name = %s", (tree_name,))
        tree_id = self.cursor.fetchone()
        if tree_id:
            return tree_id[0]
        return False

    def tree_not_connect_to_user(self, tree_id, token):
        self.cursor.execute("SELECT tree_id FROM account,connection where account.token= %s"
                            " AND account.email=connection.email AND connection.tree_id= %s", (token, tree_id))
        tree_row_count = self.cursor.rowcount
        if tree_row_count < 1:
            return True
        return False

    def get_tree_persons(self, tree_id):
        self.cursor.execute("SELECT person_id FROM root WHERE tree_id= %s", (tree_id,))
        persons_id = self.cursor.fetchall()
        persons_in_tree = []
        for person_id in persons_id:
            self.cursor.execute("SELECT * FROM person WHERE id= %s", (person_id[0],))
            person_data = self.cursor.fetchone()
            persons_in_tree.append(person_data)
        return persons_in_tree
