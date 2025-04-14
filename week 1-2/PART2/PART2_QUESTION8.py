#importing random for the random function
import random

#storing random number in variable ran
ran=random.randrange(1,100)

#range is 5 so the user has 5 chances to guess the number
for x in range(5):
    guess=int(input("Enter your guess from 1-100"))
    if guess==ran:
        print("Correct number")
        break
    elif guess>ran:
        print("Too high")
    else:
        print("Too low")

if guess!=ran:
    print("Game Over!")