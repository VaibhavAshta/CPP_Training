import csv
ID_list = []
with open('student.csv', mode ='+r',newline="")as f:
    r = csv.reader(f)
    ID_list = list(r)
    for i in ID_list:
        for j in i:
            print(i)
    