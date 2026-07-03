'''
prime number
------------
eg:

num=int(input("enter a number: "))
count = 0
for j in range(1,num+1):
    if num % j == 0:
       count += 1
if count == 2:
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")


eg:

limit_=10
for j in range(2, limit_+1):
    count=0
    for i in range(1,j+1):
        if j % i == 0:
            count += 1
    if count == 2:
        print(f"{j} is a prime")

eg:
limit_=10
for j in range(2, limit_+1):
    count=0
    for i in range(1,j+1):
        if j % i == 0:
            count += 1
            print(count)
    if count == 2:
        print(f"{j} is a prime")


3.right angle triangle:
-----------------------

eg:

num=5
for j in range(1,num+1):
    for i in range(1,j+1):
        print("*", end = " ") # end is used to make the content in horizontal form 
    print()

4.numbers:
----------
eg:
num=5
for j in range(1,num+1):
    for i in range(1,j+1):
        print(j, end = " ") 
    print()

eg:

num=5
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i, end = " ") 
    print()

eg:

num=5
count=0
for j in range(1,num+1):
    for i in range(1,j+1):
        count += 1
        print(count, end = " ") 
    print()


eg:reverse
----------

num=4
count=0
for j in range(num,0,-1):
    for i in range(1,j+1):
        count += 1
        print(i, end = " ") 
    print()


5.Amstrong num
--------------
eg:
am_str=int(input("enter a number: "))
length_=len(str(am_str))
all_sum = 0
for j in str(am_str):
    all_sum += int(j) 
if all_sum == am_str:
    print(f"{am_str} is a amstrong")
else:
    print(f"{am_str} is not an amstrong")


6.pyramid
---------
eg:
num=6
for j in range(num):
    print(" " *(num - j -1),end = " ")
    print("*" *(2 * j + 1))


'''














