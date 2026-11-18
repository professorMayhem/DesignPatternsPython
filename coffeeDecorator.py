from abc import ABC, abstractmethod


# 1. Component Interface
class Coffee(ABC):
  @abstractmethod
  def get_description(self) -> str:
    pass

  @abstractmethod
  def get_cost(self) -> float:
    pass


# 2. Concrete Component
class PlainCoffee(Coffee):

  def get_description(self) -> str:
    return "Plain Coffee"

  def get_cost(self) -> float:
    return 2.00


# 3. Base Decorator
class CoffeeDecorator(Coffee):

  def __init__(self, coffee: Coffee):
    self._coffee = coffee

  def get_description(self) -> str:
    return self._coffee.get_description()

  def get_cost(self) -> float:
    return self._coffee.get_cost()


# 4. Concrete Decorators
class Milk(CoffeeDecorator):

  def get_description(self) -> str:
    return f"{self._coffee.get_description()}, Milk"

  def get_cost(self) -> float:
    return self._coffee.get_cost() + 0.50


class Sugar(CoffeeDecorator):

  def get_description(self) -> str:
    return f"{self._coffee.get_description()}, Sugar"

  def get_cost(self) -> float:
    return self._coffee.get_cost() + 0.20


class Flavor(CoffeeDecorator):

    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, Flavor"
    
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.75


# --- Usage at Runtime ---
# Start with a plain coffee
my_coffee = PlainCoffee()
print(f"{my_coffee.get_description()} -> ${my_coffee.get_cost():.2f}")
# Output: Plain Coffee -> $2.00

# Wrap it with milk
my_coffee = Milk(my_coffee)
print(f"{my_coffee.get_description()} -> ${my_coffee.get_cost():.2f}")
# Output: Plain Coffee, Milk -> $2.50

# Wrap it again with sugar
my_coffee = Sugar(my_coffee)
print(f"{my_coffee.get_description()} -> ${my_coffee.get_cost():.2f}")
# Output: Plain Coffee, Milk, Sugar -> $2.70

my_coffee = Flavor(my_coffee)
print(f"{my_coffee.get_description()} -> ${my_coffee.get_cost():.2f}")
