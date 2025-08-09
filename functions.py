from card import Card

def check_card_already_drawn(cards_drawn, card):
    for drawn in cards_drawn:
        if drawn.suit == card.suit and drawn.rank == card.rank:
            print("The " + card.rank + " of " + card.suit + " has already been drawn.")
            return True
    return False

def players_turn(drawn_cards):
    score = 0
    while score < 21:
        choice = ""
        while choice != "h" and choice != "s":
            choice = input("\nHit (h)\nStand (s)\nYour choice: ")

        if choice == "s":
            print("You stood with " + str(score) + " points")
            return score
        else:
            card = Card()
            while check_card_already_drawn(drawn_cards, card):
                card = Card()

        print("\nYou drew a " + card.rank + " of " + card.suit + "!")
        drawn_cards.append(card)
        score = calculate_score(drawn_cards)
        print("Your current score is: " + str(score))

    print("\nYou busted!")
    return score

def calculate_score(drawn_cards):
    score = 0
    aces = 0
    for card in drawn_cards:
        if card.rank == "A":
            aces += 1
            continue
        else:
            score += card.value

    for i in range (aces):
        if(score + 11) > 21:
            score +=1
        else:
            score += 11

    return score