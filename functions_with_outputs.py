# TODO: Create a function that takes in first name, last name and then make the full name in uniform format
first = "FeBiN"
last = "seBAstIAn"


def format_name(first_name, last_name):
    """This function formats both first and last names that are passed"""  # Doc String(This can be seen while hovered over function call)
    formatted_fname = first_name.title()  # Capitalize first letter in each string and all others are made to small
    formatted_lname = last_name.title()
    return formatted_fname, formatted_lname


first, last = format_name(first_name=first, last_name=last)
print(first, " ", last)

# return -> This empty return exits the function with returning None
