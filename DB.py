import mysql.connector

USERS_TABLE = "users"
PERSON_TABLE = "person"
RELATION_TABLE = "relation"
TREE_TABLE = "tree"
ROOT_TABLE = "root"
CONNECTION_TABLE = "connection"


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

    def add_person(self):
        pass

    def add_parents(self):
        pass

    def add_tree(self, name):
        pass

    def create_tree_person_relation(self):
        pass

    def create_tree_user_relation(self):
        pass

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
