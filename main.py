import os
from platform import node
import sys
from typing import List

args: List[str] = sys.argv

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
    print(Fore.RED+"[Error] You did not input anything in input.txt!\nExample for a spam message:\n"+Fore.CYAN+"Hello! {spam}")
    raise SystemExit(1)

# Gives you a warning if there is no spam variable.
if f"{lines}".find("{spam}") == -1:
    print(Fore.YELLOW+"[Warning] Some software may have a check for similar messages. It is recommended you put the {spam} tag in your desired message.")

# Handles all arguments
argHandleCount = -1
for arg in args:
    argHandleCount += 1
    if "--pressBeforeSpam" in arg:
        pressBeforeSpam = arg.split(":")[1]
        print(Fore.LIGHTBLUE_EX+f"[Argument] Detected \"pressBeforeSpam\" argument. Value: {pressBeforeSpam}")
    
    elif "--limitedSpam" in arg:
        try:
            limitedSpam = int(arg.split(":")[1])
            print(Fore.LIGHTBLUE_EX+f"[Argument] Detected \"limitedSpam\" argument. Value: {limitedSpam}")
        except ValueError:
            print(Fore.RED+f"[Argument] Argument Error: You can only provide an integer for \"limitedSpam\" argument.")
            raise SystemExit(1)
    
    elif "--spamSpeed" in arg:
        try:
            spamSpeed = float(arg.split(":")[1])
            print(Fore.LIGHTBLUE_EX+f"[Argument] Detected \"spamSpeed\" argument. Value: {spamSpeed}")
        except ValueError:
            print(Fore.RED+f"[Argument] Argument Error: You can only provide a number for \"spamSpeed\" argument.")
            raise SystemExit(1)
        
    elif "--noDelay" in arg:
        noDelay = True
        print(Fore.LIGHTBLUE_EX+f"[Argument] Detected \"noDelay\" argument.")
    
    elif "main.py" in arg:
        pass
    
    else:
        print(Fore.RED+f"[Argument] Detected unknown argument \"{arg}\". To check the arguments list, go to the GitHub.")
        raise SystemExit(1)

print(Fore.GREEN+"[Ready] You have 3 seconds to switch to your desired program you want to spam on.")
sleep(3)
kb = Controller()

if 'spamSpeed' in vars():
    print('')
else:
    spamSpeed = 0.7

# We will define the function first.
progBreak = 0
def loopLine_Func():
    for loopLine in lines:
        print(Fore.BLUE+"[Spammer] Text sent.")
        # Now, we will add 1 to the break variable, and we will check if it's time to stop.
        global progBreak
        progBreak += 1
        global noDelay
        if bool('noDelay' in vars()) == False:
            noDelay = False
        elif noDelay == True:
            pass
        else:
            if progBreak == 10:
                print(Fore.CYAN+"[Program Break] It is time for a break.\nIf you need to stop it, press Ctrl+C.\nAfter 2 seconds, the program will keep running.")
                sleep(2)
                print(Fore.GREEN+"[Program Break] The break is over. The program will keep running.")
                progBreak = 0
        
        if 'pressBeforeSpam' in vars():
            kb.press(pressBeforeSpam)
            kb.release(pressBeforeSpam)
            print(pressBeforeSpam)
        
        # First, we will make a random text out of ABC, numbers and symbols.
        uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
        lowercase = "qwertyuiopasdfghjklzxcvbnm"
        numbers = "0123456789"
        characters = "!@#$%^&*()_+-=[]{}\|;:'\"?/<>,."
        
        randomText = "["+(''.join(random.choice(uppercase+lowercase+numbers+characters) for i in range(30)))+"]"
        
        # Now, we will replace the {spam} in the messages.
        loopLine = loopLine.replace("{spam}", f"{randomText}")
        
        # Now, typing the spam message.
        kb.type(loopLine+"\n\n")
        sleep(spamSpeed)

if 'limitedSpam' in vars():
    for i in range(limitedSpam):
        loopLine_Func()
    
    print(Fore.GREEN+f"[Finished] Spammed for {limitedSpam} times.")
    
else:
    while True:
        loopLine_Func()

