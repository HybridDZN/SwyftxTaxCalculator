import csv

with open('data/transactions.csv', newline='') as transactions:
    transactionReader = csv.reader(transactions, delimiter = ' ', quotechar = '|')
    for row in transactionReader:
        print((', '.join(row)))