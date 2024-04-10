# iterators: An iterator is an object that will allow us to iterate over a container
# _iter_() and _next_() are the two methods that are used to iterate over an object
# it raises StopIteration when there are no more elements to iterate over
# example:
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import starmap
from itertools import groupby
from itertools import dropwhile
from itertools import takewhile
from itertools import compress
import operator
from itertools import accumulate
from itertools import count
from itertools import islice
from itertools import cycle
from itertools import chain


class MyIterator:

    def __init__(self, letters):
        """
        Constructor
        """

        self.letters = letters
        self.position = 0

    def __iter__(self):
        """
        Returns itself as an iterator
        """

        return self

    def __next__(self):
        """
        Returns the next letter in the sequence or 
        raises StopIteration
        """

        if self.position >= len(self.letters):
            raise StopIteration
        letter = self.letters[self.position]
        self.position += 1
        return letter


if __name__ == '__main__':
    i = MyIterator('abcd')
    for item in i:
        print(item)

# python provides a module for iterators called itertools
# itertools.count(start=0, step=1): Returns an iterator that counts indefinitely
for i in count(10):
    print(i)
    if i == 15:
        break
# itertools.cycle(iterable): Returns an iterator that cycles indefinitely over the iterable
count = 0
for c in cycle('RACECAR'):
    print(c)
    if count > 7:
        break
    count += 1
# itertools.accumulate(iterable[, func]): Returns an iterator that returns accumulated sums,
# or accumulated results of other binary functions (specified via the optional func argument)
print(list(accumulate(range(1, 5), operator.mul)))

# itertools.repeat(object, times=None): Returns an iterator that repeats the object times times

# itertools.chain(*iterables): Returns an iterator that combines the iterables into one long sequence
my_list = [1, 2, 3]
aList = ["a", "b", "c"]
merged_list = list(chain(my_list, aList))

# itertools.islice(iterable, start, stop[, step]): Returns an iterator that returns selected items from the iterable
for i in islice(count(10), 5):
    print(i)

# itertools.compress(data, selectors): Returns an iterator that filters elements from the data returning only those that have a
# corresponding element in selectors that evaluates to True
# The compress sub-module is useful for picking the first iterable values according to the second iterable Boolean values.
# This works by making the second iterable a list of Booleans (or ones and zeroes which amounts to the same thing). Here’s how it works:
letters = 'ABCDEFG'
bools = [True, False, True, True, False]
print(list(compress(letters, bools)))

# itertools.dropwhile(predicate, iterable): Returns an iterator that drops elements from the iterable as long as the predicate evaluates to True;
# afterwards, returns every element
print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

# itertools.takewhile(predicate, iterable): Returns an iterator that returns
# elements from the iterable as long as the predicate evaluates to True;
# afterwards, stops and does not return any more elements and so on.
# It is just an opposite of dropwhile().
print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

# itertools.groupby(iterable[, key]): Returns an iterator that
# returns consecutive keys and groups from the iterable.
vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'),
            ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
            ('Dodge', 'Charger'), ('Ford', 'GT')]

sorted_vehicles = sorted(vehicles)

for key, group in groupby(sorted_vehicles, lambda make: make[0]):
    for make, model in group:
        print('{model} is made by {make}'.format(model=model,
                                                 make=make))
    print("**** END OF GROUP ***\n")

# Output
# Cobalt is made by Chevrolet
# **** END OF GROUP ***

# Charger is made by Dodge
# Durango is made by Dodge
# **** END OF GROUP ***

# F150 is made by Ford
# GT is made by Ford

# starmap: The starmap tool will create an iterator that can compute
# using the function and iterable provided
# The starmap function is similar to map, but instead of constructing
# a tuple from multiple iterators, it splits up the items in a single iterator
# as arguments to the mapping function using the * syntax.


def add(a, b):
    return a+b


for item in starmap(add, [(2, 3), (4, 5)]):
    print(item)
# 5
# 9

# create combination of data: nCr
print(list(combinations('WXYZ', 2)))
for item in combinations('WXYZ', 2):
    print(''.join(item))

# nPr
for item in permutations('WXYZ', 2):
    print(''.join(item))

# cartesian product of the data
arrays = [(-1, 1), (-3, 3), (-5, 5)]
cp = list(product(*arrays))
print(cp)
