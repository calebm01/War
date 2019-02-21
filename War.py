#  Colton Northcutt,  Parker Dean, Matthew Walker, Caleb Mouritsen
# 2-21-19
# War

import Card, games

class Player(Card.Hand):

    def __init__(self, self):
        self.hand = []
        self.name = name

    def __str__(self):
        rep = self.name
        return rep


class War_card(Card.card):

    @property
    def value(self):
        value = Card.RANKS.index(self.rank)
        return value

class War_deck(Card.Deck):
    def populate(self):
        for suit in War_card.SUITS:
            for rank in War_card.RANKS:
                card = War_card(rank,suit,True)
                self.add(card)
        
class War_game(self):

    def __init__(self):
        self.pot = []
        self.deck = War_deck.populate
        self.deck = War_deck.shuffle
        
        player_one =  Player(input("Enter player one's name: "))
        player_two = Player(input("Enter player two's name: "))

        card.Deck.deal(self.hands,  per_hand = 26)


        def  play(self):
            for i in self.players:
                played_card = self.players.hand[0]
                self.players.hand.remove(played_card)
                self.pot.append(played_card)

        def deal(self, hands, per_hand=26):
            for rounds in range(per_hand):
                for hand in hands:
                    if self.cards:
                        top_card = self.cards[0]
                        self.give(top_card, hand)
                    else:
                        print("Can't continue to deal. Out of cards!")










                
