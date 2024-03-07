import re
count = 0
pattern = re.compile("Python")
matcher = pattern.finditer("Python knows the usual control flow statements that other languages speak — if, for, while and range — with some of its own twists, of course. More control flow tools in Python")
for i in matcher:
    count+=1
    print(i.start(),"....",i.end(),"...",i.group())
    