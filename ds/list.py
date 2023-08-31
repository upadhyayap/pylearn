# List
# Creating a list
l = [10, 20, 30, 40, 50]
# Accessing elements of a list using index
print(l[0])
# Accessing elements of a list using negative index
print(l[-1])
# Slicing a list
print(l[0:3])

# Adding elements to a list
l.append(60)
print(l)
# Adding elements to a list at a specific index
l.insert(0, 5)
print(l)
# Removing elements from a list
l.remove(5)
print(l)
# Removing elements from a list using index
l.pop(1)
print(l)

# Updating elements of a list
l[0] = 5
print(l)

# Concatenating two lists
l2 = [70, 80, 90]
l3 = l + l2
# or l.extend(l2)
print(l3)

# Repetition of elements in a list
l4 = l * 2
print(l4)

# Finding the length of a list
print(len(l))

# Finding the index of an element in a list
print(l.index(30))

# Sorting a list
l5 = [10, 50, 20, 40, 30]
l5.sort()
print(l5)

# Reversing a list
l5.reverse()

# Removing all the elements from a list
l5.clear()
print(l5)

# Deleting a list
del l5

# Iterating through a list
for i in l:
    print(i)

# List comprehension
# List comprehension is a way to create a list using an existing list
# Syntax: [expression for item in list]
nums_double = [n * 2 for n in l]
print(nums_double)


sum_list = [(n1, n2) for n1 in l2 for n2 in l3 if n1 + n2 > 100]
print(sum_list)
