import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    """My way of fix"""
    # def __init__(self, name, amount):
    #     self.name = name
    #     self.balance = 0
    #     self.transaction_list = []
    #     self.deposit(amount)
    #     print("Account created for " + self.name)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print('Not enough money.')
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print('{:6} {} on {} (local time was {})'.format(amount,
                                                             tran_type,
                                                             date,
                                                             date.astimezone()))


if __name__ == '__main__':
    tim = Account('Tim', 0)
    tim.show_balance()

    tim.deposit(5000)
    tim.withdraw(1000)
    tim.withdraw(6999)
    tim.show_transactions()

    ali = Account('Ali', 800)
    ali.__balance = 200
    ali.deposit(100)
    ali.withdraw(200)
    ali.show_transactions()
    ali.show_balance()
    print(ali.__dict__)
