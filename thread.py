'''from threading import *
import threading 
import time 
def activate():
    for i in range(1,11):
        time.sleep(2)
        print("This is chlid thread\n")
        
t = Thread(target=activate)
t.start 

for i in range(1,11):
    time.sleep(2)
    print("This is = ", threading.current_thread().getName())
   '''
'''from threading import *
import threading 
import time 
class MyThread(Thread):
    def run(self):
        for i in range(1,11):
            time.sleep(2)
            print("This is chlid thread\n")
        
obj_t = MyThread()
obj_t.start() 

for i in range(10):
    time.sleep(2)
    print("Main Thread -1")'''
    
from threading import *
class MyTest:
    def display(self):
        for i in range(10):
            print("This is chlid thread\n")
        
obj = MyTest()
t = Thread(target=obj.display)
t.start() 

for i in range(10):
    print("Main Thread -1")

from threading import *
import threading 
import time 
class MyThread(Thread):
    def run(self):
        for i in range(1,11):
            time.sleep(2)
            print("This is chlid thread\n")
        
obj_t = MyThread()
obj_t.start() 

for i in range(10):
    time.sleep(2)
    print("Main Thread -1")
    
from threading import *
import threading 
import time 
def activate():
    for i in range(1,11):
        time.sleep(2)
        print("This is chlid thread\n")
        
t = Thread(target=activate)
t.start 

for i in range(1,11):
    time.sleep(2)
    print("This is = ", threading.current_thread().getName())
    
from threading import *
class MyTest:
    def display(self):
        for i in range(10):
            print("This is chlid thread\n")
        
obj = MyTest()
t = Thread(target=obj.display)
t.start() 

for i in range(10):
    print("Main Thread -1")
    
'''import time
def add(num):
    for n in num:#[2,4,6,8,9]
        time.sleep(1)
        print("Addition=:", 2+n)
        print()
def mul(num):
    for n in num:
        time.sleep(1)
        print("Multipilcation =",n*n)
        print()
def sub(num):
    for n in num:
        time.sleep(1)
        print("Subraction =",n-n)
        print()
num=[2,4,6,8,9]        
starttime = time.time()
add(num)
mul(num)
sub(num)
print("Total time =",time.time()-starttime)'''

'''
import time
def add(num):
    for n in num:#[2,4,6,8,9]
        time.sleep(1)
        print("\tAddition= ", 2+n)
        print()
def mul(num):
    for n in num:
        time.sleep(1)
        print("\tMultipilcation= ",n*n)
        print()
def sub(num):
    for n in num:
        time.sleep(1)
        print("\tSubraction= ",n-n)
        print()
num=[2,4,6,8,9]        
starttime = time.time()
t1=Thread(target=add,args=(num,))
t2=Thread(target=mul,args=(num,))
t3=Thread(target=sub,args=(num,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Total time =",time.time()-starttime)
'''
 
    
