''''class Faculty: # parent class
  def __init__(self, f_name, dpartment, f_id):
    self.f_name    = f_name
    self.dpartment = dpartment
    self.f_id      = f_id

  def print_info(self):
    print('faculty information=',self.f_name, self.dpartment, self.f_id)

obj = Faculty("Ashish", "computer_science", 1001)
obj.print_info() '''
#================================================================================
'''class Cse(Faculty): # child class
  pass  # no statement
obj = Cse("Jyoti mam", "computer_science", 1002)
obj.print_info() '''
#================================================================================
'''class Me(Faculty): # child class
  pass
obj = Me("xyz mam", "science", 1003)
obj.print_info()  '''
#=======================================================================
# Single level inheritance
'''class College: # parent class
  def college_name(self):
    print("Modern College")

class Student(College): # child class
  def student_info(self):
    print("Name:   Prashant Jha")
    print("Branch: Mechanical")

obj = Student()
obj.college_name()
obj.student_info()'''
#=========================================================================
# Multilevel inheritance
'''class College:   #first class  first- level
  def college_name(self):
    print("Modern College")
#============================================
class Student(College): #second class second - level
  def student_info(self):
    print("Name:   Prashant Jha")
    print("Branch: Mechanical")
#=============================================
class Exam(Student): #child class
  def subject(self):
    print("Subject1: Designe Engineering")
    print("Subject2: Math")
    print("Subject3: C-Language")

obj = Exam()
obj.college_name()
obj.student_info()
obj.subject()'''

#==============================================================
# Multiple inheritance
class SubjMarks: # class-1
  math = int(input("Enter paper marks of math"))
  DE = int(input("Enter paper marks of designe engineering"))
  c = int(input("Enter paper marks of c language"))
  english = int(input("Enter paaper marks of english"))
#================================= parent class -1
class PractMarks: # class-2
  cpract = int(input("Enter practicals marks of c language"))  
  
#================================= parent class -2

class Result(SubjMarks,PractMarks): # child class
  #print("if student pass in both = subject and practical paper then pass")
  def total(self):
    if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
      print("pass")
    else:
      print("fail")
 
obj = Result()
obj.total()
#print(issubclass(TotalMarks,SubjMarks))
  