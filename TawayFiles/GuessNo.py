from random import randint
randomnumber = randint(0,10)



def secret(guess):
    if (guess == randomnumber):
        print("Well done, you've guessed correctly")
        
    elif (guess < randomnumber):
        print("Sorry, your guess is too low, please guess again.")
        guess = int(input("please enter your new guess"))
        secret(guess)
        
    elif (guess > randomnumber):
        print("Sorry, your guess is too high, please guess again.")
        guess = int(input("please enter your new guess"))
        secret(guess)

print("Please enter your guess between 1 & 10 ")
guess = int(input())
secret(guess)
