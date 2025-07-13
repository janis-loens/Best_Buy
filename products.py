# type: ignore
class InventoryError(Exception):
    pass


class Product:

    def __init__(self, name: str, price: float, quantity: int):
        if name == "":
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be of negative value.")
        if quantity < 0:
            raise ValueError("Quantity cannot be of negative value.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        return self.quantity
    

    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False
    

    def is_active(self) -> bool:
        return self.active
    

    def activate(self):
        self.active = True


    def deactivate(self):
        self.activate = False


    def show(self):
        print(f"{self.name}, Price($): {self.price}, Quantity: {self.quantity}")

    
    def buy(self, quantity: int) -> float:
        if self.quantity < quantity:
            raise InventoryError(f"Only {slef.quantity} units are available for purchase.")
        price = quantity * self.price
        self.quantity -= quantity
        return price
    

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()
