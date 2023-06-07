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
        print('==================/n')
        return self

    def yield_interest(self):
        if self.balance > 0 :
            intrestGained = self.int_rate * self.int_rate
            self.balance += intrestGained
            print(f'You account balance plus intrest is: {self.balance}')
            return self

Sokka = BankAccount()
Toph = BankAccount(.10, 1070)

Sokka.deposit(10).deposit(100).deposit(40).withdraw(75).yield_interest().display_account_info()

Toph.deposit(1000).deposit(2500).withdraw(400).withdraw(250).withdraw(200).withdraw(100).yield_interest().display_account_info()
