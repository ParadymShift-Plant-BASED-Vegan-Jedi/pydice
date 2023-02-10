import numpy as np
import random

print("""Here are the instruction for how to play Mastermind:

The goal of the game is to correctly guess the color code consisting of four colors (repeats allowed) with six color options to choose from.

The six colors include: Red, Green, Blue, Pink, Purple, Yellow.

Once you guess the code, choices will be marked with either a white or a black marker below.

A white marker below the color indicates that you guessed the correct color in the correct location.

A black marker below the color indicates that you guessed the correct color in the wrong location.

No marker means that you guessed the wrong color.

Keep guessing to try to figure out the code and win Mastermind. But be careful! You only get 11 guesses before you lose and you need to type the colors correctly spelled without any spaces.

Can you solve the puzzle?""")

colors = ["Red", "Green", "Blue", "Pink", "Purple", "Yellow"]
code = random.choices(colors, k=4)
print(code)
attempts = 11
while attempts > 0:
    guesses = []
    while len(guesses) != 4:
        guess = input("Type each color guess in order one at a time here: ")
        if guess.capitalize() not in colors:
            print("Invalid entry. Please try again!")
            continue
        guesses.append(guess.capitalize())
    attempts -= 1
    markers = []
    index = 0
    for it in guesses:
        if it in code:
            if it.capitalize() == code[index]:
                markers.append("White")
            else:
                markers.append("Black")
        else:
            markers.append(" ")
        index += 1
            
    display = np.array([guesses, markers])
    print(display)
print("Sorry, you ran out of guesses and lost.")
    
