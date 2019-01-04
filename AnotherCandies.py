import sys

testcases = int(input())
for i in range(testcases):
    blank_space = input()
    students = int(input())
    candies = 0

    for j in range(students):
        candies += int(input())

    if (candies % students == 0):
        print("YES")
    else:
        print("NO")

