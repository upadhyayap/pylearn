# chainMap: 1. It is a dictionary like class for creating a single view of multiple mappings.
from collections import ChainMap
from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple
from collections import OrderedDict

car_parts = {"hood": 500, "engine": 5000, "front_door": 750}
car_options = {"A/C": 1000, "Turbo": 2500, "rollbar": 300}
car_accessories = {"cover": 100, "hood_ornament": 150, "seat_cover": 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print(car_pricing["hood"])

# counter: 1. It is a dictionary subclass for counting hashable objects.
c = Counter("Hello World")
print(c["l"])
print(c.most_common(1))
# substracting a counter
c2 = Counter("World")
c3 = c - c2
print(c3["l"])

# defaultdict: 1. It is a dictionary subclass that calls a factory function to supply missing values.
sentence = "The red fox jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

# Here int is the factory function that will be called to supply missing values
# if the key does not exist in the dictionary then it is created and
# the value is set to 0 automatically
d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)

# lambda can also be pssed as a factory function
d = defaultdict(lambda: "monkey")  # default value is monkey

# deque: 1. It is a list like container with fast appends and pops on either end.

# namedtuple: 1. It is a factory function for creating tuple subclasses with named fields.
# example
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# _replace() function
pt = pt._replace(x=100)
print(pt)

# ordereddict: 1. It is a dictionary subclass that remembers the order in which its contents are added.
# example
d = OrderedDict()
d['a'] = 1
d['b'] = 2
print(d)
