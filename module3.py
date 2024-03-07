'''import math 
print(math.sqrt(4)) 
print(math.pi)'''

'''import math as m 
print(m.sqrt(4)) 
print(m.pi)'''

'''from math import *
print(int(sqrt(4)))
print(ceil(10.1))
print(floor(10.1))
print(fabs(-10.6))
print(fabs(10.6))'''

#random module: 
#This module defines several functions to generate random numbers. We can use these functions while developing games 
'''from random import *
for i in range(5):#0-4
    print(random())'''

#To generate random integer beween two given numbers(inclusive) 
'''from random import *
for i in range(10): #0-9
    print(randint(1,100000))'''

#random float values between 2 given numbers 
'''from random import *
for i in range(10):
    print(uniform(1,10))'''

#choice() function:  
#It wont return random number. It will return a random object from the given list or tuple.

'''from random import *
list=["prashant","rahul","ashish","sandip","sunil","nikhil"]
for i in range(10):
    print(choice(list))'''

#The Special variable __name__: 
#For every Python program , a special variable __name__ will be added internally.
#This variable stores information regarding whether the program is executed as
# an individual program or as a module. 
#If the program executed as an individual program then the value of this variable is __main__ 

'''def call():
    if __name__ == '__main__':
        print("This is executed as a individual program")
    else:
        print("The is executed as a module from some other program")

call()'''

'''from random import *

print(randint(1,100000))'''

#WAP for bubblesort
'''def bubbleSort(array):
    
   for i in range(len(array)):
       for j in range(0, len(array)-i-1):
           if array[j] > array[j+1]:
               (array[j], array[j+1]) = (array[j+1],array[j]) 

data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print('Sorted Array in Asc ending Order:')
print(data)'''

# Selection sort
'''def selectionSort(array,size):

    for i in range(size):
        min = i

        for j in range(i+1, size):
            if array[j]< array[min]:
                min = j
        (array[i],  array[min])  = (array[min],array[i])
    
array = [16,23,13,9,5,7]
size = len(array)
selectionSort(array, size)
print("After selection sort array")
print(array)'''