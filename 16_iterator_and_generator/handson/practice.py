# ITERATORS AND GENERATORS HANDS-ON 


# --------------------------------------------------
# TASK 1: CREATE AN ITERATOR MANUALLY
# --------------------------------------------------

print("\nTASK 1")

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

it = iter(fruits)

try:
    while True:
        print(next(it))
except StopIteration:
    print("Iterator exhausted")


# --------------------------------------------------
# TASK 2: WHAT HAPPENS AFTER EXHAUSTION
# --------------------------------------------------

print("\nTASK 2")

nums = [1, 2]

it = iter(nums)

try:
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("StopIteration occurred")



# --------------------------------------------------
# TASK 3: NEXT() WITH DEFAULT VALUE
# --------------------------------------------------

print("\nTASK 3")

data = [10, 20]

it = iter(data)

while True:
    value = next(it, "No More Data")

    if value == "No More Data":
        print(value)
        break

    print(value)


# --------------------------------------------------
# TASK 4: GENERATOR COUNT UP TO N
# --------------------------------------------------

print("\nTASK 4")


def count_up_to(n):
    for i in range(1, n + 1):
        yield i


for num in count_up_to(5):
    print(num)


# --------------------------------------------------
# TASK 5: SQUARE GENERATOR
# --------------------------------------------------

print("\nTASK 5")


def square_generator(n):
    for i in range(1, n + 1):
        yield i * i


print("n = 5")
for value in square_generator(5):
    print(value)

print("n = 0")
for value in square_generator(0):
    print(value)

print("n = -3")
for value in square_generator(-3):
    print(value)


# --------------------------------------------------
# TASK 6: INFINITE GENERATOR
# --------------------------------------------------

print("\nTASK 6")


def infinite_numbers():
    num = 1

    while True:
        yield num
        num += 1


gen = infinite_numbers()

for _ in range(10):
    print(next(gen))


# --------------------------------------------------
# TASK 7: EXHAUSTED GENERATOR
# --------------------------------------------------

print("\nTASK 7")

gen = (x for x in range(3))

print("First iteration")

for x in gen:
    print(x)

print("Second iteration")

for x in gen:
    print(x)


