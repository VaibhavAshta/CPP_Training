'''import csv
f = open("BuubleSort.csv","a",newline="")
a = csv.writer(f)
a.writerow(['ProductID',"Product_Name","Price"])
n = int(input("Enter the no. of records you want to enter:"))
for i in range(0,n):
    p_ID      = 100+i
    p_name    = input    ("Enter Product Name     : ")
    price     = int(input("Enter Product Price    : "))
    a.writerow([p_ID,p_name,price])
print("Record has been saved")'''

'''import csv
with open("BuubleSort.csv","r") as file:
    my_reader = csv.reader(file,delimiter=' ')
    for row in my_reader:
        print(row)
print(my_reader)

import pandas as pd

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(0,len(a) -i-1):
            if a[j] > a[j+1]:
                (a[j], a[j+1]) = (a[j+1], a[j])
d = my_reader
bubble_sort(d)
print("The sorted list is ")
print(d)
#continued in jupyter notebook
'''

        
