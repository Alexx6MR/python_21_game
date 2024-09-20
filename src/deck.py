import random

class Deck:
    def __init__(self) -> None:
      
    
        self.cardsSuit: dict = {
            "Hearts": "Hearts",
            "Diamonds": "Diamonds",
            "Clubs": "Clubs",
            "Spades": "Spades",
        }

        self.deckOfCard = [
            dict(number=1, suit=self.cardsSuit["Hearts"], value=1),
        dict(number=2, suit=self.cardsSuit["Hearts"], value=2),
        dict(number=3, suit=self.cardsSuit["Hearts"], value=3),
        dict(number=4, suit=self.cardsSuit["Hearts"], value=4),
        dict(number=5, suit=self.cardsSuit["Hearts"], value=5),
        dict(number=6, suit=self.cardsSuit["Hearts"], value=6),
        dict(number=7, suit=self.cardsSuit["Hearts"], value=7),
        dict(number=8, suit=self.cardsSuit["Hearts"], value=8),
        dict(number=9, suit=self.cardsSuit["Hearts"], value=9),
        dict(number=10, suit=self.cardsSuit["Hearts"], value=10),
        dict(number=11, suit=self.cardsSuit["Hearts"], value=11),
        dict(number=12, suit=self.cardsSuit["Hearts"], value=12),
        dict(number=13, suit=self.cardsSuit["Hearts"], value=13),
    
        dict(number=1, suit=self.cardsSuit["Diamonds"], value=1),
        dict(number=2, suit=self.cardsSuit["Diamonds"], value=2),
        dict(number=3, suit=self.cardsSuit["Diamonds"], value=3),
        dict(number=4, suit=self.cardsSuit["Diamonds"], value=4),
        dict(number=5, suit=self.cardsSuit["Diamonds"], value=5),
        dict(number=6, suit=self.cardsSuit["Diamonds"], value=6),
        dict(number=7, suit=self.cardsSuit["Diamonds"], value=7),
        dict(number=8, suit=self.cardsSuit["Diamonds"], value=8),
        dict(number=9, suit=self.cardsSuit["Diamonds"], value=9),
        dict(number=10, suit=self.cardsSuit["Diamonds"], value=10),
        dict(number=11, suit=self.cardsSuit["Diamonds"], value=11),
        dict(number=12, suit=self.cardsSuit["Diamonds"], value=12),
        dict(number=13, suit=self.cardsSuit["Diamonds"], value=13),
    
        dict(number=1, suit=self.cardsSuit["Clubs"], value=1),
        dict(number=2, suit=self.cardsSuit["Clubs"], value=2),
        dict(number=3, suit=self.cardsSuit["Clubs"], value=3),
        dict(number=4, suit=self.cardsSuit["Clubs"], value=4),
        dict(number=5, suit=self.cardsSuit["Clubs"], value=5),
        dict(number=6, suit=self.cardsSuit["Clubs"], value=6),
        dict(number=7, suit=self.cardsSuit["Clubs"], value=7),
        dict(number=8, suit=self.cardsSuit["Clubs"], value=8),
        dict(number=9, suit=self.cardsSuit["Clubs"], value=9),
        dict(number=10, suit=self.cardsSuit["Clubs"], value=10),
        dict(number=11, suit=self.cardsSuit["Clubs"], value=11),
        dict(number=12, suit=self.cardsSuit["Clubs"], value=12),
        dict(number=13, suit=self.cardsSuit["Clubs"], value=13),
    
        dict(number=1, suit=self.cardsSuit["Spades"], value=1),
        dict(number=2, suit=self.cardsSuit["Spades"], value=2),
        dict(number=3, suit=self.cardsSuit["Spades"], value=3),
        dict(number=4, suit=self.cardsSuit["Spades"], value=4),
        dict(number=5, suit=self.cardsSuit["Spades"], value=5),
        dict(number=6, suit=self.cardsSuit["Spades"], value=6),
        dict(number=7, suit=self.cardsSuit["Spades"], value=7),
        dict(number=8, suit=self.cardsSuit["Spades"], value=8),
        dict(number=9, suit=self.cardsSuit["Spades"], value=9),
        dict(number=10, suit=self.cardsSuit["Spades"], value=10),
        dict(number=11, suit=self.cardsSuit["Spades"], value=11),
        dict(number=12, suit=self.cardsSuit["Spades"], value=12),
        dict(number=13, suit=self.cardsSuit["Spades"], value=13),
    ]


    def RemoveCard(self, currentDeck, number, suit):
        card_to_remove = None
        for card in currentDeck:
            if card.number == number and card.suit == suit:
                card_to_remove = card
                break
            if card_to_remove:
                currentDeck.remove(card_to_remove)
                print(f"The card '{card_to_remove}' has been removed from the deck.")
            else:
                print(f"The card '{number} of {suit}' is not in the deck.")


    def ShuffleTheDecks(self)-> None:
        random.shuffle(self.deckOfCard)
        print("The deck has been shuffled.")
