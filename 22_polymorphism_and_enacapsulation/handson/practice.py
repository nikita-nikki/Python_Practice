# ==========================================
# HANDS-ON: POLYMORPHISM + ENCAPSULATION
# PROJECT: FOOD DELIVERY APP
# ==========================================


# -----------------------------
# PART 1 → ENCAPSULATION
# -----------------------------
# Goal:
# Protect order amount and allow access only
# through methods.


class Order:

    def __init__(self, customer_name, amount):

        self.customer_name = customer_name

        # Encapsulation
        self.__amount = amount


    # Getter
    def get_amount(self):
        return self.__amount


    # Setter
    def update_amount(self, new_amount):

        if new_amount > 0:
            self.__amount = new_amount
            print("Order updated")

        else:
            print("Invalid amount")


# -----------------------------
# PART 2 → POLYMORPHISM
# -----------------------------
# Goal:
# Different payment methods
# same function call


class Payment:

    def pay(self):
        pass


class CreditCard(Payment):

    def pay(self):
        print("Payment done using Credit Card")


class UPI(Payment):

    def pay(self):
        print("Payment done using UPI")


class Cash(Payment):

    def pay(self):
        print("Payment done using Cash")



# Common function
def process_payment(method):

    # Same method
    # Different behavior
    method.pay()



# -----------------------------
# TESTING
# -----------------------------

print("ENCAPSULATION")

order = Order("Nikki", 500)

print("Current Amount:", order.get_amount())

order.update_amount(700)

print("Updated Amount:", order.get_amount())


print("\nPOLYMORPHISM")

card = CreditCard()
upi = UPI()
cash = Cash()

process_payment(card)
process_payment(upi)
process_payment(cash)



