'''
#Datatypes:
-----------
int
---
eg: num=8

float
-----
eg: num_2=7.89

num_2= 7.89
num= 6.89
print(num//2)

string
------
--> String is a sequence of char that are enclosed in ' '," ", """ """
--> str is immutable

Concatination
-------------
--> The addition operator (+) acts as to concatinate more than 2 strings...

eg:

so="Python"
any_=" is a Language"
print(so+any_)

Indexing:
---------
--> This is used to access the particular character in a string by passing index position value..
--> Index starts from zero[0]
--> We have negative indexing to count the positions from last to first with [-1]

eg:

so="Python is a language"
print(so[12])

so="Python is a language"
print(so[-2])


methods
-------

1.replace()
-----------
--> This method is used to chnage any substring in that particular string..
string--> variable_name.replace("old string","new string",count) #count means how many times we want to replce it..

eg:
so="Python is a language"
print(so.replace("Python","Java"))
print(so)

eg:count
so="Python is a language"
print(so.replace("a","A",2))

2.join()
--------
-->This method is used to add new substring after each char in the string...
syntax-->"string".join(variable_name)

eg:
so="Python is a language"
print("$".join(so))

3.split()
---------
--> This method can divide the string into different index into list, based on the string pass by us...
syntax--> variable_name.split("substring")

eg:

so="Python is a language"
print(so.split(" "))
print(so.split("is"))
    
4.count()
--------
--> Used to count the substring in the particular string and also specify the index position
syntax-->variable_name.count("substring",start index, ending index)

eg:
so="Python is a language"
print(so.count("a",0,12))

eg:
so="Python is a language"
print(so.count("a"))

String:It is a sequence of characters...
String functions:
1.len():
--------
-->It will find out the length of the characters in the string
eg:

so="Python is a language"
print(len(so))

2.max():
--------
--> we will get the max char in the string

eg:
so="Python is a language"
print(max(so))


2.min():
--------
--> we will get the min char in the string

eg:
so="Python is a language"
print(min(so))

'''









