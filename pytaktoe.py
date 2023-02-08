import time
import random

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

print(""" | |
-+-+-
 | |
-+-+-
 | | """)

if frst == True:
    chc1 = input("Where would you like to make your first move? Type your two letters into the console: ")
    chc1 = chc1.upper()
    if chc1 == "TL":
        print("""X| |
-+-+-
 | |
-+-+-
 | | """)
    elif chc1 == "TM":
        print(""" |X|
-+-+-
 | |
-+-+-
 | | """)
    elif chc1 == "TR":
        print(""" | |X
-+-+-
 | |
-+-+-
 | | """)
    elif chc1 == "ML":
        print(""" | |
-+-+-
X| |
-+-+-
 | | """)
    elif chc1 == "MM":
        print(""" | |
-+-+-
 |X|
-+-+-
 | | """)
    elif chc1 == "MR":
        print(""" | |
-+-+-
 | |X
-+-+-
 | | """)
    elif chc1 == "BL":
        print(""" | |
-+-+-
 | |
-+-+-
X| | """)
    elif chc1 == "BM":
        print(""" | |
-+-+-
 | |
-+-+-
 |X| """)
    elif chc1 == "BR":
        print(""" | |
-+-+-
 | |
-+-+-
 | |X""")
    else:
        print("Invalid option. Please restart the game and try again!")
        
    


            
