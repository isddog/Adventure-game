import time
import random


def get_random_characteristic():
    characteristics = ["pretty", "hungry", "gloomy"]
    characteristic = random.choice(characteristics)
    return characteristic


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1.5)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro():
    characteristic = get_random_characteristic()
    print_pause("You find yourself lost in the woods.")
    print_pause("You struggle to find a way back home.")
    print_pause("As you go on, you come across a damp, muddy swamp.")
    print_pause("Suddenly a " + characteristic + " monster jumps out"
                " and tries to attack you.")
    print_pause("You instantly look through your backpack for "
                "anything to defend yourself with.")


def mirror(characteristic):
    if "pretty" in characteristic:
        print_pause("The monster seems to enjoy it.")
        print_pause("Now is your chance to run!")
        print_pause("You run as fast as you can...")
        print_pause("...and hooray! You've make it back home!")
    else:
        print_pause("UH OH. The monster is furious.")
        print_pause("You try fighting back, but the monster is no match.")
        print_pause("You have been defeated!")
        play_again(characteristic)


def sandwich(characteristic):
    if "hungry" in characteristic:
        print_pause("The monster seems to enjoy it.")
        print_pause("Now is your chance to run!")
        print_pause("You run as fast as you can...")
        print_pause("...and hooray! You've make it back home!")
    else:
        print_pause("UH OH. The monster is furious.")
        print_pause("You try fighting back, but the monster is no match.")
        print_pause("You have been defeated!")
        play_again(characteristic)


def teddy(characteristic):
    if "gloomy" in characteristic:
        print_pause("The monster seems to enjoy it.")
        print_pause("Now is your chance to run!")
        print_pause("You run as fast as you can...")
        print_pause("...and hooray! You've make it back home!")
    else:
        print_pause("UH OH. The monster is furious.")
        print_pause("You try fighting back, but the monster is no match.")
        print_pause("You have been defeated!")
        play_again(characteristic)


def choose_item(characteristic):
    print_pause("Please enter the item of your choice: \n")
    item = input("mirror\n"
                 "sandwich\n"
                 "teddy\n")
    if "mirror" in item:
        mirror(characteristic)
    elif "sandwich" in item:
        sandwich(characteristic)
    elif "gloomy" in item:
        teddy(characteristic)
    else:
        print_pause("Sorry, I don't understand")
        choose_item(characteristic)


def play_again(characteristic):
    response = valid_input(" Would you like to play again?"
                           " Please say 'yes' or 'no'. \n ", "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good! Let's start over.")
        play_game(characteristic)
    else:
        print_pause("Sorry, I don't understand.")
        play_again(characteristic)


def play_game(characteristic):
    intro()
    get_random_characteristic()
    choose_item(characteristic)


characteristics = ["pretty", "hungry", "gloomy"]
characteristic = random.choice(characteristics)
play_game(characteristic)
