import sys

for i in sys.stdin:
    i = int(i)
    count = 2
    divisors = [1]      #1 will divide all integers

    while (count**2 <= i):
        if (i % count == 0):    
            divisors.append(count)              #count is a divisor
            quotient = int(i/count)             #Also a divisor
            if (quotient not in divisors):      #Avoids repeats in case of squares
                divisors.append(int(i/count))    

        count += 1

    total = 0
    for value in divisors:
        total += value

    if (total == i):                #Check for perfect first
        print("%d perfect" % i)
        
    elif (total-2 <= i <= total+2):   #Check for almost perfect
        print("%d almost perfect" % i)

    else:
        print("%d not perfect" % i)
