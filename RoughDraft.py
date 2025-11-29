# Basic Sequential Terminal Game
import random

#Classes
class Player:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.inventory = []
        self.wins = 0  # keeps track of wins

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to {self.name}'s inventory.")

    def show_inventory(self):
        print(f"{self.name}'s Inventory:")
        if not self.inventory:
            print("  (empty)")
        else:
            i = 1
            for item in self.inventory:
                print("  " + str(i) + ". " + item)
                i += 1

    def add_win(self):
        self.wins += 1
        print(f"{self.name} now has {self.wins} win(s).")

    def show_stats(self):
        print(f"{self.name} - Level {self.level}, Wins: {self.wins}")
        self.show_inventory()

    def __str__(self):
        return f"{self.name} (Level {self.level})"
    
    def save_to_file(self, filename="player_save.txt"):
        with open(filename, "w") as file:
            file.write(self.name + "\n")
            file.write(str(self.level) + "\n")
            file.write(str(self.wins) + "\n")
            file.write(",".join(self.inventory) + "\n")
        print("Progress saved successfully!")

    @staticmethod
    def load_from_file(filename="player_save.txt"):
        try:
            with open(filename, "r") as file:
                name = file.readline().strip()
                level = int(file.readline().strip())
                wins = int(file.readline().strip())
                inventory_line = file.readline().strip()

            player = Player(name, level)
            player.wins = wins
            if inventory_line:
                player.inventory = inventory_line.split(",")
            else:
                player.inventory = []

            print(f"Save file loaded! Welcome back, {name}.")
            return player

        except FileNotFoundError:
            return None
    
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
def level_one(player):
    print("Level 1: You encounter a wild goblin!")
    action = input("Do you (A)ttack or (R)un? ").lower()
    if action == "a":
        print("You swing your sword and defeat the goblin!")
        player.add_item("Goblin Dagger")
        return True
    elif action == "r":
        print("You try to run, but the goblin scratches you. Game Over!")
        return False
    else:
        print("Invalid choice! You hesitate and the goblin strikes. Game Over!")
        return False


#Level 2, treasure chest
def level_two(player):
    print("\nLevel 2: You find a locked treasure chest.")
    action = input("Do you (O)pen it, (I)gnore it, or (S)mash it open? ").lower()
    if action == "o":
        print("You open it carefully and find a mysterious artifact!")
        player.add_item("Mysterious Artifact")
        player.level += 1
        return True
    elif action == "s":
        print("You smash it open—BOOM! It's a trap. Game Over!")
        return False
    elif action == "i":
        print("You ignore it and move on safely.")
        return True
    else:
        print("You waste too much time deciding. The dungeon collapses! Game Over.")
        return False

#Level 3, dragon king
def level_three(player):
    print("\nLevel 3: You face the Dragon King!")
    action = input("Do you (F)ight, (N)egotiate, or (R)un? ").lower()
    if action == "f":
        print("You battle bravely and slay the dragon!")
        player.add_item("Dragon Scale Shield")
        player.level += 1
        return True
    elif action == "n":
        print("You talk to the dragon and become allies. Victory through peace!")
        player.add_item("Dragon Ally Token")
        player.level += 1
        return True
    elif action == "r":
        print("You try to run, but the dragon burns you to ashes. Game Over!")
        return False
    else:
        print("Invalid input! The dragon strikes while you hesitate. Game Over!")
        return False

#Level 4, the wizard (Tic-Tac-Toe)
def level_four(player):
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
            a,b,c = win
            if board[a] != None and board[a] == board[b] and board[a] == board[c]:
                return board[a]
        return None

    def is_draw(board):
        return None not in board
    
    def ai_move(board):
        empty = []
        for i in range(len(board)):
            if board[i] is None:
                empty.append(i)
        return random.choice(empty)

    #game setup
    board = [None] * 9
    current = "X"
    symbols = {"X": "You", "O": "Wizard"}

# Game loop 
    while True:
        print_board(board)

        if current == "X":
            move = input("Choose a position (1-9): ")

            # Input check
            if move not in ["1","2","3","4","5","6","7","8","9"]:
                print("Invalid input. Please enter a number 1–9.")
                continue

            move = int(move) - 1  # Convert to board index

            if board[move] is not None:
                print("That spot is already taken.")
                continue

        else:
            # Wizard's turn
            move = ai_move(board)
            print("Wizard chooses position", move + 1)

        # Place the X or O
        board[move] = current

        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "X":
                print("You defeated the Wizard! You win the game!\n")
                player.add_item("Wizard's Staff")
                player.level += 1
                return True
            else:
                print("The Wizard wins! Your adventure ends here.\n")
                return False

        # Check for draw
        if is_draw(board):
            print_board(board)
            print("It's a draw! The Wizard vanishes, letting you live.\n")
            return True

        # Switch players
        if current == "X":
            current = "O"
        else:
            current = "X"

def level_five():
    print("\nLevel 5: The Final Riddle of Eldoria!")
    print("A mystical voice echoes through the chamber:")
    print('"Answer my question, hero, and the realm shall be forever free..."')
    print()
    print("Riddle: The more there is, the less you see. What could I be?")
    answer = input("Your answer: ").strip().lower()

    if "darkness" in answer:
        print("\nThe air shimmers — the voice laughs. 'You are wise indeed, hero.'")
        print("The final seal is broken! You have conquered every challenge!")
        return True
    else:
        print("\nThe chamber shakes... 'Wrong!' the voice booms. You are cast into darkness!")
        return False

#Epilogue
# 
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

#main
def main():
    
   player = load_or_create_player()

    while True:
        intro()

        # Level 1
        if not level_one(player):
            print("\nYou failed Level 1! Try again.\n")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print(f"Thanks for playing, {player.name}!")
                break
            else:
                continue

        # Level 2
        if not level_two(player):
            print("\nYou failed Level 2! Try again.\n")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print(f"Thanks for playing, {player.name}!")
                break
            else:
                continue

        # Level 3
        if not level_three(player):
            print("\nYou failed Level 3! Try again.\n")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print(f"Thanks for playing, {player.name}!")
                break
            else:
                continue

        # Level 4 (Tic-Tac-Toe)
        if not level_four(player):
            print("\nYou failed Level 4! Try again.\n")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print(f"Thanks for playing, {player.name}!")
                break
            else:
                continue

        # Level 5
        if not level_five():
            print("\nYou failed Level 5! Try again.\n")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print(f"Thanks for playing, {player.name}!")
                break
            else:
                continue


        # If all levels completed
        player.add_win()
        print(f"\nCongratulations, {player.name}! You have completed all levels and saved the realm!")
        print(f"Total victories: {player.wins}")
        epilogue()
        player.show_stats()

        # Ask to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print(f"Thanks for playing, {player.name}!")
            break

if __name__ == "__main__": 
    main()
