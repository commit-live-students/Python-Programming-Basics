#Question - 6: Create a class Account and extend it for Saving and Current account
# - There is no constraint on deposit
# - minimum balance for Saving Account is 1000
# - minimum balance for Current Account is 15000 and withdrawal fees 1% of the amount

class Account:
   balance = 0
   def __init__(self, acctNumber):
      self.acctNumber = acctNumber

   def __str__(self):
      return "Account number: " + str(self.acctNumber) + "\n" + \
             "Balance: " + str(self.balance)

   def deposit(self, amount):
      self.balance += amount

class Current(Account):
   def __init__(self, acctNumber):
      Account.__init__(self, acctNumber)

   def __str__(self):
      retStr = "Account type: Current\n"
      retStr += Account.__str__(self)
      return retStr

   def withdraw(self, amount):
      if amount > self.balance or self.balance < 15000:
         print("Insufficient funds.")
      else:
         self.balance = self.balance - amount - (amount * 0.1)

class Savings(Account):
   def __init__(self, acctNumber):
      Account.__init__(self, acctNumber)

   def __str__(self):
      retStr = "Account type: Savings\n"
      retStr += Account.__str__(self)
      return retStr

   def withdraw(self, amount):
      if amount > self.balance or self.balance < 1000:
         print("Insufficient funds.")
      else:
         self.balance = self.balance - amount