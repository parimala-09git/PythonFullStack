'''
Genarators
----------
-->This generator is a special function that returns the iterator. Instead of returning all the values at once...
-->Here we are going to use yield keyword
eg:
def some():
    yield 1
    yield 2
    yield 3
so = some()
print(next(so))
print(next(so))
print(next(so))

working of generator:
---------------------
-->When a function is called it does not execute the function immediiately..
-->It will return the generator object..
-->Then the function will pause at each field..
-->When the next() is called again, execution resumes from where it stopped or left..

eg:
def demo():
    print("start")
    yield 1

    print("middle")
    yield 2

    print("end")
    yield 3

how = demo()
print(next(how))
print(next(how))
print(next(how))

With Generator
--------------
eg:
def how(so):
    for i in range(so):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))


Without Generator
-----------------
eg:
def sqt(n):
    for j in range(n):
        print(j*j)
sqt(5)

yield keyword
-------------
--> This will produce the value
--> But the yield pauses the function
--> And yield will save the current state of functions
--> Yield will continue where it stopped...

next() keyword
--------------
--> The next() function is used to retrieve the next value from a generator...

eg:
def how(so):
    for i in range(so):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

StopIteration
-------------
--> Calling next() function after all values retrieve then it will raise StopIteration exception
eg:
def how(so):
    for i in range(so):
        yield i*i
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

Generator expression
--------------------
--> The generator expression is similar to a list comprehension but uses parenthesis () instead of []
--> we did not need to use yield function...
gen=(x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

''' 




















