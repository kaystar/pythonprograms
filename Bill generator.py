import time
import pprint

menu = {
"Gas water" : 0.5,
"CocaCola" : 1,
"Fanta" : 1,
"Salad" : 1.50,
"Soup" : 2,
"Sandwich" : 2,
"Spagheti" : 2,
"Hamburger" : 3,
"Pizza" : 4,
"Steak" : 6,
}

bill = 0


def take_orders():
    global bill
    global menu
    while True:
        order = str(input("What would you like to order today?: "))
        if order == '':
            break
        time.sleep(1)
        quantity = int(input("How many would you like to order?: "))
        query = input("Anything else? (y/n): ")
        if query.lower() == 'y':
            take_orders()
        elif query.lower() == 'n':
            bill = menu[order] * quantity
            print("The total of your bill is: " + str(bill))
            break
        else:
            menu = str(menu)
            print(str("I did not recognise that order, our menu is: " + menu))



print("Good evening.")
time.sleep(2)
print("Here's our menu")
time.sleep(1)
pprint.pprint(menu)
time.sleep(3)

take_orders()
#print(bill)



