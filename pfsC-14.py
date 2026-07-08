'''
Lambda Function
--------------
-->This is also called as annonymous function...
-->A lamda function can take n number of arguments but having only on expression
syntax --> lambda arguments: expression
eg:
some = lambda an: an+5
print(some(10))
eg:
some = lambda an: an-5
print(some(10))
eg:
some = lambda an: an*5
print(some(10))
eg:
some = lambda an,so,why : an + so + why 
print(some(10,8,89))

filter()
--------
-->The filter() function is a built-in function used to filter elements from an itterables such as list, tuple and set based on condition
-->syntax: filter(function, itterable)
-->This filter() function returns filter object so we can convert that into other types such as list, set,and tuple

eg:
nums=[1,2,3,4,5]
rev=filter(lambda a: a%2 == 0, nums) #even num
print(list(rev))

eg:
nums=[1,2,3,4,5]
rev=filter(lambda a: a%2 != 0, nums) #it gives the filter object
print(rev)

eg:
nums=[1,2,3,4,5]
rev=filter(lambda a: a%2 != 0, nums) #odd num
print(list(rev))


list comprehension
------------------
-->This offers a shorter syntax when we want to create a new list from the old list
-->syntax: variable_name = [expression loop condition]
eg:
old_=[1,2,3,4,5,6]
new_=[j for j in old_]
print(new_)

eg:
old_=[1,2,3,4,5,6]
new_=[j for j in old_ if j % 2 == 0]
print(new_)

Dictionary comprehension
------------------------
-->This offers a shorter syntax when we want to create a new dict from the old dict
-->syntax: variable_name = [expression loop]
eg:
old_dict = {1:2, 3:7, 5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)


'''












