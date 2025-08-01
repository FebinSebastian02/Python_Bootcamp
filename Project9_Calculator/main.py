# TODO: Define functions for all mathematical operations
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

# TODO: Create a dictionary for the operations symbols
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    num1 = float(input("Enter the first number..."))
    should_continue = True
    while should_continue:
        for ops in operations:
            print(ops)
        operand = input("Pick an operation")

        num2 = float(input("Enter the second number..."))

        result = operations[operand](n1=num1, n2=num2)    # Accessing the key with the parameters call the respective function
        print(f"{num1} {operand} {num2} = {result}")

        choice = input(f"Enter 'y' to continue with {result}, or enter 'n' to start with a new number")
        if choice == "y":
            num1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()    # Recursion -> Function calling itself

calculator()

"""should_continue = True

first_number = int(input("Enter the first number..."))

# TODO: Define all mathematical operations
def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

result = 0

while should_continue:
    op = input("\n+\n-\n*\n/\nPick an operation")
    second_number = int(input("\nEnter the second number..."))

    match op:
        case "+":
            result = add(first_number, second_number)
            print(f"{first_number} + {second_number} = {result}")
        case "-":
            result = subtract(first_number, second_number)
            print(f"{first_number} - {second_number} = {result}")
        case "*":
            result = multiply(first_number, second_number)
            print(f"{first_number} * {second_number} = {result}")
        case "/":
            result = divide(first_number, second_number)
            print(f"{first_number} / {second_number} = {result}")

    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation")
    if choice == "y":
        first_number = result
    if choice == "n":
        first_number = int(input("Enter the first number..."))"""