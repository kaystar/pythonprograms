number = int(input("Please input a number tp divide: "))

listRange = range(1, number+1)
#listRange = list(range(1,num+1))
y = []

for elem in listRange:
    if number % elem == 0:
        y.append(elem)

print(y)