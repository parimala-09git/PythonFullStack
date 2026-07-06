'''
Functions
---------
--> Function is a block of code that can be reusable
--> Function can avoid the repeated lines of code...

Functions are of two types:
---------------------------
1.built-in
----------
eg--> print(), max(), type(), min(), sum() #comes with python when installing

2.User-define
-------------
eg--> This function starts with keyword (def)

def func_name(parameters): #definition line where we use def
    ----------
    --------- #code
    -------
func_name(argument) #the values which we are passing are called as arguments(calling function and we are calling with the same name)
eg:
def add():
    print("Hello")
add()

types of arguments
------------------
1.Required arguments
--------------------
--> We have to pass same number of arguments as the definition function

eg:
def add(a,b):
    print(a+b) #it should not be like this when passing the arguments
add(2)

eg:
def add(a,b):
    print(a+b) # it should be like this
add(2,5)

2.Default
---------
eg:
num=7
num_2=5
num_3=6
def add(a,b,c):
    print(a)
    print(b)
    print(c)
add(num,num_2,num_3)

3.Keyword
---------
--> we can pass as a pair like(variable = datatype)
eg:
def add(a,b):
    print(a+b)
add(a=8,b=6)

4.Variable length
-----------------
--> Can pass n number of argumnets by just args (*) in the parameters, the we will get receive tuple of arguments
eg:
num=7
num_2=5
num_3=6
def add(*a):
    print(a)
add(num,num_2,num_3)

eg:
num=7
num_2=5
num_3=6
num_4='python'
def add(*a):
    print(a)
add(num,num_2,num_3,num_4)

eg: *args
num=7
num_2=5
num_3=6
def add(*a):
    print(a[0])  # by using indexing we can get that particular value
add(num,num_2,num_3)

eg: **asterick
def all_(**Any):
    print(Any['Age'])
all_(Name="pari",Age=20)

eg:
def add(a,b):
    print(a+b)
add(a="pari",b="mala")

#Scope of variables
-------------------
#global variable--> this global variable can be used through out the program
eg:
num=9
def func_():
    print(num)
func_()

note
----
--> To change the global variable by using keyword (global) that can be changed completely inside and outside of the function
eg:
num=9
def func_():
    global num
    num=49   
    print(num)
func_()
print(num)


#local variable--> Inside is the local variable and i cannot access outside the function
def func_():
    num=9   
    print(num)
func_()
print(num)

'''















