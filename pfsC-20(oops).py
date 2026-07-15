'''
OOPS
-----
Object-oriented programming system (oops), This will be organizes the code using classes and objects...

uses
-----
-Code reusable
-Easy maintainance
-Clear understanding
-Better Security

Classes
--------
Class is a blue-print or a template used to create an object...

Class Batch_4:
    pass

Object
-------
-Object is a instance of the class

eg:
---
class student:
    studn = 'Pari'
st_ = student() #object created
print(st_) #calling th obj



Attributes
-----------
-Attributes are the variable that belongs to an object or the class

eg:
class how:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def nam(self):
        print(self.name)
s1 = how('Pari',67)
print(s1.nam())

eg:
class how:
    def details(self,name,age):
        self.name = name
        self.age = age

s1 = how()        
s1.details('Pari',67)
print(s1.name)

Methods
--------
-Methods are nothing but, the functions inside the class

eg:
class Calculator:
    def add(self,num,num_2): #attributes are the var inside the class
        print(num + num_2)
cal = Calculator()
cal.add(45,6)

eg:
class Calculator:
    def add(self,num,num_2):
        print(num + num_2)
    def sub(self,num,num_2):
        print(num - num_2)
cal = Calculator()
cal.sub(51,4)

'''

