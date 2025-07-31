print("!!!Welcome to the secret auction program!!!")

# TODO: Creating a flag to decide whether the program should re-run or not and an empty dictionary to store bidders name and price
re_run = True
bidders_dictionary = {}

# TODO: Defining a function to decide the highest bidder
def highest_bidder_is(bid_list):
    winner = ""
    highest_bid = 0
    for bidder in bid_list:
        bid_amount = bid_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder.capitalize()
    print(f"The winner is {winner} with the highest bid of €{highest_bid}")

# TODO: Taking inputs from user regarding bidder name and price.
while re_run:
    name = input("Enter your name...").lower()
    bid = int(input("Enter your bid... €"))
    choice = input("Are there any other bidders? Enter yes / no").lower()

    print("\n" * 100)
    bidders_dictionary[name] = bid

    if choice == "no":
        highest_bidder_is(bid_list=bidders_dictionary)
        re_run = False




