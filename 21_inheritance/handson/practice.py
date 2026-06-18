"""
===========================================================
PYTHON OOP — INHERITANCE
===========================================================

WHAT IS INHERITANCE?

Inheritance means:

    Child class gets features of Parent class.

Goal:

    Reuse code instead of rewriting.

Industry sentence:

    "Build common functionality once,
     extend only what changes."

===========================================================
REAL COMPANY EXAMPLE
===========================================================

Every employee can:

- login
- logout

But:

Developer:
    - write_code()

Manager:
    - assign_tasks()

HR:
    - conduct_interview()

Instead of writing login/logout
inside every class, create once.

That is inheritance.

===========================================================
"""


# ==========================================================
# PARENT CLASS
# ==========================================================

class Employee:

    """
    Parent (Base) Class

    Shared functionality lives here.

    Every employee has:
        name
        login
        logout

    Child classes inherit these automatically.
    """

    def __init__(self, name):

        """
        Constructor.

        Runs when object is created.

        Shared setup goes here.
        """

        self.name = name

    def login(self):

        print(f"{self.name} logged in")

    def logout(self):

        print(f"{self.name} logged out")


# ==========================================================
# CHILD CLASS — DEVELOPER
# ==========================================================

class Developer(Employee):

    """
    Developer inherits Employee.

    Means:

        Developer gets:

        - name
        - login()
        - logout()

    without rewriting.
    """

    def write_code(self):

        print(f"{self.name} is writing Python code")


# ==========================================================
# CHILD CLASS — MANAGER
# ==========================================================

class Manager(Employee):

    """
    Another child.

    Same parent.

    Different capability.
    """

    def assign_task(self):

        print(f"{self.name} assigned work")


# ==========================================================
# CHILD CLASS — HR
# ==========================================================

class HR(Employee):

    def conduct_interview(self):

        print(f"{self.name} is conducting interview")


# ==========================================================
# MAIN EXECUTION
# ==========================================================

"""
Create Developer.

Developer constructor?

Developer doesn't have __init__.

Python automatically uses:

Employee.__init__()
"""

dev = Developer("Nikki")

dev.login()          # inherited
dev.write_code()     # own method
dev.logout()         # inherited


print("\n----------------")


mgr = Manager("Aman")

mgr.login()
mgr.assign_task()
mgr.logout()


print("\n----------------")


hr = HR("Riya")

hr.login()
hr.conduct_interview()
hr.logout()


# ==========================================================
# OUTPUT
# ==========================================================

"""
Nikki logged in
Nikki is writing Python code
Nikki logged out

----------------

Aman logged in
Aman assigned work
Aman logged out

----------------

Riya logged in
Riya is conducting interview
Riya logged out
"""


# ==========================================================
# METHOD OVERRIDING
# ==========================================================

"""
Inheritance becomes powerful when child
changes parent behavior.

Industry example:

Managers login differently.
"""


class SecureManager(Employee):

    def login(self):

        """
        Same method name.

        Parent version replaced.
        """

        print(
            f"{self.name} logged in with 2FA"
        )


print("\n--- OVERRIDE ---")

secure = SecureManager("Rahul")

secure.login()


"""
Output:

Rahul logged in with 2FA
"""


# ==========================================================
# USING super()
# ==========================================================

"""
Sometimes child needs:

Parent logic
+
Extra logic

Use super()
"""


class SeniorDeveloper(Employee):

    def __init__(self, name, level):

        """
        Reuse parent constructor.

        Avoid duplicate code.
        """

        super().__init__(name)

        self.level = level

    def show(self):

        print(
            f"{self.name} -> {self.level}"
        )


print("\n--- SUPER ---")

senior = SeniorDeveloper(
    "Meera",
    "SDE-3"
)

senior.login()

senior.show()


# ==========================================================
# EDGE CASE
# ==========================================================

"""
Inheritance relation:

Developer IS AN Employee

Manager IS AN Employee

Wrong thinking:

Laptop IS Employee

No.

Use inheritance only when
child truly IS parent.

Bad inheritance creates bad design.
"""


# ==========================================================
# MULTILEVEL INHERITANCE
# ==========================================================

class User:

    def authenticate(self):
        print("User authenticated")


class EmployeeUser(User):

    pass


class Admin(EmployeeUser):

    pass


admin = Admin()

admin.authenticate()

"""
Admin

inherits

Admin
↓

EmployeeUser
↓

User
"""


# ==========================================================
# FINAL MEMORY
# ==========================================================

"""
Inheritance =
Reuse existing behavior

Syntax:

class Child(Parent)

Important concepts:

1. Parent class
2. Child class
3. Method overriding
4. super()
5. IS-A relationship

Industry advice:

Use inheritance for common behavior.

Do not inherit just to reuse code.
"""