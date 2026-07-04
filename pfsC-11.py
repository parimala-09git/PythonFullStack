'''
1.palindrome
------------
eg:
so="pari"  #-->irap
empty_=""
for j in so:
    empty_ = j + empty_  #string will be reversed
if empty_ == so:
    print(f"{so} is Palindrom")
else:
    print(f"{so} is not palindrom")


2.fibonacci series
------------------
eg:
num = 0
num_2 = 1
limit_ = int(input("enter a number: "))
print(num, num_2, end=" ")
for i in range(1,limit_+1):
      all_ = num + num_2
      num = num_2
      num_2 = all_
      print(all_, end=" ")


3.calculator
------------
val_= int(input("enter a number: "))
val_2= int(input("enter a number: "))
user_in=int(input("enter \n1.add \n2.sub \n3.mul \n4.pow \n5.div \n6.mod "))
if user_in == 1:
    print(val_+val_2)
elif user_in == 2:
    print(val_-val_2)
elif user_in == 3:
    print(val_*val_2)
elif user_in == 4:
    print(val_**val_2)
elif user_in == 5:
    print(val_/val_2)
elif user_in == 6:
    print(val_%val_2)
else:
    print("Enter correct number ")
    

4.table
-------
table_=int(input("enter your number: "))
for val in range(1,11):
    print(f"{table_} * {val} = {table_ * val}")
    

5.perfect number
----------------
num=int(input("enter your number:"))
sum_=0
for j in range(1,num):
    if num % j == 0:
        sum_ += j
if sum_ == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")


6.ATM
------
details_={"name":"Pari",
          "ATM PIN":"6600",
          "Balance":50000}
print("----welcome----")
user_pin=input("pls enter your 4 digit ATM pin: ")
if len(user_pin) == 4:
    if user_pin in details_['ATM PIN']:
        func_=int(input("Enter \n1.Withdraw \n2.Deposite \n3.Balance: "))
        if func_ == 1:
            withdraw_m = int(input("Enter the amount you want to withdraw: "))
            if withdraw_m <= details_['Balance'] and withdraw_m % 100 == 0:
                details_['Balance'] -= withdraw_m
                print(f"you have withdraw {withdraw_m} and total balance is {details_['Balance']}")
            else:
                print("Insufficient funds or change can't be withdrawn")
    else:
        print("Incorrect pin entered")
else:
    print("pls enter only 4 digit pin")

'''














    



    
