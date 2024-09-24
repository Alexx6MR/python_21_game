import random


class Card:
    def __init__(self, name:str, suit:str, value:int) -> None:
        self.name: str = name
        self.suit: str = suit
        self.value: int = value

class Deck:
    def __init__(self) -> None:    
        #* This is the template of the deck
        self.__sampleDeckOfCard: list[Card] = [
            Card("Ace", "Hearts", 1),
            Card("2", "Hearts", 2),
            Card("3", "Hearts", 3),
            Card("4", "Hearts", 4),
            Card("5", "Hearts", 5),
            Card("6", "Hearts", 6),
            Card("7", "Hearts", 7),
            Card("8", "Hearts", 8),
            Card("9", "Hearts", 9),
            Card("10", "Hearts", 10),
            Card("Jack", "Hearts", 11),
            Card("Queen", "Hearts", 12),
            Card("King", "Hearts", 13),
            
            Card("Ace", "Diamonds", 1),
            Card("2", "Diamonds", 2),
            Card("3", "Diamonds", 3),
            Card("4", "Diamonds", 4),
            Card("5", "Diamonds", 5),
            Card("6", "Diamonds", 6),
            Card("7", "Diamonds", 7),
            Card("8", "Diamonds", 8),
            Card("9", "Diamonds", 9),
            Card("10", "Diamonds", 10),
            Card("Jack", "Diamonds", 11),
            Card("Queen", "Diamonds", 12),
            Card("King", "Diamonds", 13),
           
            Card("Ace", "Clubs", 1),
            Card("2", "Clubs", 2),
            Card("3", "Clubs", 3),
            Card("4", "Clubs", 4),
            Card("5", "Clubs", 5),
            Card("6", "Clubs", 6),
            Card("7", "Clubs", 7),
            Card("8", "Clubs", 8),
            Card("9", "Clubs", 9),
            Card("10", "Clubs", 10),
            Card("Jack", "Clubs", 11),
            Card("Queen", "Clubs", 12),
            Card("King", "Clubs", 13),
            
            Card("Ace", "Spades", 1),
            Card("2", "Spades", 2),
            Card("3", "Spades", 3),
            Card("4", "Spades", 4),
            Card("5", "Spades", 5),
            Card("6", "Spades", 6),
            Card("7", "Spades", 7),
            Card("8", "Spades", 8),
            Card("9", "Spades", 9),
            Card("10", "Spades", 10),
            Card("Jack", "Spades", 11),
            Card("Queen", "Spades", 12),
            Card("King", "Spades", 13),
        ]
        
        #* This makes that every time the deck is used, the cards are randomly shuffled.
        self.deckOfCard: list[Card] = random.sample(self.__sampleDeckOfCard, len(self.__sampleDeckOfCard))
        
    
    #* Getters
        
    #* function to get a card from the deck
    def get_OneCard(self)-> Card:
        return self.deckOfCard.pop()
    
    
    