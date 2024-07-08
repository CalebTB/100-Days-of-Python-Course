def check_resources(user_coffee_type):
    if user_coffee_type == "espresso":
        menu_water, menu_coffee = (MENU[user_coffee_type]["ingredients"]["water"],
                                   MENU[user_coffee_type]["ingredients"]["coffee"])
        water, coffee = (resources["water"],
                         resources["coffee"])
        if menu_water > water:
            return "Sorry, We are out of water."
        if menu_coffee > coffee:
            return "Sorry, We are out of coffee."
        return "Good"

    if user_coffee_type == "latte" or user_coffee_type == "coffee":
        menu_water, menu_milk, menu_coffee = (MENU[user_coffee_type]["ingredients"].values())
        water, milk, coffee = (resources["water"],
                               resources["milk"],
                               resources["coffee"])

        if menu_water > water:
            return "Sorry, We are out of water."
        if menu_milk > milk:
            return "Sorry, We are out of milk."
        if menu_coffee > coffee:
            return "Sorry, We are out of coffee."
        return "Good"


def coffee_machine(user_coffee_type):
    if user_coffee_type == "espresso":
        menu_water, menu_coffee = (MENU[user_coffee_type]["ingredients"]["water"],
                                   MENU[user_coffee_type]["ingredients"]["coffee"])
        water, milk, coffee = (resources["water"],
                               resources["milk"],
                               resources["coffee"])

        resources["water"] = water - menu_water
        resources["milk"] = milk
        resources["coffee"] = coffee - menu_coffee

    if user_coffee_type == "latte" or user_coffee_type == "coffee":
        menu_water, menu_milk, menu_coffee = MENU[user_coffee_type]["ingredients"].values()
        water, milk, coffee = (resources["water"],
                               resources["milk"],
                               resources["coffee"])

        resources["water"] = water - menu_water
        resources["milk"] = milk - menu_milk
        resources["coffee"] = coffee - menu_coffee


def report():
    for key, value in resources.items():
        print(f'{key}: {value}'.title())


def get_change():
    change_pennies = int(input("How many pennies? "))
    change_nickles = int(input("How many nickles? "))
    change_dimes = int(input("How many dimes? "))
    change_quarters = int(input("How many quarters? "))
    return (change_pennies * 0.01) + (change_dimes * 0.05) + (change_nickles * 0.10) + (change_quarters * 0.25)


def main():
    money_earned = 0
    user_input = input("What would you like (espresso/latte/cappuccino)? ")
    while user_input != "off":
        if user_input == "report":
            resources.update({"Money": money_earned})
            report()
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            check_response = check_resources(user_input)
            if check_response == "Good":
                money = get_change()
                if money >= MENU[user_input]["cost"]:
                    money_back = money - MENU[user_input]["cost"]
                    coffee_machine(user_input)
                    money_earned += MENU[user_input]["cost"]
                    print(f"You got ${money_back:.2f} in change back!")
                else:
                    print(f"Sorry, that is not enough money. It cost ${MENU[user_input].get('cost')}")
            else:
                print(check_response)
        else:
            print("\nThat is not on our menu, sorry.")
        user_input = input("\nWhat would you like (espresso/latte/cappuccino)? ")


if __name__ == '__main__':
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    main()
