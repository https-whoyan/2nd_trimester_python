from auth import Auth
from utils import (
    getBooksList,
    writeJSONFile,
    getBooksListFromJSON,
    getDataOfBook
)
from typing import List, Dict




if __name__ == '__main__':
    auth = Auth()
    # Логинюсь
    # Класс по приколу написал
    try:
        username, password = input("Введите данные: ").split()
    except Exception as e:
        print(e.__class__.__name__)
        exit(0)
    isLogined: bool = auth.login(username, password)
    if isLogined: print("Вы залогинены")
    else:
        print("Нет, ваших данных нету в файле users.csv")
        exit(0)
    # Перезасисываю по заданию книги из csv в json, перед этим их получив
    curBooks: List[Dict] = getBooksList()
    writeJSONFile(curBooks)
    # Получаю книги уже из JSON файла (мне же делать нечего что бы это
    # в ассайманте писать, меня же попросили))0)
    jsonCurBooks = getBooksListFromJSON()
    # Вывожу
    print("Ознакомьтесь с каталогом книг:")
    for bookData in jsonCurBooks:
        for key in bookData.keys():
            print(key, ": ", bookData[key])
        print()
    try:
        nameOfBook: str = input("Введите название книги: ")
        bookData: Dict = getDataOfBook(nameOfBook)
        if bookData == None:
            print("Книги с таким именем не существует")
            exit(0)
        else:
            print(f"Информация о книге с именем {nameOfBook}: {bookData}")
        print("Всего доброго!")
    except Exception as e:
        print(e.__class__.__name__)
        exit(0)