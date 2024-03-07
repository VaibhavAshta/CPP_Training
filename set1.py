myset={1,2,"sanjay",5.66,"rahul","ayush","ramesh","ankit",'rishikesh'} 
print(myset)
#print(myset[0])
#set is growable in nature, based on our requirement we can increase or decrease the size.   
#myset.add(60)
#print(myset)
# if we want to add more then one item then we should go for update()
# update() method can take multiple argument but all must be iterable
#myset.update(range(1,10,2))
'''myset.discard(3)
print(myset)
myset.remove(3)
print(myset)'''

#newset={1,2,3,"sanjay",5.66,"rahul","ayush"}   
#print(type(newset))
#print(newset)

'''fs=frozenset(myset)
print(type(fs))
print(fs)'''

# pop() method is used to remove object but pop() always remove from last

'''myset = {10,20,30,40}
yorset ={"prashant", "jha"}
newset = myset.union(yorset)
print(newset)'''

# union() this method will return newset

'''myset = {10,20,30,40}
yorset ={40,50,60,30}
newset = myset.union(yorset)
print(newset)'''
#union() method add yorset{} item into myset{}

'''mylist = [10,20,30,40]
print(mylist)
print(set(mylist))'''

# intersection return common element
'''myset = {10,20,30,40}
yorset ={10,50,60,30}
print(myset.intersection(yorset))'''

#  here set compresion is possible
# here indexing and slcing not possible on set object

# difference() method this will return the element prsent in myset but not in yorset
''''myset = {10,20,30,40}
yorset ={10,50,60,30}
print(myset.difference(yorset))'''
#clear()  we can use to clear data