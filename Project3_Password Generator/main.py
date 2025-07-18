import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

print("Password configuration:-")
print(nr_letters, "letter(s)")
print(nr_symbols, "symbol(s)")
print(nr_numbers, "number(s)")

#Easy level - Password in a sequence
"""password = ""

for i in range(1, nr_letters + 1):
    random_letters = random.choice(letters)
    password += random_letters

for i in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    password += random_symbols

for i in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password += random_numbers

print(password)"""

#Hard level
password_list = []

for i in range(0, nr_letters):
    random_letters = random.choice(letters)
    password_list.append(random_letters)

for i in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    password_list.append(random_symbols)

for i in range(0, nr_numbers):
    random_numbers = random.choice(numbers)
    password_list.append(random_numbers)

#print(password_list)
random.shuffle(password_list)
#print(password_list)

password = ("")
for item in password_list:
    password += item
print("Your Password:", password)
