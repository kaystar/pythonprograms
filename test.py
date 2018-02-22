import random

passwordlength = 10
weakpasswordlength = 7
weak_list = ['cat','man','dog','pop']
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"


def weakpassword():
    phrase = random.choice(weak_list)
    code = "".join(random.sample(s,weakpasswordlength))
    print(phrase + code)

def strongpassword():
    password = "".join(random.sample(s,passwordlength))
    print(password)

while True:
    choice = input("Would you like a strong password or weak password? (Type \'Strong' or \'Weak')\n ")
    if choice.lower() == 'strong':
        strongpassword()
        break
    elif choice.lower() == 'weak':
        weakpassword()
        break
    else:
        print("Sorry I didn't understand your choice, please select again...\n")
        True
