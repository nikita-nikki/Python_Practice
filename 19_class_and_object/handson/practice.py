"""
====================================================
CLASSES AND OBJECTS 
====================================================

CLASS:
A blueprint/template used to create objects.

OBJECT:
Actual thing created from the class.

Example:
Class  -> Student
Object -> student1, student2

Why classes?
Without classes:
data and functions become scattered.

With classes:
data + behavior stay together.
"""


# ==================================================
# PART 1 — BASIC CLASS
# ==================================================

class Student:
    """
    Class = blueprint.

    Every student object created from this class
    will contain:
    - name
    - age
    """

    def __init__(self, name, age):
        """
        __init__ = Constructor

        WHY?
        Automatically initializes object values.

        self → current object being created.

        Example:
        student1 = Student("Nikki",22)

        Internally:
        self.name="Nikki"
        self.age=22
        """

        self.name = name
        self.age = age

    def introduce(self):
        """
        Method = function inside class

        WHY?
        Behavior belongs to object.

        student1.introduce()
        """

        print(f"My name is {self.name}")
        print(f"My age is {self.age}")


# Creating objects
student1 = Student("Nikki", 22)
student2 = Student("Rahul", 25)

print("\n--- PART 1 ---")

student1.introduce()
student2.introduce()

"""
Reason:

One class → multiple objects

Memory:
student1 → separate data
student2 → separate data
"""


# ==================================================
# PART 2 — OBJECTS STORE THEIR OWN DATA
# ==================================================

print("\n--- PART 2 ---")

student1.age = 23

print(student1.name, student1.age)
print(student2.name, student2.age)

"""
WHY only student1 changed?

Objects are independent.

student1.age
≠
student2.age
"""


# ==================================================
# PART 3 — CLASS ATTRIBUTE
# ==================================================

class Employee:

    """
    Class attribute

    WHY?
    Shared among all objects.

    Stored once.
    """

    company = "OpenAI"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Aman")
emp2 = Employee("Sara")

print("\n--- PART 3 ---")

print(emp1.company)
print(emp2.company)

Employee.company = "Tech Corp"

print(emp1.company)
print(emp2.company)

"""
WHY both changed?

Because company belongs to class,
not object.
"""

emp1.company = "OK"
print(emp1.company)
print(emp2.company)



# ==================================================
# PART 4 — VALIDATION INSIDE CLASS
# ==================================================

class BankAccount:

    def __init__(self, owner, balance):

        """
        WHY validation?

        Prevent invalid objects.

        Bad:
        balance=-100

        Good:
        raise error immediately
        """

        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        """
        WHY check amount?

        Avoid bad updates.
        """

        if amount <= 0:
            print("Deposit must be positive")
            return

        self.balance += amount

    def withdraw(self, amount):

        """
        WHY validation?

        Prevent negative balance.
        """

        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount

    def show_balance(self):

        print("Balance:", self.balance)


print("\n--- PART 4 ---")

account = BankAccount("Nikki", 500)

account.deposit(200)
account.withdraw(100)

account.show_balance()

# Edge cases
account.deposit(-10)
account.withdraw(99999)

print(account)


# ==================================================
# PART 5 — MAGIC METHOD
# ==================================================

class Book:

    def __init__(self, title):
        self.title = title

    def __str__(self):

        """
        WHY __str__ ?

        Controls object display.

        Without it:
        memory address appears.
        """

        return f"Book({self.title})"


print("\n--- PART 5 ---")

book = Book("Python")

print(book)


# ==================================================
# PART 6 — OBJECT COMPARISON
# ==================================================

class Product:

    def __init__(self, price):
        self.price = price

    def __eq__(self, other):

        """
        WHY __eq__ ?

        Custom comparison.

        Without this:
        objects compare addresses.

        With this:
        compare values.
        """

        if not isinstance(other, Product):
            return False

        return self.price == other.price


print("\n--- PART 6 ---")

p1 = Product(100)
p2 = Product(100)

print(p1 == p2)


