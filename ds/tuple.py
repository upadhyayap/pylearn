# tuple is an immutable list
t = (10, 20, 30, 40, 50)
print(t[0])

# search in tuple
print(t.index(30))

# count the number of occurences of an element in a tuple
print(t.count(30))

# iterate through a tuple
for i in t:
    print(i)

# convert a tuple to a list
l = list(t)
print(l)

# merge two tuples
t2 = (60, 70, 80)
t3 = t + t2
print(t3)
