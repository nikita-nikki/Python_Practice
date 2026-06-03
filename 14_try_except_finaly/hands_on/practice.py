# try, except, else, and finally are used for exception handling in Python.

'''
try:
    # risky code
except:
    # runs if an exception occurs
else:
    # runs if no exception occurs
finally:
    # runs no matter what

'''

# Simple try-except
try:
    num = int("abc")
except ValueError:
    print("Invalid number")


# Multiple Exceptions
try:
    num = 10 / 0
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Cannot divide by zero")


# Catching Multiple Exceptions Together
try:
    num = int("abc")
except (ValueError, TypeError):
    print("Some error occurred")