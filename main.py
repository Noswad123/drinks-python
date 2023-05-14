from Drink import add_drink, view_drinks, search_drink 
def main():
    while True:
        print("\nCommands: add, view, search, exit")
        command = input("Enter command: ")

        if command.lower() == 'add':
            add_drink()
        elif command.lower() == 'view':
            view_drinks()
        elif command.lower() == 'search':
            drink_name = input("Enter the name of the drink to search: ")
            search_drink(drink_name)
        elif command.lower() == 'exit':
            break
        else:
            print("Invalid command, please try again.")

if __name__ == "__main__":
    main()
    