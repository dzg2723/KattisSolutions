import sys
import math


while (True):
    people = int(input())
    if (people == 0):
        break
    endpoints = []
    for i in range(people):
        directions = input().split()
        x = float(directions[0])
        y = float(directions[1])
        angle = float(directions[3])
        

        for j in range(4,len(directions),2):
            if directions[j] == 'walk':
                dist = float(directions[j+1])
                x += dist * math.cos(math.radians(angle))
                y += dist * math.sin(math.radians(angle))

            elif directions[j] == 'turn':
                angle += float(directions[j+1])

        endpoints.append((x,y))

    average = [0,0]
    for point in endpoints:
        average[0] += point[0]
        average[1] += point[1]
    average[0] /= len(endpoints)
    average[1] /= len(endpoints)

    longest_dist = 0
    for point in endpoints:
        dist = math.sqrt((average[0] - point[0])**2 + (average[1]-point[1])**2)
        if dist > longest_dist:
            longest_dist = dist

    print (average[0], average[1], longest_dist)
