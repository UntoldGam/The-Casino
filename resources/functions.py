# IMPORTS

from os import system, name
from blackjack import blackjack
from higherorlower import higherorlower

# CLEAR FUNCTION

def clear():
    system('cls' if name == 'nt' else 'clear')

# GAMECHOICE FUNCTION

def gameChoice(member, money, dev_bypass):
    choices = {"h/l", "b"}
    choicefunctions = {"h/l": higherorlower, "bj": blackjack}
    name = member["name"]
    print(
        f"Welcome to game selection {name} \nYou currently have £{str(money)}")

    choiceMade = False
    if dev_bypass == True:
        choice = "h/l"  # for testing purposes
        choicefunctions[choice](member, dev_bypass)
        choiceMade = True
    while choiceMade == False:
        choice = input(
            "\nWhat game do you wish to play? \n B = Blackjack, H/L = Higher Or Lower \nYour choice: ")
        if choice.lower() in choices:
            function = choicefunctions[choice.lower()]
            function(member)
            choiceMade = True
        elif not choice.lower() in choices:
            choiceMade = False