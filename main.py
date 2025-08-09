import functions

from card import Card
from functions import check_card_already_drawn

drawn_cards = []

for i in range (10):
    card = Card()

    while check_card_already_drawn(drawn_cards, card):
        card = Card()

    drawn_cards.append(card)



print("\n\nFinal 10 drawn cards")

for card in drawn_cards:
    print(card.rank + " of " + card.suit )