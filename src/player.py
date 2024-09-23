import pyinputplus as pyip
from src.deck import Card
class Player:
    
    def __init__(self) -> None:
        self.__currentHandCards: list[Card] = []
  
    #* This function is for let the user select the value of ACe
    def SelectAceValue(self, card:Card):
        if card.number != "Ace": 
            return card
        
        print()
        print("You got a ACE but this has two different value 1 and 14, Wich want do you want to use")    
        print()
        print("_______Menu_____")
        print()
        print("1. ACE as 1 ")
        print("2. ACE as 14 ")
        print("_________________")
        userInput:int = pyip.inputNum("Please Select a number: ", max=2, min=1)    
        
        if(userInput == 1):
            return Card(number="Ace", suit=card.suit, value=1)
        else:
             return Card(number="Ace", suit=card.suit, value=14)
 
    
    #** Setters 
        
    #* add a new card into the players current hand       
    def set_NewCard (self, newCard:Card) ->None:
            checkCard: Card = self.SelectAceValue(newCard)
            self.__currentHandCards.append(checkCard)

    #* add the inicial cards into the player hand 
    def set_InitialHand(self, card1:Card) -> None:
        self.__currentHandCards = [self.SelectAceValue(card1)]
        
    
    #** Getters
        
    #* Get the user Current hand
    def get_CurrentHand(self) -> list[Card]:
        return self.__currentHandCards
    