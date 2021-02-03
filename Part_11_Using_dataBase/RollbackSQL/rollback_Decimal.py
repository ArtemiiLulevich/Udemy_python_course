from decimal import Decimal


class Account:
    _qd = Decimal('0.00')  # Class constant

    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = Decimal(opening_balance).quantize(Account._qd)
        print("Account created for {}".format(self.name), end='')
        self.show_balance()

    def deposit(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qd)
        if decimal_amount > Account._qd:
            self._balance = self._balance + decimal_amount
            print("{} deposited".format(decimal_amount))
        return self._balance

    def withdraw(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qd)
        if Account._qd < decimal_amount <= self._balance:
            self._balance = self._balance - decimal_amount
            print("{} withdrawn". format(amount))
            return decimal_amount
        else:
            print("The amount must be greater than zero and not more than your account balance")
            return Account._qd

    def show_balance(self):
        print("Balance on account {} is {}".format(self.name, self._balance))


if __name__ == '__main__':
    john = Account('John')
    john.deposit(10.10)
    john.deposit(0.10)
    john.deposit(0.10)
    john.withdraw(0.30)
    john.withdraw(0)
    john.show_balance()
