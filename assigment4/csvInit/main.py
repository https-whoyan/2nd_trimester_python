import csv

rowNames = [
    ['name', 'quantity']
]

with open('../csvFiles/product.csv', 'w') as f:
    csv_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    csv_writer.writerows(rowNames)