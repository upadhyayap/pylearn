# ** denotes power operator
a=2**4
print(a)

# // denotes floor division then normal division i.e is float division
a=10//3
print(a)

# Rest of the operators are same as other languages

# is and is not are the identity operators
# is operator returns True if both the variables point to the same object
# is not operator returns True if both the variables point to different objects
a=10
b=10
print(a is b)
print(id(a))
print(id(b))
# Why the id of both the variables are same?
# Python caches the integer objects in the range of -5 to 256 (both inclusive) and whenever you create an integer in this range, Python will always point to the same object in memory.
# In Python, the id() function returns the identity (memory address) of an object. When you create an object, such as an integer, and assign it to multiple variables, Python tries to optimize memory usage by reusing the same memory location if the values are the same. This is known as "object interning."