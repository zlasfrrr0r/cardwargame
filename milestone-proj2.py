import random
import pdb

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
values = ({"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7,
        "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14})
ranks = tuple(values.keys())

"""    Card Clas    """

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit
    
"""    Deck Class   """

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
        
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop() # Deal the top card not the bottom card
    
    def show_cards(self):
        for card_object in self.all_cards:
            print(card_object)

"""    Player Class    """

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def hand(self):
        for card in self.all_cards:
            print(card)

""""    the game logic here    """

new_deck = Deck()
new_deck.shuffle()
p1 = input("Player 1: ")
p1 = Player(f"{p1}")
p2 = input("Player 2: ")
p2 = Player("{}".format(p2))

for x in range(26):
    p1.add_cards(new_deck.deal_one())
    p2.add_cards(new_deck.deal_one())

def play_game():

    print("\nWelcome to WAR!")   
    round = 0
    game = True

    while game:
        round += 1
        print("\n---Round {}---\n".format(round))
        print("{} has {} cards.".format(p1.name, len(p1.all_cards)))
        print("{} has {} cards.".format(p2.name, len(p2.all_cards)))
        if len(p1.all_cards) == 0:
            print("{} runs out of cards! {} wins the game!".format(p1.name, p2.name))
            game = False
            break
        if len(p2.all_cards) == 0:
            print("{} runs out of cards! {} wins the game!".format(p2.name, p1.name))
            game = False
            break
        p1_card = p1.remove_one()
        p2_card = p2.remove_one()
        print("{} plays {}".format(p1.name, p1_card))
        print("{} plays {}".format(p2.name, p2_card))
        if p1_card.value > p2_card.value:
            p1.add_cards([p1_card, p2_card])
            continue
        elif p1_card.value < p2_card.value:
            p2.add_cards([p1_card, p2_card])
            continue
        else:
            print("\nWAR!\n")
            war = True
            war_stack = [p1_card, p2_card]
            while war:
                if len(p1.all_cards) >= 4 and len(p2.all_cards) >= 4:
                    [war_stack.extend(p1.remove_one() for i in range(3))]
                    [war_stack.extend(p2.remove_one() for i in range(3))]
                    p1_war_card = p1.remove_one()
                    p2_war_card = p2.remove_one()
                    print("{} war card: {}".format(p1.name, p1_war_card))
                    print("{} war card: {}".format(p2.name, p2_war_card))
                    if p1_war_card.value > p2_war_card.value:
                        p1.add_cards(war_stack + [p1_war_card, p2_war_card])
                        print("{} wins the war!".format(p1.name))
                        break
                    elif p1_war_card.value < p2_war_card.value:
                        p2.add_cards(war_stack + [p1_war_card, p2_war_card])
                        print("{} wins the war!".format(p2.name))
                        break
                    else:
                        war_stack.extend([p1_war_card, p2_war_card])
                        print('WAR continues!')
                elif len(p1.all_cards) < 4:
                    print("{} unable to war! {} wins it!".format(p1.name, p2.name))
                    war = False
                    game = False
                elif len(p2.all_cards) < 4:
                    print("{} unable to war! {} wins it!".format(p2.name, p1.name))
                    war = False
                    game = False
                else:
                    print("No one able to war! just carry on i guess..?")
                    war = False
        continue        
    
play_game()