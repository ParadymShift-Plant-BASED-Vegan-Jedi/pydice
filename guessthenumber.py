import random

print("""Welcome to Guess The Number!

The game is simple, you tell the computer how many numbers you'd like to guess, starting from 1 and going to any positive integer of your choice, and the computer will think of a number between 1 and that number and your job is to guess the number that the comuter is thinking of!

If you guess too high, the computer will tell you so. If you guess too low, the computer will also let you know. 

Can you guess the rigth number? 

Be careful; you only have 6 tries!""")

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
tries = 6

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
        break

while True:
