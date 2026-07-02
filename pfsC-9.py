'''
loops
-----
1.for loop
----------
-->A for loop is used to iterate over a sequence, list, tuple, dict(getting inside the values one by one)
eg:
any_="python is a language"
for j in any_:
    print(j)

any_=(1,2,3,4,5)
for j in any_: #here j is an instance variable which is mentioned after 'for' where it does not show any error as it it is a temperary variable
    print(j)

any_= {"Name":"Teja",
       "Role":"Mentor"}
for key in any_.values():
    print(key)    
    
else in for loop
----------------
--> The else block will be executed after the for loop, but incase the loop is broke then it will never enter into the else block
eg:
any_=[1,2,3,4,5]
for val in any_:
    print(val)
else:
    print("Program ended")

eg:
any_=[1,2,3,4,5]
for j in any_:
    print(j)  
else:
    print("Entered")

eg:
any_=[1,2,3,4,5]
for j in any_:
    print(j)
    if j==3:
        break
else:
    print("Entered")
    
2.while loop
------------
--> The while loop will executed until the condition becomes true...

eg:
i=1
while i<5:
    print(i) 
eg:
i=1
while i<5:
    print(i)
    i+=1

Control statements
------------------
1.break
-------
-->The break statement is used to exit from the loop if we meet the condition that we want
eg:
any_=[1,2,3,4,5]
for j in any_:
    print(j)
    if j==3:
        break
else:
    print("Entered")

2.continue
----------
--> The continue will skip the current iteration
eg:
any_=[1,2,3,4,5]
for j in any_:
    if j==3:
        continue
     print(j)
else:
    print("Entered")

3.pass
------
-->It is space holder
eg:
any_=[1,2,3,4,5]
for j in any_:
    pass

**range()
-------
-->range is an in-built function that is used to generate sequence upto certain range(limit)
-->syntax:range(start,end,step):
-->step is optional like it is used to skip the the value you mentioned (if 2 is mentioned then 2 values are skipped and print)
eg:
any_=[1,2,3,4,5]
for j in range(1,50):
    print(j)

eg:
any_=[1,2,3,4,5]
for j in range(1,50,2):
    print(j)

**assert
--------
--> It is used to check the condition, but it will raise an error incase it is false...

eg:
num=10
assert num>0, "has to be positive" #it does not shows any error if the condition is true

eg:
num=10
assert num<0, "has to be positive" #it shows error if the condition is false

eg:
age=int(input("Enter you age: "))
assert age>=18, "you must have 18 years"

'''















    
