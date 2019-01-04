import sys
def main():
    inp = [int(x) for x in input().split()]

    p = inp[0]
    q = inp[1]
    s = inp[2]


    a = 0
    b = 0

    a += p
    b += q
    while (a <= s or b <= s):
        if (a == b):
            print ("yes")
            raise sys.exit()
        elif (a < b):
            a += p
        else:
            b += q

    print("no")
            
main()
