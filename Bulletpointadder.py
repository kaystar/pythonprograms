import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] #Adds a star and the start of each line
print((lines))

text = '\n'.join(lines)

pyperclip.copy(text)