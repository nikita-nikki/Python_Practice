# METHOD:
# A method is a function that belongs to an object.
name = "python"
print(name.upper())

# Common mistake
# Methods that modify an object in-place usually return None.
nums = [3, 1, 2]
nums = nums.sort()
print(nums)

# correct way
nums = [3, 1, 2]
nums.sort()
print(nums)



# Strings are immutable.
# Methods create new strings
s = "hello"
s.upper()
print(s)

# correct way:
s = "hello"
s = s.upper()
print(s)