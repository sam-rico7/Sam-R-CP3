#We start classes with keyword class and we name them using PascalCase

class Animal:
    #We start with the constructor
    def __init__(self, name, species, age, gender, rarity):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSpecies: {self.species}\nGender: {self.gender}\nRarity: {self.rarity}"
    

cat = Animal("Tom", "Cat", 21, "Male", "Common")



print(cat)