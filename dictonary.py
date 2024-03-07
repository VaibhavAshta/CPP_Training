# indexing and slicing are not possible in dictionary{key:value}
'''mydict =	{
  "name": "prashant",
  "professional": "developer",
  "empid":1001 
}
print(mydict)
print(type(mydict))'''

mydict =	{
  101: "prashant",
  102: "ashish",
  "103": "mohini",
  "104": "trivani",
  101: "ashish",
  104: "ashish"
}
print(mydict)

# with the help of key we have to print values
'''a =  mydict[102]
print(a)'''

# We will replace old value by new value
'''mydict[102]="peter"
print(mydict)'''


# only print key x=0,1
'''for x in mydict:
  print(x)'''

# only print values
'''for x in mydict.values():
  print(x)'''

# Priniting Key and Values both
'''for x, y in mydict.items():
  print(x, y)'''

'''mydict["mobile_no"]= 4646463738
print(mydict)

mydict["Department"] = "management"
print(mydict)'''

#imp: if we want to reprsent binary data like images, videos then we can go for bytes and bytearray
'''mydict =	{
  101: "prashant",
  "professional": "developer",
  "empid": 1001
}
mydict.pop(101)
print(mydict)'''
# pop() method remove pair by specific key name

'''mydict =	{
  "name": "prashant",
  "professional": "developer",
  "empid": 1001

}
newdict = mydict.copy()
print(newdict)'''

# in dictionary comprehension is possible TCS
'''fruits=['apple','banana','carrot']
fruits2=[i.lower() for i in fruits]
print(fruits2[2][0])'''
#ans c

'''x ="hello world"
print(x[::-1])'''
#ans = dlrowolleh
#question no 4

'''a = [20,5,33]
b = [20,5,3]
print(a<b)
#ans false
#Qno 8'''

# Q 10 3 option

'''d ={1:'one',2:'two',3:'three'}
di ={v:k for k, v in d.items()}
print(di)
Q 12 third option'''

#print('{#}'.format(1112223334))
#Q no 13 error

'''import array as arr
newArray = arr.array('i',[1,2,3,4])
print(newArray[::-1])
Q 14 third'''

'''x = (1,2,3)
x.append((4,5))
print(len(x))
error'''

'''a = 'help4code'
print('z'in a)'''



