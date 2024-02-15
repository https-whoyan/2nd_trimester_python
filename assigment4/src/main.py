from data.csvWork import addToCsv, allNeedProducts
from schemas.Product import Product
from schemas.CustomException import CustomException

from typing import List

print("Добро пожаловать! Это сервис по поиску и добавлению товаров.")

while True:
    typeOfAction: int
    print("Пожалуйста, выберите желаемое действие: ")
    print("1: Найти нужный товар (товар с нужным именем)")
    print("2: Добавить свой товар.")
    print("3: Выйти из системы.")
    print("Ваше действие: ", end="")
    try:
        typeOfAction: int = int(input().split()[0])
        if typeOfAction < 1 or typeOfAction > 3: raise Exception
    except Exception:
        newException: CustomException = CustomException("Действие должно быть целым числом от 1 до 3")
        newException.printErr()
        print()
        continue
    if typeOfAction == 1:
        productName: str = input("Введите наименивание товара: ")
        needProducts: List[Product] = allNeedProducts(productName)
        if len(needProducts) == 0:
            print(f"Подходящих товаров с наименованием {productName} не найдено.")
        else:
            print("Найденные следующие товары:")
            for id, uniqueProdict in enumerate(needProducts):
                print(f"id: {id + 1}", end="")
                uniqueProdictDict: dict = uniqueProdict.__dict__
                for key in uniqueProdictDict.keys():
                    print(f", {key}: {uniqueProdictDict[key]}", end="")
                print()
            print()
        print()
    elif typeOfAction == 2:
        newProduct: Product = Product()
        print("Введите наименивание добавляеного товара: ", end="")
        newProductName: str = input()
        newProductQuantity: int
        print("Введите количество нового добавляемного товара: ", end="")
        try:
            newProductQuantity: int = int(input().split()[0])
        except Exception:
            newException: CustomException = CustomException("Число нужно.")
            newException.printErr()
            print()
            continue
        newProduct.name = newProductName
        newProduct.quantity = newProductQuantity
        addToCsv(newProduct)
        print("Товар добавлен.")
        print()
    elif typeOfAction == 3: break

print()
print("Спасибо за использование сервиса!")
