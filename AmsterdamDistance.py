import sys, math

segments, rings, radius = [float(x) for x in input().split()]
x1, y1, x2, y2 = [int(x) for x in input().split()]

smallest_dist = 99999999999999999999
count = 0
while (y1 >= 0):
    arc_dist = abs(x2-x1) * (2*math.pi * (y1 / rings)*radius * (180/(segments*360)))
    seg_dist = abs(y2-y1) * (radius/rings) + count*(radius/rings)

    total_dist = arc_dist + seg_dist
    if (total_dist < smallest_dist):
        smallest_dist = total_dist

    y1 -= 1
    count += 1

print(smallest_dist)
