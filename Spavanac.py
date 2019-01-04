start_time = input().split()
start_time[0] = int(start_time[0])
start_time[1] = int(start_time[1])


if (start_time[1] >= 45):
    print(start_time[0], start_time[1]-45)
else:
    overlap = 45 - start_time[1]
    start_time[0] -= 1
    start_time[1] = 60 - overlap
    if start_time[0] < 0:
        start_time[0] += 24

    print(start_time[0], start_time[1])
