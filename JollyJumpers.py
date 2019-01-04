import sys

##sys.stdin = open("1.in")
for i in sys.stdin:
    input_list = i.split()
##    input_list = [1, 5, 6, 8, 12, 17]
    difference_list = []
    for j in range(2,len(input_list)):
        dif = abs(int(input_list[j]) - int(input_list[j-1]))
        if (dif not in difference_list and dif < len(input_list)-1):
            difference_list.append(dif)
        else:
            print("Not jolly")
            break
    if (len(input_list)-2 == len(difference_list)):
        print("Jolly")
        
        
