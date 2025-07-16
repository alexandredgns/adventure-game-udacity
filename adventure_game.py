import random
import time


def print_pause(message, wait_time):
    print(message)
    time.sleep(wait_time)


def intro():
    print_pause(
        "You find yourself standing at the edge of a dense, ancient "
        "forest shrouded in shadows.", 2
    )
    print_pause(
        "Rumors speak of lurking dangers and fierce enemies "
        "terrorizing the nearby villages.", 2
    )
    print_pause(f"Some villagers have spotted a {enemy} lurking nearby", 2)
    print_pause(
        "In front of you, an abandoned small castle looms — the "
        "silent hallways echo with strange noises and unsettling "
        "whispers, begging to be explored.", 3
    )
    print_pause(
        "To your right, a dark cave gleams with an eerie, flickering "
        "light deep within, promising secrets — perhaps treasure "
        "or menace— hidden in its depths.", 3
    )
    print_pause(
        f"In your hand you hold your trusty (but not very effective) "
        f"{weapon}", 2
    )


def where_to():
    print_pause("Enter 1 to go inside the castle", 2)
    print_pause("Enter 2 to peer into the cave", 2)
    print_pause("What would you like to do?", 1)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("Please enter 1 or 2\n")

    if choice == '1':
        castle()
    elif choice == '2':
        cave()


def combat(weapon):
    print_pause(f"The {enemy} attacks you!", 2)
    if weapon in weapons:
        print_pause(
            f"You feel under-prepared for this with only a small "
            f"{weapon}.", 2
        )

    choice = ''
    while choice not in ['1', '2']:
        choice = input("Would you like to Fight(1) or to Run Away(2)? ")
        if choice == '1':
            if weapon in weapons:
                print_pause("You do your best...", 1)
                print_pause(
                    f"But your {weapon} is no match for the {enemy}", 2
                )
                print_pause("You have been defeated!", 2)
            elif weapon == 'sword':
                print_pause(
                    f"As the {enemy} moves to attack, you unsheath your "
                    "new sword", 2
                )
                print_pause("The Sword of Doom shines in your hand!", 2)
                print_pause(f"The {enemy} looks at it and runs away!", 2)
                print_pause(
                    f"You have rid the villagers of the {enemy}. "
                    "You are victorious!", 2
                )

        elif choice == '2':
            print_pause(
                "You run back into the forest. Luckily, you "
                "were not followed.", 2
            )
            where_to()


def cave():
    global cave_visited
    global weapon
    print_pause("You peer cautiously into the cave", 2)
    if cave_visited:
        print_pause(
            "You've gotten all the good stuff, It's just an "
            "empty cave!", 2
        )
    else:
        print_pause("It is a dark and small cave", 2)
        print_pause("Your eyes catch a glint of a metal behind a rock", 2)
        print_pause("You have found the magical Sword of Doom", 2)
        print_pause(
            f"You discard your old {weapon} and take the sword with you", 2
        )
        weapon = 'sword'
    cave_visited = True
    print_pause("You walk back to the forest", 2)
    where_to()


def castle():
    print_pause("You approach the front gate", 2)
    print_pause(
        f"You enter the main hall, when suddenly the {enemy} appears!", 2
    )
    print_pause(f"This is the {enemy}'s house", 2)
    combat(weapon)


def play_again():
    print_pause("Would you like to play again? (y/n)\n", 1)
    choice = ''
    while choice not in ['y', 'n']:
        choice = input(
            "\nPlease enter 'y' for Yes or 'n' for No\n"
        )
    return 'running' if choice == 'y' else ''


game_state = 'running'
while game_state == 'running':
    enemies = ['vampire', 'dark elf', 'werewolf', 'dragon']
    enemy = random.choice(enemies)
    weapons = ['dagger', 'wooden axe', 'club']
    weapon = random.choice(weapons)
    cave_visited = False

    intro()
    where_to()

    game_state = play_again()
