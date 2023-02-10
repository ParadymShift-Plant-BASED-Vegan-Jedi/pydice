import random

print("""Welcome to Guess The Number!

The game is simple, you tell how many numbers you'd like to guess from 1 to any positive integer and the computer will think of a number between 1 and that number and your job is to guess the number!

If you guess too high, the computer will tell you so. If you guess too low, the computer will also let you know. 

Can you guess the rigth number? 

Be careful; you only have 10 tries!"""

nums = [i for i in range(1, int(input("What would you like the upper range of the numbers to guess to be? Example: 100 (will choose a number between 1 and 100). Enter answer here: ")) + 1)]
num = random.choice(nums)
tries = 10
