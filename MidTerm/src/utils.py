import os, json
from typing import List, Dict
from csv import DictReader, QUOTE_NONNUMERIC


def writeJSONFile(curBooks: List[Dict]) -> None:
    os.chdir("../csv_files")
    with open('inventory.json', 'w') as f:
        f.write(json.dumps(curBooks))
    os.chdir("../src")


def validateToUserSchema():
    pass


def validateToBookSchema(row: Dict) -> Dict:
    returnedRow = dict()
    for key in row.keys():
        if key == 'Year Of Publication':
            returnedRow[key] = int(row['Year Of Publication'])
        elif key == 'Price':
            returnedRow[key] = int(row['Price'])
        else:
            returnedRow[key] = row[key]
    return returnedRow


def getBooksListFromJSON():
    jsonCurBooks = []
    with open("../csv_files/inventory.json", 'r') as f:
        jsonCurBooks = json.load(f)
    return jsonCurBooks

def getBooksList() -> List[Dict]:
    os.chdir("../csv_files")
    rowBooksData: List[Dict] = []
    with open('books.csv', 'r') as f:
        scv_reader = DictReader(f)
        for row in scv_reader:
            rowBooksData.append(row)
    booksData: List[Dict] = []
    for row in rowBooksData:
        booksData.append(validateToBookSchema(row))
    os.chdir("../src")
    return booksData


def getUsersList() -> List[Dict]:
    os.chdir("../csv_files")
    usersData: List[Dict] = []
    with open('users.csv', 'r') as f:
        scv_reader = DictReader(f)
        for row in scv_reader:
            usersData.append(row)
    os.chdir("../src")
    return usersData


def getDataOfBook(name: str) -> Dict:
    curBooks: List[Dict] = getBooksList()
    for book in curBooks:
        if book['Name'] == name:
            return book
    return None