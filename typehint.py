# typehint: a simple type hinting system for Python
# it is about passing the type of a variable as a parameter to a function

# here we are hinting that the variable number is of type int and name is of type str and it returns None
def some_function(number: int, name: str) -> None:
    print("%s entered %s" % (name, number))
