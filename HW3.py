class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance can't lower 0")
        else:
            self._balance = amount

bank1 = BankAccount(0)

bank1.balance = 2000
print(bank1.balance)

bank2 = BankAccount(0)
bank2.balance = -1000
