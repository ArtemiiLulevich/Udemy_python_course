import sqlite3

db = sqlite3.connect("contracts.sqlite")


for row in db.execute("SELECT * FROM contracts"):
    print(row)
print('-' * 20)

symbol = "123456;drop table userData"

for row in db.execute("SELECT name, email FROM contracts WHERE phone = %s" % symbol):
    print(row)

print("=" * 20)

t = ('123456 union select * from usersData--', )
for row in db.execute('SELECT name, email FROM contracts where phone = ?', t):
    print(row)

for row in db.execute('SELECT * FROM userData'):
    print(row)

db.close()
