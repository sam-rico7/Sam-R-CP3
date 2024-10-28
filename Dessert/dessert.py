#Class names: DessertItem, Candy, Cookie, IceCream, Sundae
class DessertItem:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Candy(DessertItem):
    def __init__(self, name: str = '', candy_weight: float = 0.0, price_per_pound: float = 0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

class Cookie(DessertItem):
    def __init__(self, name: str = '', cookie_quantity: int = 0, price_per_dozen: float = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

class IceCream(DessertItem):
    def __init__(self, name: str = '', scoop_count: int = 0, price_per_scoop: float = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

class Sundae(IceCream):
    def __init__(self, name: str = '', scoop_count: int = 0, price_per_scoop: float = 0.0, 
                 topping_name: str = '', topping_price: float = 0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

class Order:
    def __init__(self):
        self.order = []
    def add(self, item):
        self.order.append(item)
    def __len__(self):
        size = len(self.order)
        return size

def main():
    orderone = Order()
    orderone.add(Candy("Candy Corn", 1.5, .25))
    orderone.add(Candy("Gummy Bears", .25, .35))
    orderone.add(Cookie("Chocolate Chip", 6, 3.99))
    orderone.add(IceCream("Pistachio", 2, .79))
    orderone.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    orderone.add(Cookie("Oatmeal Raisin", 2, 3.45))
    for item in orderone.order:
        print(item)
    print(f"Total number of items in order: {len(orderone)}")

main()

