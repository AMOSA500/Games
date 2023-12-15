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

menu_instruction = """
Welcome to Cooffii Shop - Table Menu?
1. Espresso
2. Latte
3. Cappuccino
4. Check resources report
0. Turn off the machine\n
"""

revenue = 0
machine_resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}


# check resources
def is_resources_enough(drink_resources):
    for item in drink_resources:
        if drink_resources[item] > machine_resources[item]:
            print(f'The machine is low on {item}')
            return False
    return True


def process_coin():
    coin_type = {'quarter': 0.25, 'dime': 0.1, 'nickle': 0.05, 'pennie': 0.01}
    total = 0
    coin = 0
    for index, (key,value) in enumerate(coin_type.items()):
        try:
            total += int(input(f"How many {key} do you have?"))*value
        except ValueError as e:
            print(f'Please insert only coins - {e}')
    return total


start_machine = True

while start_machine:
    coffee = ['espresso', 'latte', 'cappuccino']
    choice = int(input(menu_instruction))
    if 0 <= choice <= len(coffee):
        drink = MENU[coffee[choice - 1]]
        # Check is resource is enough
        if is_resources_enough(drink['ingredients']):
            print(process_coin())

    elif choice == 4:
        print('-' * 20)
        print(f"Water: {machine_resources['water']}ml")
        print(f"Milk: {machine_resources['milk']}ml")
        print(f"Coffee: {machine_resources['coffee']}g")
        print(f"Money: ${revenue}")
        print('=' * 20)
    elif choice == 0:
        start_machine = False
    else:
        print('Wrong button')
