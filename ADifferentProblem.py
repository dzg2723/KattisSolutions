import sys

for i in sys.stdin:
    val_one, val_two = i.split()
    solution = abs(int(val_one) - int(val_two))
    print(solution)
