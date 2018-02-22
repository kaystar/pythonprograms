import random
import time

playerChoice = input("Please select your choice. (R)ock, (P)aper or (S)cissors: ").lower()

print("You chose:", playerChoice)
time.sleep(1)

cpuChoice = random.randint(1,3)

if cpuChoice == 1:
    computer = 'r'
elif cpuChoice == 2:
    computer = 'p'
else:
    computer = 's'

print(computer)

if playerChoice == computer:
    print("DRAW! You chose {}, and CPU chose {}").format(playerChoice, cpuChoice)
elif playerChoice == 'r' and cpuChoice == 's':
    print("WIN! {} beats {}").format(playerChoice, cpuChoice)
elif playerChoice == 's' and cpuChoice == 'r':
    print ("LOSE! {cpuChoice} beats {playerChoice}").format(cpuChoice, playerChoice)



