# A decorator in Python is a function that adds extra functionality to another function without modifying its original code.

print("TASK 1 - Basic Decorator")

def greet_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@greet_decorator
def greet():
    print("Hello")

greet()

# @decorator
# def greet():
#     print("Hello!")

# EQUIVALENT

# def greet():
#     print("Hello!")
# greet = decorator(greet)


print("\nTASK 2 - Decorator With Arguments")

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(10, 20))


print("\nTASK 3 - Multiple Decorators")

def star(func):
    def wrapper():
        print("*" * 10)
        func()
        print("*" * 10)
    return wrapper

def hash_line(func):
    def wrapper():
        print("#" * 10)
        func()
        print("#" * 10)
    return wrapper

@star
@hash_line
def message():
    print("Decorators")

message()


print("\nTASK 4 - Edge Case: Preserve Return Value")

def timer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@timer
def square(n):
    return n * n

print(square(5))


print("\nTASK 5 - Edge Case")

def star(func):
    def wrapper():
        func()
    return wrapper

@star
def add():
    return 10 + 20

print(add())