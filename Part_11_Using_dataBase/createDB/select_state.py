import sqlite3

db = sqlite3.connect("contracts.sqlite")

new_email = "anotherupdate@update.com"
phone = 123456

update_sql = "UPDATE contracts SET email = 'update@update.com' " \
             "WHERE contracts.phone = 123456"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

for row in db.execute("SELECT * FROM contracts"):
    print(row)

db.close()
