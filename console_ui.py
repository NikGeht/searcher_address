import os
import sqlite3
import sys
import time

import dadata

from handler_db import DatabaseHandler

db = DatabaseHandler()


def settings():
    """The menu with settings for users,
    contain basic settings that need to check for correct work with dadata"""
    os.system("cls")

    print("1. Change API key")
    print("2. Change Secret key")
    print("3. Change language")
    print("4. Back")

    var_choice: int = int(input("< "))

    match var_choice:
        case 1:
            print("Enter new API key:")
            new_api_key: str = input("< ")
            try:
                db.change_api(new_api_key)

            except sqlite3.Error:
                print("Error: couldn't change API key")
            else:
                print("API key was successfully changed")

            print("Back to the settings...")
            time.sleep(3)
            settings()

        case 2:
            print("Enter new Secret key:")
            new_secret_key: str = input("< ")
            try:
                db.change_secret_key(new_secret_key)

            except sqlite3.Error:
                print("Error: couldn't change Secret key")
            else:
                print("Secret key was successfully changed")

            print("Back to the settings...")
            time.sleep(3)
            settings()

        case 3:
            print("Enter language:")
            print("1. Russian")
            print("2. English")

            var_language = int(input("< "))

            if var_language == 1:
                db.change_language("ru")
            else:
                db.change_language("en")

            print("Back to the settings...")
            time.sleep(3)
            settings()

        case 4:
            main_menu()


def new_request() -> None:
    """The menu which needed for taking request address from users to dadata"""
    os.system("cls")
    api_key: str = db.get_api()
    secret_key: str = db.get_secret()
    data_client = dadata.Dadata(token=api_key, secret=secret_key)
    language: str = db.get_language()
    while True:
        print("Enter your request. Enter exit for quit")
        search_address = input("< ")
        if search_address == "exit":
            break
        search_result = data_client.suggest(
            "address", search_address, language=language, count=20
        )
        for count, response_address in enumerate(search_result):
            print(f"{count}. {response_address['value']}")

        print("Select the appropriate address to receive the geotags")
        choice_address: int = int(input("< "))
        final_address: str = search_result[choice_address-1]["value"]

        result: list[dict] = data_client.suggest(
            "address", final_address, count=1, language=language
        )

        print(
            f"""The geometries of the address you selected:\n
            Latitude: {result[0]['data']['geo_lat']}\n
            Longitude: {result[0]['data']['geo_lon']}"""
        )


def main_menu() -> None:
    """The main menu with 3 ability:
    1. Go to settings
    2. Send a new request
    3. Quit the program
    """
    os.system("cls")
    print("1. Settings")
    print("2. New request")
    print("3. Exit")

    var_choice: int = int(input("< "))

    match var_choice:
        case 1:
            settings()
        case 2:
            new_request()
        case 3:
            sys.exit()


main_menu()
