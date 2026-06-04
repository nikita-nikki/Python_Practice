


# type() → Returns the data type of a variable
print("type: ",type(10))

# len() → Returns the number of items in a sequence
print("len: ",len("Python"))

# int() → Converts value into integer
print("int: ", int("100"))

# float() → Converts value into decimal number
print("float: ",float("3.14"))

# str() → Converts value into string
print("str: ",str(123))

# sum() → Adds all numbers in an iterable
print("sum: ",sum([10, 20, 30]))

# max() → Returns the largest value
print("max: ",max([5, 2, 9]))

# min() → Returns the smallest value
print("min: ",min([5, 2, 9]))

# sorted() → Returns a sorted list
print("sorted: ",sorted([3, 1, 2]))
print("tyoe of sorted: ",type(sorted("pythoN")))

# range() → Generates a sequence of numbers
print("range: ",(range(5)))


# enumerate() → Returns index and value pairs
print("enumerate")
for i, v in enumerate(["A", "B", "C"]):
    print(i, v)

# abs() → Returns absolute (positive) value
print("abs: ",abs(-10))

# round() → Rounds a number to given decimal places
print(round(3.14159, 2))

# any() → True if at least one value is True
print(any([0, 1, 0]))

# all() → True if all values are True
print(all([1, 1, 1]))

# isinstance() → Checks data type of a variable
print("isinstance: ", isinstance(10, int))

# id() → Returns memory address of object
print(id("Python"))

# pow() → Returns power of a number
print(pow(2, 3))

