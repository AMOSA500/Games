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
4. Check resources level
0. Turn off the machine\n
"""

revenue = 0
machine_resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}


# check resources
def is_resources_enough():
    pass


start_machine = True

while start_machine:
    coffee = ['espresso', 'latte', 'cappuccino']
    choice = int(input(menu_instruction))
    if 0 <= choice <= len(coffee):
        drink = MENU[coffee[choice]]
        # Check is resource is enough
        print(drink)

    else:
        print('Wrong button')
