''' FUNCTION '''

# A function is a reusable block of code that performs a specific task.
def greet(name):
    return f"Hello, {name}"

print(greet("Bottle"))

# Default arguments are evaluated only once when the function is defined, not every time it is called.
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
print(add_item(3))

# correct way 
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
print(add_item(3))

# If no return statement exists, Python returns None.
def square(x):
    print(x*x)

result = square(5)
print(type(result))



''' Argument & Parameter '''
# Actual values passed during function call.
# Parameter is the variables in the function definition.

''' Variable Length Arguments'''
# *args collects extra positional arguments into a tuple.

"""
*args in Python

*args allows a function to accept a variable number of positional arguments.

Without *args:

"""

def add(a, b):
    return a + b

print(add(10, 20))      # Works

# print(add(10, 20, 30))
# TypeError: add() takes 2 positional arguments but 3 were given


"""
With *args:
-----------
"""

def add_multiple(*args):
    return sum(args)

print(add_multiple(10, 20))
print(add_multiple(10, 20, 30))
print(add_multiple(10, 20, 30, 40))


"""
How it works:
-------------
When you call:

    add_multiple(10, 20, 30)

Python automatically packs the arguments into a tuple:

    args = (10, 20, 30)

Inside the function, args is just a tuple.
"""

def demo(*args):
    print("\nInside demo()")
    print("args =", args)
    print("type =", type(args))

demo(10, 20, 30)


"""
Why not just pass a tuple?

we can do that too.
"""

def total(numbers):
    print("\nReceived tuple:", numbers)
    return sum(numbers)

result = total((10, 20, 30))
print("Sum =", result)


"""
Using *args instead:
--------------------
The caller doesn't need to create a tuple.
"""

def total_args(*numbers):
    print("\nReceived args:", numbers)
    return sum(numbers)

result = total_args(10, 20, 30)
print("Sum =", result)


"""
Packing vs Unpacking
--------------------
"""

nums = (1, 2, 3)

print("\nUnpacking a tuple:")
print(*nums)   # Output: 1 2 3


def show(*args):
    print("\nPacking into tuple:")
    print(args)

show(*nums)
# nums is unpacked -> 1,2,3
# *args packs them back -> (1,2,3)












