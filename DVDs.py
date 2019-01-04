test_cases = int(input())
for i in range(test_cases):
    first_pull = 0
    num_of_dvds = int(input())
    order = input().split()
    disc_dict = {}

    for k in range(len(order)):
        disc_dict[order[k]] = k
    
    for j in range(2, num_of_dvds+1):
##        if (order.index(str(j)) < order.index(str(j-1))):
        if (disc_dict[str(j)] < disc_dict[str(j-1)]):
            first_pull = j
            break

    if (first_pull == 0):
        print(0)
    else:
        print(num_of_dvds - first_pull + 1)


