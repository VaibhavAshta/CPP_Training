n=str(input("Enter your Name"))
clg=str(input("Enter your college Name:"))
cn=str(input("CLass Name: "))
rno=int(input("Roll No: "))

p1=int(input("Enter Marks of DAA :"))
p2=int(input("Enter Marks of OS:"))
p3=int(input("Enter Marks of NWT:"))
p4=int(input("Enter Marks of AI :"))
p5=int(input("Enter Marks of DS :"))

pr1=int(input("Enter Marks of NWT Practical :"))
pr2=int(input("Enter Marks of DAA Practical :"))
pr3=int(input("Enter Marks of AI Practical :"))
pr4=int(input("Enter Marks of DS Practical :"))

if p1>40 and p2>40 and p3>40 and p4>40 and p5>40 and pr1>=25 and pr2>=25 and pr3>=25 and pr4>=25:
    print('Pass')
    
else:
    print('fail')
    
total = p1+p2+p3+p4+p5
percentage = total/5

print("Total:",total)
print("Percentage:",percentage)
