import sqlite3

db = sqlite3.connect("contracts.sqlite")

new_email = "anotherupdate@update.com"
phone = input("Enter a phone number: ")

update_sql = "UPDATE contracts SET email = ? " \
             "WHERE contracts.phone = ?"
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

for row in db.execute("SELECT * FROM contracts"):
    print(row)

db.close()
