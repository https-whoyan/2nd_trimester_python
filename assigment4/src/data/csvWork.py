from typing import List
from csv import *
from src.schemas.Product import Product


def validateDoProductSchema(dictedProduct: dict) -> Product:
    newProduct: Product = Product()
    for key in dictedProduct.keys():
        value: str = dictedProduct[key]
        if key == 'quantity':
            newProduct.quantity = int(value)
        elif key == 'name': newProduct.name = value
    return newProduct


def readCsv() -> List[Product]:
    allProducts: List[Product] = []
    with open('../csvFiles/product.csv') as f:
        csvReader: DictReader = DictReader(f)
        for row in csvReader:
            allProducts.append(validateDoProductSchema(row))
    return allProducts


def addToCsv(product: Product) -> None:
    with open('../csvFiles/product.csv', 'a') as f:
        csv_writer: writer = writer(f, quoting=QUOTE_NONNUMERIC)
        csv_writer.writerow(product.__dict__.values())


def allNeedProducts(productName: str) -> List[Product]:
    allProducts: List[Product] = readCsv()
    allNeedProducts: List[Product] = []
    for product in allProducts:
        if product.name == productName:
            allNeedProducts.append(product)
    return allNeedProducts