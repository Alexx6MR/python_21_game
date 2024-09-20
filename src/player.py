from src.gameUI import GameUI
from src.game import GameSetup

class player:
    def __init__(self, actualDeck) -> None:
        isPlayerTurn: bool = True
        self.actualDeck = actualDeck
    
    def PlayerTurn(self, playerCards:list[any], pcCards:list[any], deck: list[any]):
        currentPlayerCards: list[deck] = playerCards
        
    
        
        def oneMoreCard(self):
            currentPlayerCards.append(self.actualDeck.pop())
    
        def NoMoreCard(self):
            self.isPlayerTurn = False
        
    
        while True:
    
            value = GameSetup.CheckHandTotalValue(currentPlayerCards)
    
            if(value > 21):
                GameUI.EndMessageOfTheGame(
                    message="The game is over, your total value is too hight", 
                    currentPlayerCards=currentPlayerCards, 
                    pcCards=pcCards
            )
        
            elif value == 21:
                GameUI.EndMessageOfTheGame(
                    message="Congratulacion you wont this match", 
                    currentPlayerCards=currentPlayerCards, 
                    pcCards=pcCards
            )
            else:
                GameUI.PrintBoard(currentPlayerCards, pcCards)
         
                GameUI.MenuUI(userInputText= "Select a number: ", 
                options=[
                    GameUI.OptionMenu(title="One more card", action=oneMoreCard),
                    GameUI.OptionMenu(title="No more card", action=NoMoreCard),
                ])
             
