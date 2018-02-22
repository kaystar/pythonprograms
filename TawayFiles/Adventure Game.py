import time
import random

# game function
def game():
    
# Welcome   
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Welcome to the City in the sky!")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



#Story Start
def intro():
    print("You awaken.......")
    time.sleep(5)
    for i in range (8):
        print ("........")
        print (" ")

    print("You stand up in a marvellous city in the sky.")
    time.sleep(3)
    print("After examining your surroundings you enter unlocked garden gate")
    time.sleep(3)
    pick=ask("You tread through the undergrowth and find a sword on the floor, it looks kinda.....ancient, wanna pick it up anyway?")
    time.sleep(3)
    if pick.lower() in ['y','yes']:
        print("Nice, you've picked up the sword")
        sword = 1
        print("+1 old ancient sword")


    else:
        print("I guess old swords aren't that cool anyways, I mean this isn't Zelda")
        

       


def ask(question):
    answer = input(question + " [y/n]")
    return answer.lower in ['y' 'yes']
  
    
#Introduction
player_name = input("What is your name brave adventurer? ")
print("Oh, it's " + player_name, " what a lovely name.")
print("Well " + player_name, "it's time you went on your own adventure, through the skies!")
ready = input("Are you ready? ")
if ready.lower() in ['y','yes']:
    print("Have fun!")
    
    for i in range (0,5):
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print (" ")
        intro()

else:
    print("Oh....well maybe next time then, when you're feeling a little braver.....")


game()
