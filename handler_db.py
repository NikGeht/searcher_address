import sqlite3


class DatabaseHandler:
    def __init__(self, url_to_db: str = "main_database.db"):
        self.url_to_db: str = url_to_db
        try:
            self.connection = sqlite3.connect(url_to_db)
        except sqlite3.Error:
            print("Не удалось связаться с базой данных")

        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Creating db, table
        try:
            self.cursor.execute(
                """create table if not exists config(
                        id integer primary key,
                        api_key text default "",
                        secret_key text default "",
                        language text check( language in ("en", "ru")) not null default ru
            )"""
            )
        except sqlite3.Error as e:
            print(e)

    def change_api(self, new_api_key: str):
        try:
            self.cursor.execute(
                f'update config set api_key = "{new_api_key}" where id=1'
            )
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(e)

    def change_secret_key(self, new_secret_key: str):
        try:
            self.cursor.execute(
                f'update config set secret_key = "{new_secret_key}" where id=1'
            )
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(e)

    def change_language(self, new_language: str):
        try:
            self.cursor.execute(
                f'update config set language = "{new_language}" where id=1'
            )
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(e)

    def get_api(self) -> str:
        try:
            api_key = self.cursor.execute(
                "select api_key from config where id=1"
            ).fetchone()
            return str(api_key[0])
        except sqlite3.Error as e:
            print(e)

    def get_secret(self) -> str | None:
        try:
            secret_key = self.cursor.execute(
                "select secret_key from config where id=1"
            ).fetchone()
            return secret_key[0]
        except sqlite3.Error as e:
            print(e)
            return None

    def get_language(self) -> str | None:
        try:
            language = self.cursor.execute(
                "select language from config where id=1"
            ).fetchone()
            return language[0]
        except sqlite3.Error as e:
            print(e)
            return None
