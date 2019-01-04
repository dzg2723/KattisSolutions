import sys

def main():
    data = sys.stdin.read().splitlines()
    num_of_sets = int(data[0])
    print(data)
    
    for inp in range( 1, num_of_sets+1 ):
        k, days = data[inp].split()
        days = int(days)
        
        total = days * (days+1) / 2
        total += days
        
        print(str(inp) + " " + str(int(total)))

main()

