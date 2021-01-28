import sqlite3

db = sqlite3.connect('contracts.sqlite')

select_statement = 'SELECT * FROM contracts WHERE name LIKE ?'

name = input('Enter a name: ')

for row in db.execute(select_statement, (name, )):
    print(row)

db.close()
