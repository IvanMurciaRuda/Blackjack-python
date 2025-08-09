from functions import players_turn, dealer_turn

print("Welcome to the Blackjack!")

while 1:
    #reset the gamestate
    drawn_cards = []
    #player's and dealer's turn
    player_score = players_turn(drawn_cards)

    if player_score == 21:
        print("You won!")
    elif player_score > 21:
        print("You busted!")
    else:
        dealers_score = dealer_turn(drawn_cards)
        print("\n\n\nYour score is: " + str(player_score))
        print("Dealer's score: ", str(dealers_score) + "\n")

        if player_score < 21 < dealers_score:
            print("You won!")
        elif player_score > 21 > dealers_score:
            print("You lost!")
        elif player_score > dealers_score:
            print("You won!")
        else:
            print("You lost!")

    play_again = input("\n\n\nWould you like to play again? (n to exit the game): ")
    if play_again == "n":
        break