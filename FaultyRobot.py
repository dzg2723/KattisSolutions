import sys

def main():
    inp = sys.stdin.read().splitlines()
    print(inp)
    data = inp[0].split()
    num_of_nodes = int(data[0])
    num_of_edges = int(data[1])

    optional_paths = {x+1: [] for x in range(num_of_nodes)}
    forced_paths = {y+1: 0 for y in range(num_of_nodes)}

    #Build the two dictionaries
    for i in range(1, num_of_edges+1): #Skip first input
        path = inp[i].split()
        print(path)
        path[0] = int(path[0])
        path[1] = int(path[1])

        if (path[0] < 0):
            forced_paths[abs(path[0])] = path[1]
        else:
            optional_paths[path[0]].append(path[1])

    #Holds all nodes that the robot can stop on
    stopping_nodes = []

    #Move through nodes
    curr_node = 1
    visited_nodes = []
    deviant_nodes = []
    while True:
        
        #Stops if path begins to repeat
        if (curr_node in visited_nodes):
            break
        visited_nodes.append(curr_node)

        #Possible nodes accessible through 1 unforced path
        for node in optional_paths[curr_node]:
            deviant_nodes.append(node)

        #Move along the forced path if it exists
        if (forced_paths[curr_node] != 0):
            curr_node = forced_paths[curr_node]

        #No more forced paths
        else:
            stopping_nodes.append(curr_node) #Robot doesn't need to break rules
            break


    #Deviant nodes have already used their 1 bug
    #If Robot deviated to these nodes, find where it'll end through forced paths
    for node in deviant_nodes:
        explored_nodes = []
        exploring_node = node
        while True:
            #Stops if path begins to repeat
            if (exploring_node in explored_nodes):
                break
            explored_nodes.append(exploring_node)

            #Follow forced path
            if (forced_paths[exploring_node] != 0):
                exploring_node = forced_paths[exploring_node]

            #End of path, robot can stop here
            else:
                if exploring_node not in stopping_nodes:
                    stopping_nodes.append(exploring_node)
                break

    print(len(stopping_nodes))
        
        
        

import random
def makeInp(n,m):
    file = open("3.in", 'w')

    file.write("%d %d\n" % (n,m))

    forced_paths = n//2
    for i in range(1, forced_paths+1):
        file.write("%d %d\n" % (-i*2, random.randint(1, n)))

    other_paths = m - forced_paths
    for i in range(other_paths):
        file.write("%d %d\n" % (random.randint(1, n), random.randint(1, n)))

    file.close()

makeInp(900, 1850)
main()
