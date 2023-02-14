class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep):
        self.balance += dep
        print(f"{self.owner}, the operation was successful!\nYour balance is {self.balance}")
    def withdraw(self, wit):
        self.balance -= wit
        print(f"{self.owner}, the operation was successful!\nYour balance is {self.balance}")
print("Please, write your name and balance. Press 'enter' to continue...")
owner1 = Account(input("Account owner's name: "), int(input("Balance: ")))
str1 = input("Write Withdraw or Deposit: ")
if str1 == "Withdraw":
    owner1.withdraw(int(input("Write the amount: ")))
if str1 == "Deposit":
    owner1.deposit(int(input("Write the amount: ")))