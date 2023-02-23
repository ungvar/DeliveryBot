import sqlite3

class Database:

#   Initialization
    def __init__(self,database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

#   Checking if a user exists in the system
    def check_id(self,user_id):
        with self.connection:
            return self.cursor.execute("""SELECT user_id from users where user_id = ?""", (user_id,)).fetchone()

#   Registering user if not exist
    def register(self,user_id,first_name,last_name):
        with self.connection:
            self.cursor.execute("""insert into users (user_id, first_name, last_name) values (?,?,?)""",(user_id, first_name, last_name))
            self.connection.commit()

#   Choosing the name of the soup and its price
    def choise_soup(self):
        with self.connection:
            return self.cursor.execute("""select soup_name,price from soups where availability = 1""").fetchall()

#   Choosing the name of the dish and its price
    def choise_main_dish(self):
        with self.connection:
            return self.cursor.execute("""select dish_name,price from main_dish where availability = 1""").fetchall()

#   Choosing the name of the salad and its price
    def choise_salad(self):
        with self.connection:
            return self.cursor.execute("""select salad_name,price from salads where availability = 1""").fetchall()

#   Choosing the name of the drink and its price
    def choise_drink(self):
        with self.connection:
            return self.cursor.execute("""select drink_name,price from drinks where availability = 1""").fetchall()

#
#
#
