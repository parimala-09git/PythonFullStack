'''
Error handling
---------------
syntax error
-------------
for j in range(1,10:
    print(j)

o/p -- SyntaxError

indentation error
------------------

    a=20
for j in range(1,10):
    print(j)
else:
print()

o/p -- IndentationError

num = int(input("Enter a num: "))

o/p -- ValueError


try
----
The try block will test the code for errors
syntax -- try:

except
-------
This except block let us handle the errors in the code

syntax -- except:

else
----
If the try block does not have any error then the else block will execute

finally
--------
This block will execute either you have error or not in your code

eg:
try:
    print(num)
except:
    print("will get name error")
    
eg:
try:
    num = int(input("Enter a num: "))
except:
    print("will get name error")
    
eg:
try:
    num = int(input("Enter a num: "))
except NameError:
    print("will get name error")

eg:
try:
    num = int(input("Enter a num:"))
    num_2=int(input("Enter a num:"))
    print(num/num_2)
except:
    print('will get zerodivision error')
eg:
try:
    num = int(input("Enter a num:"))
    num_2=int(input("Enter a num:"))
    print(num/num_2)
except :
    print('will get zerodivision error')

eg:
try:
    num = int(input("Enter a num: "))
except ValueError:
    print('will get zerodivision error')

eg:
try:
    num = int(input("Enter a num:"))
    num_2=int(input("Enter a num:"))
    print(num/num_2)
except ZeroDivisionError:
    print('will get zerodivision error')
except ValueError:
    print('will get value error')

eg:
try:
    num = int(input("Enter a num:"))
    num_2=int(input("Enter a num:"))
    print(num/num_2)
except ZeroDivisionError:
    print('will get zerodivision error')
except ValueError:
    print('will get value error')
else:
    print('no error')

eg:
try:
    num = int(input("Enter a num:"))
    num_2=int(input("Enter a num:"))
    print(num/num_2)
except ZeroDivisionError:
    print('will get zerodivision error')
except ValueError:
    print('will get value error')
else:
    print('no error')
finally:
    print('end')

