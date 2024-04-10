# generators: A normal Python function will always return one value,
# whether it be a list, an integer or some other object.
# But what if we call a function and it yields a series of values?
# That is where generators come in.
# A generator works by “saving” where it last left off (or yielding)
# and giving the calling function a value.
# So instead of returning the execution to the caller,
# it just gives temporary control back. To do this magic, a generator function
# requires Python’s yield statement.

def doubler_generator():
    number = 2
    while True:
        yield number
        number *= number


doubler = doubler_generator()
print(next(doubler))


print(next(doubler))


print(next(doubler))


print(type(doubler))

# under the hood, generators are implemented as iterators
