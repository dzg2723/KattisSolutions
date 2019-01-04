import sys

def main():

    inp = sys.stdin.read().splitlines()
    line1 = inp[0]
    line2 = inp[1]
    edge_length, max_chew, startID, honeyID, wax_cells = [int(z) for z in line1.split()]
    wax_cells = [int(y) for y in line2.split()]
    total_cells = (edge_length**3) - (edge_length-1)**3


    #Get rid of this initial case
    if (startID == honeyID):
        print (0)
        raise sys.exit()
    
    #List of lists: index Z contains list of points accessible in Z moves
    accessible_cells = [[startID]]
    
    for i in range(max_chew):

        accessible_cells.append([]) #new list of cells accessible at current moves

        #Follow all possible paths
        for cell in accessible_cells[i]:
            curr_row, curr_spot = combToGrid(cell, edge_length)

            #Determine how to point to adjacent cells
            if (curr_row < edge_length):
                adjacent = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, 0], [1, 1]]
            elif (curr_row == edge_length):
                adjacent = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, -1], [1, 0]]
            else:
                adjacent = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0]]
            
            #Check all adjacent cells to current position
            for a in adjacent:
                pot_cell = gridToComb(curr_row+a[0], curr_spot+a[1], edge_length)
                if (pot_cell != 0 and pot_cell not in wax_cells):
                    if(pot_cell not in accessible_cells[i] and pot_cell not in accessible_cells[i+1]): #TODO i-1??
                        if (i > 0):
                            if (pot_cell not in accessible_cells[i-1]):
                                accessible_cells[i+1].append(pot_cell)
                        else:
                           accessible_cells[i+1].append(pot_cell)

        #Check for honey block in currently accessible cells
        if (honeyID in accessible_cells[i+1]):
            print(i+1)
            raise sys.exit()
        

    print("No")
        

def combToGrid(combID, edge_length):
    remove = edge_length
    row = 1
    while (combID > remove):
        combID -= remove
        row += 1
        if (row <= edge_length):
            remove += 1
        else:
            remove -= 1
    slot = combID
    return (row, slot)

def gridToComb(row, slot, edge_length):
    #Handle DNE Cases
    if (row <= 0 or row > 2*edge_length-1):
        return 0
    
    if (slot <= 0) or (row <= edge_length and slot >= edge_length+row
                       ) or (row > edge_length and slot > (3*edge_length-row-1)):
        return 0
        
    combID = 0
    adder = 0
    for i in range(1, row):
        combID += edge_length + adder
        if ( i < edge_length):
            adder += 1
        else:
            adder -= 1
    combID += slot
    return combID

import random
def makeInp(edge_length, max_chew, startID, honeyID, wax_cells):
    file = open("3.in", 'w')
    file.write("%d %d %d %d %d\n" % (edge_length, max_chew, startID, honeyID, wax_cells))

    cap = (edge_length**3) - (edge_length-1)**3
    waxes = ""
    for i in range(wax_cells):
        new = random.randint(2, cap)
        if (i!=0):
            waxes = waxes + " " + str(new)
        else:
            waxes = str(new)

    file.write(waxes)
    file.close()

makeInp(20, 245, 1, 375, 105)
main()








        
