import queue, sys

def main():

    inp = sys.stdin.read().split()

    num_of_syllables = int(inp[0])
    num_of_players = int(inp[1])

    #[playerNumber, Status]
    W = 'W' #Player has whole coconut
    F = 'F' #Fist
    O = 'O' #Open

    #Fill queue with each player
    game_queue = queue.Queue()
    for player in range(1, num_of_players+1):
        player_object = [player, W]
        game_queue.put(player_object)

    #Each round of game
    while (game_queue.qsize() > 1): 

        #Go through syllables except for last one
        for syllable in range(num_of_syllables-1):
            next_player = game_queue.get()
            game_queue.put(next_player)

        #Last Syllable
        unlucky_player = game_queue.get()
        if (unlucky_player[1] == W):            
            length = game_queue.qsize()                 #Get length first
            game_queue.put( [unlucky_player[0], F] )    #Add fists
            game_queue.put( [unlucky_player[0], F] )
            resetQueue(game_queue, length)              #Put both fists at start of queue

        elif(unlucky_player[1] == F):
            game_queue.put( [unlucky_player[0], O] )


    #One player left
    winner = game_queue.get()
    print(winner[0])

def resetQueue(queue, length):
    for item in range(length):
        player = queue.get()
        queue.put(player)
    

main()


