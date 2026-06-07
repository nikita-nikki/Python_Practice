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
print('\n')


# 1. ZeroDivisionError
print("\nZeroDivisionError")

try:
    a = 10
    b = 0   
    print("Result =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")



# 2. ValueError
print("\nValueError")

try:
    num = int("abc")   
    print("Your entered integer is:", num)

except ValueError:
    print("Invalid integer")



# 3. Multiple Exceptions
print("\nMultiple Exceptions")

try:
    x = 10
    y = 0
    print(x / y)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Division by zero is not allowed")



# 4. IndexError
print("\nIndexError")

numbers = [10, 20, 30, 40]

try:
    index = 10   # invalid index
    print(numbers[index])

except IndexError:
    print("Index out of range")



# 5. KeyError
print("\nKeyError")

student = {
    "John": 90,
    "Alice": 95
}

try:
    print(student["Bob"])  # key doesn't exist

except KeyError:
    print("Key not found")





# 6. Else Block
print("\nElse Block")

try:
    num = int("42")  

except ValueError:
    print("Invalid input")

else:
    print("No exception occurred")
    print("Number =", num)



# 7. Finally Block
print("\nFinally block")

try:
    num = int("100")
    print(num)

except ValueError:
    print("Invalid input")

else:
    print("No exception occurred")
    print("Number =", num)

finally:
    print("This always executes")



# 8. Generic Exception
print("\nGeneric Exception")

try:
    a = 10
    b = 0
    print(a / b)

except Exception as e:
    print("Error:", e)



# 9. Raise Custom Exception
print("\nRaise Custom Exception" )

try:
    age = 16

    if age < 18:
        raise ValueError("Age must be at least 18")

    print("Eligible")

except ValueError as e:
    print(e)