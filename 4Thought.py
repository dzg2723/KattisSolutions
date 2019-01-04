import sys

possibilities = {256: '4 * 4 * 4 * 4 = 256', 1: '4 - 4 + 4 / 4 = 1',
                 2: '4 / 4 + 4 / 4 = 2', 4: '4 - 4 / 4 / 4 = 4',
                 0: '4 - 4 - 4 + 4 = 0', 7: '4 - 4 / 4 + 4 = 7',
                 8: '4 - 4 + 4 + 4 = 8', 9: '4 + 4 + 4 / 4 = 9',
                 15: '4 * 4 - 4 / 4 = 15', 16: '4 - 4 + 4 * 4 = 16',
                 17: '4 / 4 + 4 * 4 = 17', 24: '4 + 4 + 4 * 4 = 24',
                 -60: '4 - 4 * 4 * 4 = -60', 32: '4 * 4 + 4 * 4 = 32',
                 60: '4 * 4 * 4 - 4 = 60', 68: '4 + 4 * 4 * 4 = 68',
                 -16: '4 - 4 - 4 * 4 = -16', -15: '4 / 4 - 4 * 4 = -15',
                 -8: '4 - 4 - 4 - 4 = -8', -7: '4 / 4 - 4 - 4 = -7',
                 -4: '4 / 4 / 4 - 4 = -4', -1: '4 - 4 - 4 / 4 = -1'}


count = 0
for i in sys.stdin:
    count += 1
    if (count == 1):                    #Ignore the first input
        continue
    try:
        print(possibilities[int(i)])    #Look for input in dictionary  
    except KeyError:
        print("no solution")            #Input is not a key, so it is not possible

