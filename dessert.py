
#Class names: DessertItem, Candy, Cookie, IceCream, Sundae
class Dessert_item:
    def __init__(self, name):
        self.name = name

    




class Candy(Dessert_item):
    candy_weight: float = 0.0
    price_per_pound: float = 0.0


class Cookie(Dessert_item):
    cookie_quantity: int = 0
    price_per_dozen: float = 0.0


class Icecream(Dessert_item):
    scoop_count: int = 0
    price_per_scoop: float = 0.0

class Sundae(Icecream):
    scoop_count: int = 0
    price_per_scoop: float = 0.0
    topping_name: str = ''
    topping_price: float = 0.0
