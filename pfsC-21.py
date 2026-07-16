'''

class Test:
    def display(self):
        print(self)
    te = Test()
    print(te)
    te.display()

constructor
------------
--> This constructor initializes the object automatically when it is created...

class Batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def display(self):
        print(self.name)
        print(self.branch)
B4 = Batch('Pari','CSE')
B4.display()

eg:
class Batch:
    def __init__(self,name,branch):
        self._name = name
        self.branch = branch
    def display(self):
        print(self._name)
        print(self.branch)
B4 = Batch('Pari','CSE')
B4.display()

eg:
class fam:
    def __init__(self):
        self._name = "Pari"
f = fam()
print(f._name)

eg: protecting the class and calling the private variables 
class bank:
    def __init__(self):
        self.__pin = '6600'
AC = bank()
print(AC._bank__pin)

eg:
class Bank:
    def __init__(self):
        self.__pin = '6600'
    def display(self):
        print(self.__pin)
ac = Bank()
ac.display()


Encapsulation
--------------
--> Means wrapping the data and methods into
'''
class atm:
    def __init__(self,balance):
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
        print(self._balance)
tran = atm(balance = int(input("Enter Amount: ")))
tran.deposit(amount = int(input("Enter Amount: ")))













        
