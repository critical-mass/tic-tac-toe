from helpers import draw_board, check_turn, check_for_win
import os

spots = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # Reset screeen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # Check for invalid turn, let the user know
    if prev_turn == turn:
        print("invalid spot selected, please pick a different spot")
    prev_turn = turn
    print("playter " + str((turn % 2) +1 ) + "'s turn: pick your spot or press q to quit")
    choice = input()
    # Get user input
    if choice == 'q':
        playing = False
    # Check if the input is 1-9 int
    elif str.isdigit(choice) and int(choice) in spots:
        # Check if the spot is already taken
        if not spots[int(choice)] in {"X", "O"}:
            # If input meets criteria, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)
    # Check if the game has ended (and if someone won)        
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False

# Outside the, print the results 
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

if complete:
    if check_turn(turn) == 'X':
        print("Player 1 Wins!")
    else:
        print("Player 2 wins!")
else:
    print("No Winner")

print("Thanks for playing, you're both losers!")