import sys

##sys.stdin = open("1.in")
input_arr = []
for i in sys.stdin:
    input_arr.append(i.split())

for i in range(int(input_arr[0][0])):
    total = 0
    good_stu = 0
    for j in range(int(input_arr[i+1][0])):
        total += int(input_arr[i+1][j+1])
    average = float(total)/float(input_arr[i+1][0])
    for j in range(int(input_arr[i+1][0])):
        if (int(input_arr[i+1][j+1]) > average):
            good_stu += 1
    percent = 100.0*float(good_stu)/float(input_arr[i+1][0])
    print(str("{0:.3f}".format(percent)) + "%")
        
