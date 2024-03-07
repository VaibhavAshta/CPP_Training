'''An abstract class can be considered as a blueprint for other classes.
It allows you to create a set of methods that must be created within
any child classes built from the abstract class.
A class which contains one or more abstract methods is called an abstract class. 
An abstract method is a method that has a declaration but does not have an implementation. 

While we are designing large functional units we use an abstract class. 
When we want to provide a common interface for different implementations of a component, 
we use an abstract class.'''

'''
Why use Abstract Base Classes :
By defining an abstract base class, 
you can define a common Application Program Interface(API) for a set of subclasses.
This capability is especially useful in situations where a third-party is going to provide implementations, 
such as with plugins, but can also help you when working in a large 
team or with a large code-base where keeping all classes in your mind
is difficult or not possible.'''

'''
How Abstract Base classes work :
By default, Python does not provide abstract classes. 
Python comes with a module which provides the base for defining Abstract Base classes(ABC) 
and that module name is abc. 
ABC works by decorating methods of the base class as abstract and then registering 
concrete classes as implementations of the abstract base. 
A method becomes abstract when decorated with the keyword @abstractmethod. 
For Example –'''
'''from abc import ABC #(abstract base class), abstractmethod 
class Polygon(ABC):#abstract class
    # abstract method 
    @abstractmethod
    def noofsides(self): 
        pass

class Triangle(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 3 sides") 
  
class Pentagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides") 
  
class Hexagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides") 
  
class Quadrilateral(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 4 sides") 
  
# Driver code 


R = Triangle() 
R.noofsides() 
  
K = Quadrilateral() 
K.noofsides() 
  
R = Pentagon() 
R.noofsides() 
K = Hexagon() 
K.noofsides()'''



'''from abc import ABC, abstractmethod
class Programming(ABC): # abstract class
    @abstractmethod
    def training(self):# abstract method
        pass
     
    @abstractmethod   # abstract method
    def placement(self):
        pass

class Ashish(Programming):
    def training(self):
        print('C , C++ , Java')
    def placement(self):
        print("Java placement")

class Ankush(Programming):
    def training(self):
        print("Python | Django")
    def placement(self):
        print("Python placement students")

class Prashant(Programming):
    def training(self):
        print("Machine learning")
    def placement(self):
        print("Data science placement")

obj1 = Ashish()
obj1.training()

obj2 = Ankush()
obj2.training()

obj3 = Prashant()
obj3.training()'''

'''from abc import ABC, abstractmethod 

class Irctc(ABC):#abstract class

    @abstractmethod
    def bookTicket(self): # abstract method
        pass

class MakeMyTrip(Irctc):

    def bookTicket(self):
        source      = input("Enter a source station name")
        destination = input("Enter destination name")
        date        = input("Enter date")

class GoIbibo(Irctc):
    
    def bookTicket(self):
        print("    Welcome To GOIBIBO")
        source      = input("Enter a source station name")
        destination = input("Enter destination name")
        date        = input("Enter date")

class Yatra(Irctc):
    
    def bookTicket(self):
        print("    Welcome To Yatra.com   ")
        source      = input("Enter a source station name")
        destination = input("Enter destination name")
        date        = input("Enter date")

m = MakeMyTrip()
m.bookTicket()

g = GoIbibo()
g.bookTicket()

y = Yatra()
y.bookTicket()'''
















