"Operators are used to perform operations on variables and values."

# Python divides the operators in the following groups:

# 1.Arithmetic operators
# 2.Assignment operators
# 3.Comparison operators
# 4.Logical operators
# 5.Identity operators
# 6.Membership operators
# 7.Bitwise operators

# 1. Arithmetic operators
a = 2
b = 3
c = a + b
print("Use of Arithmetic operators:",c)

# 2. Assignment operators
x = 5
x += 3
print("Use of Assignment operators:",x)

# 3. Comparison operators
a = 5
b = 3
print("Use of Comparison operators:",a > b)

# 4. Logical operators
print("and")
x = 0
y = 0
z = x and y
print("Use of and Logical operators:",z)

a = 0
b = 1
c = a and b
print("Use of and Logical operators:",c)


print("or")
x = 0
y = 0
z = x or y      
print("Use of or Logical operators:",z)

a = 0
b = 1       
c = a or b
print("Use of or Logical operators:",c)

print("not")
x = 0
y = not x
print("Use of not Logical operators:",y)

# 5. Identity operators
a = 5
b = 5
print("Use of Identity operators:",a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print("Use of Identity operators on lists:",a is b)   # is works on the memory location of the variable, not the value
print("Use of == operators on lists:",a == b)   # == compares the values

# 6. Membership operators
x = "Hello"
print("Use of Membership operators - 'H' in x:",'H' in x)
print("Use of Membership operators - 'h' in x:",'h' in x)

# 7. Bitwise operators
a = 1  # In binary: 0001
b = 2  # In binary: 0010
print("Use of Bitwise operators - a & b:",a & b)  # Bitwise AND
print("Use of Bitwise operators - a | b:",a | b)  # Bitwise OR
print("Use of Bitwise operators - a ^ b:",a ^ b)  # Bitwise XOR     
