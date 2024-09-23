import sys

from src.gameUI import GameUI
from src.player import Player
from src.deck import Deck, Card



class Game21Setup:
    def __init__(self) -> None:
        self.__isGameRunning: bool = True
        self.currentPcHand: list[Card] = []
        
        #* Import and initiate the classes needed for the application to work
        self.gameUI = GameUI()
        self.currentPlayer = Player()
        self.deck = Deck()
   

    #* Make the program to finish and print a message
    def ExitGame(self)->None:
        print()
        print("Thank you for Playing :) ")
        print("See you soon!!!!! ")
        print()
        sys.exit(0)
        
    
    #* function to return the Current player/pc hand
    def CheckHandTotalValue(self, currentHand: list[Card])->int:
        totalValue: int = 0

        for card in currentHand:
            totalValue += card.value
             
        return totalValue    
 
 
    #* This function works as a "Page" that the user can check if they want to see the rules of the game  
    def PrintRules(self)-> None:
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
        self.gameUI.MenuUI(userInputText="Select a Number: ",
            menuOptions=[ 
                {"title": "Back", "action":self.StartGame},
                {"title": "Exit", "action":self.ExitGame},
            ])
          
            
    #* This function will handle all the logic and condition to the user turn
    def PlayerTurn(self) -> None:
        isPlayerTurn: bool = True
        
        #* function to handle if the player will pass his turn
        def NoMoreCard() -> None:
            nonlocal isPlayerTurn
            isPlayerTurn = False         

        #* function to let the user select if they want the ACE to has a 1 or 14 value or add a single card into the player hand
        def addCard() -> None:
            self.currentPlayer.set_NewCard(self.deck.get_OneCard())
            
        #* loop to control the player turn
        while isPlayerTurn:
            playerHandTotalvalue: int = self.CheckHandTotalValue(self.currentPlayer.get_CurrentHand())            
            
            if(playerHandTotalvalue > 21):
                self.gameUI.EndMessage(
                    message="Sorry the game is over, your total value is too hight", 
                    currentPlayerCards=self.currentPlayer.get_CurrentHand(), 
                    pcCurrentCards=self.currentPcHand,
                    menuOptions =[
                        {"title": "ReMatch", "action":self.InGame},
                        {"title": "Go to Menu", "action":self.StartGame},
                    ]
                )
            elif playerHandTotalvalue == 21:
                self.gameUI.EndMessage(
                    message="Congratulacion you won this match", 
                    currentPlayerCards=self.currentPlayer.get_CurrentHand(), 
                    pcCurrentCards=self.currentPcHand,
                    menuOptions =[
                        {"title": "ReMatch", "action":self.InGame},
                        {"title": "Go to Menu", "action":self.StartGame},
                    ]
                )
            else:
                self.gameUI.PrintBoard(currentPlayerCards=self.currentPlayer.get_CurrentHand(), pcCurrentCards=self.currentPcHand)
                self.gameUI.MenuUI(userInputText="Select a number: ", 
                menuOptions=[
                    {"title": "One more Card", "action":addCard},
                    {"title": "No more card", "action":NoMoreCard},
              
            ])
    
    
    #* This function handle the logic of the whole 21 game and works as the "Game Page"         
    def InGame(self)-> None:
        isPcTurn: bool = True
        print("-----------------")
        print("")
        print("**The Game is On**")
    
        #* Preparing the inital hand for player and pc
        self.currentPlayer.set_InitialHand(card1=self.deck.get_OneCard(), card2=self.deck.get_OneCard())
        self.currentPcHand = [self.deck.get_OneCard()]


        while self.__isGameRunning:
            
            self.PlayerTurn()
            playerHandValue = self.CheckHandTotalValue(self.currentPlayer.get_CurrentHand()) 
                
            
            while isPcTurn:
                if isPcTurn == False: break
                
                #* Take the current value of pc hand every round
                pcHandValue = self.CheckHandTotalValue(self.currentPcHand) 
                
                #* checking the winner before start the Turn.                
                if pcHandValue > playerHandValue and pcHandValue > 21:
                    self.gameUI.EndMessage(
                    message="Congratulation you won this match, The PC's hand is higher than 21", 
                    currentPlayerCards=self.currentPlayer.get_CurrentHand(), 
                    pcCurrentCards=self.currentPcHand,
                    menuOptions =[
                        {"title": "ReMatch", "action":self.InGame},
                        {"title": "Go to Menu", "action":self.StartGame},
                    ]
                    )
                elif pcHandValue > playerHandValue and pcHandValue < 21:
                    self.gameUI.EndMessage(
                    message="Sorry you loose, the computer was luckier this time", 
                    currentPlayerCards=self.currentPlayer.get_CurrentHand(), 
                    pcCurrentCards=self.currentPcHand,
                    menuOptions =[
                        {"title": "ReMatch", "action":self.InGame},
                        {"title": "Go to Menu", "action":self.StartGame},
                    ]
                    )
                else:
                    #* Adding a new card to pc Hand
                    card: Card = self.deck.get_OneCard()
                    if card.number != "Ace": 
                        self.currentPcHand.append(card)
                    else:
                        if pcHandValue + 14 > playerHandValue and pcHandValue + 14  < 21:
                            print(" this is true" + pcHandValue + 14)
                            self.currentPcHand.append(Card(number="Ace", suit=card.suit, value=14))
                        else:
                            self.currentPcHand.append(card)

    
    #* Start menu: here the user can choose what to do
    def StartGame(self) -> None:                         
            print("")
            print("**Welcome to 21 Games**")
            print("**I hope you know the rules if you dont please select rules and will see them**")
        
            print("---In this interface you have to select a number to do something!---")

            #* Main Menu to Controll the Game
            self.gameUI.MenuUI(userInputText="Select a number: ", 
                menuOptions=[
                    {"title": "Start Game", "action":self.InGame},
                    {"title": "See Rules", "action":self.PrintRules},
                    {"title": "Exit the Game", "action":self.ExitGame},

            ])
        
        

        
     
