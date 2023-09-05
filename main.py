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

machineIsOn = True

# TODO
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while machineIsOn:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        machineIsOn = False
# 3. Print report.
    elif choice == "report":
        print(resources)
        continue
# 4. Check resources sufficient?
    elif choice == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            print("Please insert coins.")
    elif choice == "latte":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            print("Please insert coins.")
    elif choice == "cappuccino":
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            print("Please insert coins.")
    else:
        print("Sorry that's not available.")
# 5. Process coins.
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(total)
# 6. Check transaction successful?
    if total >= MENU[choice]["cost"]:
        print("Here is your " + choice + " ☕️ Enjoy!")
# 7. Make Coffee.
        if choice == "espresso":
            resources["water"] -= 50
            resources["coffee"] -= 18
        elif choice == "latte":
            resources["water"] -= 200
            resources["milk"] -= 150
            resources["coffee"] -= 24
        elif choice == "cappuccino":
            resources["water"] -= 250
            resources["milk"] -= 100
            resources["coffee"] -= 24
        print(resources)
    else:
        print("Sorry that's not enough money. Money refunded.")


