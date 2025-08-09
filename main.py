from functions import players_turn

print("Welcome to the Blackjack!")

while 1:
    #reset the gamestate
    drawn_cards = []
    #player's and dealer's turn
    player_score = players_turn(drawn_cards)
    play_again = input("would you like to play again? (y/n): ")
    if play_again == "n":
        break