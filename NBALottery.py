# NBA lottery
#
#
import os
import pprint
import random
import time

teams = []
draft_order = {}
bye_lottery = "Thank you for participating in this years NBA lottery\nHave an amazing evening."

def nbateams():
    with open('nbateams.txt') as f:
        lines = list(f)
    for i in range(15):
        teams.append(random.choice(lines[i].rstrip('\n').split(',')))
    pprint.pprint(teams)


def lottery():
    for i in range(15, 0, -1):
        select = random.choice(teams)
        print("The {}th pick in the 2018 NBA draft goes to the... {}".format(i,select))
        #draft_order[i]
        teams.remove(select)
        time.sleep(3)
    to_draft = input("Would you like to proceed to the NBA draft?: [Yes/No] ")
    if to_draft.lower() in ['y', 'yes']:
        draft()
    elif to_draft.lower() in ['n', 'no']:
        print(bye_lottery)
        return


def draft():
    return


def main():
    pprint.pprint("***** Welcome to the 2018 NBA Lottery *****")
    time.sleep(1)
    print("The teams in this years NBA lottery are:")
    time.sleep(2)
    nbateams()
    time.sleep(2)
    lottery()
    return

if __name__ == "__main__":
    main()