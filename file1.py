'''f = open("myfile.txt","w")
print("name of file",f.name)
print("file mode",f.mode)
print(" readeble ",f.readable())
print(" writeable ",f.writable())
print(" file has closed",f.closed)
f.close()
print(" file has closed",f.closed)'''

# performing write operation
'''f = open("covid.txt","a")
f.write("\n NGP is full vaccinated city")
f.close()
print("file operation is done")'''

# inserting list 
'''f = open("covid.txt","w")
mylist=["prashant","mahesh","suresh"]
f.writelines(mylist)   # here we can only pass string not int and float
f.close()
print("written work has done successfully")'''

# reading data from a file
'''f = open("covid.txt","r")
print(f.read())
print(f.read(5))
print(f.readline())
print(f.readlines())
f.close()'''

'''with open("myfile.txt","w") as f:
    f.write("amit\n")
    f.write("ashish\n")
    f.write("Prashant\n")
    print("file closed:",f.closed)

print("file closed:",f.closed)'''

# tell(), seek() method working
'''f = open("myfile.txt","r")
print("current index position of file pointer",f.tell())
print(f.read(5))'''

'''f = open("myfile.txt","r")
print("total data=", f.read())
print("current position of cursor", f.tell())
f.seek(5)
print("the current position of cursor", f.tell())
print(f.read())
f.close()'''

# reading and writing binary data

'''f1=open("Guido.jpg","rb")
f2=open("Rossom.jpg","wb")
data = f1.read()
f2.write(data)
print("New Image is available with the name:")'''

# operation with CSV file
import csv
f = open("student.csv","a",newline="")
a = csv.writer(f) # here it will return csvwriter object
a.writerow(["rollno","name","mobileno"])    
#rollno = 1001
#name= "prashant"
#mobileno =646464646
rollno = int(input("Enter your roll number"))
name   = input("Enter your name")
mobileno= int(input("Enter your mobile no"))
a.writerow([rollno,name,mobileno])
print("student record has save ")


# example of pickling and unpickling

'''import pickle
class Student:
    def __init__(self, s_name, s_rollno , s_class):
        self.s_name = s_name
        self.s_rollno = s_rollno
        self.s_class = s_class
    
    def show(self):
        print(self.s_name,"\n",self.s_rollno,"\n", self.s_class,"\n")

with open("myfile.txt","wb") as f:
    obj1 = Student("prashant",1001,5) # object creation
    pickle.dump(obj1,f)  # pickling has done
    print("pickling of student class object compleeted")

with open("myfile.txt","rb") as f:
    obj2 = pickle.load(f)
    print("unpickling of student class object compleeted")
    obj2.show()  '''   # unpickling  has done

'''import csv
p1=int(input("Enter paper1 marks"))
p2=int(input("Enter paper2 marks"))
p3=int(input("Enter paper3 marks"))

if p1>=40 and p2>=40and p3>=40:
    result = "pass"
    print("You are pass")
else:
    result = "fail"
total = p1+p2+p3
per   = total/3.0'''

'''import csv
f = open("student.csv","w",newline="")
a = csv.writer(f) # here it will return csvwriter object
a.writerow(["rollno","name","mobileno","p1","p2","p3","total","percentage","email","result"])
rollno = int(input("Enter your roll number"))
name   = input("Enter your name")
mobileno= int(input("Enter your mobile no"))
p1=int(input("Enter paper1 marks"))
p2=int(input("Enter paper2 marks"))
p3=int(input("Enter paper3 marks"))
email = input("Enter your email")

if p1>=40 and p2>=40and p3>=40:
    result = "pass"
    print("You are pass")
else:
    result = "fail"

total = p1+p2+p3
per   = total/3.0
#rollno,name,mobileno,p1,p2,p3,total,per,email,result=101,"ankush",4444,45,88,55,100,50,"p@gmail.com","pass"

a.writerow([rollno,name,mobileno,p1,p2,p3,total,per,email,result])
print("student record has save ")'''








# WAP input column name:= name,rollno,emaild,address,mobileno,p1,p2,p3,p4,p5,total,percentage,Result
# Input : = name,rollno,emaild,address,mobileno
# input :   = p1,p2,p3,p4,p5
# calculate: = total , Percentage
# condition:= if you will pass in all paper then result will be = pass else Fail 40
