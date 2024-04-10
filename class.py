# Declaring a class
from abc import ABC, abstractmethod


# In Python, pass is a null statement. It performs no operation and acts
# as a placeholder where syntactically a statement is required, but no action
# needs to be taken. It is often used as a placeholder in situations where code
# must be syntactically correct but no action is required or intended.
# Here's an example of how pass can be used:
if 1 == 1:
    pass


class Employee:
    pass

    total_employees = []
    # This is an object initializer, called when an object of this class is created.
    # The first parameter of this function is always self, which is a reference to the current object.
    # And rest are whatever parameters you want to pass while creating the object.

    def __init__(self, ID, salary, department) -> None:
        print("Employee created")

    # defining the properties and assigning them none
    ID = None
    salary = None
    department = None
    # Note that you do not initialize the values of properties, the Python code will not compile. Initializing the values of properties inside the class is necessary.
# Defining methods

# Object methods: Methods that are available for objects of the class
# Firt parameter is always self, which is a reference to the current object.
# And rest are whatever parameters you want to pass while calling the method.
# unlike other language explicit method overloading is not possible in python
# instead you can use default parameters


def tax(self, percentage, income=None):
    return self.salary * percentage / 100

# class methods: Methods that are available for the class itself
# First parameter is always cls, which is a reference to the current class.
# they can be called using the class name itself and not the object
# And rest are whatever parameters you want to pass while calling the method.


@classmethod
def get_total_employees(cls):
    return cls.total_employees

# static methods: Methods that are not available for the class or objects
# They are just like normal functions, but are defined inside a class.
# They can be called using the class name itself and not the object


@staticmethod
def to_string():
    return "This is a static method"


# Creating an object
p1 = Employee(123, 10000, "IT")
# Assigning values to the properties of the object
p1.ID = "123"
p1.salary = 10000
p1.department = "IT"
# calling the class method
print(Employee.get_total_employees())
# print(p1)

# Adding a dynamic property to an object
p1.name = "Raj"
# This property will be available only for this object and not for other objects of the same class.

# You can also have a default initializer that has all properties as optional.
# In this case, all the new objects will be created using the properties initialized in the initializer definition


class Person:
    def __init__(self, name=None, age=None, hieght=None) -> None:
        self.name = name
        self.age = age
        self.__hieght = hieght  # hieght is a private property
        # private property can be access outside of the class using _classname__propertyname

# Access modifiers
# Pubic : can be accessed inside the class and outside the class.
# all methods and properties in a class are publicly available by default
# Private : can be accessed only inside the class. you can make the methods private by prefixing them with __


def __private_method(self):
    pass


# Creating an object
# Both are valid
p1 = Person("Raj", 30)
p2 = Person()


# In Python, whenever we create a class, it is, by default, a subclass of the built-in Python object class
# This means that all the classes we create in Python are subclasses of the object class.
# This is why we can use the built-in functions like __init__(), __str__(), and so on, in our classes.

# Inheritance
# How to declare a child class
# class ChildClass(ParentClass):
# attributes of the child class
# methods of the child class
# super  is used in a child class to refer to the parent class without explicitly naming it
class GoodEmployee(Employee, Person):
    def __init__(self, ID, salary, department) -> None:
        print("Good Employee created")
        super().__init__(ID, salary, department)

    def tax(self, percentage, income=None):
        return super().tax(percentage, income)


# Abstract base class
# An abstract base class is a class that cannot be instantiated.
# It is used to define a blueprint for other classes.
class ParentClass(ABC):
    @abstractmethod
    def method(self):
        pass
