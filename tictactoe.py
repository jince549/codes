import random
import logo_art
board = ["_", "_", "_",
        "_", "_", "_",
        "_", "_", "_"]

human_player = "X"
com_player = "O"

def print_board(brd):
    print(brd[0] + " | " + brd[1] + " | " + brd[2])
    print("_________")
    print(brd[3] + " | " + brd[4] + " | " + brd[5])
    print("_________")
    print(brd[6] + " | " + brd[7] + " | " + brd[8])
    print("\n#################")


def player_input(brd):
    while True:
        try:
            player_move = int(input("Enter a number (1-9) :")) - 1
            if player_move >= 0 and player_move <=8 and brd[player_move] == "_":
                brd[player_move] = human_player
                break
            else:
                print("oops... Position already occupied, Try again")
        except ValueError:
            print("Enter a valid number")

def com_input(brd):
    while True:
        com_mov = random.randint(0, 8)
        if brd[com_mov] == "_":
            brd[com_mov] = com_player
            break
        

def check_win(brd):
    if brd[0] == brd[1] == brd[2] and brd[0] != "_":
        return True
    elif brd[3] == brd[4] == brd[5] and brd[3] != "_":
        return True
    elif brd[6] == brd[7] == brd[8] and brd[6] != "_":
        return True
    elif brd[0] == brd[3] == brd[6] and brd[0] != "_":
        return True
    elif brd[1] == brd[4] == brd[7] and brd[1] != "_":
        return True
    elif brd[2] == brd[5] == brd[8] and brd[2] != "_":
        return True
    elif brd[0] == brd[4] == brd[8] and brd[0] != "_":
        return True
    elif brd[2] == brd[4] == brd[6] and brd[2] != "_":
        return True
    else:
        return False

def tie(brd):
    if "_" not in brd:
        return True
        
print(logo_art.logo)
while True:
    print(("Player move\n-----------------"))
    print_board(board)
    player_input(board)
    if check_win(board):
        print("####################### PLAYER WINS!!! #######################")
        break
    if tie(board):
        print("Tie!!!")
        break
    print("Computer played...")
    print()
    com_input(board)
    if check_win(board):
        print("####################### COMPUTER WINS!!! #######################")
        break
    if tie(board):
        print("Tie!!!")
        break
    
print_board(board)
