'''
Conditional statements
------------------------
-->these statements are used to check the condition

1.if--> It is used to check a condition is true or not

eg:
num=9
if num % 2 == 0: 
   print(f"{num} is a even number")

2.if-else
-------
-->else is the fall-back statement incase the if condition is false, then this else will be executed

eg:
num=9
if num % 2 == 0: 
   print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")

eg:
teja_ICIC_details={"ATM PIN":'6600'}
pin_=input("Enter your 4 digit ATM pin:")
if pin_ in teja_ICIC_details['ATM PIN']: # if 1234 in 6600: false
    print("Welcome to ICIC ATM")
else:
    print("You have entered incorrect pin") 

3.nested it
--------- 
-->it is if inside another if is called as nested if

eg:
teja_ICIC_details={"ATM PIN":'6600'}
pin_=input("Enter your 4 digit ATM pin:")
if len(pin_) == 4:
    if pin_ in teja_ICIC_details['ATM PIN']:
        print("Welcome to ICIC ATM")
    else:
        print("you have entered incorrect pin")
else:
    print("please enter only 4 digit pin")

4.elif
------
--> It will give more options

eg:
marks_=int(input("Enter your marks:"))
if marks_>=90:
    print("A+")
elif marks_>=80:
    print("A")
elif marks_>=70:
    print("B+")
elif marks_>=60:
    print("B")
elif marks_>=50:
    print("C")
else:
    print("Failed")

2.Control statements
--------------------
-->it is used to control the program


3.Loop statements










































