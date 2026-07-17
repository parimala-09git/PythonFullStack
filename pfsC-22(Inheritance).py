'''
Inheritance
-----------
-->Inheritance is an OOP concept where one class (child/derived) acquired the properties and methods of another class (parent/base)

class parent:
    pass
class child(parent):
    pass

1.Single inheritance
---------------------
A child class inherits from one parent is single inheritance

eg:
class animal:
    def sound(self):
        print('Animals make sounds')
class dog(animal):
    def barks(self):
        print("Dog barks")
d = dog()
d.sound()
d.barks()

eg:
class father:
    def land(self):
        print('5 ar of land')
class son(father):
    def flat(self):
        print('3BHK flat')
s = son()
s.land()
s.flat()


2.multiple inheritance
---------------------
A child inherits more than one parent is called
eg:
class father:
    def skills(self):
        print("Driving")
class mother:
    def talent(self):
        print("Cooking")
class daughter(father,mother):
    def mine(self):
        print("Singing")
all_ = daughter()
all_.skills()
all_.talent()
all_.mine()


3.multi-level
------------
one child class becomes the parent for another class

class grandfather:
    def house(self):
        print('Owns House')
class father(grandfather):
    def flat(self):
        print('New 3BHK Flat')
class son(father):
    def car(self):
        print('Have a car')
fam = son()
fam.house()
fam.flat()
fam.car()


4.Hierarchical inheritance
-------------------------
Multiple childs inherits from the same parent

class mother:
    def gold(self):
        print("10 KG gold")
class pinky(mother):
    def show(self):
        print('Will get 5 kg gold')
class yuktha(mother):
    def show_2(self):
        print('Will get remaining 5 kg gold')
child_1 = pinky()
child_2 = yuktha()

child_1.gold()
child_1.show()
child_2.gold()
child_2.show_2()


eg:
class father:
    def land(self):
        print("6 acrs of land")
class ram(father):
    def show(self):
        print('Will get 2 acrs of land')
class charan(father):
    def show_2(self):
        print('Will get 2 acrs of land')
class mahesh(father):
    def show_3(self):
        print('will get the remaining 2 acrs of land')
        
child_1 = ram()
child_2 = charan()
child_3 = mahesh()

child_1.land()
child_1.show()
child_2.land()
child_2.show_2()
child_3.land()
child_3.show_3()


5.Hybrid inheritance
-------------------
-->This is the combination of two or more types of inheritance example of multiple + multi-level
eg:
class A:
    def methodA(self):
        print('Class A')
class B(A):
    def methodB(self):
        print('Class B')
class C(A):
    def methodC(self):
        print('Class C')
class D(B,C):
    def methodD(self):
        print('Class D')
so = D()
so.methodA()
so.methodB()
so.methodC()


super()
-------
-->This super() function is used to access the parent class methods or constructor in the child class..
eg:
class parent:
    def show(self):
        print('Parent method')
class child(parent):
    def show(self):
        super().show()
        print('child class')
chi_ = child()
chi_.show()

eg:
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(self.name)
        print(self.roll)
an = student('Teja',101)
an.display()















        
