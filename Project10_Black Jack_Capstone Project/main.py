import random

"""Goal of this game is to add up the cards in your hand without going over 21.
You lose/bust immediately if gone over 21.
Card Traits:- Cards 2- 10 -> Face values
              Cards J, Q, K -> 10
              Special Card A -> It can be 1 or 11 depending on its proximity to 21
Rules: The dealer shows his first card and conceals his second card.
       The user has 2 cards and should be able to guess whether deal could win / lose the game with the hidden second card.
       Depending on the guess, user can then ask for a 3rd card from dealer which should add up to not more than 21. If it's above 21, user lose.
       If we tell the dealer, we don't need any more cards, dealer reveals his second card. Then both user and dealer compares their cards to find who have
       the cards whose sum is near to 21. If both dealer and user has same score, the game leads to a draw. In case, dealer is having Ace as the second card
       and 10 as the first card, they can consider Ace as 11 and the sum becomes 21. Here, we lose.
       In addition, if dealer ends with a hand(sum of 2 cards) less than 17, dealer should take a 3rd card."""


# TODO: Create a deal_cards function to return a random card from a list of cards
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# TODO: Create a calculate_score function to calculate the sum of cards
def calculate_score(hand):
    """Takes a list as input and returns the calculated score"""
    if sum(hand) == 21 and len(hand) == 2:  # To check if there's a black jack.(10 + 11(ace) -> Black jack)
        return 0
    if 11 in hand and sum(hand) > 21:  # Changing an Ace to value 1 as the sum exceeds 21
        hand.remove(11)
        hand.append(1)

    return sum(hand)  # Built-in function that gives the sum of an iterable


# TODO: Create a compare_score function to compare both user and computer scores
def compare_score(player_score, dealer_score):
    """This function compares the score of both user and computer and returns the result of the game"""
    if player_score == dealer_score:
        return "It's a draw"
    elif player_score == 0:
        return "Player Wins with a black jack"
    elif dealer_score == 0:
        return "Player lost as dealer has black jack"
    elif player_score > 21:
        return "Player went over. Dealer wins"
    elif dealer_score > 21:
        return "Dealer went over. Player wins"
    elif player_score > dealer_score:
        return "Player wins"
    else:
        return "Dealer wins"


# TODO: Create a function to play black jack
def play_blackjack():
    """This function allows the user to keep on playing black jack until he wishes to quit"""
    user_hand = []
    com_hand = []
    is_game_over = False
    user_score = -1  # Default value
    com_score = -1  # Default value
    for _ in range(2):  # _ used to denote a specific variable. We just need to iterate twice here.
        user_hand.append(deal_card())
        com_hand.append(deal_card())

    while not is_game_over:  # Same process repeats till game is over
        user_score = calculate_score(user_hand)
        com_score = calculate_score(com_hand)
        print(f"User's hand: {user_hand}, User's score: {user_score}")
        print(f"Computer's hand: {com_hand[0]}")

        if user_score == 0 or com_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal_again = input("\nType 'y' to get another card, type 'n' to pass: ")
            if user_deal_again == 'y':
                user_hand.append(deal_card())
            else:
                is_game_over = True

    while com_score != 0 and com_score < 17:
        com_hand.append(deal_card())
        com_score = calculate_score(com_hand)

    print(f"\nUser final hand: {user_hand}, User final score: {user_score}")
    print(f"Computer final hand: {com_hand}, Computer final score: {com_score}")
    print(compare_score(user_score, com_score))

while input("\nDo you want to play a game of blackjack, type 'y' / 'n'").lower() == "y":
    print("\n" * 20)  # Clears the terminal
    play_blackjack()

# If user enter n or any other letter at the beginning itself, program quits there.
