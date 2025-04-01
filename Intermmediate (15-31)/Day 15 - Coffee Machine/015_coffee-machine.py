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
    "money": 0
}

def choose_coffee():
    while True:
        try:
            user_choice = input("What would you like? (espresso/latte/cappuccino)? ").strip().lower()
            if user_choice not in ["espresso", "latte", "cappuccino", "report", "off"]:
                raise ValueError("Invalid coffee choice.")
            return user_choice
        except ValueError as invalid_coffee:
            print(invalid_coffee, "Please try again.\n")

def report(machine_resources):
    print("="*50)
    print("Pinaki - Report")
    print("="*50)
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${machine_resources['money']}")
    print("=" * 50)

def check_resources(coffee_choice, machine_resources, mode, payment=None):

    global MENU
    ingredients = MENU[coffee_choice]['ingredients']
    cost = MENU[coffee_choice]['cost']
    enough_resources = True

    water = ingredients['water']
    milk = ingredients.get('milk')
    coffee = ingredients['coffee']


    available_water = machine_resources['water']
    available_milk = machine_resources['milk']
    available_coffee = machine_resources['coffee']

    if mode == "resources":
        if available_water < water:
            print("-" * 50)
            print("Sorry there is not enough water.")
            print("-" * 50)
            enough_resources = False
        if milk is not None and available_milk < milk:
            print("-" * 50)
            print("Sorry there is not enough milk.")
            print("-" * 50)
            enough_resources = False
        if available_coffee < coffee:
            print("-" * 50)
            print("Sorry there is not enough coffee.")
            print("_" * 50)
            enough_resources = False

    if mode == "cost":
        if payment < cost:
            print("-" * 50)
            print("That is not enough money.")
            print(f"${payment:.2f} was refunded.")
            print("_" * 50)
            enough_resources = False
        elif payment > cost:
            change = payment - cost
            print(f"Here is ${change:.2f} dollars in change")
    return enough_resources
def make_coffee(coffee_choice, machine_resources):
    ingredients = MENU[coffee_choice]['ingredients']

    profit = MENU[coffee_choice]['cost']
    water = ingredients['water']
    milk = ingredients.get('milk')
    coffee = ingredients['coffee']

    available_water = machine_resources['water']
    available_milk = machine_resources['milk']
    available_coffee = machine_resources['coffee']
    current_money = machine_resources['money']

    available_water = max(0, available_water - water)
    if milk is not None:
        available_milk = max(0, available_milk - milk)
    available_coffee = max(0, available_coffee - coffee)
    current_money += profit

    machine_resources['water'] = available_water
    machine_resources['milk'] = available_milk
    machine_resources['coffee'] = available_coffee
    machine_resources['money'] = current_money

    print()
    print(f"Here is your {coffee_choice}! Thanks for coming!")
    print()

    return machine_resources


print("=" * 50)
print("Welcome to the Pinaki: The Coffee Machine!")
print("=" * 50)
while True:
    choice = choose_coffee()
    if choice == "off":
        break
    elif choice == "report":
        report(resources)
    else:
        resource_check = check_resources(choice, resources, "resources")
        if not resource_check:
            continue
        print()
        print("Insert the coins:\n")
        try:
            n1 = int(input("Quarter(s): ")) / 4
        except ValueError:
            n1 = 0
        try:
            n2 = int(input("Dime(s): ")) / 10
        except ValueError:
            n2 = 0
        try:
            n3 = int(input("Nickle(s): ")) / 20
        except ValueError:
            n3 = 0
        try:
            n4 = int(input("Pennie(s): ")) / 100
        except ValueError:
            n4 = 0
        total_pay = n1+n2+n3+n4
        print(f"\nTotal Coins: {total_pay:.2f}")
        money_check = check_resources(choice, resources, "cost", total_pay)
        if not money_check:
            continue
        resources = make_coffee(choice, resources)







