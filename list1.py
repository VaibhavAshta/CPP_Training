mylist = ["prashant", "Ashish", "Rahul","ankit","komal","ankush","Ashish",77,"sandip",60.52,"prashant"]
print(mylist)
'''print(type(mylist))
print(mylist[0])
print(mylist[1])   
print(mylist[2])
print(mylist[-1])
print(mylist[2:5]) # n=5,n-1=4
print(mylist[:5])  # n=5 , n-1=4
print(mylist[1:]) # n=8, n-1=8-1=7
print(mylist[1:8:2])#1,3,5,7'''
#

'''mylist[2]="Pratik"
print(mylist)'''


'''print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
print(mylist[5])'''

'''for i in mylist:
    print(i)'''

'''i =0 prashant
i= 1 Ashish
i =2 Rahul
i =3 sandip
:
:
i = 11
train = 20'''



'''if "ankush" in mylist:
    print("yes ankush is avilable")
else:
    print('not avilable')'''

'''x=0
x=1
x=2
x=3
x=4
x=5'''

'''mylist.append('harsh')
mylist.append("laxman")
print(mylist)'''
#append() and extend() both work like same

# to add an item at specified position

'''mylist.insert(3,"vaishnavi")
print(mylist)'''

'''mylist.remove("sandip")
print(mylist)'''

'''newlist = mylist.copy()  # cloning
print(newlist)'''

'''mytuple = ("prashant", "Ashish", "Rahul","sandip","komal","ankush","rajesh",23,3.15,77,"sandip")
print(mytuple)
print(type(mytuple))
mytuple[2]="sunil"
print(mytuple)'''



mylist = [['prashant', 'jha'] , ['85.56'],[440022,"yyy"]]
'''print("example of multidimensional list: ")
print(mylist)
#print(mylist[row][col])
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])'''
#instead of multidimensional list Dictionary will be the better choice

'''list1=["prashant", "jha"]
#print(list1*2)
list2 =[50,25.50]
print(list1+list2)'''
# it will print two times

'''student_rollno=[]
for i in range(1,5): 
    student_rollno.append(i)
print("list of elements")
print(student_rollno)'''

'''list2 =[50,25.50,'prashant']
#del list2[0]
del list2
print(list2)'''

'''list2 =[50,25.50,'prashant']
print(list2)
list2.clear()
print(list2)'''

'''name="prashant"
print(name)
myname=list(name)#typecasting
print(myname)'''
# we have used list constructor

'''name= "help4code containing 5000 plus programs"
mylist = name.split()
print(mylist)
print(name)'''
# reverse() method'''

'''mylist = [40,30,20,10]
mylist.reverse()
print(mylist)'''


#sorting example
'''mylist=[44,22,77,0,9,88]#0,9,22,44,77,88
mylist.sort()
print(mylist)'''
# default sorting order for number is ascending order
# default sorting order for string is alphabetical order
# we should know that list should contain homogenious data otherwise we will get typeerror
# python2 first short number then string follow'''
#=========================================================================================

# Alising **********************************
# alising means assigining one variable reference to another variable
'''mylist=[44,22,77,0,9,88]
newlist = mylist
print(id(mylist))
print(id(newlist))'''

'''mylist=[44,22,77,0,9,88]
newlist = mylist
newlist[3] = 4
print(mylist)'''
# the problem is here if we are changing in one list then it reflecting in other also
# the solution of this problem is cloning (there are two ways first one is slicing [:] and second copy())
'''mylist=[44,22,77,0,9,88]
print(0 in mylist)
print(100 in mylist)'''

