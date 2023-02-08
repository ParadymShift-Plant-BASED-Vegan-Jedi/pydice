import random

options = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "~", "`", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/"]

while True:
    try:
        chars = int(input("How long would you like your password to be? Enter number of characters here: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
passlist = []
for i in range(chars):
    passlist.append(random.choice(options))
password = "".join(passlist)

print(f"Your password is: \n\n{password}")
