import sqlite3

db = sqlite3.connect("contracts.sqlite")
# db.execute("CREATE TABLE IF NOT EXISTS contracts (name TEXT, phone INTEGER, email TEXT)")
# db.execute("INSERT INTO contracts (name, phone, email) VALUES ('artem', 654378, 'artem@mail.com')")
# db.execute("INSERT INTO contracts VALUES ('vasia', 123456, 'vasia@mail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contracts")

print(cursor.fetchall())

# print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)

cursor.close()
db.commit()
db.close()
