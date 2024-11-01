import random

class Monster:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
    
    def attack(self):
        pass
    
    def introduce(self):
        return f"I am {self.name}, a terrifying monster from {self.origin}!"

class Vampire(Monster):
    def __init__(self, name, origin, preferred_blood_type):
        super().__init__(name, origin)
        self.preferred_blood_type = preferred_blood_type
    
    def attack(self):
        return f"{self.name} swoops in silently and sinks their fangs into your neck! They have a particular taste for {self.preferred_blood_type} blood."
    
    def transform(self):
        return f"{self.name} transforms into a bat and flies away into the night!"

class Werewolf(Monster):
    def __init__(self, name, origin, moon_phase):
        super().__init__(name, origin)
        self.moon_phase = moon_phase
    
    def attack(self):
        return f"{self.name} howls at the {self.moon_phase} moon and lunges at you with razor-sharp claws!"
    
    def sniff(self):
        return f"{self.name} raises their snout and sniffs the air, tracking their prey."

class Zombie(Monster):
    def __init__(self, name, origin, decomposition_stage):
        super().__init__(name, origin)
        self.decomposition_stage = decomposition_stage
    
    def attack(self):
        return f"{self.name}, a {self.decomposition_stage} zombie, shuffles towards you with outstretched arms, groaning 'Braaains!'"
    
    def infect(self):
        return f"{self.name} attempts to spread the zombie virus through a bite!"

class Ghostly_Apparition(Monster):
    def __init__(self, name, origin, haunting_specialty):
        super().__init__(name, origin)
        self.haunting_specialty = haunting_specialty
    
    def attack(self):
        return f"{self.name} materializes suddenly, causing a bone-chilling cold, and unleashes their {self.haunting_specialty} haunting!"
    
    def possess(self, object):
        return f"{self.name} attempts to possess the {object}, making it float ominously!"

# Create some monster instances
dracula = Vampire("Count Dracula", "Transylvania", "O-negative")
luna = Werewolf("Luna Howler", "Black Forest", "full")
shambler = Zombie("Shambler", "Abandoned Mall", "moderately decayed")
whisper = Ghostly_Apparition("Whisper", "Ancient Manor", "terrifying whispers")

# Demonstrate their abilities
monsters = [dracula, luna, shambler, whisper]

print("Welcome to the Monster Mash! Let's meet our terrifying contestants:")
for monster in monsters:
    print("\n" + monster.introduce())
    print(monster.attack())

    # Demonstrate unique methods
    if isinstance(monster, Vampire):
        print(monster.transform())
    elif isinstance(monster, Werewolf):
        print(monster.sniff())
    elif isinstance(monster, Zombie):
        print(monster.infect())
    elif isinstance(monster, Ghostly_Apparition):
        random_object = random.choice(["chandelier", "rocking chair", "old painting"])
        print(monster.possess(random_object))

print("\nHappy Halloween! 🎃👻")