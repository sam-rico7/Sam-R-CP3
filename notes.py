#We start classes with keyword class and we name them using PascalCase

class Animal:
    #We start with the constructor (defines all the atttributes of the object being created)
    def __init__(self, name, species, age, gender, rarity):

        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity


    #Methods are functions inside of the class
    def fight(self, other):
        if len(self.name) > len(other.name):
            other.losses += 1
            return self.name
        elif len(self.name) < len(other.name):
            self.losses +=1
            return other.name
        else:
            self.losses += 1
            other.losses += 1
            return "Tie"
        

    def get_name(self):
        return self.name

    #Makes a more readable string when printed
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSpecies: {self.species}\nGender: {self.gender}\nRarity: {self.rarity}"
    


#We generally store object in variables (individually or in a list) so we can use it.
cat = Animal("Cat", 21, "Male", "Common")
frog = Animal("Jarrod", "Poison Dart Frog", 500, "Female", "Rare")


#To call a method you put the name of the object.name of the method (any arguments that are needed)
cat.losses = 0
frog.losses = 0
print(cat.fight(frog))
print(cat.losses)

cat.name = "Thomas"
print(cat.losses)

print(cat.fight(frog))
print(cat.losses)
print(frog.losses)

cat = None
print(cat.name)