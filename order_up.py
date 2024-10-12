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
    prices = {
        "Drinks": {"Water": 0.00, "Lemonade": 2.50, "Manzana Postobon": 3.00, "Colombiana": 3.00, "Refajo (Jarra)": 5.00, "Pony Malta": 2.50, "Jugo de Lulo": 3.00, "Jugo de Maracuya": 3.00},
        "Appetizers": {"Patacones": 4.50, "Chicharron Carnudo": 5.00, "Empanadas": 3.00, "Chorizos": 4.00, "Morcillas": 4.50, "Arepa de Chocolo": 3.50, "Chunchullo": 5.00},
        "Main Courses": {"Bandeja Paisa": 15.00, "Mondongo": 13.00, "Ajiaco": 12.50, "Bistec a Caballo": 14.00, "Lengua en Salsa Criolla": 16.00, "Menu infantil": 10.00, "Picada Antioqueña": 18.00, "Cazuela de Frijoles": 13.50, "Mazamorra Chiquita": 12.00},
        "Sides": {"Arroz": 2.00, "Papa Francesa": 2.50, "Patacon": 2.00, "Papa en Cascos": 2.50, "Platano Maduro": 2.50, "Frijoles": 3.00, "Arepa": 1.50},
        "Desserts": {"Leche Asada": 4.00, "Brevas con Arequipe": 4.50, "Dulce de Mora": 4.00, "Brownie con Helado": 5.00, "Duraznos con Arequipe": 4.50}
    }

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

    @staticmethod
    def calculate_total(drink, appetizer, main, side1, side2, dessert):
        total = 0
        if drink in Dinner.prices["Drinks"]:
            total += Dinner.prices["Drinks"][drink]
        if appetizer in Dinner.prices["Appetizers"]:
            total += Dinner.prices["Appetizers"][appetizer]
        if main in Dinner.prices["Main Courses"]:
            total += Dinner.prices["Main Courses"][main]
        if side1 in Dinner.prices["Sides"]:
            total += Dinner.prices["Sides"][side1]
        if side2 in Dinner.prices["Sides"]:
            total += Dinner.prices["Sides"][side2]
        if dessert in Dinner.prices["Desserts"]:
            total += Dinner.prices["Desserts"][dessert]
        return total

    def display_menu(self):
        print("\n=== This is our menu of the day! You can choose a drink, an appetizer, a main course, two sides, and a dessert. ===")
        print("1. Drinks")
        print("2. Appetizers")
        print("3. Main Courses")
        print("4. Sides")
        print("5. Desserts")
        print("6. Exit and order.")
        print("==============================")

    def get_choice(self, category, menu):
        print(f"\n{category} Menu:")
        for i, item in enumerate(menu[category], 1):
            print(f"{i}. {item}")
        
        while True:
            try:
                choice = int(input(f"Please select a {category.lower()[:-1]} by typing its number: "))
                if 1 <= choice <= len(menu[category]):
                    selected_item = menu[category][choice - 1]
                    print(f"Got it! You selected {selected_item}.")
                    return selected_item
                else:
                    print(f"Invalid selection. Please choose a number between 1 and {len(menu[category])}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

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

        # Calculate the total cost
        total_price = Dinner.calculate_total(self.drink, self.appetizer, self.main, self.side1, self.side2, self.dessert)
        print(f"Total Price: ${total_price:.2f}")

menu = {
    "Drinks": ["Water", "Lemonade", "Manzana Postobon", "Colombiana", "Refajo (Jarra)", "Pony Malta", "Jugo de Lulo", "Jugo de Maracuya"],
    "Appetizers": ["Patacones", "Chicharron Carnudo", "Empanadas", "Chorizos", "Morcillas", "Arepa de Chocolo", "Chunchullo"],
    "Main Courses": ["Bandeja Paisa", "Mondongo", "Ajiaco", "Bistec a Caballo", "Lengua en Salsa Criolla", "Menu infantil", "Picada Antioqueña", "Cazuela de Frijoles", "Mazamorra Chiquita"],
    "Sides": ["Arroz", "Papa Francesa", "Patacon", "Papa en Cascos", "Platano Maduro", "Frijoles", "Arepa"],
    "Desserts": ["Leche Asada", "Brevas con Arequipe", "Dulce de Mora", "Brownie con Helado", "Duraznos con Arequipe"]
}

dinner1 = Dinner()
dinner1.run(menu)
