def check_card_already_drawn(cards_drawn, card):
    for drawn in cards_drawn:
        if drawn.suit == card.suit and drawn.rank == card.rank:
            print("The " + card.rank + " of " + card.suit + " has already been drawn.")
            return True
    return False