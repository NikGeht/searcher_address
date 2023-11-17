import os
from handler_db import databaseHandler
import sqlite3
import time
from dadata import Dadata

db = databaseHandler()

def settings():

    os.system('cls')
    print('1. Изменить API ключ')
    print('2. Изменить Secret ключ')
    print('3. Изменить язык ответа')
    print('4. Назад')

    varChoice = int(input("< "))
    
    match varChoice:
        case 1:
            print("Введите новый API ключ:")
            newAPIKey = input("< ")
            try:
                db.changeAPI(newAPIKey)
                
                
                
            except sqlite3.Error:
                print("Возникла ошибка при изменении ключа")
            else:
                print("API ключ успешно изменен")
            
            print("Возврат в главное меню...")
            time.sleep(3)
            settings()

        case 2:

            print("Введите новый secret ключ:")
            newSecretKey = input("< ")
            try:
                db.changeSecretKey(newSecretKey)
                
            except sqlite3.Error:
                print("Возникла ошибка при изменении ключа")
            else:
                print("Secret ключ успешно изменен")
            
            print("Возврат в главное меню...")
            time.sleep(3)
            settings()
        
        case 3:

            print("Выберите язык:")
            print("1. Русский язык")
            print("2. Английский язык")

            varLanguage = int(input("< "))

            if varLanguage == 1:
                db.changeLanguage("ru")
            else:
                db.changeLanguage("en")
            
            print("Возврат в главное меню...")
            time.sleep(3)
            settings()

        case 4:
            main_menu()

def newRequest():

    os.system('cls')
    token = db.getAPI()
    secret = db.getSecret()
    dadata = Dadata(token=token, secret=secret)
    language = db.getLanguage()
    while True:
        print("Введите ваш запрос адреса. Для выхода наберите exit")
        address = input("< ")
        if address == "exit":
            break
        result = dadata.suggest("address", address, language=language, count=20)
        count = 0
        for address in result:
            count += 1
            print(f"{count}. {address['value']}")
        
        print("Выберите подходящий адрес для получения геометок")
        choice = int(input("< "))
        address = result[choice-1]['value']
        result = dadata.suggest("address", address, count=1, language=language)
        
        print(f"Геометки выбранного вами адреса:\nШирота: {result[0]['data']['geo_lat']}\nДолгота: {result[0]['data']['geo_lon']}")




def main_menu():

    os.system('cls')
    print('1. Настройки')
    print('2. Новый запрос')
    print('3. Выход')

    varChoice = int(input("< "))

    match varChoice:
        case 1:
            settings()
        case 2:
            newRequest()
        case 3:
            exit


main_menu()
