Design Patterns examples for my CSCI 305 class at Montana Tech.

Payment Factory:

Problem:  Your e-commerce application needs to process payments, and customers can choose to pay via Venmo, PayPal, or Bank Transfer. If you write new VenmoPayment() or new PayPalPayment() directly inside your checkout code, your business logic becomes tightly coupled to specific third-party APIs. Whenever you add a new payment method (like Apple Pay or Crypto), you have to modify your checkout code everywhere.

Solution:  Create a common interface and a factory class that hides the instantiation details: 
* Common Interface: A PaymentProcessor interface with a processPayment() method.
* Concrete Classes: VenmoProcessor, PayPalProcessor, and BankTransferProcessor that implement that interface.
* The Factory: A PaymentFactory class with a method like createPaymentProcessor(type) that inspects the user's choice and returns the right object.

See paymentFactory.py for example solution.
