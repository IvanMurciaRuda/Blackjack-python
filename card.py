import random

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

class Card:
    def __init__(self):
        self.suit = random.choice(suits)
        self.rank = random.choice(ranks)

        if self.rank in "JKQ":
            self.value = 10
        elif self.rank == "A":
            self.value = 11
        else:
            self.value = int(self.rank)
