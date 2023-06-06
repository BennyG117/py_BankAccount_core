
#GOALS:
"""
-create a class
-implement default arguments in parameters for attributes that can be assigned on instantiation
-implement the functionality of a bank account
-handle edge cases such as insufficient funds, with control structures like (if-else, code flow, or early exit)
-Students create and update attributes of an object instance from within the class using "self"
-test the functionality by creating instances and calling methods with diferent test data
"""

class BankAccount:

    def __init__(self, int_rate = 0.05, balance = 0): 
        self.int_rate = int_rate 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print(f'Insufficient funds: Charging a $5 fee')
            self.balance -= 5
            print(self.balance)
            return self
        else:
            self.balance -= amount 
            print(self.balance)
            return self

    def display_account_info(self):
        print(f'Your intrest rate is: {self.int_rate}\nYour current balance is: {self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0 :
            intrestGained = self.int_rate * self.int_rate
            self.balance += intrestGained
            print(f'You account balance plus intrest is: {self.balance}')
            print('==================/n')
            return self

Sokka = BankAccount()

Sokka.deposit(500)
Sokka.withdraw(50)
Sokka.display_account_info()
Sokka.yield_interest()

Sokka.deposit(1000).withdraw(1001).display_account_info().yield_interest()

