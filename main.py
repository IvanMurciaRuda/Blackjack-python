from card import Card

drawn_cards = []

for i in range (10):
    already_drawn = False

    while already_drawn:
        card = Card()
        for drawn in drawn_cards:
            if (drawn.suit == card.suit) and (card.value == drawn.value):
                already_drawn = True
            else:
                print(card.rank + " of " + card.suit + " added")
                drawn_cards.append(card)
