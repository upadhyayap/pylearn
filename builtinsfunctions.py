# There are some built-in functions in Python which are used frequently while programming. Some of them are discussed below:
# any: This function returns true if any of the items in the iterable is true. If the iterable object is empty, the any() function will return false.
widget_one = ''
widget_two = ''
widget_three = 'button'
widgets_exist = any([widget_one, widget_two, widget_three])
print(widgets_exist)

# all: This function returns true if all of the items in the iterable are true. If the iterable object is empty, the all() function will return true.
widget_one = ''
widget_two = ''
widget_three = 'button'
widgets_exist = all([widget_one, widget_two, widget_three])
print(widgets_exist)

# enumerate: This function adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))
# converting to list
print(list(enumerateGrocery))
# changing the default counter
# index 0 is added to the counter using
enumerateGrocery = enumerate(grocery, -2)
for item in enumerateGrocery:
    print(item)

# eval: This function parses the expression passed to this function and runs python expression (code) within the program.
x = 1
print(eval('x + 1'))

# filter: The filter built-in function will take a function and an iterable and return an iterator for those elements within the iterable
# for which the passed in function returns True.


def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
result = filter(is_even, numbers)
print(list(result))


# map: The map built-in function will take a function and an iterable and return an iterator that applies the function to each element of the iterable.
def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5, 6]
result = map(square, numbers)
print(list(result))


# zip: The zip built-in function will take one or more iterables and return an iterator that will aggregate elements from each iterable.
keys = ['x', 'y', 'z']
values = [5, 6, 7]
print(zip(keys, values))


print(list(zip(keys, values)))

# creating dictionary using zip()
keys = ['x', 'y', 'z']
values = [5, 6, 7]
my_dict = dict(zip(keys, values))
print(my_dict)
