'''
------Modules------
--> A module is a python file. (.py) that contain resuable code:-
1.variables
2.functions.
3.classes
4.obejects
5.Statements

why is it used?
--> instead of writing the same code repeatedly, we can store it in a module and use it whenever needed.

types of modules:- we have two types.
1.user-defined
import first_module
print(first_module.sub(45,7))

how to import specific functions??
from first_module import add,sub
print(sub(45,7))                  #only specific functions add and sub are imported from module. other than that no other operation can be done.

need to import all functions??
eg1:
from first_module import *
print(add(45,7))         #to run all the operations use * 

eg2:-
from first_module import *
print(add(45,7))
print(sub(45,7))
print(mul(45,7))
print(div(45,7))
print(div(45,7))
print(pow(45,7))

to import module with aka??
import first_module as m
print(m.sub(45,7))              # we should specify in the print statement how we meant module ad. here (m).


2.built-in:-
-->math:- used to perform all math operations 
eg:-
import math
print(math.sqrt(25))
print(math.factorial(2))
print(math.pow(2,5))
print(math.pi)

sqrt() = square root
factorial() = factorial
pow() = power
ceil() = roundup
floor() = rounddown
pi = pi value

-->os:- the os module is used to interact with operating system
eg:-
import os
print(os.getcwd()) #getcwd= to get current directory (current directory)
os.mkdir("empty monicafile") #mkdir = to create new folder (make directory)
os.rename(old file name, new file name) # to rename an existing file

--->sys:- this will provide the information about python interpeter.
eg:
import sys
print(sys.version)

--->random:- used to generate random values. ( just like otp )
import random
print(random.randint(1000,9999)) #generates random values from 1000 to 9999 ( randint:- random integer)

eg2:
import random
colors = ['yellow','red','blue','green']
print(random.choice(colors))
