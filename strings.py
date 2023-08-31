# Anything between single or double quotes is a string
# Can be visualized as a sequence of characters
# Strings are immutable
# Strings can be indexed
# you can also reverse index a string
# for example:
a = "Hello"
print(a[0])
# prints the last character of the string
print(a[-1])

# Strings can be sliced
# for example:
a = "Hello"
# prints the first 3 characters of the string, start is inclusive and end is exclusive
print(a[0:3])

# Strings can be concatenated
# for example:
a = "Hello"
b = "World"
print(a + b)

# Strings can be repeated
# for example:
a = "Hello"
print(a * 3)


# Strings can be iterated
# for example:
a = "Hello"
for i in a:
    print(i)

# Strings can be checked for membership
# for example:
a = "Hello"
if "H" in a:
    print("H is present in the string")

# Strings can be checked for non-membership
# for example:
a = "Hello"
if "H" not in a:
    print("H is not present in the string")

# Strings can be compared
# for example:
a = "Hello"
b = "Hello"
if a == b:
    print("Both the strings are equal")

# length of the string
# for example:
a = "Hello"
print(len(a))

# formatted print
# for example:
a = "Hello"
b = "World"
print("Hello %s" % b)
a=10
b=20
print("a is {0} and b is {1}".format(a, b))



