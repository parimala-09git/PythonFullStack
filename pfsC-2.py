#Python-class2:

'''
Operators:
---------
1)Arithmetic Operator
---------------------
--> It is used for mathematical operations (+, -, *, /, **, //, %)


2)Assignment Operator
---------------------
--> Assigning data type into variable (=, +=, -=, *=, %=)

3)Comparision Operator
----------------------
--> It is used to compare the values using these operators (==, !=, <=, >=, <, >)

4)Logical Operator
------------------
--> and - Returns true if both conditions are true
    or  - Returns true if any one is correct
    not - Expected output becomes the opposite (reverse the output)

5)Identity Operator
-------------------
--> is  - It looks for the same object or not
    is not - It is the opposite of is

6)Membership Operator
---------------------
--> in  - To check weather the number or value is present inside
    not in - It is the opposite of in

7)Bitwise Operator
------------------
--> It gives the output based on the binery objects (&, <<, >>, |, ^)


eg:arithmentic opt:

a=9
b=10
print(a+b)#addition
print(a*b)# mul
print(a**b) #power(exponential)
print(a/b) #division

eg:assignment opt:
    
a=20
a += 4  #used for increment
print(a)
a -= 4 #used for decrement
print(a)
a *= 4
print(a)

eg:comparision opt:

a=20
b=7
print(a==b) #to compare th values 
print(a!=b) #not equal to
print(a<=b) #less than 
print(a>=b) #greater than

eg:Logical opt:

a=20
b=7
c=89
print(a >= b and b <= c) #both the conditions must be staisfied
print(a >= b or b >= c) #atleast one of the two must be true
print(not(a>=b or b>=c) #expected output will be reverse

eg:Identity opt:

a=20
b=2
print(a==b)
print(a is b) #it looks for the object that is same or not
print(a is not b) #opposite of is


eg: Membership opt:

a=[1,2,3,4,5]
print(2 in a) #to check weather the value is present inside
print(20 not in a) # opposite of in


eg: Bitwise opt:

print(5&4)
print(5|3)
print(5<<3)
print(5>>1)

'''
