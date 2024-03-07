








'''try:
    a = int(input("Enter first  no"))
    b = int(input("Enter second number"))
    print(a+b)
except:
    print(" Enter only decim value")

print(" Welcome to programming")'''






'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except:
    print("Enter any valid value")'''


'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except:
    print("plz ensure that you can't divide any no by zero")'''

'''def msg():
    print("helllo")'''
   


'''try:
    print(2/0)
    
except ZeroDivisionError as message:  # division by zero
    print("The description of exception:",message)'''



#a=int(input("enter first integer no"))
#b=int(input("enter second integer no"))
# multiple except block
'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except ZeroDivisionError as message:
    print("plz ensure that you can't divide any no by zero:",message)
except ValueError as message:
    print("Enter only interger no=>", message)'''

#Handling multiple diffrent kinds of exception with single except block. 
'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except (ValueError, ZeroDivisionError) as message:
    print(message)'''

# The concept of default except block , generly we used for writng normal message or showing normal error
'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except (ValueError, ZeroDivisionError) as message:
    print("Enter correct number: ",message)
except:
    print("This is default part of except block")'''

#IMP: If we have requarment of multiple except block then in that switiation default except block
# should be in last other wise syntax error will encounter 
'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except:
    print("This is default part of except block")
except (ValueError, ZeroDivisionError) as message:
    print("Enter correct number: ",message)'''


# We can use else block if no error will genrate it is depend on our own need and neccessity
'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except (ValueError, ZeroDivisionError) as message:
    print("Enter correct number: ",message)
else:
    print("Everything is ok")'''

# Finally block will always executed whether try block genrate error or not 
'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except (ValueError, ZeroDivisionError) as message:
    print("Enter correct number: ",message)
finally:
    print("I will allways executed")'''

# nested try except block
'''try:
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    try:
        print(a/b)
    except ZeroDivisionError as msg:
        print(msg)
    
except ValueError as msg:
    print(msg)'''


# (else) we can  use else block with try except and finally when there are no error  in try block

'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except (ZeroDivisionError, ValueError) as message:
    print(message)
else:
    print("there are no error in try block")
finally:
    print("i am finally block i always excuted wheather error raise or not")'''

# user defined exception by raise keyword 

bank_bal = 2000
if bank_bal>1000:
    raise Exception("your account balance is below a accessing limit")
else:
    print("Your amount has withdrawl")




'''class InterviewEligibal(Exception):
   pass

print("1.BE\n 2.Mtech\n 3.BCA\n 4.other")

choice = int(input("Enter your choice"))

if choice==1:
    raise InterviewEligibal("you are eligibal")
elif choice==2:
    raise InterviewEligibal("you are eligibal")
elif choice==3:
    raise InterviewEligibal("you are eligibal")
elif choice==4:
    raise InterviewEligibal("you are NOT eligibal")
else:
    print("you have entered wrong choice")'''

# python logging
'''import logging
logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
logging.debug("this indicates the debugging information")
logging.info("this indicates the important information")
logging.error("this indicates the error information")
logging.warning("this indicates the warning infromation")
logging.critical("this indicates the critical information")'''

'''import logging
logging.basicConfig(filename="newexception.txt", level=logging.DEBUG)
try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except (ZeroDivisionError,ValueError) as message:
    print(message)
    logging.exception(message)'''


'''a=int(input("enter first integer no"))
b=int(input("enter second integer no"))
print(a/b)'''
# assertion example
'''import time
markslist=[45,55,66,77,39]

for i in markslist:
    time.sleep(1)
    assert i<=40 ,"you are fail in this subject"
    print("you are pass in ", i)'''


'''a = 10
b = 16
print(id(a))
print(id(b))
print( a is not b)'''

'''a = 'help4code'
print('a' not in a)
print('e' in a)'''
