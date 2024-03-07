'''# polymorphism example
class Principal:
    def role(self):
        print("i am managing all activity of college")

class Dean:
    def role(self):
        print('Dean= I am decision taking person')
        
class Hod:
    def role(self):
        print('Hod= I have responsibility of Teachers and Students')
        
class Faculty:
    def responsibilty(self):
        print('Faculty= I have to complete syllabus successfully')
# ========== class declaration completed=====================================

def  func(obj): # called func obj =1:Dean
    obj.role()# calling func
    
campus=[Principal(),Dean(),Hod(),Faculty()] 
for obj in campus: #obj =[0:principle ,1:Dean(),2:HOD(), 3:Faculty()]
    func(obj)   # calling fun'''
#=====================================================================================================
#The problem in this approach is if obj does not contain role() method then we will get AttributeError 
#But we can solve this problem by using hasattr() function. 
'''class Principal:
    def role(self):
        print("Principal= I am visiting in campus")

class Dean:
    def order(self):
        print('Dean= I am decision taking person')

def call(obj): # called fun
    obj.role()

obj = Principal()  # creating object of principal class
call(obj) # calling fun

obj = Dean()  # creating object of dean class
call(obj) # calling fun'''

#============Solution of above problem==============
'''class Principal:
    def role(self):
        print("Principal= I am visiting in campus")

class Dean:
    def order(self):
        print('Dean= I am decision taking person')

def call(obj): # called function
    if hasattr(obj,'role'):
        obj.role()
    elif hasattr(obj,'order'):
        obj.order()

obj = Principal()  # creating object of principal class 1
call(obj)# calling fun

obj = Dean()  # creating object of dean class 2
call(obj) # callling fun'''
#===============================================================================================
'''print('prashant'+'jha')
print(2+2)
print(2.5+2.5)'''
#print('prashant'*3)
#operator overloading
#operator overloading internally implemented by using magic method
'''class Deposit:
    def __init__(self,cash):
        self.cash = cash

d1=Deposit(1000)
d2=Deposit(2000)
print(d1+d2)'''
#magic method avilable for every operator  To overload any operator we have to override that Method in our class.
#the __add__ method is a magic method which gets called when we add two numbers using the + operator.
'''class Deposit:
    def __init__(self,cash):
        self.cash = cash

    def __add__(self,other):  # magic method
        return self.cash + other.cash

d1=Deposit(1000)
d2=Deposit(2000)
print("Total cash deposit amount=",d1+d2)'''

'''+ ==>   object.__add__(self,other)
   - ==>   object.__sub__(self,other) 
   * ==>   object.__mul__(self,other) 
   / ==>   object.__div__(self,other) 
   //==>   object.__floordiv__(self,other) 
   % ==>   object.__mod__(self,other) 
   **==>   object.__pow__(self,other) 
   += ==>  object.__iadd__(self,other) 
   -= ==>  object.__isub__(self,other) 
   *= ==>  object.__imul__(self,other) 
   /= ==>  object.__idiv__(self,other)
   //= =>  object.__ifloordiv__(self,other) 
   %=  =>  object.__imod__(self,other) 
   **= =>  object.__ipow__(self,other)
   <   =>  object.__lt__(self,other) 
   <= ==>  object.__le__(self,other) 
   >  ==>  object.__gt__(self,other) 
   >= ==>  object.__ge__(self,other) 
#=============================================================================================
#in Python Method overloading is not possible. 
#If we are trying to declare multiple methods with same name and
#different number of arguments then Python will always consider only last method. '''
'''class Arithmatic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj = Arithmatic()
obj.add(10)
obj.add(10,20)
obj.add(1,2,3)'''
# To handel overloaded method in python
#if method with variable number of arguments required then we can handle with default arguments 
'''class Arithmatic:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None:
            print(a+b)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)
        else:
            print("enter atleast two argument")
            
obj = Arithmatic()
#obj.add(10)
#obj.add(10,20)
obj.add(1,2,3)'''
#===========================================================================================
# contructor overloading
#Constructor overloading is not possible in Python. 
#If we define multiple constructors then the last constructor will be considered. 

'''class Arithmatic:
    def __init__(self):
        print("There is no argument")
    def __init__(self,a):
        print("passing one argument")
    def __init__(self,a,b):
        print("passing two arguments")

#obj = Arithmatic()
#obj = Arithmatic(10)
obj = Arithmatic(2,2)'''

#========================================================================================
#method overriding concept
'''class Father:# parent class
    def bike(self):
        print("harley Devidson")

    def laptop(self):
        print("laptop with 2GB RAM and 500GB HDD I3 processor")

class Aman(Father): # child class
    
    def laptop(self): # method overiding
        print("As per my programming software requarment this is not cool for me")
        print("laptop with 8GB RAM and 1TB HDD  I7")

obj = Aman()
obj.bike()
obj.laptop()'''

'''class Father:
    def bike(self):
        print("Bike")

    def laptop(self):
        print("laptop with 2GB RAM and 500GB HDD  of parent class")

class Child(Father):
    def laptop(self):
        super().laptop()# here we are calling parent class method using super()
        print("===============================================================")
        print("As per my programming software requarment this is not cool for me")
        print("laptop with 8GB RAM and 1TB HDD")

obj = Child()
obj.bike()
obj.laptop()'''
#===============================================================================
#Constructor overriding
'''class Father:
    def __init__(self):
        print("Father:= i am on time at breakfast table")

class Child(Father):
    def __init__(self):
        print("Child:= i will be late for breakfast")

obj = Child()'''

'''class Father:
    def __init__(self):
        print("Father:= i am on time at breafast table")

class Child(Father):
    def __init__(self):
           # using super() method we can call parent class constructor
        print("Child:= i will be late for breakfast")
        super().__init__()

obj = Child()'''