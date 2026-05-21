# Basic
age = 20
if age > 18 and age < 25:
    print("Eligible")

marks = 85

if marks > 90 or marks > 80:
    print("Good Marks")

# Handling Division by Zero
x = 0

if x != 0 and 10/x > 1:
    print("Yes - Division is possible and result is greater than 1")
else:
    print("No - Division by zero or result is not greater than 1")

'''
No error occurs because:
x != 0 is False
Python never evaluates 10/x

'''

# Short-circuiting with 'or'
a = "" or "Python"
print("a =", a)

b = 0 or 42 or "Hello"
print("b =", b)

'''
or returns first truthy value

'''
# Short-circuiting with 'and'
x = 0 and 10
print("x =", x)
print("Type of x =", type(x))

y = 5 and 10
print("y =", y)
print("Type of y =", type(y))

z = "Hi" and 100
print("z =", z)
print("Type of z =", type(z))

'''
and returns first falsy value or last value if all are truthy

'''

