import os
import csv

os.chdir("../csv_files")

usersData = [
    ['Name', 'Password'],
    ['Yan', 'testPass'],
    ['NeYan', '123123']
]

with open('users.csv', 'w') as f:
    csv_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    csv_writer.writerows(usersData)

booksData = [
    ['Name', 'Author', 'Year Of Publication', 'Price'],
    ['CalcalusBook', 'Syndar A.', '2009', '2200'],
    ['Bibliya', 'God', '0', '1000'],
    ['Harry Potter 1', 'Some author....', '2003', '8000']
]


with open('books.csv', 'w') as f:
    csv_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    csv_writer.writerows(booksData)