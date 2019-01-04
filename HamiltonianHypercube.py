import sys

values = input().split()
decimal_points = []

#Mathematics taken from http://mathworld.wolfram.com/GrayCode.html
for point in range(1,3):
    graycode = values[point] #string number
    graycode = [str(x) for x in graycode]

    for digit in range(len(graycode)-1, -1, -1):
        total = 0
        for i in range(digit-1, -1, -1):
            total += int(graycode[i])
        if (total%2) == 1:
            graycode[digit] = str(1 - int(graycode[digit]))
    binnum = "".join(graycode)
    decimal_points.append(int(binnum, 2))

print(decimal_points[1] - decimal_points[0] - 1)





