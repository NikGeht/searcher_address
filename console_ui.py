import os
from handler_db import databaseHandler
import sqlite3
import time

db = databaseHandler()

def settings():

    os.system('clear')
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

    os.system('clear')



def main_menu():

    os.system('clear')
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
