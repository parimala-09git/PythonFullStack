#Python Class-4:

'''
List datatype
-------------
-->List is a collection of different datatypes that are enclosed in[] seperated by ,(comas)
-->List is mutable


eg:
all_type=[1,'python',[1,2]]


method
------
1.append()
----------
-->This is used to add new item into list, but it will add in the last index position
-->it will consider only one index value

eg:
any_=[1,2,3,4]                                  
print(any_)                                                                      
any_.append(5)
print(any_)
any_.append(10)
print(any_)

         
mutable                                         immutable
-------                                         ---------
The datatype that can be modified               It cannot be modified


#eg:                                            #eg:
                                                so="python is a language"                                                                                           
any_=[1,2,3,4]                                  print(so.replace('python','java'))
print(any_)                                     print(so)                                 
any_.append(5)
print(any_)
any_.append(10)
print(any_)
                                               

2.extend()
----------
-->This adds an item in the last index position, but it will give each value in the each index position means in seperate index position..
-->It will take only list, tuple, and string

eg:

any_=[1,2,3,4]
any_.extend('python')
print(any_)
print(len(any_))

eg:
any_=[1,2,"python is a language",[45,78,"java is a language",[1,23],90],'hello']
print(any_[3][2][10])


3.pop()
-------
-->Pop will remove the value from the list, but it will remove based on the index position..
-->variable_name.pop(index position)

eg:

any_=[1,2,45,78,23,90]
any_.pop(1)
print(any_)

4.remove()
----------
-->It is used to delete the item from the list, but it will delete direct value from the list..
-->variable_name.remove(delete the value you want to delete)

eg:

any_=[1,2,45,78,23,90]
any_.remove(1)
print(any_)

5.insert()
----------
-->
eg:


6.sort()
--------
eg:

any_=[78,45,34,1]
any_.sort()
print(any_)
any_.append(10)
print(any_)
any_.sort()
print(any_)


tuple
-----
-->tuple is a collection of different datatypes represented in() parenthesis and seperated by comas(,)
-->It is immutable

eg: 
how=(1,2,3,4)
print(how)    

eg:

how=(1,2,3,4,"python",[4,5],(90,78))
print(how[4])
print(len(how))

Tuple methods
-------

1.index()
-------
eg:

how=(1,2,3,4,"python",[4,5],(90,78))
print(how.index('python'))

2.count()
---------
eg:

how=(1,2,3,4,"python",[4,5],(90,78))
print(how.count('python'))

'''









