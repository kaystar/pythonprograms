def identity(x):
    return x

lambda x: x 

(lambda x: x + 1)(2)

#Traditional function
def add_one(x):
    return x + 1

#The above can be written as
add_one = lambda x: x + 1
add_one(2) 


full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')
print(full_name)


Address = lambda street, number: f'Home address: {street.title()} {number.title}'
Address("madison avenue", '100')
print(Address)

lambda x, y: x + y 
_(2, 5)

(lambda x, y: x + y)(22, 48)

(lambda x:
(x % 2 and "odd" or "even"))
_(23)

#################################


# Map in Python 
'''Standard/Traditional method'''
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

'''Map Method with Lambda expression'''
items = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, items))
print(doubled)

#################################


# Filter in Python

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]

#################################


# Reduce function in Python
'''Standard/Traditional method'''
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
    print(product)

# product = 24

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

#################################

# Set function 

'''Standard method'''
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
# Output: ['b', 'n']

'''Set function method'''
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)
