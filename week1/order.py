from abc import ABC, abstractmethod
from typing import List
from menu import MenuItem


class Order(ABC):
    _id_counter = 1000

    def __init__(self, customer_id: int, items: List[MenuItem]):
        self.order_id = Order._id_counter
        Order._id_counter += 1
        self.customer_id = customer_id
        self.items = items
        self.status = "PENDING"

    @abstractmethod
    def calculate_delivery_fee(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    def get_total(self):
        total = sum(item.price for item in self.items)
        return total + self.calculate_delivery_fee()

    def __str__(self):
        return (
            f"Order #{self.order_id} [{self.get_type()}] | "
            f"Items: {len(self.items)} | "
            f"Total: ₹{self.get_total():.2f} | "
            f"Status: {self.status}"
        )


# ---------------- Delivery ----------------

class DeliveryOrder(Order):

    def __init__(self, customer_id, items, address):
        super().__init__(customer_id, items)
        self.address = address

    def calculate_delivery_fee(self):
        return 40.0

    def get_type(self):
        return "DELIVERY"


# ---------------- Dine In ----------------

class DineInOrder(Order):

    def __init__(self, customer_id, items, table_number):
        super().__init__(customer_id, items)
        self.table_number = table_number

    def calculate_delivery_fee(self):
        return 0.0

    def get_type(self):
        return "DINE_IN"


# ---------------- Pickup ----------------

class PickupOrder(Order):

    def __init__(self, customer_id, items):
        super().__init__(customer_id, items)

    def calculate_delivery_fee(self):
        return 0.0

    def get_type(self):
        return "PICKUP"


# ---------------- Scheduled ----------------

class ScheduledOrder(Order):

    def __init__(self, customer_id, items, address, scheduled_time):
        super().__init__(customer_id, items)
        self.address = address
        self.scheduled_time = scheduled_time

    def calculate_delivery_fee(self):
        return 20.0

    def get_type(self):
        return "SCHEDULED"


# ---------------- Factory ----------------

class OrderFactory:

    @staticmethod
    def create(order_type, customer_id, items, **kwargs):

        order_type = order_type.upper()

        if order_type == "DELIVERY":

            address = kwargs.get("address")
            if address is None:
                raise ValueError("Delivery order requires address.")

            return DeliveryOrder(customer_id, items, address)

        elif order_type == "DINE_IN":

            table = kwargs.get("table")
            if table is None:
                raise ValueError("Dine-in order requires table number.")

            return DineInOrder(customer_id, items, table)

        elif order_type == "PICKUP":

            return PickupOrder(customer_id, items)

        elif order_type == "SCHEDULED":

            address = kwargs.get("address")
            scheduled_time = kwargs.get("scheduled_time")

            if address is None:
                raise ValueError("Scheduled order requires address.")

            if scheduled_time is None:
                raise ValueError("Scheduled order requires scheduled_time.")

            return ScheduledOrder(
                customer_id,
                items,
                address,
                scheduled_time
            )

        else:
            raise ValueError("Invalid order type.")


# ---------------- Example ----------------

if __name__ == "__main__":

    burger = MenuItem("Burger", 199)

    o4 = OrderFactory.create(
        "SCHEDULED",
        customer_id=4,
        items=[burger],
        address="24 Park Street",
        scheduled_time="2026-07-01 19:30"
    )

    print(o4)