import pyinputplus as pyip

class Player:
    
    def __init__(self, ) -> None:
        self.__currentHandCards: list[dict] = []
  
    #* This function is for let the user select the value of ACe
    def SelectAceValue(self, card):
        if card["number"] != "1": 
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
            return dict(number="1", suit=card["suit"], value=1)
        else:
             return dict(number="1", suit=card["suit"], value=14)
 
    
    #** Setters 
        
    #* add a new card into the players current hand       
    def set_NewCard (self, newCard) ->None:
            checkCard: dict = self.SelectAceValue(newCard)
            self.__currentHandCards.append(checkCard)

    #* add the inicial cards into the player hand 
    def set_InitialHand(self, card1, card2) -> None:
        self.__currentHandCards = [self.SelectAceValue(card1), self.SelectAceValue(card2)]
        
    
    #** Getters
        
    #* Get the user Current hand
    def get_CurrentHand(self) -> list[dict]:
        return self.__currentHandCards
    