# Local Scope: Any variable declared within a function is only available inside that function
# Global Scope: Any variable declared inside a block like if, else or declared outside a function is available over the whole program
ball = "stitch"

def cricket():
    bat = "wood"


if 1 < 2:
    wicket = "plastic"

"""print(bat)"""  # Not possible as bat is having a local scope

print(ball)  # Will be printed as it is having a global scope
print(wicket)  # Will be printed as it is having a global scope


# TODO: Create a program for detecting prime numbers
number = int(input("Enter a number"))
def is_prime(num):
    result = True
    if num == 1:
        result = False
        return result
    if num == 2:
        result = True
        return result
    for item in range(2,num):
        if num % item == 0:
            result = False
            return result
    return result

result = is_prime(num=number)
print(result)
