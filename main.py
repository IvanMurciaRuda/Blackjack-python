import functions

from card import Card
from functions import check_card_already_drawn

drawn_cards = []
print("Welcome to the Blackjack!")

while 1:
    #player's and dealer's turn
    play_again = input("would you like to play again? (y/n): ")
    if play_again == "n":
        break