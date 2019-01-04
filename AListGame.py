import sys

for i in sys.stdin:
    i = int(i)
    count = 2
    primes = []
    while (count**2 <= i):

        if (int(i) % count == 0):      #Num divides remaining value i
            primes.append(count)  #Num is prime and needed in the output
            i /= count           #Divide the remaining value i by num and loop again

        else:                   
            count += 1           #Increment 

    primes.append()
    print(len(primes))
