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


def divisor():
    print('=' * 20)


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
    index = 0
    items_list = list(coin_type.items())
    while index < len(coin_type):
        key, value = items_list[index]
        try:
            total += int(input(f"How many {key} do you have? $")) * value
            index += 1
        except ValueError as e:
            print(f'Please insert only coins - {e}')
    return round(total, 2)


def check_transaction(cost, drink):
    """
    This function
    :param drink:
    :param cost:
    :type cost: object
    """
    print("Coffee machine resources level")
    divisor()
    report()
    divisor()
    cost_of_drink = drink['cost']
    if cost >= cost_of_drink:
        change = cost - cost_of_drink
        print(f"Cooffii Receipt - Customer Copy\nYou have ${cost} USD\nDrink cost: ${cost_of_drink} USD\nHere is your change of ${change} dollars")
        global revenue
        revenue += cost_of_drink
        return True

    else:
        print(f"Sorry that's not enough money. Money refunded. You need ${cost_of_drink} to get this coffee")
        return False


def make_coffee(order, type_of_coffee):
    for item in order['ingredients']:
        machine_resources[item] -= order['ingredients'][item]
    print(f'Here is your {type_of_coffee}')
    divisor()


def report(show_profit=0):
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    if show_profit == 1:
        print(f"Money: ${revenue}")


while True:
    coffee = ['espresso', 'latte', 'cappuccino']
    choice = int(input(menu_instruction))
    if 0 <= choice <= len(coffee):
        drink = MENU[coffee[choice - 1]]  # (-1) is used based on the menu list
        # Check is resource is enough
        if is_resources_enough(drink['ingredients']):
            price = process_coin()
            divisor()
            if check_transaction(price, drink):
                make_coffee(drink, coffee[choice-1])
                turn_off = input('Enter 0 to turn off the machine\nEnter to Continue')
                if turn_off == '0':
                    break

    elif choice == 4:
        print('-' * 20)
        report(1)
        divisor()
        turn_off = input('Enter 0 to turn off the machine\nEnter to Continue')
        if turn_off == '0':
            break
    elif choice == 0:
        break
    else:
        print('Wrong button')
