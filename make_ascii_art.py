from art import *
from os import system, name


def clear():
    # For windows
    if name == 'nt':
        _ = system('cls')
    # for mac
    else:
        _ = system("clear")


make_art = input("Would you like to make ascii art?\n").lower()
while make_art == "yes":
    clear()
    the_thing = input("What would you like to see as ascii art?\n")
    font = input("""What font?(type none to pass)
    fonts:
    block
    small
    cybermedium
    white_bubble
    shasha
    fari
    sheqi
    random for random\n""").lower()
    if font == "none":
        tprint(the_thing)
    else:
        tprint(the_thing, font=font)
    make_art = input("Would you like to make more ascii art?\n").lower()
clear()
print("Goodbye")