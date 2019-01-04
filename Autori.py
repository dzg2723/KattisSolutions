import sys
string = ""
for i in sys.stdin:
    spl_str = i.split('-')
result = ""
for i in spl_str:
    result = result + i[0]
print (result)
