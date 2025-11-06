import random

def print_board(board):
    print()
    for i in range(3):
        row = []
        for j in range(3):
            cell = board[3*i + j]
            row.append(str(3*i + j + 1) if cell is None else cell)
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_draw(board):
    return all(cell != None for cell in board)

def ai_move(board):
    empty = [i for i in range(9) if board[i] is None]
    return random.choice(empty)

def play():
    board = [None] * 9
    current = "X"
    print("Tic-Tac-Toe (You = X, Computer = O)")

    while True:
        print_board(board)

        # Player move
        if current == "X":
            move = input("Choose a position (1-9): ")
            if not move.isdigit() or not (1 <= int(move) <= 9):
                print("Invalid move. Try again.")
                continue
            move = int(move) - 1
            if board[move] != None:
                print("That spot is taken.")
                continue
        else:
            move = ai_move(board)
            print(f"Computer (O) chooses {move + 1}")

        board[move] = current

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    play()