# ENUMERATE

# enumerate() is actually a built-in function, not a method. It is used to get both the index and the value while iterating.

# enumerate(iterable, start=0)
# iterable → list, tuple, string, etc.
# start → starting index (default = 0)

fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


# It returns an enumerate object (an iterator)
fruits = ["apple", "banana", "mango"]
e = enumerate(fruits)
print(e)
print(list(e))

# enumerate() takes each item from fruits and pairs it with a counter.
fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

