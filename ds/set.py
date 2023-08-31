# Creating a set
s = {10, 20, 30, 40, 50}
# or usig set constructor
s = set({10, 20, 30, 40, 50})
# Adding elements to a set
s.add(60)
print(s)

# Removing elements from a set
s.remove(10)

# Updating elements of a set
s.update([60, 70, 80])
print(s)


# union of two sets
s2 = {90, 100, 110}
s3 = s.union(s2)

# intersection of two sets
s4 = s.intersection(s2)

# difference of two sets
s5 = s.difference(s2)
