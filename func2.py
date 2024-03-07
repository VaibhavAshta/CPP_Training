#default argument
'''def func(city = "Nagpur"):# called function
  print("I am from ", city )

func("Delhi")# calling function
func("LA")
func()'''

#unknown argument
'''def func(**name): # called function
  print("my name is " ,name["lname"])

func(fname = "prashant", lname = "jha") # calling function'''

# returning multiple value at a time'''

'''def add_product(a,b):#called function
    add=a+b
    product=a*b
    return add,product

x ,y = add_product(100,50)#calling function 5,6
print("The add is :",x)
print("The product is :",y)'''


'''def func(name):# called function name ["prashant","rahul","sandip","sunil"]
  for i in name:#i=0,1,2,3,4
    print(i)

name_of_p = ["prashant","rahul","sandip","sunil"]
func(name_of_p) # calling function'''


'''def func(name):
  for i in name:#i=0,1 prashant
    print(i)

name_of_p = "prashant"
func(name_of_p)'''



'''def func(name):
    j=0
    for i in name:
        if i=='n':
            print("the charatar present at index no",j,"value is :",name)
            break
        j=j+1

name=input("enter the name") # prashant
func(name)'''

# variable length argument/ variable number of argument
'''def name(*name):
  print(name)

name("Ashish","prashant","Tushar",1001)'''
