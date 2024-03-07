


''''def login():# called function
    while True:
        username = input("Enter your username")
        password = input("Enter your password")
        if username ==  password:
            print("login successfully")
            break
        else:
            print("you have entered wrong credentials")

#calling function
login()'''

# function defination
'''import time
def msg(): # called function
    print("hello world")

msg() # calling function
time.sleep(2)
msg() 
time.sleep(2)
msg()'''
'''import time
def welcome():# called function
    print("Welcome to python class")

print('first time call')
welcome()# calling function
time.sleep(2)
print('second time call')
welcome()
time.sleep(2)
print('third time call')
welcome()
print('fourth time call')
welcome()'''


'''def hello():#called function     
    print(" hello python")


hello()# calling function
hello()
hello()'''


'''def info(firstname,lastname): # called function positional argument
    print('First name=', firstname)
    print('Last name=', lastname)

info('prashant','jha') # calling function'''


'''def addition(value): #Called func
    print("addition of two no=", value+value)


addition(5)# calling func'''

#positional argument passing in correct order

'''def add(num1,num2):
    return num1+num2

result =add(2,3)# calling function

print(result)'''













'''def arithmatic(a,b): # called function
    r = a+b
    n = a*b
    m = a-b
    return r,n,m

result = arithmatic(10,5)#calling function
print("Result = ", result)'''

'''def chk_even_odd(number):
    if number%2==0:
        print(number,"This is Even Number")
    else:
        print(number,"This is Odd Number")

chk_even_odd(5)# calling function
chk_even_odd(10)'''


'''def func(fname,lname):#called function
    print("Hi",fname)
    print("Hi",lname)

#func(fname="prashant",lname="jha")#calling function
fname = input("Enter first name")
lname = input("Enter last name")
func(fname, lname) #calling function'''
# keyword arguments:
# We can pass argument values by keyword i.e by parameter name.
# here order is not matter but argument should be matched

'''def add(v1, v2):
    r = v1+v2
    return r

v1= int(input("Enter value one"))
v2= int(input("Enter value two"))
result = add(v1,v2) # calling function
print(result)'''


'''def add(val1, val2):
    add = val1+val2
    return add

result = add(5,6)
print("Add of two no =",result)'''
