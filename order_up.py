#Create a program that uses a class to take an order at a diner. 

 

#The class for the order needs to have space for

#A drink
#An appetizer 
#A main course
#Two sides
#A dessert
#Please note that the user doesn't have to order an item for each category, they just need to be given the option

#The class needs to have methods that

#Prints out everything the user has ordered
#Gives the user a total for their order 
#Checks to see if ordered items are on the men (Tells user if what they ordered isn't on the menu)
#Makes sure that the user has ordered at least 1 item
#Allows user to place their order 
#Allows user to change an item in their order



class Dinner:
    def __init__(self, drink="", appetizer="", main="", side1="", side2="", dessert=""):
        self.drink = drink
        self.appetizer = appetizer
        self.main = main
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert

    def __str__(self):
        return (f"Drink: {self.drink}\n"
                f"Appetizer: {self.appetizer}\n"
                f"Main Course: {self.main}\n"
                f"Side 1: {self.side1}\n"
                f"Side 2: {self.side2}\n"
                f"Dessert: {self.dessert}")

    def display_menu(self):
        print("\n=== This is our menu of the day! You can choose a drink, an appetizer, a main course, two sides, and a dessert. ===")
        print("1. Drinks")
        print("2. Appetizers")
        print("3. Main Courses")
        print("4. Sides")
        print("5. Desserts")
        print("6. Exit")
        print("==============================")

    def get_choice(self, category, menu):
        print(f"\n{category}:")
        print(", ".join(menu[category]))
        choice = input(f"Would you like to order any of the {category.lower()}?\n(1) Yes  (2) No:  ")
        if choice == '1':
            print("Perfect!")
            item = input(f"What {category.lower()[:-1]} would you like? Please type the entire name: ").title()
            if item in menu[category]:
                print("Got it!")
                return item
            else:
                print(f"This {category.lower()[:-1]} is not in our menu, please try again.")
        return ""

    def run(self, menu):
        while True:
            self.display_menu()
            choice = input("Please select what category you want to see (1-6): ")

            if choice == '1':
                self.drink = self.get_choice("Drinks", menu)
            elif choice == '2':
                self.appetizer = self.get_choice("Appetizers", menu)
            elif choice == '3':
                self.main = self.get_choice("Main Courses", menu)
            elif choice == '4':
                print("\nSides:")
                print(", ".join(menu["Sides"]))
                self.side1 = self.get_choice("Sides", menu)
                if self.side1:
                    self.side2 = self.get_choice("Sides", menu)
            elif choice == '5':
                self.dessert = self.get_choice("Desserts", menu)
            elif choice == '6':
                print("\nExiting the program.")
                break
            else:
                print("\nInvalid choice. Please try again.")

        print("\nYour dinner order:")
        print(self)

menu = {
    "Drinks": ["Water", "Lemonade", "Manzana Postobon", "Colombiana", "Refajo (Jarra)", "Pony Malta", "Jugo de Lulo", "Jugo de Maracuya"],
    "Appetizers": ["Patacones", "Chicharron Carnudo", "Empanadas", "Chorizos", "Morcillas", "Arepa de Chocolo", "Chunchullo"],
    "Main Courses": ["Bandeja Paisa", "Mondongo", "Ajiaco", "Bistec a Caballo", "Lengua en Salsa Criolla", "Menu infantil", "Picada Antioqueña", "Cazuela de Frijoles", "Mazamorra Chiquita"],
    "Sides": ["Arroz", "Papa Francesa", "Patacon", "Papa en Cascos", "Platano Maduro", "Frijoles", "Arepa"],
    "Desserts": ["Leche Asada", "Brevas con Arequipe", "Dulce de Mora", "Brownie con Helado", "Duraznos con Arequipe"]
}

dinner1 = Dinner()
dinner1.run(menu)