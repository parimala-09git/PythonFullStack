'''
Dictionaries
------------
-->Dict is a key: value pair seperated by :, abd keys are unique means duplicates are not allowed..
-->in the place of keys we have to use immutable data type...
-->dict is mutable

eg:
details_={"name":"pari",
          1: "number",
          (6,7):[1,2]}
print(details_)

eg: duplicate value
details_={"name":"pari",
          1: "number",
          "name":"kiran"}
print(details_)
    

methods
-------
1.keys()
------
-->It is used to get all the keys from the dict
-->syntax:variable_name.keys()

eg:
details_={"Name":"pari",
          "Age":56,
          "Gender":"Female"}
print(details_.keys())


2.values()
--------
-->To get all the values from the dictionary
-->syntax: variable_name.values()

eg:
details_={"Name":"pari",
          "Age":56,
          "Gender":"Female"}
print(details_.values())


3.items()
---------
-->It is used to get both the key and value in a pair
-->syntax: variable_name.items()

eg:
details_={"Name":"pari",
          "Age":56,
          "Gender":"Female"}
print(details_.items())

eg:
any_=[22,45,6,7]
print(any_[0])

eg:
details_={"Name":"pari",
          "Age":56,
          "Gender":"Female"}
print(details_['Name']) # we will be accessing the value using the key name instead of seperate index value


4.clear()
---------
-->the dictionary will become empty after using this method
-->syntax: variable_name.clear()
eg:
details_={"Name":"pari",
          "Age":56,
          "Gender":"Female"}
details_.clear()
print(details_)


5.update()
----------
-->we can update any value using this method
-->syntax: variable_name.update({key:value})
eg:

details_={"Name":"pari",
          "Age":56,
          "Gender":"Female"}
details_.update({"Name":"Pathivada"})
details_.update({"Age":20})
print(details_)

eg:
details_={"Name":"pari",
          "Age":56,
          "Gender":"Female"}
details_.update({"mob":123456789})
print(details_)


Sets
----
-->Set is collection of unordered elements that are seperated by comma(,)
-->Set is mutable
-->can remove duplicate values by itself

eg:
go={1,2,3,4,2}
print(go)

methods
-------

1.union()(|)
------------
-->It is used to combine the elements from both sides 
-->method syntax: set_1.union(set_2)
-->symbol syntax: set_1|set_2        #set_1 and set_2 is called the variable names
eg:
go={1,2,3,4}
so={4,5,6,7}
print(go|so)
print(go.union(so))


2.intersection() &
------------------
-->It gives the common element from both sets
-->syntax: set_1.intersection(set_2)
eg:
go={1,2,3,4}
so={4,5,6,7}
print(go&so)
print(go.intersection(so))


3.symmetric_difference() ^
--------------------------
-->It will show the values which are common from both the set of elements
-->syntax: set_1.symmetric_difference(set_2)
eg:
go={1,2,3,4}
so={4,5,6,7}
print(go^so)
print(go.symmetric_difference(so))


4.add()
-------
-->It is used to add new elements in the set
-->syntax: var_name.add(value you wanted to add)
eg:
go={1,2,3,4}
go.add(5)
print(go)


5.remove()
----------
-->To delete the elements from set based on element
-->it will throw an error when the element is not present in the set
-->syntax: var_name.remove(value you wanted to remove)
eg:
go={1,2,3,4}
go.remove(2)
print(go)


6.pop()
-------
-->If we do not give any element we want to pop then it will remove the last element
-->syntax: var_name.pop(value you wanted to pop)
eg:
go={1,2,3,4}
go.pop()
print(go)


7.discard()
-----------
-->To delete the elements from the set
-->It will not throw an error when an element is not present in the set
-->syntax: var_name.discard(value you wanted to remove)
eg:
go={1,2,3,4}
go.discard(2)
print(go)

eg:
go={1,2,3,4}
go.discard(7)
print(go)















