import time
import random

weapon = "Sword"

def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.\n")
    print_pause(f"Rumor has it that a {boss} is somewhere around here,"
                "and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark dave.\n")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger. \n")


def knock_on_the_door():
    print_pause("You approach the door of the house.\n")
    print_pause(f"You are about to knock on the door..Then,"
                "opens and here comes a {boss}.\n ")
    print_pause(f"Oh no! This is the {boss}'s HOME!\n")
    print_pause(f"The {boss} attacks!!!\n")
    print_pause("You feel not prepared for this.."
                "you only have a dagger!.\n")


def cave():
    print_pause("Peering into the cave..\n")
    print_pause("It's a very very small cave.\n")
    print_pause("There's  a huge piece of metal behind a rock.\n")
    print_pause("You found the sword of a thousand truths!\n")
    print_pause("You take it and wield it!")
    weapon.append("Sword")


def empty_cave():
    if "Sword" not in weapon:
        cave()
    else:
        print_pause("Peering into the cave..\n")
        print_pause("last time you grabbed the good loot."
                    "nothing is here now.\n")


def fight():
    fight_choice = input("What would you choose your fate as?"
                         "(1) fight or (2) Flee ?\n")
    if fight_choice == '1':
        if "Sword" in weapon:
            print_pause(f"As the {boss} moves in,"
                        "you take out your Sword\n")
            print_pause("The Sword of a Thousand Truths glimmers"
                        "you await the combat\n")
            print_pause(f"The {boss} sees the Sword of a Thousand Truths,"
                        "he immediately flees")
            print_pause("You've defeated the foe")

        else:
            print_pause("You've tried")
            print_pause(f"But the {boss} is way too strong.\n")
            print_pause("YOU LOSE!")

    elif fight_choice == '2':
        print_pause("You run away to the field. Fast!"
                    "there's no one behind you\n")

        game()

    else:
        print_pause("Please enter valid input.\n")
        fight()


def play_game_again():
    play_game = input("Wanna play again?"
                      "Yes or no?\n").lower()
    if "yes" in play_game_again():
        print_pause("Great! let's play again!")
        intro()
        game()
    elif "no" in play_game_again():
        print_pause("Thanks for playing")

    else:
        print_pause("Enter valid input\n")
        play_game_again()


def game():
    global boss
    boss = ["warlock", "warrior", "paladin", "rogue"]
    b = random.choice(boss)
    weapon = []

    game_choice = input("Enter 1 to knock on the door.\n"
                        "Enter 2 to enter the cave.\n"
                        "Which would you choose?\n"
                        "Enter 1 or 2?\n")
    if game_choice == '1':
        knock_on_the_door()
        fight()
        play_game_again()

    elif game_choice == '2':
        empty_cave()
        game()

    else:
        print_pause("Enter valid input.\n")
        game()
game()
intro()