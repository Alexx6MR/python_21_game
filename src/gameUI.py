import pyinputplus as pyip
from src.deck import Card

class GameUI:
    def __init__(self) -> None:
        pass
    

    #* This is the Menu that let the users take a decision.
    def MenuUI(self, menuOptions:list[dict]=[], userInputText: str = "")->None:
        optionLength:int = len(menuOptions)
    
        print()
        print("_______Menu_____")
        print()
    
        #* Loop to print all the title from the option dictionary in order
        for item in range(optionLength):
            option:dict = menuOptions[item]
            print(f"{item + 1}. {option["title"]}")


        #* Input to choose a option Obs: I use pyinputplus for validation
        print("_________________")
        userInput:int = pyip.inputNum(userInputText, max=optionLength, min=1)    
        
        
        #* Loop to print and run the action in the selected object
        for item in range(optionLength):
            option:dict = menuOptions[item]
            if(userInput == item + 1):
                #* this is to run the option function
                option["action"]()

    
    #* This function will print the cards and total value of the players/Pc hands
    def ShowCurrentHandAndTotalValue(self, currentHand:list[Card]):
        currentTotalCards:int = len(currentHand)
        currentTotalCardsValue:int = 0
        
        #* loop to show current cards in order
        for cardIndex in range(currentTotalCards):
            card:Card = currentHand[cardIndex]
            print(f"{cardIndex + 1}. {card.name} {card.suit}")

        #* loop to add every card value and show the total value
        for card in currentHand:
            currentTotalCardsValue += card.value
        
        print(f"Total Value: {currentTotalCardsValue}")
    
    
    #* Show a Message when someone Win and give some options
    def EndMessage(self, currentPlayerHand:list[Card], currentPcHand:list[Card], message:str, menuOptions: list[dict])-> None:
        print()
        print("PC Total hand:")
        self.ShowCurrentHandAndTotalValue(currentPcHand)
        print()
        print("Player Total hand:")
        self.ShowCurrentHandAndTotalValue(currentPlayerHand)
        print()
        print("*******************************************************")
        print(f"{message}")
        print("*******************************************************")
        self.MenuUI(userInputText= "What do you want to do: ", 
        menuOptions=menuOptions)

    #* To print the board
    def PrintBoard(self, currentPlayerHand:list[Card], currentPcHand:list[Card])-> None:
        print("--------------")
        print("")
        print("PC Hand: ")
        self.ShowCurrentHandAndTotalValue(currentPcHand)
        print("")
        print("------vs------")
        print("")
        print("Player Hand: ")
        self.ShowCurrentHandAndTotalValue(currentPlayerHand)
