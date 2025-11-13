# Basic Sequential Terminal Game
#Player Class (for rubric "Designing with Classes")
class Player:
    def __init__(self, name):
        # instance variables
        self.name = name
        self.wins = 0

    def add_win(self):
        # method to track wins
        self.wins += 1

#Game intro
def intro():
    print("========================================")
    print("          ADVENTURE GAME  ")
    print("========================================")
    print("\nThe kingdom of Eldoria has fallen into chaos.")
    print("Dark creatures roam the land, a fierce Dragon King rules the skies,")
    print("and deep within the ancient dungeon, a powerful Wizard awaits.")
    print("\nYou are a brave hero, chosen to restore peace to the realm.")
    print("To succeed, you must survive through 4 perilous levels:")
    print("  1  Face the wild goblin in the forest.")
    print("  2  Uncover the secret of the trapped chest.")
    print("  3  Confront the mighty Dragon King.")
    print("  4  Defeat the cunning Wizard in his final challenge.")
    print("\nYour courage and choices will decide the fate of Eldoria.")
    print("Prepare yourself, hero... your journey begins now!\n")
    
#Level 1, goblin encounter
def level_one():
    print("Level 1: You encounter a wild goblin!")
    action = input("Do you (A)ttack or (R)un? ").lower()

    if action == "a":
        print("You swing your sword and defeat the goblin!")
        return True
    elif action == "r":
        print("You try to run, but the goblin catches you. Game Over!")
        return False
    else:
        print("Invalid choice! You hesitate and the goblin strikes. Game Over!")
        return False

#Level 2, treasure chest
def level_two():
    print("\nLevel 2: You find a locked treasure chest.")
    action = input("Do you (O)pen it, (I)gnore it, or (S)mash it open? ").lower()

    if action == "o":
        print("You open it carefully and find a healing potion!")
        return True
    elif action == "s":
        print("You smash it open—BOOM! It's a trap. You lose.")
        return False
    elif action == "i":
        print("You ignore it and move on safely.")
        return True
    else:
        print("You waste too much time deciding. The dungeon collapses! Game Over.")
        return False

#Level 3, dragon king
def level_three():
    print("\nLevel 3: You face the Dragon King!")
    action = input("Do you (F)ight, (N)egotiate, or (R)un? ").lower()

    if action == "f":
        print("You battle bravely and slay the dragon! You win the game!")
        return True
    elif action == "n":
        print("You talk to the dragon and become allies. Victory through peace!")
        return True
    elif action == "r":
        print("You try to run, but the dragon burns you to ashes. Game Over!")
        return False
    else:
        print("Invalid input! The dragon strikes while you hesitate.")
        return False

#Level 4, the wizard (Tic-Tac-Toe)
def level_four():
    print("Level 4: Face the Wizard!")
    print("The Wizard challenges you to a game of Tic-Tac-Toe!")
    print("You are X, the Wizard is O. Defeat him to win the game!\n")

    import random
    
#Collections: Lists used for the board and winning positions
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
#Check for winner
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
        return True

    def ai_move(board):
        empty = []
        for i in range(9):
            if board[i] == None:
                empty.append(i)
        return random.choice(empty)

#game setup
    board = [None] * 9
    current = "X"
#Example of second collection type (dictionary)
    symbols = {"X": "You", "O": "Wizard"} #symbol to player name

# This is the Game loop 
    while True:
        print_board(board)
#Basic input
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
                print("That spot is already taken.")
                continue
        else: #Wizards move
            move = ai_move(board)
            print("Wizard chooses position", move + 1)
            
        #places the mark on the board
        board[move] = current

        #Check for the winner
        winner = check_winner(board)
        if winner != None:
            print_board(board)
            if winner == "X":
                print("You defeated the Wizard! You win the game!\n")
                return True
            else:
                print("The Wizard wins! Your adventure ends here.\n")
                return False
        #Check for draw
        if is_draw(board):
            print_board(board)
            print("It's a draw! The Wizard vanishes, letting you live.\n")
            return True
        #Switch turns
        if current == "X":
            current = "O"
        else:
            current = "X"
#Epilogue (Ending story)
def epilogue():
    print("\n--- EPILOGUE ---")
    print("As the Wizard’s final spell fades, the dungeon begins to tremble.")
    print("The torches flicker and the ground cracks beneath your feet.")
    print("You step forward, clutching your sword, as a soft light fills the room.")
    print("The Wizard’s staff shatters, releasing a burst of golden magic that restores peace to the land.")
    print("The goblins retreat to their caves, the dragons return to their mountains, and the realm is finally free.")
    print("You emerge from the dungeon into the sunlight—scarred but victorious.")
    print("Villagers cheer your name as tales of your bravery spread across the kingdoms.")
    print("You have proven yourself a true hero, not only by strength but by courage and wisdom.")
    print("\nThank you for playing the Adventure Game! The realm will forever remember your valor.\n")

#Game Flow/ levels
def main():
    name = input("Enter your hero's name:")
    player = Player(name)
    while True:
        intro()
        if not level_one():
            print("\nYou've died! Try again.\n")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print(f"Thanks for playing, {player.name}!")
                break
            else:
                continue

        if not level_two():
            print("\nYou've died! Try again.\n")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print(f"Thanks for playing, {player.name}!")
                break
            else:
                continue

        if not level_three():
            print("\nYou've died! Try again.\n")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print(f"Thanks for playing, {player.name}!")
                break
            else:
                continue

        if not level_four():
            print("\nYou've died! Try again.\n")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print(f"Thanks for playing, {player.name}!")
                break
            else:
                continue
        
        # If they complete all levels
        player.add_win()
        print(f"\nCongratulations, {player.name}! You have completed all levels and saved the realm!!")
        print(f"Total victories: {player.wins}")
        epilogue()
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != "y":
            print(f"Thanks for playing, {player.name}!")
            break
# Start the game
if __name__ == "__main__":
    main()
