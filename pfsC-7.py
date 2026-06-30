'''
Input Formatting from user

input()
---------
--> The input function is used to to take input from the user....

1.int
-----
eg:
num=int(input("Enter a number: ")
num_2=int(input("Enter a number: ") # its not compulsory to mention a string saying enter a number...
print(num+num_2)

2.string
--------
eg:
how=input("Enter a char: ")
print(how+'Pari')

3.float
-------
eg:
num=float(input("Enter your salary: "))
print(num,"is the monthly salary")

4.list
------
eg:
group_=list(map(int,input().split()))
print(group_)

eg:
group_= list(input())
print(group_)

5.tuple
-------
eg:
some=tuple(map(int,input().split()))
print(some)

group_=tuple(map(int,input().split()))
print(group_)

**eval: Any datatype can be given in eval and it will show the output based on the given datatype
num=eval(input("Enter:"))
print(type(num))

eg:
name_=input("Enter your name: ")
age_=int(input("Enter your age:" ))
print(name_,age_) 

eg:
name_=input("Enter your name: ")
age_=int(input("Enter your age:" ))
print(name_,"your age is",age_)

**f string or doc string:
eg: formatted string or doc string
name_=input("Enter your name: ")
age_=int(input("Enter your age:" ))
print(f"{name_} your age is {age_}") #formatted string or doc string

**modulus format:
eg: using modulus format
name_=input("Enter your name: ")
age_=int(input("Enter your age:" ))
print("My name is %s and i'm %d years old" %(name_,age_)) #using modulus format

'''




























