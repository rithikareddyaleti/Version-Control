##########Black Jack Game##########
#The Deck is unlimited in size. There are no jokers. The Jack/Queen/King all count as 10. The Ace can count as 11 or 1.
#The cards in the list have equal probability of being drawn. The cards are not removed from the deck as they are drawn.
#Use the following list as the deck of cards:
##cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
# from an import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """Returns a random card from the deck."""
  return random.choice(cards)
#Create a function called calculate_score() that takes a List of cards as input and returns the score.
#look up the sum() function to help you do this.
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    #Black Jack! (a hand with only 2 cards: ace + 10)
    if len(cards) == 2 and 11 in cards and 10 in cards:
        return 0

    score = sum(cards)
    #change the 11 (ace) to 1 if the score is over 21
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score
#inside the while loop, ask the user if they want to draw another card. If they answer yes, then use the deal_card() function to add another card to their hand. If they answer no, then the game should end.
def compare(user_score, computer_score):
    """Compares the scores of the user and the computer and returns the result of the game."""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose💔 "
    if user_score == computer_score:
        return "Draw 🙆🏼‍♀️"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack🤡 "
    elif user_score == 0:
        return "Win with a Blackjack 😈"
    elif user_score > 21:
        return "You went over. You lose💔 "
    elif computer_score > 21:
        return "Opponent went over. You win💰 "
    elif user_score > computer_score:
        return "You win💰 "
    else:
        return "You lose💔 "
def play_game():
    """run one complete game of blackjack"""
    # print(logo)
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 :
            is_game_over = True
        if user_score > 21:    
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
#computer starts playing after the user is done. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

        #main_program
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print()
    play_game() 
    print()
        #deal the user and computer 2 cards each using deal_card()
        # call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        # if the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user's hand. If no, then the game has ended.
        # the score will need to be rechecked with every new card drawn and the checks in step 3 need to be repeated until the game ends.
        # once the user is done, it's time for the computer to play. The computer should keep drawing cards as long as it has a score less than 17.
        # Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

