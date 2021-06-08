import mysql.connector

FAMILY_TREE_DB = "familytreedb"
USERS_TABLE = "users"
PERSON_TABLE = "person"
RELATION_TABLE = "relation"
TREE_TABLE = "tree"
ROOT_TABLE = "root"
CONNECTION_TABLE = "connection"


class Table:
    def __init__(self, name, attributes):
        self.name = USERS_TABLE
        self.attr_list = attributes

    def attr_to_string(self):
        return ', '.join(self.attr_list)


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
        self.users = Table(USERS_TABLE, ["id int PRIMARY KEY AUTO_INCREMENT","name VARCHAR(50)", "password int"])
        self.person = Table()
        self.relation = Table()
        self.tree = Table()
        self.connection = Table()

    # temp - not in use
    def create_table(self):
        create_command = "CREATE TABLE IF NOT EXISTS {table_name} ({params})"
        return self.cursor.execute(create_command.format(self.users.name, self.users.attr_to_string()))

    def create_tables(self):
        create_command = "CREATE TABLE IF NOT EXISTS {table_name} ({params})"
        # create users table
        self.cursor.execute(
            create_command.format(USERS_TABLE,
                                  "id int PRIMARY KEY AUTO_INCREMENT, "
                                  "name VARCHAR(50), "
                                  "password int")
        )

        # create person table
        self.cursor.execute(
            create_command.format(PERSON_TABLE,
                                  "id int PRIMARY KEY, "
                                  "first_name VARCHAR(50), "
                                  "last_name VARCHAR(50), "
                                  "gender ENUM('M', 'F')")
        )

        # create person-parents-relation table
        self.cursor.execute(
            create_command.format(RELATION_TABLE,
                                  "person_id int PRIMARY KEY, "
                                  "mother_id int,"
                                  "father_id int")
        )

        # create tree table ( the name of the the is the last name of the family members )
        self.cursor.execute(
            create_command.format(TREE_TABLE,
                                  "id int PRIMARY KEY AUTO_INCREMENT, "
                                  "name VARCHAR(50)")
        )

        # create tree-person-relation table
        self.cursor.execute(
            create_command.format(ROOT_TABLE,
                                  "tree_id int PRIMARY KEY,"
                                  " person_id int")
        )

        # create tree-user-relation table
        self.cursor.execute(
            create_command.format(CONNECTION_TABLE,
                                  "tree_id int PRIMARY KEY, "
                                  "user_id int")
        )

    def add_user(self, name, password):
        self.cursor.execute(
            "INSERT INTO " + USERS_TABLE + "(name, password) VALUES (%s,%s)", (name, password)
        )
        self.db.commit()

    def add_person(self, person_id, first_name, last_name, gender):
        self.cursor.execute(
            "INSERT INTO " + PERSON_TABLE + "(id, first_name, last_name, gender) VALUES (%s,%s,%s,%s)",
            (person_id, first_name, last_name, gender)
        )
        self.db.commit()

    def add_parents(self, person_id, mother_id, father_id):
        self.cursor.execute(
            "INSERT INTO " + RELATION_TABLE + "(person_id, mother_id, father_id) VALUES (%s,%s,%s)",
            (person_id, mother_id, father_id)
        )
        self.db.commit()

    def add_tree(self, tree_id, name):
        self.cursor.execute(
            "INSERT INTO " + RELATION_TABLE + "(id, name) VALUES (%s,%s)",
            (tree_id, name)
        )
        self.db.commit()

    def create_tree_person_relation(self, tree_id, person_id):
        self.cursor.execute(
            "INSERT INTO " + ROOT_TABLE + "(tree_id, person_id) VALUES (%s,%s)",
            (tree_id, person_id)
        )
        self.db.commit()

    def create_tree_user_relation(self, tree_id, user_id):
        self.cursor.execute(
            "INSERT INTO " + CONNECTION_TABLE + "(tree_id, user_id) VALUES (%s,%s)",
            (tree_id, user_id)
        )
        self.db.commit()

    def delete_user(self):
        pass

    def delete_person(self):
        pass

    def delete_tree(self):
        pass

    def remove_tree_person_relation(self):
        pass

    def remove_tree_user_relation(self):
        pass

    def get_user(self):
        pass

    def get_person(self):
        pass

    def get_tree(self, name, user):
        pass

    def get_tree_person_relation(self):
        pass

    def get_tree_user_relation(self):
        pass


def main():
    db = FamilyTreeDB()
    db.create_tables()
    db.add_user("Liat", 2345)
    # db.cursor.execute("SELECT * FROM users")
    # for x in db.cursor:
    #     print(x)


if __name__ == "__main__":
    main()
