import sqlite3

class databaseHandler:

    def __init__(self, url_to_db='main_database.db'):

        self.url_to_db = url_to_db
        try:
            self.connection = sqlite3.connect(url_to_db)
        except sqlite3.Error as e:
            print("Не удалось связаться с базой данных")
        
        self.cursor = self.connection.cursor()
        self.create_table()
        

    def create_table(self):

        ## Creating db, table ##
        try:
            self.cursor.execute('''create table if not exists config(
                        id integer primary key,
                        api_key text default "",
                        secret_key text default "",
                        language text check( language in ("en", "ru")) not null default ru
            )''')
        except sqlite3.Error as e:
            print(e)

    def changeAPI(self, new_api_key):
        try:
            self.cursor.execute(f'update config set api_key = "{new_api_key}" where id=1')
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(e)
    
    def changeSecretKey(self, new_secret_key):
        try:
            self.cursor.execute(f'update config set secret_key = "{new_secret_key}" where id=1')
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(e)

    def changeLanguage(self, new_language):
        try:
            self.cursor.execute(f'update config set language = "{new_language}" where id=1')
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(e)



