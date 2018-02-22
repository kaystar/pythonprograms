def divide(number):
        if number % check == 0:
            print("The number {} is divisible by {}".format(number, check))
        elif number % check != 0:
            print("This number {} is not divisible by {}".format(check))
        else:
            print("The number is odd")


num = int(input("Please input a number: "))
check = int(input("Please enter a number to divide by: "))
divide(num)