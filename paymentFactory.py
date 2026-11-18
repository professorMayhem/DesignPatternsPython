from abc import ABC, abstractmethod


# 1. Common Interface
class PaymentProcessor(ABC):

  @abstractmethod
  def process_payment(self, amount: float) -> None:
    pass


# 2. Concrete Implementations
class VenmoProcessor(PaymentProcessor):

  def process_payment(self, amount: float) -> None:
    print(f"Processing ${amount:.2f} via Venmo API...")


class PayPalProcessor(PaymentProcessor):

  def process_payment(self, amount: float) -> None:
    print(f"Processing ${amount:.2f} via PayPal SDK...")


class BankTransferProcessor(PaymentProcessor):

  def process_payment(self, amount: float) -> None:
    print(f"Initiating ${amount:.2f} ACH Bank Transfer...")


# 3. The Factory
class PaymentFactory:

  @staticmethod
  def get_processor(payment_type: str) -> PaymentProcessor:
    processors = {
        "venmo": VenmoProcessor,
        "paypal": PayPalProcessor,
        "bank": BankTransferProcessor,
    }

    processor_class = processors.get(payment_type.lower())
    if not processor_class:
      raise ValueError(f"Unknown payment type: {payment_type}")

    return processor_class()


# 4. Client Code (Checkout)
if __name__ == "__main__":
  user_choice = "bank"

  # The checkout flow doesn't care which class is instantiated
  processor = PaymentFactory.get_processor(user_choice)
  processor.process_payment(99.99)

  
