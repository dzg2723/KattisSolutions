import sys

input_list = []
result_list = [0,0,0]
##sys.stdin = open("2.in")
for i in sys.stdin:
    input_list.append(i.split())
for i in range(len(input_list[0])):
    input_list[0][i] = int(input_list[0][i])
input_list[0].sort()
result_list[input_list[1][0].index("A")] = str(input_list[0][0])
result_list[input_list[1][0].index("B")] = str(input_list[0][1])
result_list[input_list[1][0].index("C")] = str(input_list[0][2])

print (" ".join(result_list))
