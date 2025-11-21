import os
from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def ask_password(prompt, password, tip=None):
    while True:
        os.system("cls")
        if tip:
            print(tip)
        guess = input(prompt + "\nAnswer: ").lower()
        if guess == password.lower():
            print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
            sleep(2)
            break
        else:
            print(Fore.RED + "Wrong, try again!" + Style.RESET_ALL)
            input("Press Enter to try again...")

def lvl1():
    tip = "This is level one while im writing this i have no idea what im doing\nWhzzdvyk:(sla tll pu)"
    ask_password("" ,"let mee in", tip)
    lvl2()
def lvl2():
    prompt = "What word in the English Language is always spelled incorrectly?"
    ask_password(prompt, "incorrectly")
    lvl3()
def lvl3():
    tip = "Tip: Don't use space between them\n16,1,19,19,23,15,18,4,9,19,9,12,15,22,5,2,15,25,19"
    ask_password("", "iloveboys", tip)
    print(Fore.GREEN + "Congratulations! You completed all 3 levels!" + Style.RESET_ALL)
    lvl4()
def lvl4():
    prompt = "Decode this."
    ask_password(prompt,"42isTheAnswer","01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01101001 01110100 01111010 00101101 01101000 01110111 01101101 01101110 00101110 01100111 01101001 01110100 01101000 01110101 01100010 00101110 01101001 01101111 00101111 01110011 01100101 01100011 01110010 01100101 01110100 00101101 01100111 01100001 01101101 01100101 00101111 01100110 01101001 01101001 01100101 01100110 01101001 01000010 01000110")

if __name__ == "__main__":
    # Game intro
    print("Hey Guys!")
    print("I felt bored so I made this game")
    print("Try figuring out how levels work")
    print("Enjoy!")
    sleep(5)
    os.system("cls")

    # Start the game
    lvl1()
