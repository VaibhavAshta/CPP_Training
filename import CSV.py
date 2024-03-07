'''import csv
from Module2 import *
f = open("student.csv","a",newline="")
a = csv.writer(f)
#a.writerow(['Roll No','Name',"Mobile No"])
roll_no   = int(input("Enter your Roll No  : "))
name      = input    ("Enter your name     : ")
mobile_no = int(input("Enter your Moblie No: "))
a.writerow([roll_no,name,mobile_no])
print("Student record has saved")

print("Read Record\n")
try:
    Enter_ID = int(input("Enter ID to search: "))
    if Enter_ID == ID_list:
        print("ID found",name)
except:
    print("Invaild ID")'''
    
import csv
f = open("info.csv","a",newline="")
a = csv.writer(f)
#a.writerow(['name','roll No','email_id',"address","mobile no","p1","p2","p3","p4","p5","total","percentage","result"])
name      = input    ("Enter your name     : ")
roll_no   = int(input("Enter your Roll No  : "))
email_id  = input    ("Enter your Email-ID : ")
address   = input    ("Enter your address  : ")
mobile_no = int(input("Enter your Moblie No: "))
p1         = int(input("Enter the marks of 1st subject: "))
p2         = int(input("Enter the marks of 2nd subject: "))
p3         = int(input("Enter the marks of 3rd subject: "))
p4         = int(input("Enter the marks of 4th subject: "))
p5         = int(input("Enter the marks of 5th subject: "))
total      = p1+p2+p3+p4+p5/5
percentage = total*100/500
if percentage >= 40:
    result="Pass"
else:
    result="Fail"
a.writerow([name,roll_no,email_id,address, mobile_no,p1,p2,p3,p4,p5,total,percentage,result])
print("Student record has saved")
        
    
    