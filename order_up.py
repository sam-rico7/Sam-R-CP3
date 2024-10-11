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

    def run(self, menu):
        while True:
            self.display_menu()
            choice = input("Please select what category you want to see (1-6): ")

            if choice == '1':
                print("\nDrinks:")
                print(", ".join(menu["Drinks"]))
                drinkchoice = input("Would you like to order any of the drinks?\n(1) Yes  (2) No:  ")
                if drinkchoice == '1':
                    print("Perfect!")
                    yesdrinkchoice = input("What drink would you like? Please type the entire name: ")
                    yesdrinkchoice1 = yesdrinkchoice.capitalize()
                    if yesdrinkchoice1 in menu.values():
                        print("Got it!")   
                    else:
                        print("This drink is not in our menu, please try again.")
            elif choice == '2':
                print("\nAppetizers:")
                print(", ".join(menu["Appetizers"]))
                appetizerchoice = input("Would you like to order any of the appetizers?\n(1) Yes  (2) No:  ")
                if appetizerchoice == '1':
                    print("Perfect!")
                    yesappetizer = input("What drink would you like? Please type the entire name: ")
                    yesappetizer1 = yesappetizer.capitalize()
                    if yesappetizer1 in menu.values():
                        print("Got it!")   
                    else:
                        print("This appetizer is not in our menu, please try again.")
            elif choice == '3':
                print("\nMain Courses:")
                print(", ".join(menu["Main Courses"]))
                maincourse = input("Would you like to order any of the Main Courses?\n(1) Yes  (2) No:  ")
                if maincourse == '1':
                    print("Perfect!")
                    yesmaincourse = input("What Main Course would you like? Please type the entire name: ")
                    yesmaincourse1 = yesmaincourse.capitalize()
                    if yesmaincourse1 in menu.values():
                        print("Got it!")   
                    else:
                        print("This Main Course is not in our menu, please try again.")
            elif choice == '4':
                print("\nSides:")
                print(", ".join(menu["Sides"]))
            elif choice == '5':
                print("\nDesserts:")
                print(", ".join(menu["Desserts"]))
                dessertchoice = input("Would you like to order any of the drinks?\n(1) Yes  (2) No:  ")
                if dessertchoice == '1':
                    print("Perfect!")
                    yesdessertchoice = input("What drink would you like? Please type the entire name: ")
                    yesdessertchoice1 = yesdessertchoice.capitalize()
                    if yesdessertchoice1 in menu.values():
                        print("Got it!")   
                    else:
                        print("This drink is not in our menu, please try again.")
            elif choice == '6':
                print("\nExiting the program.")
                break
            else:
                print("\nInvalid choice. Please try again.")


menu = {
    "Drinks": ["Water", "Lemonade", "Manzana Postobon", "Colombiana", "Refajo (Jarra)", "Pony Malta", "Jugo de Lulo", "Jugo de Maracuya"],
    "Appetizers": ["Patacones", "Chicharron Carnudo", "Empanadas", "Chorizos", "Morcillas", "Arepa de Chocolo", "Chunchullo"],
    "Main Courses": ["Bandeja Paisa", "Mondongo", "Ajiaco", "Bistec a Caballo", "Lengua en Salsa Criolla", "Menu infantil", "Picada Antioqueña", "Cazuela de Frijoles", "Mazamorra Chiquita"],
    "Sides": ["Arroz", "Papa Francesa", "Patacon", "Papa en Cascos", "Platano Maduro", "Frijoles", "Arepa"],
    "Desserts": ["Leche Asada", "Brevas con Arequipe", "Dulce de Mora", "Brownie con Helado", "Duraznos con Arequipe"]
}

dinner1 = Dinner()
dinner1.run(menu)



























