'''
passing by value
----------------
def some(a):
    for j in a:
        print(j)
some ([1,2,3])

passing by reference
--------------------
a=(1,2,3)
def some(a):
    for j in a:
        print(j)
some ([1,2,3])        

return keyword
--------------
-->return holds the calling function
-->in a function if return is executed then it will exit from the function with csertain returned values

def myfunc_(b):
    return 5 + b
a=myfunc_(10)
c=myfunc_(100)
print(a)
print(c)

built-in functions
------------------
import builtins

builtin_functions=[
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}")


Recursive function
------------------
-->recursive function that calls itself repeatedly until a specified condition is met...
syntax:
-------
def func_name(parameter):
    if condition: -->base case
        return statement
    else:
        return statement
print(func_name(arguments))


def func_name(num):
    if num==1:
        return 1
    else:
        return num * func_name(num-1)
num=7
print(func_name(num))

'''





















