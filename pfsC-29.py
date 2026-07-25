'''
Matplotlib
-------------
eg:
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,15,30,5]
plt.plot(x,y)
plt.title('Simple Plot')
plt.xlabel('x axis') #no of years
plt.ylabel('y axis') #sales
plt.show()

eg:
import matplotlib.pyplot as plt
x=[2026,2025,2024,2023,2022]
y=[120,150,135,95,70]
plt.plot(x,y)
plt.title('Car Sales')
plt.xlabel('years') 
plt.ylabel('no of cars') 
plt.show()

eg:bar
import matplotlib.pyplot as plt
x=[2026,2025,2024,2023,2022]
y=[120,150,135,95,70]
plt.bar(x,y,color='red',edgecolor='black')
plt.title('Car Sales')
plt.xlabel('years') 
plt.ylabel('no of cars') 
plt.show()

eg:bar
import matplotlib.pyplot as plt
x=['BMW','Audi','Benz','Rolls Royce']
y=[110,70,98,160]
plt.bar(x,y,color='Purple',edgecolor='black')
plt.title('Car Sales')
plt.xlabel('years') 
plt.ylabel('no of cars') 
plt.show()

eg:pieplot
import matplotlib.pyplot as plt
subjects_=['python','java','C']
stu_=[69,13,50]
plt.pie(stu_,labels=subjects_,colors=['red','blue','green'],autopct='%1.1f%%')
plt.legend(subjects_)
plt.title('Courses')
plt.show()

eg:scatter
import matplotlib.pyplot as plt
x=['BMW','Audi','Benz','Rolls Royce']
y=[110,70,98,160]
plt.scatter(x,y,color='orange')
plt.title('Car Sales')
plt.xlabel('Years') 
plt.ylabel('Number of cars')
plt.show()



eg:bar(cars)
import matplotlib.pyplot as plt
x=['BMW','Audi','Benz','Rolls Royce']
y=[90,130,120,100]
plt.plot(x,y)
plt.title('Simple Plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


import matplotlib.pyplot as plt
y=[69,13,50,60]
plt.hist(y,bins=20)
plt.title('Cars')
plt.xlabel('years')
plt.ylabel('Number of cars')
plt.show()








