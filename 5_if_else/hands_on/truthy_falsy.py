#In Python, every value is considered either Truthy or Falsy when used in conditions like if, while, logical operators, etc.


#Truthy values are those that evaluate to True in a boolean context. Examples of Truthy values include:
# - Non-empty strings (e.g., "hello", "0", "False")
if "hello":
    print("hello is Truthy")
else:
    print("Falsy")

# - Non-zero numbers (e.g., 1, -1, 3.14)
if 10:
    print("10 is Truthy")
else:
    print("10 is Falsy")

# - Non-empty lists, tuples, sets, and dictionaries (e.g., [1, 2], (1, 2), {1, 2}, {"key": "value"})
if [1, 2]:
    print("[1, 2] is Truthy")
else:
    print("[1, 2] is Falsy")



# Falsy values in Python include:
if "":
    print("Empty string is Truthy")
else:
    print("Empty string is Falsy")

# Number
print("bool(0):", bool(0))
print("bool(5):", bool(5))
print("bool(-1):", bool(-1))

# String
print("bool(''): ", bool(''))
print("bool('hello'): ", bool('hello'))

# List
print("bool([]): ", bool([]))
print("bool([1,2]): ", bool([1,2]))

# Dictionary
print("bool({}): ", bool({}))
print("bool({'a':1}): ", bool({'a':1}))

# None
print("bool(None): ", bool(None))



# usecase:
print("Usecase of Truthy and Falsy values:")
name = ""

if name:
    print("Name exists")
else:
    print("Empty name")