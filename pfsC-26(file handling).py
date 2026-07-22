'''
File Handling
--------------

File handler is an object that gives more options like creating, updating

two ways to open a file...
1.open()
---------
syntax: do = open('file_name','mode')
        close()
eg:
do = open('demo.txt','r')
print(do.read())

2.with(keyword)
----------------
syntax: with open('file_name','mode') as do:

with open('demo.txt','r') as do:
   print(do.read())
   
Modes
------
r --> used to read the file, incase if the file is not present it will raise an error
w --> The file is used to write the text inside the file and it will  override the text inside file, incase if the files is not present it will create a new file with the name given

eg:
with open('demo.txt','w') as do:
   print(do.write('This is python class'))
eg:
with open('dem.txt','w') as do:
   print(do.write('This is python class'))

a --> This is used to add the text at last position inside the file
eg:
with open('demo.txt','a') as do:
   print(do.write('We are using file handling'))

x --> This is used to create a new file by adding the text inside the file, incase if the file is present it will raise an error...
eg:
with open('hlo.txt','x') as do:
   print(do.write('We are using file handling'))

write()
-------
-> This functionality is used to add the text inside a file or update a file with new text
eg:
with open('demo.txt','w') as do:
   print(do.write('This is python class'))

eg:
with open('demo.txt','a') as do:
   print(do.write('This is python class'))

read()
-------
-> This function is used to read a file and this read() will read file chunk by chunk.. and we can also specify the size
eg:
with open('demo.txt','r') as do:
   print(do.read(5))

readline()
----------
-> this function will read one line at a time
eg:
with open('demo.txt','r') as do:
   print(do.readline())

readlines()
----------
-> This function will read entire file and give it in a list as each line is one index in that list...
eg:
with open('demo.txt','r') as do:
   print(do.readlines())


