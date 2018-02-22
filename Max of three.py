import random

CPU_Guess = random.randint(1,9)

while True:
    Guessed_Number = int(input("Please guess a number: "))
    if Guessed_Number > CPU_Guess:
        print(("You've guessed too high. Try again {}" .format(Guessed_Number)))
    elif CPU_Guess < Guessed_Number:
        print(("You've guessed too low. Try again {}") .format(Guessed_Number))
    elif Guessed_Number == CPU_Guess:
        print("Congrats, you've guessed right!")
        print("User selected: {}, CPU selected: {}" .format(Guessed_Number, CPU_Guess))
        False
