# dictionary is like a map
# Creating a dictionary
d = {1: "one", 2: "two", 3: "three"}
# or using dict() constructor
d = dict({1: "one", 2: "two", 3: "three"})

# Accessing elements of a dictionary using key
print(d[1])
# Accessing elements of a dictionary using get method
print(d.get(1))
# Accessing elements of a dictionary using get method with default value
print(d.get(4, "Not found"))

# Adding elements to a dictionary
d[4] = "four"
print(d)
# Removing elements from a dictionary
del d[4]
print(d)

# Updating elements of a dictionary
d[1] = "ONE"
print(d)

# Concatenating two dictionaries
d2 = {4: "four", 5: "five"}
d3 = {**d, **d2}

# iterating through a dictionary
for key, value in d.items():
    print(key, value)

# dictionary comprehension
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)
