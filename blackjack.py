from random import randrange


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit


class Deck:
    suits = ["diamonds", "heart", "spades", "clubs"]
    max_number = 13

    def __int__(self):
        self.cards = []

        for suit in self.suits:
            for number in range(1, self.max_number):
                self.cards.append(Card(number, suit))

    def give_random_card(self):
        return self.cards.pop(randrange(len(self.cards)))


class Player:
    def __int__(self, name, points):
        self.name = name
        self.points = points


class BlackjackGame:
    def __int__(self, player, deck):
        self.player = player
        self.deck = deck