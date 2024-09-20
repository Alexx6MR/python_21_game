
from src.gameUI import GameUI
# from player import player


class GameSetup:
    def __init__(self) -> None:
        self.isGameRunning: bool = True
        self.currentPcCards: list[any] = []
        self.gameUI = GameUI()

   

    # def ExitGame(self)->None:
    #     self.isGameRunning = False
    #     print("")
    #     print("Thank you for Playing :) ")
    #     print("See you soon!!!!! ")
    #     print("")
    

    # def CheckHandTotalValue(playerHand)->bool:
    #     value = sum(card.value for card in playerHand)

    #     ace_count = sum(1 for card in playerHand if card.number == "Ace")
    
    #     while value > 21 and ace_count > 0:
    #         value -= 10  
    #         ace_count -= 1
    
    #     return value


    # def PrintBoard(playerCards, pcCards)->None:
    
    #     #* Take the length of both list to print the index and the the data
    #     pcCardLength = len(pcCards)
    #     playerCardLength = len(playerCards)
    #     print("")
    #     print("--------------")
    #     print("")
    #     print("PC Hand: ")
    #     for pcCard in range(pcCardLength):
    #         print(f"{pcCard +1}. {pcCards[pcCard].number} {pcCards[pcCard].suit}")
    #     print("")
    #     # print(f"Player total: {CheckHandTotalValue(pcCards)}")
    #     print("")
    #     print("")
    #     print("------vs------")
    #     print("")
    #     print("Player Hand: ")
    #     for playerCard in range(playerCardLength):
    #         print(f"{playerCard +1}. {playerCards[playerCard].number} {playerCards[playerCard].suit}")
    #     print("")
    #     # print(f"Player total: {CheckHandTotalValue(playerCards)}")
    #     print("")



    # def InGame(self)-> None:
    #     self.isGameRunning
    #     self.deck
    #     self.currentPcCards
    #     print("-----------------")
    #     print("")
    #     print("**The Game is On**")
    
    #     #* Preparing inital hand
    #     # ShuffleTheDecks()
    #     initialPlayerCards = [self.deckOfCard.pop(), self.deckOfCard.pop()]
    #     initialPcCards = [self.deckOfCard.pop()]
    #     currentPcCards = initialPcCards
    
    #     while self.isGameRunning:
    #         player.PlayerTurn(initialPlayerCards, initialPcCards)
        
        
    #         while True:
    #             value = self.CheckHandTotalValue(currentPcCards)
    
    #             if(value > 21):
    #                 GameUI.EndMessageOfTheGame(
    #                 message="Congratulations you have won the game, the pc's total value is too hight.", 
    #                 currentPlayerCards=self.currentPlayerCards, 
    #                 pcCards=currentPcCards
    #                 )
    
    #             elif value == 21:
    #                 GameUI.EndMessageOfTheGame(
    #                 message="Sorry, the PC was very lucky and won this match.", 
    #                 currentPlayerCards=self.currentPlayerCards, 
    #                 pcCards=currentPcCards
    #                 )
         
    def PrintRules(self, action)-> None:
        print("")
        print("**Welcome to the Rules pages**")
        print("")
        print("1. Spelet går till så att spelaren får ett kort i taget och efter varje kort får avgöra om han vill ha ytterligare kort eller inte. ")
        print("")
        print("2. Det gäller för spelaren att försöka få summan av kortens valörer så nära 21 som möjligt utan att överskrida detta tal.")
        print("")
        print("3. Ess räknas som antingen 1 eller 14.")
        print("")
        print("4. Om spelaren får över 21 förlorar hen och datorn vinner.")
        print("")
        print("5. Om spelaren stannar under 21 får också datorn dra ett kort i taget och efter varje kort avgöra om den skall fortsätta eller inte. ")
        print("")
        print(".6 Om datorn får mer än 21 poäng eller lägre poäng än användaren vinner användaren, annars vinner datorn.")
        print("")
        print("7.Datorn vinner alltså på samma poäng.")
        print("")
        # self.MenuUI(userInputText="Select a Number: ",
        #     menuOptions=[self.OptionMenu(title="Exit", action=action)])
              

    def StartGame(self) -> None:
        while self.isGameRunning:
            print("")
            print("")
            print("**Welcome to 21 Games**")
            print("**I hope you know the rules if you dont please select rules and will see them**")
        
            print("---In this interface you have to select a number to do something!---")
        
            self.gameUI.MenuUI(userInputText="Select a number: ", 
                menuOptions=[
                self.gameUI.OptionMenu(title="Start Game", action=self.PrintRules),
                self.gameUI.OptionMenu(title="See Rules", action=self.PrintRules),
                self.gameUI.OptionMenu(title="Exit the Game", action=self.PrintRules),
            ])
              
        
        

        
     
    
    