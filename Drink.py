class Drink:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

drinks = []

def add_drink():
    name = input("Enter drink name: ")
    num_ingredients = int(input("Enter the number of ingredients: "))
    ingredients = []
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)

    instructions = input("Enter the instructions to prepare the drink: ")
    new_drink = Drink(name, ingredients, instructions)
    drinks.append(new_drink)

def view_drinks():
    for drink in drinks:
        print("\nDrink:", drink.name)
        print("Ingredients:", ", ".join(drink.ingredients))
        print("Instructions:", drink.instructions)

def search_drink(drink_name):
    found = False
    for drink in drinks:
        if drink.name.lower() == drink_name.lower():
            print("\nDrink:", drink.name)
            print("Ingredients:", ", ".join(drink.ingredients))
            print("Instructions:", drink.instructions)
            found = True
            break

    if not found:
        print("No drink found with the given name.")