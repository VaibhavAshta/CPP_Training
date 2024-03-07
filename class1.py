'''class Hod: 
    def __init__(self):# constructor
        self.name='sonali' #data member
        self.age=21
        self.empid=1001

    def info(self):# instance method
        print("My name is :",self.name)
        print("My Age is:",self.age) 
        print("My emp id:",self.empid)  

obj = Hod()#object create
obj.info()'''

class Hod:
    def __init__(self,name,age,rollno): # parameterize constructor 
        self.name = name
        self.age = age
        self.rollno = rollno

    def show(self):
        print('name = ',self.name)
        print('age  = ',self.age)
        print('rollno =', self.rollno)

obj = Hod('Arjun',45,101)
obj.show()





# Garbage collector program
'''import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())'''


'''class Student:
    roll_number = 101
    num1 = 50
    num2 = 100   # data member

    def add(self):  #member function
        print(self.num1+self.num2)
        self.name = input("Enter name:")
        print(self.name)
    #-----------------------------------

obj = Student()
obj.add()
print(obj.roll_number)'''
#add,mul,div,sub by using class
#SI,Factorial,Fibnacci'''









'''class New:
    x=10    # data member inside of class

    def display(self):   # data member function of class
        print('hello python')

obj = New()
obj.display()
print(obj.x)
#print(obj.a)'''


'''class NewClass:
    def __init__(self): #constructor
        print("my name is constructor and i allways execute first")

    def show(self):   # member function inside of class
        print('welcome to class level programming')

obj = NewClass()
obj.show()
#obj2 = NewClass()'''



'''class NewConst:

    def __init__(self):
        print('i am constructor i always call automatically')

    def info(self):
        print('this is manually, using object we have to call')

    def show(self):
        print('this is for calling purpose')
obb = NewConst()
obb.show()
obb.info()'''

# declaring instance variable inside a constructor by using self variable.
'''class Student:
    def __init__(self):
        self.s_name   ="prashant" 
        self.l_name   ="jha" # instance variable
        self.s_rollno = 101
        self.s_branch = "CS"
        self.s_mb     = 000000000000

obj = Student()
print(obj.__dict__)'''

#declaring instance variable inside a instance method by using self variable.
'''class Student:
    def __init__(self):
        self.s_name   ="prashant"
        self.s_rollno = 101
        self.s_branch = "CS"
        
    def getdata(self):# instance method
        self.s_mb     = 28282828282

obj = Student() # untill and unless we call the method it will not not added to the object
obj.getdata()
print(obj.__dict__)'''

# declaring instance variable outside a class by using object
'''class Student:
    def __init__(self):
        self.s_name   ="prashant"
        self.s_rollno = 101      
    
    def getdata(self):
        self.s_mb     = 28282828282

obj = Student() 
obj.getdata()
obj.s_branch = "CS"   # adding instance variable by using object
print(obj.__dict__)'''

# accessing and deleting instance variable from the class
'''class Student:
    def __init__(self):
        self.s_name   =input("Enter your name")
        self.s_rollno = 101      
    
    def getdata(self):
        self.s_mb     = 28282828282

obj = Student() 
obj.getdata()
obj.s_branch = "CS"   # adding instance variable by using object
del obj.s_rollno      # deleteing a instance variable
print(obj.s_name)     # accessing a variable outside a class
print(obj.__dict__)'''
    
# for every object a seprate copy of instance variable created but in case of static variable only
# one copy will be created and it is accessble for every object of the class
'''class College:
    collegename= "Modern College"  #static variable (1 memory)

    def __init__(self):
        self.studentname = "prashant" #instance varible(3 seprate memory)

principal  = College() # object creation
teacher    = College()                 
accountant = College()                 
print("principal=",principal.collegename,"....",principal.studentname)
print("teacher  =",teacher.collegename,".....", teacher.studentname)
print("accountant=", accountant.collegename,"....", accountant.studentname)

College.collegename="HBD"  # second way to add static variable
principal.studentname="prashant jha"

print("principal=",principal.collegename,"|",principal.studentname)
print("teacher  =",teacher.collegename,"|", teacher.studentname)
print("accountant=", accountant.collegename,"|", accountant.studentname)'''


# where we can declare static varaible
#inside a class but outside of method
#in a constructor by using class name
#in a instance method by using class name
#in a classmethod using class name or cls varible
#staticmethod by using class name
#===================================================
# how do we access static variable
# inside instance method using self or class name
# in a constructor using self or class name
# in a class method using cls variable or class name
# in a static method using class name
# outside of the class using object or class name
#===================================================
# how to we delete the static variable 
# del classname.variablename
# inside classmethod we can use cls variable: del cls:variablename

# instance method example

'''class Student:
    def __init__(self, name, rollno, mob):
        self.name= name    # instance variable
        self.rollno= rollno
        self.mob = mob

    def display(self): # instance method
        print(self.name," ",self.rollno, " ",self.mob)

stud = Student("prashant", 1001, 6464646464)
stud.display()'''
'''
# static method =================================
class Student:
    # by using class name we can access static method
    @staticmethod # decorator (used to modify the behavior of the function)
    def get_personal_detail(firstname,lastname):
        print("your personal detail=",firstname,lastname)

    @staticmethod
    def contact_detail(mobil_no, rollno):
        print("your contact detail=", mobil_no,rollno)

Student.get_personal_detail("prashant", "jha")
Student.contact_detail(5456454646, 1001)'''

# implementing inner class concept
'''class BE_first_year:
    def __init__(self):
        self.college_name = "Modern College"
        self.branch_name = "CSE"
        self.objsem = self.FirstSem() # inner class 
    def display(self):
        print("College Name = ",self.college_name)
        print("branch_name  =", self.branch_name)
    # inner class
    class FirstSem:
        def __init__(self):
            self.sub1 = "M1"
            self.sub2 = "physics"
            self.sub3 = "chemistry"
            self.sub4 = "English"
            self.sub5 = "C-language"

        def show(self):
            print("subject1 =",self.sub1)
            print("subject2 =",self.sub2)
            print("subject3 =",self.sub3)
            print("subject4 =",self.sub4)
            print("subject5 =",self.sub5)

obj = BE_first_year()
obj.display()
objsem = obj.objsem
objsem.show()'''

# Destructor example
'''class Sample:
    def __init__(self):
        print("i am constructor")

    def __del__(self):
        print("i am destructor i am calling for clean up code")

obj = Sample()
print("end")'''

'''a = 10
pi = 3.14
name = 'prashant'
name2 = 'a'
print(pi)
print("Name = ",name)
print(type(a))
print(type(pi))
print(type(name))
print(type(name2))
print(id(a))
print(id(pi))
print(id(name))'''


'''class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs...'.format(name,cls.legs))

Animal.walk('Dog')
Animal.walk('Cat')  '''