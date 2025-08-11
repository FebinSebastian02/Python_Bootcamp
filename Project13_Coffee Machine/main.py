from menu import menu

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

coffee_machine_on = True

# TODO: Create a function to return current resource values
def generate_resources():
    """Generates current value of resources present in the coffee machine"""
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: $ {profit}")

def check_resources(ordered_ingredients):
    """Returns True if there are sufficient resources and False vice-versa"""
    for item in ordered_ingredients:
        if ordered_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins...")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    global profit
    """Returns True if the transaction is successful, else False"""
    if money_received >= drink_cost:
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, ordered_ingredients):
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy")

while coffee_machine_on:
    # TODO: Take choice from user and store it in a variable
    choice = input("What would you like to have? (Espresso, Latte, Cappuccino)").lower()

    # TODO: Turn off coffee machine by entering off to the prompt
    if choice == "off":
        coffee_machine_on = False

    # TODO: When user enters report, a report should be generated with current resource values
    elif choice == "report":
        generate_resources()

    # TODO: Check whether there are enough resources
    else:
        drink_selected = menu[choice]
        if check_resources(drink_selected["ingredients"]):
            #   TODO: Calling the function to process coins
            payment = process_coins()
            # TODO: Calling the function to see if the transaction is successful or not
            if is_transaction_successful(payment, drink_selected["cost"]):
                make_coffee(choice, drink_selected["ingredients"])

