import mysql.connector


class FamilyTreeDB:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="RRROOOTTT12345",
            database="familytreedb"
        )
        self.cursor = self.db.cursor()

    def create_tables(self):
        # create users table
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), password int)"
        )

        # create person table
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS person(id int PRIMARY KEY, first_name VARCHAR(50),"
            " last_name VARCHAR(50), gender ENUM('M', 'F'))"
        )

        # create person-parents-relation table
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS relation (person_id int PRIMARY KEY,"
            " mother_id int, father_id int)"
        )

        # create tree table ( the name of the the is the last name of the family members )
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS tree (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))"
        )

        # create tree-person-relation table
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS root (tree_id int PRIMARY KEY, person_id int)"
        )

        # create tree-user-relation table
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS connection (tree_id int PRIMARY KEY, user_id int)"
        )

    def add_user(self,name, password):
        self.cursor.execute(
            "INSERT INTO users(name, password) VALUES (%s,%s)", (name, password)
        )
        self.db.commit()

    def add_person(self):
        pass

    def add_parents(self):
        pass

    def add_tree(self):
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

    def get_tree(self):
        pass

    def get_tree_person_relation(self):
        pass

    def get_tree_user_relation(self):
        pass


def main():
    db = FamilyTreeDB()
    db.create_tables()
    db.add_user("Lihi", 123456)
    # db.cursor.execute("SELECT * FROM users")
    # for x in db.cursor:
    #     print(x)


if __name__ == "__main__":
    main()
