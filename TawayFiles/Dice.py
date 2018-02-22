from random import randint
import time


dicemin = 2
dicemax = 12
answer = ""

def dice(answer):
    if (answer == "yes" or answer =="y"):
        
        result = randint(dicemin, dicemax)
        print("Rolling........")
        time.sleep(1)
        print("The number you rolled is...", result)
        answer = input("Would you like to roll again?: ")
        dice(answer)

    elif (answer == "no" or answer == "n"):
         print("Thanks for playing")

         
answer = input("Would you like to roll the dice?")
dice(answer)
