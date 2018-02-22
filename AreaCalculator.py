#Shape area checker
import time

condition = True

def calculate_circle():
    pi = 3.14159
    radius = int(input("What is the radius of the circle?: "))
    area = pi * (radius * radius)
    print("The are of your circle is " + str(area))
    time.sleep(1)


def calculate_triangle():
    base = int(input("What is the base of the triangle?: "))
    height = int(input("What is the height?: "))
    area = base * height / 2
    print("The area of your shape is " + str(area))
    time.sleep(1)


def calculate_square():
    width = int(input("What is the width of the shape?: "))
    length = int(input("What is the length of the shape?: "))
    area = width * length
    print("The area of your shape is " + str(area))
    time.sleep(1)


while condition == True:
    print("Hello".center(20,'*'))
    time.sleep(1)
    print("What shape do you want to check the area for?" )
    shape = input('c = circle  t = triangle  s = square or rectangle: ')


    if shape == 'c':
        calculate_circle()
    elif shape == 't':
        calculate_triangle()
    elif shape == 's':
        calculate_square()
    elif shape not in ['c','t','s']:
        print("Please enter a valid option")
        time.sleep(1)
        condition == False




