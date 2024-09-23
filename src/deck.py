import random


class Deck:
   
    def __init__(self) -> None:    
        
        
        #* This is the template of the deck
        self.__sampleDeckOfCard: list[dict] = [
            dict(number="1", suit="Hearts", value=1),
            dict(number="2", suit="Hearts", value=2),
            dict(number="3", suit="Hearts", value=3),
            dict(number="4", suit="Hearts", value=4),
            dict(number="5", suit="Hearts", value=5),
            dict(number="6", suit="Hearts", value=6),
            dict(number="7", suit="Hearts", value=7),
            dict(number="8", suit="Hearts", value=8),
            dict(number="9", suit="Hearts", value=9),
            dict(number="10", suit="Hearts", value=10),
            dict(number="11", suit="Hearts", value=11),
            dict(number="12", suit="Hearts", value=12),
            dict(number="13", suit="Hearts", value=13),
    
            dict(number="1", suit="Diamonds", value=1),
            dict(number="2", suit="Diamonds", value=2),
            dict(number="3", suit="Diamonds", value=3),
            dict(number="4", suit="Diamonds", value=4),
            dict(number="5", suit="Diamonds", value=5),
            dict(number="6", suit="Diamonds", value=6),
            dict(number="7", suit="Diamonds", value=7),
            dict(number="8", suit="Diamonds", value=8),
            dict(number="9", suit="Diamonds", value=9),
            dict(number="10", suit="Diamonds", value=10),
            dict(number="11", suit="Diamonds", value=11),
            dict(number="12", suit="Diamonds", value=12),
            dict(number="13", suit="Diamonds", value=13),
    
            dict(number="1", suit="Clubs", value=1),
            dict(number="2", suit="Clubs", value=2),
            dict(number="3", suit="Clubs", value=3),
            dict(number="4", suit="Clubs", value=4),
            dict(number="5", suit="Clubs", value=5),
            dict(number="6", suit="Clubs", value=6),
            dict(number="7", suit="Clubs", value=7),
            dict(number="8", suit="Clubs", value=8),
            dict(number="9", suit="Clubs", value=9),
            dict(number="10", suit="Clubs", value=10),
            dict(number="11", suit="Clubs", value=11),
            dict(number="12", suit="Clubs", value=12),
            dict(number="13", suit="Clubs", value=13),
    
            dict(number="1", suit="Spades", value=1),
            dict(number="2", suit="Spades", value=2),
            dict(number="3", suit="Spades", value=3),
            dict(number="4", suit="Spades", value=4),
            dict(number="5", suit="Spades", value=5),
            dict(number="6", suit="Spades", value=6),
            dict(number="7", suit="Spades", value=7),
            dict(number="8", suit="Spades", value=8),
            dict(number="9", suit="Spades", value=9),
            dict(number="10", suit="Spades", value=10),
            dict(number="11", suit="Spades", value=11),
            dict(number="12", suit="Spades", value=12),
            dict(number="13", suit="Spades", value=13),
        ]
        
        #* This makes that every time the deck is used, the cards are randomly shuffled.
        self.deckOfCard: list[dict] = random.sample(self.__sampleDeckOfCard, len(self.__sampleDeckOfCard))
        
    
    #* Getters
        
    #* function to get a card from the deck
    def get_OneCard(self)-> dict:
        return self.deckOfCard.pop()
    
    
    