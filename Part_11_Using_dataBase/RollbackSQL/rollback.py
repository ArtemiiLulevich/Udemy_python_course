import sqlite3
import pytz
import datetime

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS "
           "accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL,"
           "account TEXT NOT NULL,"
           "amount INTEGER NOT NULL,"
           "PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS local_transactions AS "
           "SELECT strftime('%Y-%m-%d %H:%M:%f', transactions.time, 'localtime'),"
           "transactions.account, transactions.amount FROM transactions ORDER BY transactions.time")


class Account:

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name, ))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {} ".format(self.name), end='')

        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        time = Account._current_time()
        try:
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO transactions VALUES(?, ?, ?)", (time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
        else:
            db.commit()
            self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print("{:.2f} withdrawn". format(amount / 100))
            return amount / 100
        else:
            print("The amount must be greater than zero and not more than your account balance")
            return 0

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == '__main__':
    john = Account('John')
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account('Terry')
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)

    db.close()
