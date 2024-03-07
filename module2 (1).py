#import module1 as mod #import and access as shortcut name
# accessing func.obj,class,var, etc from module as module name 

# first way

'''import module1
module1.welcome("prashant", "jha")
print(module1.pi)'''

#second way

'''import module1 as mod
mod.login('prashant', 'prashant')
mod.square(4)
print(module1.pi)'''





# third way

'''from module1 import square,pi
square(4)
print(pi)'''












from module1 import*
print(pi)
square(4)
welcome('prashant', 'jha')
login('xxx', 'kkk')


'''from module1 import square,add,welcome   #to import specific things
welcome('prashant', 'jha')
add(5)'''

'''from module1 import*
username=str(input("Enter username"))
password=str(input("Enter password"))
login(username,password)
print(pi)
square(2)
welcome('prashant','jha')'''

'''import module1
welcome("prashant","jha")'''



'''try:
  print(x)
except:
  print("An exception occurred")''' 

#print(x)

'''try:
  print(a)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
else:
        '''

#print(10/0)
'''try:
    print(10/0)
except ZeroDivisionError as msg:
    print("exception explanation is:",msg)'''

'''try:
    x=int(input("Enter First Number: "))
    y=int(input("Enter Second Number: "))
    print(x/y)
except ZeroDivisionError :
    print("Can not Divide with Zero")
except ValueError:
    print("we required int value only") '''   

'''try:
    x=int(input("Enter First Number: "))
    y=int(input("Enter Second Number: "))
    print(x/y)
except (ZeroDivisionError,ValueError) as msg:
    print("Can not Divide with Zero", msg)'''

#there is no guarentee for the execution of every statement inside try block always.  
'''try:
    print("hello")
except:
    print("except")
finally:
    print("this block is always executed even error occurs or not") '''

'''try:
    print(10/0)
except ZeroDivisionError:
    print("exception explanation is:")
finally:
    print("this is compulsory box")'''


'''try:  
    fileptr = open("Admission.txt","r")    
    try:  
        fileptr.write("Join python training") 
    except:
        print("") 
    finally:  
        fileptr.close()  
        print("file has been closed")  
except:  
    print("Error occure") ''' 

    
'''a = 10
pi= 3.14
name ='p'
print(type(a))
print(type(pi))
print(type(name))'''