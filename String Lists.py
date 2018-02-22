phrase = input("Enter a word to see if it's a palindrome: ")

phrase = str(phrase)
rvs = phrase[::-1]
print(rvs)

if phrase == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")