import random

print("""Welcome to Guess The Number!

The game is simple, you tell the computer how many numbers you'd like to guess, starting from 1 and going to any positive integer of your choice, and the computer will think of a number between 1 and that number and your job is to guess the number that the comuter is thinking of!

If you guess too high, the computer will tell you so. If you guess too low, the computer will also let you know. 

Can you guess the right number? 

Be careful; you have a limited number of guesses!""")

while True:
    try:
        x = int(input("Starting at 1, what would you like the upper range of the numbers to be? Example: 100 (will choose a number between 1 and 100). Enter answer here: "))
    except:
        print("Invalid entry. Please try again.")
        continue
    if x < 10:
        print("Sorry, your number must be at least 10. Please try again.")
    else:
        break

nums = [i for i in range(1, x + 1)]
num = random.choice(nums)
if x + 1 < 22:
    tries = 4
elif x < 201:
    tries = 6
elif x < 801:
    tries = 8
elif x < 2001:
    tries = 10
elif x < 8001:
    tries = 13
elif x < 15001:
    tries = 15
elif x < 25001:
    tries = 18
elif x < 75001:
    tries = 21
elif x < 100001:
    tries = 25
elif x < 500001:
    tries = 30
else:
    tries = 35
    

while True:
    try:
        ans = int(input("What number am I thinking of? Guess here: "))
    except:
        print("Invalid entry. Please try again.")
        continue
    if ans < 1:
        print("You cannot guess a number lower than 1. Try again.")
        continue
    else:
        tries -= 1
        break
        
while True:
    if ans > num:
        print("You guessed too high! Guess again.")
    elif ans < num:
        print("You guessed too low! Guess again.")
    elif ans == num:
        print("Congatulations. You guessed correctly and won!")
        break
    else:
        print("Unknown error. Please restart game.")
        break
    while tries > 0:
        try:
            ans = int(input("What number am I thinking of? Guess here: "))
        except:
            print("Invalid entry. Please try again.")
            continue
        if ans < 1:
            print("You cannot guess a number lower than 1. Try again.")
            continue
        else:
            tries -= 1
            break
    if tries < 1:
        print("Sorry, you ran out of guesses and lost. Better luck next time!")
        break
    
