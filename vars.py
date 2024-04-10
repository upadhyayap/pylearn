# variables are declared without the type information.
a = 10
b = 20

print(a+b)

# Python is a dynamically typed language.
# This means that the type of a variable is inferred from its value.
# This is different from languages like C, C++, Java, etc. where the type of a variable needs to be explicitly declared.
# This means, for example, that we can assign any kind of data to a variable, and it will be stored correctly.
# For example, we can assign an integer value to a variable a, and later assign a string to the same variable.
# This is perfectly fine in Python, but not in statically typed languages.
# In statically typed languages, once a variable has been assigned a particular type, it cannot store values of other types.
# The following code snippet will work in Python, but not in C/C++/Java:

a = 10
print(a)
a = "Hello"
print(a)

# Multiple variable can be assigned in the same line, like this:
a, b, c = 10, 20, 30
print(a, b, c)

# Python also allows you to assign a single value to several variables simultaneously.
# For example:
a = b = c = 100
print(a, b, c)

# Python also allows you to assign multiple objects to multiple variables.
# For example:
a, b, c = 10, 20, "Hello"
print(a, b, c)

# you can check the type of a variable using the type() function.
# For example:
a = 10
print(type(a))

a = "Hello"
print(type(a))

# Everything in Python is an object, there is an object class actually,
# and every object can have attributes and methods.
# There is a dir() function which returns a list of all the attributes and methods
# of the specified object.
# For example:
a = "Hello"
print(dir(a))

# You can use the help() function to get help about any object, method, etc.
# For example:
a = "Hello"
print(help(a.upper))
