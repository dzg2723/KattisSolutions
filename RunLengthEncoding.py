import sys


def encode(String):
    result = ""
    curr_char = String[0]
    count = 0
    for letter in String:
        if (letter != curr_char):
            result = result + curr_char + str(count)
            curr_char = letter
            count = 0
            count += 1
        else:
            count += 1

    result = result + curr_char + str(count)
    print(result)


def decode(String):

    result = ""
    for i in range(0, len(String), 2):
        for num in range(int(String[i+1])):
            result = result + String[i]
    
    print(result)

def main():
    inp = input().split()

    if inp[0] == 'E':
        encode(inp[1])
    else:
        decode(inp[1])
            
main()
