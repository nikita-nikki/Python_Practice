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
# TASK 4: COUNT FROM 1 TO N
# --------------------------------------------------

print("\nTASK 4")


class Counter:

    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


for num in Counter(5):
    print(num)


# --------------------------------------------------
# TASK 5: REVERSE ITERATOR
# --------------------------------------------------

print("\nTASK 5")


class ReverseString:

    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        char = self.text[self.index]
        self.index -= 1
        return char


for ch in ReverseString("Python"):
    print(ch)

print("Empty string test:")

for ch in ReverseString(""):
    print(ch)


# --------------------------------------------------
# TASK 6: EVEN NUMBER ITERATOR
# --------------------------------------------------

print("\nTASK 6")


class EvenNumbers:

    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 2
        return value


print("Limit = 10")
for num in EvenNumbers(10):
    print(num)

print("Limit = 0")
for num in EvenNumbers(0):
    print(num)

print("Limit = -5")
for num in EvenNumbers(-5):
    print(num)

print("Limit = 1")
for num in EvenNumbers(1):
    print(num)


# --------------------------------------------------
# TASK 7: GENERATOR COUNT UP TO N
# --------------------------------------------------

print("\nTASK 7")


def count_up_to(n):
    for i in range(1, n + 1):
        yield i


for num in count_up_to(5):
    print(num)


# --------------------------------------------------
# TASK 8: SQUARE GENERATOR
# --------------------------------------------------

print("\nTASK 8")


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
# TASK 9: INFINITE GENERATOR
# --------------------------------------------------

print("\nTASK 9")


def infinite_numbers():
    num = 1

    while True:
        yield num
        num += 1


gen = infinite_numbers()

for _ in range(10):
    print(next(gen))


# --------------------------------------------------
# TASK 10: GENERATOR EXPRESSION VS LIST
# --------------------------------------------------

print("\nTASK 10")

nums = range(1000000)

list_comp = [x * x for x in nums]
gen_exp = (x * x for x in nums)

print(type(list_comp))
print(type(gen_exp))


# --------------------------------------------------
# TASK 11: EXHAUSTED GENERATOR
# --------------------------------------------------

print("\nTASK 11")

gen = (x for x in range(3))

print("First iteration")

for x in gen:
    print(x)

print("Second iteration")

for x in gen:
    print(x)


