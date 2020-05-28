'''
1.	Write python program to perform bank operations using class and objects.
       Conditions:
a.	Bank name should be static.
b.	Using menu driven program.
1 .Deposit
2. Withdraw
3. Exit

'''

import sys


class Bank:
    bankname = 'MangeshBank'

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount
        print("After deposit the balance is:", self.balance)

    def Withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to perform this transaction...")
            sys.exit()
        self.balance -= amount
        print("After withdraw the balance is:", self.balance)


print("Welcome to", Bank.bankname)
name = input("Enter your name:")
b = Bank(name)
while True:
    print("Which operation you want to perform\n1) Deposit\n2) Withdraw\n3) Exit")
    option = int(input("Choose the correct option:"))
    if option == 1:
        amount = float(input("Enter the amount you want to deposit:"))
        b.Deposit(amount)

    elif option == 2:
        amount = float(input("Enter the amount you want to withdraw:"))
        b.Withdraw(amount)

    elif option == 3:
        print("Thanks for Banking!!!")
        sys.exit()
    else:
        print("Please choose the valid option")