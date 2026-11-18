Design Patterns examples for my CSCI 305 class at Montana Tech.

Payment Factory:

Problem:  Your e-commerce application needs to process payments, and customers can choose to pay via Venmo, PayPal, or Bank Transfer. If you write new VenmoPayment() or new PayPalPayment() directly inside your checkout code, your business logic becomes tightly coupled to specific third-party APIs. Whenever you add a new payment method (like Apple Pay or Crypto), you have to modify your checkout code everywhere.

Solution:  Create a common interface and a factory class that hides the instantiation details: 
* Common Interface: A PaymentProcessor interface with a processPayment() method.
* Concrete Classes: VenmoProcessor, PayPalProcessor, and BankTransferProcessor that implement that interface.
* The Factory: A PaymentFactory class with a method like createPaymentProcessor(type) that inspects the user's choice and returns the right object.

See paymentFactory.py for example solution.

-----------------------
Coffee Decorator:

The Coffee Shop example is the classic way to explain the Decorator Design Pattern, which lets you attach new behaviors or costs to an object dynamically by placing it inside wrapper objects.

How It Works:  Instead of creating a separate class for every possible drink combination (e.g., CoffeeWithMilk, CoffeeWithMilkAndSugar, EspressoWithWhippedCream), you build the drink in layers.
• Base Component: You start with a core drink object, like a plain SimpleCoffee.
• Wrapper Layers: Each add-on (milk, sugar, caramel) is a decorator class that wraps around the drink object.
• Delegation: When you ask the final wrapped object for its total cost or description, each layer calculates its own addition and passes the request down to the layer inside it.

See coffeeDecorator.py for example solution 

-------------------------

Media Player Adapter:

The Tutorialspoint example is a good illustration of the Adapter Pattern because it demonstrates how an existing class can work with a new interface without changing the existing class.  It supports backward (or "forward") compatibility.

The example is here:  https://www.tutorialspoint.com/design_pattern/adapter_pattern.htm

The scenario is:
- An AudioPlayer can already play MP3 files.
- We want it to also play VLC and MP4 files.
- Separate advanced players know how to handle VLC and MP4 files.
- A MediaAdapter allows the existing AudioPlayer to communicate with those advanced players.
The important idea is that we don't modify the original audio player to understand every new format. Instead, we introduce an adapter that translates the requests.

<img width="969" height="632" alt="image" src="https://github.com/user-attachments/assets/17e24ba2-5398-438a-ab05-5c9eac1c460a" />

The UML:
<img width="560" height="387" alt="image" src="https://github.com/user-attachments/assets/63316d20-b8f8-4dd4-be74-737c14913176" />



