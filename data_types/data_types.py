# Ignore the import statement for now, we will discuss about it later
import sys

# Numeric Types: int, float,bool, complex
# int - 10, 100, -786, 080, 0x80
# int can be of any size and is only limited by the memory available unlike other programming languages like 
# java where int is 32 bit and long is 64 bit integer or go where int is 32 bit and int64 is 64 bit integer
a = 10
# A valid int and can be separated by underscores. sounds interesting right?
a=136_912_531_038_693_245_623_452_346_012_731_026_391_254_921_037_120_634_012_641_237_012_649_234

# float - 0.0, 15.20, -21.9, 32.3e+18, -90.0e-67
b = 10.0

# bool - True, False
c = True

# complex - 3.14j, 45.j, 9.322e-36j
# complex numbers are written with a "j" as the imaginary part
# value of a complex number is a + bj
# Addition, subtraction, multiplication, division all the mathematical operations are supported on complex numbers
d = 3+1j
# another way to create a complex number
c = complex(3, 1)
# print the real part of the complex number
print(c.real)
# print the imaginary part of the complex number
print(c.imag)

# Sequence Types: list, tuple, string, bytes, bytearray
# list - [10, 20, 30, 40] list is mutable
e = [10, 20, 30, 40]

# tuple - (10, 20, 30, 40) tuple is same like list but it is immutable
f = (10, 20, 30, 40)

# string - "Hello" string is immutable
g = 'Hello'
# or with the double quotes
g = "Hello"
# or with the triple quotes
g = """Hello"""
# all the above are same
# There is no char type in python, a character is a string of length 1


# bytes - b"Hello" bytes is immutable
h = b"Hello"

# bytearray - bytearray(10) bytearray is mutable
i = bytearray(10)
# add more elements to bytearray
i.append(10)
i.append(20)
#print(i)
# bytes and bytes arrays are used to store a sequence of bytes (numbers from 0 to 255), they are used to store binary data.

# Set Types: set, frozenset
# set - {10, 20, 30, 40} set is mutable and unordered and obiviously unique
j = {10, 20, 30, 40, 40}
j.add(50)
print(j)

# frozenset - frozenset({10, 20, 30, 40}) frozenset is immutable
k = frozenset({10, 20, 30, 40})
# k.add(50) will fail as frozenset is immutable

# Mapping Type: dict
# dict - {1:"one", 2:"two", 3:"three"} dict is mutable
l = {1:"one", 2:"two", 3:"three"}
l[4] = "four"
print(l)
# Traverse a dict
for key, value in l.items():
    print(key, value)

# want to know how much memory is used by a variable
print(sys.getsizeof(l)) # 232 bytes
print(l.__sizeof__()) # 216 bytes
# Why there is a difference in size?
# sys.getsizeof() returns the size of the object in bytes.
# It accounts for the memory used by the object itself as well as any memory used by its data, attributes, and internal structures.
# __sizeof__() returns the size of the object in bytes.
# It returns the basic size of the object without considering any additional memory that might be used by the object's attributes or internal structures.


# Type Conversion
# Python defines type conversion functions to directly convert one data type to another.
# int() - converts any data type into integer type
# float() - converts any data type into float type
# str() - Used to convert integer into a string.
# complex(real,imag) - This function converts real numbers to complex(real,imag) number.

# example
# converting float to int
print(int(10.0))
# converting int to float
print(float(10))
# converting int to string
print(str(10))
# converting string to int
print(int("10"))
# converting string to float
print(float("10.0"))
# How to convert an object
# We can use the following functions to convert an object to a different data type:
# list() - Converts an object into a list.
print(list("Hello"))
# dict() - Converts an object into a dictionary.
# print(dict("Hello")) fails
# tuple() - Converts an object into tuple.
print(tuple("Hello"))
