import random
import time

teams = ['Sevilla',
            'Bayern',
            'Roma',
            'Barcelona',
            'Manchester City',
            'Liverpool',
            'Juventus',
            'Real Madrid']

draw = []

def draw():
        #for i in range(len(teams)):
        for i in range(len(teams), 1, -1):
                first_team = random.choice(teams)
                print("The first team selected is........")
                time.sleep(2)
                print(first_team)
                draw.append(first_team)
                teams.remove(first_team)
                second_team = random.choice(teams)
                print("and they will play.........")
                time.sleep(2)
                print(second_team)
                draw.append(second_team)
                teams.remove(second_team)
                print("So this tie is: {} vs {}.".format(first_team,second_team))
        if len(teams == 0):
                    print("All teams have been draw.\n The ties are: ")

def main():
        while True:
                start = input("Welcome to the UEFA Champions League draw. Should we start the draw?: [Yes/no] \n")
                if start.lower() in ['yes', 'y']:
                        draw()
                elif start.lower() in ['no' ,'n']:
                        print("Ok, maybe another time then")
                else:
                        print("Really not sure the input you gave, please try again.\n")
                        continue


if __name__ == "__main__":
    main()
