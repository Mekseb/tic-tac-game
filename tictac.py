from helper import drow_board,check_turn,check_winner
import os

spots = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
prev_turn = -1

playing = True
complete = False
turn = 0

while playing:
    os.system('cls'if os.name == 'nt' else 'clear')
    drow_board(spots)
    if prev_turn == turn:
        print("invalid spot pls enter again")
        prev_turn = turn
    print("player" + str((turn % 2)+1) + " is turn to pick your spot or press q to quite")
    choise = input()
    if choise == 'y':
        playing=False

    elif str.isdigit(choise) and int(choise) in spots:
        if not spots[int(choise)] in {"X","O"}:

            turn += 1
            spots[int(choise)] = check_turn(turn)
    if check_winner(spots):playing,complete =False,True
    if turn > 8:
        playing=False
    os.system('cls'if os.name == 'nt' else 'clear')
    drow_board(spots)

if complete :
    if check_turn(turn) == 'X': print('winner player1')

    else:
        print('The winner is player2')
else:
    print('no winner')
    print("thanks for playing")

