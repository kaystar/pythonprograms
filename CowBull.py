#Cows and Bulls Exercise

import random
import time

def calculate(num, usernum):
    cowbull = [0,0]
    for i in range(len(num)):
        if num[i] == usernum[i]:
            cowbull[1] += 1
        else:
            cowbull[0] += 1
    return cowbull




def main():
    playing = True
    cpu_number = random.randint(1000,9999)
    guesses = 0

    print("We're playing CowBull! \n These are the rules..")
    time.sleep(2)
    print("I will think of a random 4 digit number, and you have to guess the numbers one digit at a time.")
    time.sleep(1)
    print("Every number you get in the wrong place, you get a cow.\n Every number in the right place you get a bull.")
    time.sleep(1)
    print("The game ends when you get 4 bulls!\n Type exit at any prompt to exit the game.")

    while playing:
        user_num = input("Gives me a number: ")
        if user_num.lower() == "exit":
            break
        cowbullcount = calculate(cpu_number, user_num)
        guesses += 1

        print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1] == 4:
            playing = False
            print("You won the game after " + str(guesses) + "! the number was " +str(cpu_number))
            break
        else:
            print("Your guess isn't quite right, please try again")


if __name__ == "__main__":
    main()
