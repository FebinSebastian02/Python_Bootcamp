from prettytable import PrettyTable

table = PrettyTable()

table.border = True
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"  # Left alignment

print(table)
