'''
Regular expressions
---------------------
-> RegEx is an sequence of char that can searching pattern
-> To use RegEx we have import re module....
syntax --> import re

Functions
----------
1.findall-> It will find all the char that are in the string
eg:
import re
txt = 'python is a language and also a dynamically typed language'
print(re.findall('[a]',txt))

o/p: in the list form
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

2.search-> It will find the char but It will find the first occurance in the sequence of the string..
eg:
import re
txt = 'python is a language and also a dynamically typed language'
print(re.search('[a]',txt))
o/p:
<re.Match object; span=(10, 11), match='a'>

3.split-> It is same as the split method in the string
eg:
import re
txt = 'python is a language and also a dynamically typed language'
print(re.split(' ',txt))
o/p:
['python', 'is', 'a', 'language', 'and', 'also', 'a', 'dynamically', 'typed', 'language']

4.sub->
eg:
import re
txt = 'python is a language and also a dynamically typed language'
print(re.sub(' ','&',txt))
o/p:
python&is&a&language&and&also&a&dynamically&typed&language

5.fullmatch->
eg:


Metachar
---------
[]
eg:
import re
txt = 'I have 100 Ruppee'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))
print(re.search('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))

^
eg:
import re
txt = 'I have 100 Ruppee'
print(re.findall('I have',txt))
print(re.search('I have',txt))

$
eg:
import re
some = 'I am going to school'
print(re.findall('school$',some))
print(re.search('school$',some))

.
eg:
import re
any_='Hello! This is teja'
print(re.findall('T..s',any_))
print(re.findall('T...',any_))
print(re.search('T...',any_))

*
eg:
import re
how = 'python module will going completed this week'
print(re.findall('p.*n',how))
print(re.findall('p.*ython',how))
print(re.findall('p.*',how))
print(re.search('p.*n',how))

+
eg:
import re
how = 'python is a language'
print(re.findall('p.+thon',how))
print(re.findall('p.+n',how))
print(re.search('p.+a',how))

{}
eg:
import re
now = 'Python is a language'
print(re.findall('P.{10}',now))
print(re.search('P.{10}',now))

'''
