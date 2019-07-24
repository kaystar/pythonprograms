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
