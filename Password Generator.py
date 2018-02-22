import string
import random


#string.ascii_letters
nums = []
passphrase = []
passw = ""

def password_generator():
    for i in range(3):
        nums.append(random.randint(1,9))
    for i in range(10):
        passphrase.append(random.choice(string.ascii_letters))

#print(nums)
#print(str(passphrase).format(str(nums)))

password_generator()
password = str(passphrase) + str(nums)
print(passw.join(password))

'''

# generate a password with length "passlen" with no duplicate characters in the password

#import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print(p)
'''