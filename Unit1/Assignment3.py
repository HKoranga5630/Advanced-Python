# Configurable Payment Processing System
# Using Strategy Design Pattern

from abc import ABC, abstractmethod


# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit Card Payment Strategy
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of Rs.{amount:.2f} made using Credit Card.")


# UPI Payment Strategy
class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of Rs.{amount:.2f} made using UPI.")


# PayPal Payment Strategy
class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of Rs.{amount:.2f} made using PayPal.")


# Payment Processing Context
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if amount <= 0:
            print("Invalid amount! Please enter an amount greater than zero.")
        else:
            self.strategy.pay(amount)


# Main Program
if __name__ == "__main__":

    print("===== Payment Processing System =====")
    print("1. Credit Card")
    print("2. UPI")
    print("3. PayPal")

    choice = input("Select payment method: ")

    if choice == "1":
        strategy = CreditCardPayment()
    elif choice == "2":
        strategy = UPIPayment()
    elif choice == "3":
        strategy = PayPalPayment()
    else:
        print("Invalid payment method!")
        exit()

    processor = PaymentProcessor(strategy)

    try:
        amount = float(input("Enter payment amount (Rs.): "))
        processor.process_payment(amount)
    except ValueError:
        print("Invalid input! Please enter a numeric amount.")