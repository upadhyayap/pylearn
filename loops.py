# Syntax of for loop
# for item in iterable_object:
#     do something

# iterable_object is a collection of objects like list, tuple, set, dict, string etc.
# item is a temporary variable which stores the value of the item in each iteration
# For example:
# loop will not take the last value
for i in range(1, 5):
        print(i)
# a step can be added to the range function
for i in range(1, 5, 2):
        print(i)
 # range for opposite loop
for i in range(5, 1, -1):
        print(i)

# syntax of while loop
# while condition:
#     do something

# pass statement is used to do nothing
# if a > b:
#     pass
# else:
#     print("a is less than b")

# else statement with while loop
# while condition:
#     do something
# else:
#     do something
# For example:
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("The while loop execution is over")

# else statement with for loop
i = 1
for i in range(1, 5):
    print(i)
    i += 1
else:
    print("The for loop execution is over")