
class pokemon:
    def __init__(self, name, hp, typ, lvl):
        self.name = name
        self.hp = hp
        self.typ = typ
        self.lvl = lvl

    def combat(self, other):
        if self.lvl > other.lvl:
            return f"{self.name} won!"
        elif self.lvl < other.lvl:
            return f"{other.name} won!"
        else:
            return f"{self.name} and {other.name} tied!"

    def __str__(self):
        return(f"""
               name: {self.name}
               typ: {self.typ}
               lvl: {self.lvl}
               Hp: {self.hp}
""")
    
    def lvl_up(self):
        self.lvl += 1
        self.hp = int(self.hp*1.5)

    # @classmethod used to keep method from changing object instances!

    @classmethod
    def pikachu(self):
        return pokemon(input("Give me a name: "), 50, "Electric", 1)

    # @staticmethod do not require self or class
    @staticmethod
    def hp_update(poke):
        return poke.hp - 5

    
eevee = pokemon("JayRod", 37, "Normal", 2)
pika = pokemon.pikachu()
pika.hp = pokemon.hp_update(pika)
print(pika)