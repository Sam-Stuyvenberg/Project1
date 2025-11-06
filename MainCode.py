# Basic Turn-Based Terminal Game

def intro():
    print(" Welcome to the Adventure Game!")
    print("You must survive through 3 levels to win!")
    print("Let's begin...\n")

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


# --- Game Flow ---
def main():
    intro()
    
    if not level_one():
        return
    if not level_two():
        return
    if not level_three():
        return

    print("\n Congratulations, hero! You have completed all levels!")

# Start the game
if __name__ == "__main__":
    main()
