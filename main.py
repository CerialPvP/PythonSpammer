import os

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    from pynput.keyboard import Key, Controller
except:
    print("Trying to install required libraries...\n")
    os.system("pip install colorama")
    os.system("pip install pynput")
    print("\nRequired libraries should be installed.\nYou can go ahead and restart the program.\nIf that didn't work, try installing the libraries manually with \"pip install\":\ncolorama, pynput, keyboard")
    raise SystemExit()

# Read input.txt
try:
    file = open('input.txt', 'r')
except FileNotFoundError:
    print(Fore.RED+"[Error] The file 'input.txt' doesn't exist.\nPlease make a file named 'input.txt' in the same directory as this Python script.")
    raise SystemExit(1)

from time import sleep
import random

lines = file.readlines()
# Checkers for the input.
if f"{lines}" == "[]":
    print(Fore.RED+"You did not input anything in input.txt!\nExample for a spam message:\n"+Fore.CYAN+"Hello! {spam}")
    raise SystemExit(1)

# Gives you a warning if there is no spam variable.
if f"{lines}".find("{spam}") == -1:
    print(Fore.YELLOW+"[Warning] Some software may have a check for similar messages. It is recommended you put the {spam} tag in your desired message.")

print(Fore.GREEN+"[Ready] You have 3 seconds to switch to your desired program you want to spam on.\nTo stop the program at any moment comfortably, press 'S' on your keyboard.")
sleep(3)
kb = Controller()

# This is going to be the main spammer function.
# We will use this in loops.
def main_spam():
    # Now, we loop the lines.
    for loopLine in lines:
        # Now, we will add 1 to the break variable, and we will check if it's time to stop.
        progBreak += 1
        if progBreak == 10:
            print(Fore.CYAN+"[Program Break] It is time for a break.\nIf you need to stop it, press Ctrl+C.\nAfter 2 seconds, the program will keep running.")
            sleep(2)
            print(Fore.GREEN+"[Program Break] The break is over. The program will keep running.")
            progBreak = 0
        
        # First, we will make a random text out of ABC, numbers and symbols.
        uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
        lowercase = "qwertyuiopasdfghjklzxcvbnm"
        numbers = "0123456789"
        characters = "!@##$%^&*()_+-=[]{}\|;:'\"?/<>,."
        
        randomText = "["+(''.join(random.choice(uppercase+lowercase+numbers+characters) for i in range(30)))+"]"
        
        # Now, we will replace the {spam} in the messages.
        loopLine = loopLine.replace("{spam}", f"{randomText}")
        print(loopLine)
        
        # Now, typing the spam message.
        kb.type(loopLine+"\n")
        
        sleep(0.7)

