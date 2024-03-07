'''import re  # re module for performing all the regular expression based operation
count=0
pattern = re.compile("python")
matcher = pattern.finditer("A function in python is defined by a def statement. python The general syntax looks like this: def function-name(Parameter list): statements, i.e. the function body. The parameter python list consists of none or more parameters. Parameters are called arguments, if the function is called python.")
#print(matcher)
for i in matcher:   #i=1
    count+=1 
    print(i.start(),"...",i.end(),"...",i.group())

print("The number of occurrences: ",count)'''



'''import re  
count=0 
matcher=re.finditer("Hi","HiaHiHiaHi")
for i in matcher:# loop 4 times execute
    count+=1 
    print(i.start(),"...",i.end(),"...",i.group())
print("The number of occurrences: ",count)'''


'''import re
obj = input("enter any charecter")
objmatch=re.finditer(obj,"a7b @k9z")
for match in objmatch:
    print(match.start(),"...",match.end(),"...",match.group())'''

# here we are checking quntifiers i.e the no of times match occure
'''import re
obj = input("enter any string =")
objmatch=re.finditer(obj,"hiprashanthowareyouprashant")
for match in objmatch:
    print(match.start(),"......",match.group())'''

#match() function operation
'''import re
a = input("enter string to perform match operation: ")
mtch = re.match(a, "pythonisveryimportant")
print(mtch)
if mtch!=None:
    print("match found at begining level")
    print(mtch.start(), " ", mtch.end())
else:
    print("there is no matching at begining level")'''
#========================================================
#fullmatch()'''
'''import re
a = input("enter string to perform match operation:")
mtch = re.fullmatch(a, "pythonisvery")
print(mtch)
if mtch!=None:
    print("match found at begining level")
    print(mtch.start(), " ", mtch.end())
else:
    print("there is no matching at begining level")'''
#==========================================================
# search() function

'''import re
a = input("enter string to perform match operation :")
mtch = re.search(a, "pythonisssdynamiclannn")
print(mtch)
if mtch!=None:
    print(mtch.start(), " ", mtch.end())
else:
    print("there is no matching at begining level")'''
#==========================================================
# findall() function
'''import re
mtch = re.findall('[a-z0-9]',"abch3hdh5bk6")
print(mtch)'''
#==========================================================
#sub() function
'''import re
obj = re.sub('[0-9]','*','ab3gd6nkl7')
print(obj)'''
#==========================================================
#subn() function
'''import re
obj = re.subn('[0-7]','@','ab3gd6nkl7')
print(obj)
print("the string is=",obj[0])
print("the number of replacement is=",obj[1])'''
#1234$dhfj$123dfgh$sdfghjk
#===========================================================
# split() function
'''import re
obj = re.split()
print(obj)'''

'''for o in obj:
    print(o)'''
#===========================================================
# WAp to check the valid mobile number
import re
mo = input("Enter mobile number")
obj =re.fullmatch("[0-9]\d{9}",mo) #(0,1,2,3,4,5,6,7,8,9)\d
if obj!=None:
    print("valid mobile number")
else:
    print("invalid mobile number")








