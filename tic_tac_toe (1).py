import random

def print_board(board):
    print()
    for i in range(3):
        row = []
        for j in range(3):
            position = 3 * i + j
            if board[position] == None:
                row.append(str(position + 1))
            else:
                row.append(board[position])
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
 
    for win in wins:
        a = win[0]
        b = win[1]
        c = win[2]
        if board[a] != None and board[a] == board[b] and board[a] == board[c]:
            return board[a]
    return None
    
def is_draw(board):
    for cell in board:
        if cell == None:
            return False
        else:
            continue
    return True

def ai_move(board):
    empty = []
    for i in range(9):
    if board[i] == None:
        empty.append(i)
    return random.choice(empty)

def play():
    board = [None] * 9
    current = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, Computer is O")
    
    while True:
        print_board(board)
        
        # Player move
        if current == "X":
            move = input("Choose a position (1-9): ")
            if move == "1":
                move = 1
            elif move == "2":
                move = 2
            elif move == "3":
                move = 3
            elif move == "4":
                move = 4
            elif move == "5":
                move = 5
            elif move == "6":
                move = 6
            elif move == "7":
                move = 7
            elif move == "8":
                move = 8
            elif move == "9":
                move = 9
            else:
                print("Invalid input. Please enter a number 1–9.")
                continue
            move = move - 1

        if board[move] != None:
            print("Sorry, that spot is already taken.")
            continue
        else: #Computer
            move = ai_move(board)
            print("Computer chooses position", move + 1)
            
        #This will place X or O
        board[move] = current

        winner = check_winner(board)
        if winner != None:
            print_board(board)
            print(f"{winner} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        if current == "X":
            current = "O"
        else:
            current = "X"
play()
