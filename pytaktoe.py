import time
import random
import numpy as np

print("""Welcome to Tik Tak Toe! 

Here are the instructions on how to play with the console:

Your board looks like this:
 | |
-+-+-
 | |
-+-+-
 | | 

A coin will be flipped at the beginning to decide who goes first.

To mark a box, you type two letters with no spaces. The first letter corresponds with the row you are choosing and the second letter corresponds with the column you are choosing.

Here are the first three letter options:
T - for "Top"
M - for "Middle"
B - for "Bottom"

Here are the second three letter options:
L - for "Left"
M - for "Middle"
R - for "Right"

That means to mark the center spot, you would type this into the console:
"MM"

To mark the top left spot, you would type this into the console:
"TL"

To mark the leftmost middle spot, you would type this into the console:
"ML"

Make sense? :)
""")

time.sleep(5)

rdy = ""
while rdy != "yes":
    rdy = input("Are you ready to begin the game? Type \"Yes\" when ready: ")
    rdy = rdy.lower()

coing = ""
while coing != "tails" and coing != "heads":
    coing = input("Call the coin! Type \"Heads\" or \"Tails\" to guess the flip: ")
    coing = coing.lower()
if coing == "tails":
    coing = 0
elif coing == "heads":
    coing = 1

coinr = random.randint(0,1)
print("The coin flips and lands on:")
if coinr == 1:
    print("Heads!")
elif coinr == 0:
    print("Tails!")
if coinr == coing:
    print("Congratulations, you guessed correctly and get to go first!")
    frst = True
else:
    print("Unfortunately you guessed incorrectly and get to go second.")
    frst = False

topr = [" ", " ", " "]
midr = [" ", " ", " "]
botr = [" ", " ", " "]

def display_board():
    print(f"""{topr[0]}|{topr[1]}|{topr[2]}
-+-+-
{midr[0]}|{midr[1]}|{midr[2]}
-+-+-
{botr[0]}|{botr[1]}|{botr[2]}""")
 
display_board()

options = ["TL", "TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR"]

if frst == True:
    while True:
        chc1 = input("Where would you like to make your first move? Type your two letters into the console: ")
        chc1 = chc1.upper()
        if chc1 in options:
            break
        else:
            print("Invalid Option: Please try again.")
            continue
    if chc1 == "TL":
        topr[0] = "X"
    elif chc1 == "TM":
        topr[1] = "X"
    elif chc1 == "TR":
        topr[2] = "X"
    elif chc1 == "ML":
        midr[0] = "X"
    elif chc1 == "MM":
        midr[1] = "X"
    elif chc1 == "MR":
        midr[2] = "X"
    elif chc1 == "BL":
        botr[0] = "X"
    elif chc1 == "BM":
        botr[1] = "X"
    elif chc1 == "BR":
        botr [2] = "X"
    else:
        print("Error. Invalid input. Please restart the game and try again!")
else:
    print("The computer makes a move...")
    while True:
        brchc1 = random.randint(1,3)
        bcchc1 = random.randint(0,2)
        if brchc1 == 1:
            topr[bcchc1] = "O"
            break
        elif brchc1 == 2:
            midr[bcchc1] == "O"
            break
        elif brchc1 == 3:
            botr[bcchc1] = "O"
            break
        else:
            print("Computing Error. Please restart the game and try again")
            
display_board()
    
time.sleep(3)

def player_move():
    while True:
        print("It's your turn. Where would you like your next move to be? Type your two letters into the console: ")
        chc1 = chc1.upper()
        if chc1 in options:
            if chc1 == "TL":
                if topr[0] == "X" or topr[0] == "O":
                    print("That space is already taken! Please try again.")
                    continue
                topr[0] = "X"
                break
            elif chc1 == "TM":
                if topr[1] == "X" or topr[1] == "O":
                    print("That space is already taken! Please try again.")
                    continue
                topr[1] = "X"
                break
            elif chc1 == "TR":
                if topr[2] == "X" or topr[2] == "O":
                    print("That space is already taken! Please try again.")
                    continue
                topr[2] = "X"
                break
            elif chc1 == "ML":
                if midr[0] == "X" or midr[0] == "O":
                    print("That space is already taken! Please try again.")
                    continue
                midr[0] = "X"
                break
            elif chc1 == "MM":
                if midr[1] == "X" or midr[1] == "O":
                    print("That space is already taken! Please try again.")
                    continue
                midr[1] = "X"
                break
            elif chc1 == "MR":
                if midr[2] == "X" or midr[2] == "O":
                    print("That space is already taken! Please try again.")
                    continue
                midr[2] = "X"
                break
            elif chc1 == "BL":
                if botr[0] == "X" or botr[0] == "O":
                    print("That space is already taken! Please try again.")
                    continue
                botr[0] = "X"
                break
            elif chc1 == "BM":
                if botr[1] == "X" or botr[1] == "O":
                    print("That space is already taken! Please try again.")
                    continue
                botr[1] = "X"
                break
            elif chc1 == "BR":
                if botr[2] == "X" or botr[2] == "O":
                    print("That space is already taken! Please try again.")
                    continue
                botr[2] = "X"
                break
            else:
                print("Error. Invalid input. Please restart the game and try again!")
                break
        else:
            print("Invalid Option: Please try again.")
        continue

def win_check():
    # Check for wins horizontally
    if topr[0] == "X" and topr[1] == "X" and topr[2] == "X":
        return True
    elif midr[0] == "X" and midr[1] == "X" and midr[2] == "X":
        return True
    elif botr[0] == "X" and botr[1] == "X" and botr[2] == "X":
        return True
    # Check for wins vertically
    if topr[0] == "X" and midr[0] == "X" and botr[0] == "X":
        return True
    elif topr[1] == "X" and midr[1] == "X" and botr[1] == "X":
        return True
    elif topr[2] == "X" and midr[2] == "X" and botr[2] == "X":
        return True
    # Check for wins diagonally
    if topr[0] == "X" and midr[1] == "X" and botr[2] == "X":
        return True
    elif topr[2] == "X" and midr[1] == "X" and botr[0] === "X":
        return True
    return False

def loss_check():
    # Check for losses horizontally
    if topr[0] == "O" and topr[1] == "O" and topr[2] == "O":
        return True
    elif midr[0] == "O" and midr[1] == "O" and midr[2] == "O":
        return True
    elif botr[0] == "O" and botr[1] == "O" and botr[2] == "O":
        return True
    # Check for losses vertically
    if topr[0] == "O" and midr[0] == "O" and botr[0] == "O":
        return True
    elif topr[1] == "O" and midr[1] == "O" and botr[1] == "O":
        return True
    elif topr[2] == "O" and midr[2] == "O" and botr[2] == "O":
        return True
    # Check for losses diagonally
    if topr[0] == "O" and midr[1] == "O" and botr[2] == "O":
        return True
    elif topr[2] == "O" and midr[1] == "O" and botr[0] === "O":
        return True
    return False


                                                      
        
            
