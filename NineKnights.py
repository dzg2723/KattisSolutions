import sys

inp = sys.stdin.read().splitlines()

def main():

    knight_count = 0
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] == "k":
                knight_count += 1
                checkSquare(row-2, col+1)
                checkSquare(row-2, col-1)
                checkSquare(row-1, col+2)
                checkSquare(row-1, col-2)
                checkSquare(row+1, col+2)
                checkSquare(row+1, col-2)
                checkSquare(row+2, col+1)
                checkSquare(row+2, col-1)

    if knight_count != 9:
        print ("invalid")
    else:
        print("valid")

def checkSquare(row, col):
    try:
        if (row >=0 and col >=0):
            if (inp[row][col] == "k"):
                print ("invalid")
                raise sys.exit()
    except IndexError:
        pass

main()
