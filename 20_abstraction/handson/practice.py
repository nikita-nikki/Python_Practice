"""
===========================================================
PYTHON OOP — ABSTRACTION (Industry Style)
===========================================================

WHAT IS ABSTRACTION?

Abstraction means:

    Show WHAT an object can do
    Hide HOW it actually does it

User of the class should not care about internal implementation.

Example:

notification.send("Hello")

User should NOT care:
- Is it SMTP?
- Slack API?
- Twilio?
- Retry mechanism?
- Logging?

Those details stay hidden.

WHY INDUSTRIES USE IT?

1. Replace implementation without changing business code
2. Easier testing
3. Scalability
4. Team independence
5. Cleaner architecture

Python implements abstraction mainly using:

    from abc import ABC, abstractmethod

ABC = Abstract Base Class

===========================================================
"""

from abc import ABC, abstractmethod


# ==========================================================
# ABSTRACT CLASS
# ==========================================================

class NotificationService(ABC):
    """
    This class defines CONTRACT only.

    CONTRACT means:

        Any notification system MUST implement:
            send()

    But HOW to send is not defined here.

    Think of this as:

        Backend Team → "Implement send()"

    Industry analogy:
        Interface / blueprint
    """

    @abstractmethod
    def send(self, user, message):
        """
        Abstract method.

        Child classes MUST implement.

        If they don't:
            Python throws error.

        No implementation here.
        """
        pass


# ==========================================================
# IMPLEMENTATION 1
# ==========================================================

class EmailNotification(NotificationService):

    def send(self, user, message):

        """
        Internal implementation hidden.

        Real systems may:

        - Open SMTP connection
        - Authenticate
        - Retry failures
        - Save logs

        Caller doesn't know.
        """

        print(f"[EMAIL] Sent to {user}: {message}")


# ==========================================================
# IMPLEMENTATION 2
# ==========================================================

class SlackNotification(NotificationService):

    def send(self, user, message):

        """
        Completely different implementation.

        Could call:
            Slack REST API

        But business code stays unchanged.
        """

        print(f"[SLACK] Message delivered to {user}: {message}")


# ==========================================================
# IMPLEMENTATION 3
# ==========================================================

class SMSNotification(NotificationService):

    def send(self, user, message):

        """
        Another implementation.

        Could internally:
            - call telecom provider
            - queue messages
            - retry

        Caller does not care.
        """

        print(f"[SMS] Sent to {user}: {message}")


# ==========================================================
# BUSINESS LAYER
# ==========================================================

class OrderService:

    """
    Industry pattern:
        Dependency Injection

    OrderService DOES NOT create Email/SMS.

    Instead:

        someone provides notification service.

    This allows easy replacement.
    """

    def __init__(self, notifier: NotificationService):

        """
        Accept ANY object
        that follows NotificationService contract.
        """

        self.notifier = notifier

    def place_order(self, user):

        print("\nProcessing order...")

        # Business logic
        print("Order created")

        # Notice:
        # OrderService doesn't know
        # whether this is Email/SMS/Slack

        self.notifier.send(
            user,
            "Your order was placed successfully"
        )


# ==========================================================
# MAIN EXECUTION
# ==========================================================

"""
Business requirement changes:

Day 1 → Email
Day 20 → Slack
Day 50 → SMS

No change in OrderService.
Only implementation changes.
"""

email = EmailNotification()

order = OrderService(email)

order.place_order("intern@company.com")


slack = SlackNotification()

order = OrderService(slack)

order.place_order("intern@company.com")


sms = SMSNotification()

order = OrderService(sms)

order.place_order("intern@company.com")


# ==========================================================
# EDGE CASE 1
# ==========================================================

"""
Cannot create abstract class directly.

UNCOMMENT:

x = NotificationService()

ERROR:

TypeError:
Can't instantiate abstract class
"""


# ==========================================================
# EDGE CASE 2
# ==========================================================

class BrokenNotification(NotificationService):

    """
    Forgot to implement send()
    """

    pass


"""
UNCOMMENT:

obj = BrokenNotification()

ERROR:

TypeError:
Can't instantiate abstract class

This protects industry code.
"""


# ==========================================================
# OUTPUT
# ==========================================================

"""
Processing order...
Order created
[EMAIL] Sent to intern@company.com

Processing order...
Order created
[SLACK] Message delivered

Processing order...
Order created
[SMS] Sent
"""


"""
FINAL UNDERSTANDING

Encapsulation:
    Hide DATA

Abstraction:
    Hide IMPLEMENTATION

Polymorphism:
    Same method → different behavior

Inheritance:
    Reuse/extend classes

Industry sentence:

"Code against abstractions,
not implementations."
"""