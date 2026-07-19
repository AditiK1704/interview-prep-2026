# "Every item on a restaurant menu shares these properties. 
#  The parent class captures what ALL items have in common."
# Parent class



class MenuItem:
    def __init__(self, name: str, price: float, is_available: bool = True):
        self.name         = name
        self.price        = price
        self.is_available = is_available

    def calculate_price(self, qty: int) -> float:
        # narrate: default pricing — child classes may override this
        return self.price * qty

    def get_description(self) -> str:
        # narrate: default description — child can override for richer output
        return self.name

    def __str__(self) -> str:
        status = "✓" if self.is_available else "✗"
        return f"[{status}] {self.get_description()} — ₹{self.price:.2f}"

    def __repr__(self) -> str:
        return f"MenuItem(name={self.name!r}, price={self.price})"
class FoodItem(MenuItem):
    """Hot food items — burgers, pizza, biryani."""

    def __init__(self, name: str, price: float, portion: str, is_veg: bool = False):
        super().__init__(name, price)       # narrate: always call super().__init__ first
        self.portion = portion
        self.is_veg  = is_veg

    def get_description(self) -> str:
        # narrate: override to add portion and veg/non-veg info
        veg_tag = "🟢" if self.is_veg else "🔴"
        return f"{veg_tag} {self.name} ({self.portion})"

    # narrate: no calculate_price override — inherits default (price × qty)


class DrinkItem(MenuItem):
    """Beverages — drinks get a bulk discount for 3+."""

    def __init__(self, name: str, price: float, size_ml: int):
        super().__init__(name, price)
        self.size_ml = size_ml

    def calculate_price(self, qty: int) -> float:
        # narrate: override — custom pricing logic for drinks
        discount = 0.10 if qty >= 3 else 0.0
        return self.price * qty * (1 - discount)

    def get_description(self) -> str:
        return f"{self.name} ({self.size_ml}ml)"


class DessertItem(MenuItem):
    """Cold / sweet items — served at a specific temperature."""

    def __init__(self, name: str, price: float, serving_temp: str):
        super().__init__(name, price)
        self.serving_temp = serving_temp    # "Cold", "Warm", "Room Temperature"

    def get_description(self) -> str:
        return f"{self.name} — serve {self.serving_temp}"

    def calculate_price(self, qty: int) -> float:
        # narrate: desserts use parent's default — we call super() explicitly to show it
        return super().calculate_price(qty)


class ComboItem(MenuItem):
    """Bundle of items sold together at a discount."""

    def __init__(self, name: str, components: list, discount_percent: float = 15):
        # narrate: combo price = sum of parts minus discount
        total = sum(item.price for item in components)
        combo_price = total * (1 - discount_percent / 100)
        super().__init__(name, combo_price)
        self.components      = components
        self.discount_percent = discount_percent

    def get_description(self) -> str:
        parts = " + ".join(c.name for c in self.components)
        return f"{self.name}: [{parts}] ({self.discount_percent}% off)"
class ThaliItem(MenuItem):

    def __init__(self, name, components, is_available=True):
        """
        components:
        List of tuples -> (MenuItem, quantity)

        Example:
        [
            (roti,2),
            (dal,1),
            (sabzi,1)
        ]
        """

        self.components = components

        # Calculate total base price of one thali
        base_price = sum(item.price * qty for item, qty in components)

        # Initialize parent class
        super().__init__(name, base_price, is_available)

    # Polymorphism - Override
    def calculate_price(self, qty):
        return self.price * qty

    # Polymorphism - Override
    def get_description(self):
        description = [f"{self.name} contains:"]

        for item, qty in self.components:
            description.append(f"{qty} x {item.name}")

        return ", ".join(description)


