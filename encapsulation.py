#Encapsulation

'''Encapsulation is a process of protecting the data and functionality of a class in a single unit, called an object.
This mechanism is often used to protect the data of an object from other objects. 
It’s one of the fundamental principles in any programming language that supports object-oriented programming.
We can protect the variables in the class by marking them as private. 
We need to add two underscores as a prefix to make a variable private. 
Once we make a variable as private, we can’t access them directly from the objects of that class. 
Now, let’s see how to create private variables:'''
'''_a (protected)
__a(private)'''
# Python program to
# demonstrate protected members 
# Creating a base class
'''class Base: # parent class
    def __init__(self):    
        print("parent class constructor called")
        self._a = 2  # Protected member
# Creating a derived class    
class Derived(Base): # child class
    def __init__(self):   
        # Calling constructor of
        # Base class
        Base.__init__(self) 
        print("Calling protected member of base class: ")
        print(self._a)
 
obj1 = Derived() 
#print(obj1.a)      
obj2 = Base()
# Calling protected member
# Outside class will  result in 
# AttributeError
print(obj2.a)'''

# Python program to 
# demonstrate private members
 
# Creating a Base class
'''class Base: # parent class
    def __init__(self):
        print("Parent class constructor called")
        self.a = "YCCE" # public data member
        self.__c = "IIM" #private member
 
# Creating a derived class/ child class
class Derived(Base):  # child class
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self) 
        print("Calling private member of base class: ")
        #print(self.__c)
# Driver code
obj1 = Derived()
#print(obj1.a)
#print(obj1.c) 
obj2 = Base()
print(obj2.c)'''
# raise an AttributeError

'''math = 50
print(id(math))
physics = 50
print(id(physics))
hindi = 45
print(id(hindi))'''










