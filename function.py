# function is defined using a keyword 'def'
#Example:
def my_function():
    print("Hello from a function")
my_function()

# Paramaters: Type information is not needed in python for function parameters
# Example:
def min(x,y):
    if x<y:
        return x
    return y

print(min(2,3))

# Default Parameters: Default values can be assigned to parameters
# Example:
def my_function(country = "Norway"):
    print("I am from " + country)

my_function()

# Lambda Function: Small anonymous function
# A lambda is an anonymous function that returns some form of data.
# Lambda functions are mainly used in combination with the functions filter(), map() and reduce().
# A lambda cannot have a multi-line expression. This means that our expression needs to be something that can be written in a single line.
# all the conditional expressions that we can use in a normal function can also be used in a lambda function.
# Syntax: lambda arguments : expression
# Example: 
x = lambda a : a + 10
print(x(5))

# Function inside a function: A function can be defined inside another function
# Example:
def myfunc(n):
    return lambda a : a * n

# Function as an argument: A function can be passed as an argument to another function
# Example:
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function


result = calculator(multiply, 10, 20)
print(result)
print(calculator(add, 10, 20))

# Function as a return value: A function can return another function
# Example:
def outer_function():
    def inner_function(name):
        print(f"Hello {name}")

    return inner_function  # Note we are returning function WITHOUT parenthesis
f=outer_function()
f("Raj")

