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




