import pyinputplus as pyip
import random
isGameRunning: bool = True






#* DECK and CARDS SILE
cardsSuit: dict = {
    "Hearts": "Hearts",
    "Diamonds": "Diamonds",
    "Clubs": "Clubs",
    "Spades": "Spades",
    
}


class Card:
    def __init__(self, number, suit, value):
        self.number = number 
        self.suit = suit      
        self.value = value    


#* reglas de juego, primero se da al jugador y despues a la pc y por ultimo al jugador
#* despues el jugador puede selecionar si quiere mas cartas o si quiere no tomar mas u dejar que la computadora escoja mas
#* el que la suma se sus cartas sea mas alta gana que el otro gana

deck: list[str] = [
    Card(number=1, suit=cardsSuit["Hearts"], value=1),
    Card(number=2, suit=cardsSuit["Hearts"], value=2),
    Card(number=3, suit=cardsSuit["Hearts"], value=3),
    Card(number=4, suit=cardsSuit["Hearts"], value=4),
    Card(number=5, suit=cardsSuit["Hearts"], value=5),
    Card(number=6, suit=cardsSuit["Hearts"], value=6),
    Card(number=7, suit=cardsSuit["Hearts"], value=7),
    Card(number=8, suit=cardsSuit["Hearts"], value=8),
    Card(number=9, suit=cardsSuit["Hearts"], value=9),
    Card(number=10, suit=cardsSuit["Hearts"], value=10),
    Card(number=11, suit=cardsSuit["Hearts"], value=11),
    Card(number=12, suit=cardsSuit["Hearts"], value=12),
    Card(number=13, suit=cardsSuit["Hearts"], value=13),
    
    Card(number=1, suit=cardsSuit["Diamonds"], value=1),
    Card(number=2, suit=cardsSuit["Diamonds"], value=2),
    Card(number=3, suit=cardsSuit["Diamonds"], value=3),
    Card(number=4, suit=cardsSuit["Diamonds"], value=4),
    Card(number=5, suit=cardsSuit["Diamonds"], value=5),
    Card(number=6, suit=cardsSuit["Diamonds"], value=6),
    Card(number=7, suit=cardsSuit["Diamonds"], value=7),
    Card(number=8, suit=cardsSuit["Diamonds"], value=8),
    Card(number=9, suit=cardsSuit["Diamonds"], value=9),
    Card(number=10, suit=cardsSuit["Diamonds"], value=10),
    Card(number=11, suit=cardsSuit["Diamonds"], value=11),
    Card(number=12, suit=cardsSuit["Diamonds"], value=12),
    Card(number=13, suit=cardsSuit["Diamonds"], value=13),
    
    Card(number=1, suit=cardsSuit["Clubs"], value=1),
    Card(number=2, suit=cardsSuit["Clubs"], value=2),
    Card(number=3, suit=cardsSuit["Clubs"], value=3),
    Card(number=4, suit=cardsSuit["Clubs"], value=4),
    Card(number=5, suit=cardsSuit["Clubs"], value=5),
    Card(number=6, suit=cardsSuit["Clubs"], value=6),
    Card(number=7, suit=cardsSuit["Clubs"], value=7),
    Card(number=8, suit=cardsSuit["Clubs"], value=8),
    Card(number=9, suit=cardsSuit["Clubs"], value=9),
    Card(number=10, suit=cardsSuit["Clubs"], value=10),
    Card(number=11, suit=cardsSuit["Clubs"], value=11),
    Card(number=12, suit=cardsSuit["Clubs"], value=12),
    Card(number=13, suit=cardsSuit["Clubs"], value=13),
    
    Card(number=1, suit=cardsSuit["Spades"], value=1),
    Card(number=2, suit=cardsSuit["Spades"], value=2),
    Card(number=3, suit=cardsSuit["Spades"], value=3),
    Card(number=4, suit=cardsSuit["Spades"], value=4),
    Card(number=5, suit=cardsSuit["Spades"], value=5),
    Card(number=6, suit=cardsSuit["Spades"], value=6),
    Card(number=7, suit=cardsSuit["Spades"], value=7),
    Card(number=8, suit=cardsSuit["Spades"], value=8),
    Card(number=9, suit=cardsSuit["Spades"], value=9),
    Card(number=10, suit=cardsSuit["Spades"], value=10),
    Card(number=11, suit=cardsSuit["Spades"], value=11),
    Card(number=12, suit=cardsSuit["Spades"], value=12),
    Card(number=13, suit=cardsSuit["Spades"], value=13),
]




def RemoveCard(deck, number, suit):
    card_to_remove = None
    for card in deck:
        if card.number == number and card.suit == suit:
            card_to_remove = card
            break
    if card_to_remove:
        deck.remove(card_to_remove)
        print(f"The card '{card_to_remove}' has been removed from the deck.")
    else:
        print(f"The card '{number} of {suit}' is not in the deck.")


def ShuffleTheDecks()-> list[any]:
    random.shuffle(deck)
    print("The deck has been shuffled.")


#* DECK and CARDS SILE



def ExitGame()->None:
    global isGameRunning
    isGameRunning = False
    print("")
    print("Thank you for Playing :) ")
    print("See you soon!!!!! ")
    print("")
    
    
    
class OptionMenu:
    def __init__(self, title: str, action:any) -> None:
        self.title= title
        self.action = action

    def run(self):
        self.action()



def MenuUI(options:list[OptionMenu], userInputText: any)->None:
    optionLength = len(options)
    

    print()
    print("_______Menu_____")
    print()
    
    #* Loop to print all the options we have
    for item in range(optionLength):
        print(f"{item +1}. {options[item].title}")


    #* Input to validate and select the option
    print("_________________")
    print()
    res = pyip.inputNum(userInputText, max=optionLength, min=1)    
    print()
    print()
    #* Loop to select and run the action in the selected object
    for item in range(optionLength):
        if(res == item+1):
            options[item].run()  

def PrintRules()-> None:
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
    MenuUI( userInputText="Select a Number: ",
        options=[OptionMenu(title="Exit", action=StartGame)])



def CheckHandTotalValue(playerHand)->bool:
    value = sum(card.value for card in playerHand)

    ace_count = sum(1 for card in playerHand if card.number == "Ace")
    
    while value > 21 and ace_count > 0:
        value -= 10  
        ace_count -= 1
    
    return value


def CheckPcHand(playerHand)->bool:
    value = sum(card.value for card in playerHand)

    ace_count = sum(1 for card in playerHand if card.number == "Ace")
    
    while value > 21 and ace_count > 0:
        value -= 10  
        ace_count -= 1
    
    return value


def PrintBoard(playerCards, pcCards)->None:
    
    #* Take the length of both list to print the index and the the data
    pcCardLength = len(pcCards)
    playerCardLength = len(playerCards)
    print("")
    print("--------------")
    print("")
    print("PC Hand: ")
    for pcCard in range(pcCardLength):
        print(f"{pcCard +1}. {pcCards[pcCard].number} {pcCards[pcCard].suit}")
    print("")
    print(f"Player total: {CheckHandTotalValue(pcCards)}")
    print("")
    print("")
    print("------vs------")
    print("")
    print("Player Hand: ")
    for playerCard in range(playerCardLength):
        print(f"{playerCard +1}. {playerCards[playerCard].number} {playerCards[playerCard].suit}")
    print("")
    print(f"Player total: {CheckHandTotalValue(playerCards)}")
    print("")


def EndMessageOfTheGame(currentPlayerCards, pcCards, message)->None:
    print("_______")
    print(message)
    print("--------")
    print(f"Player Total hand: {CheckHandTotalValue(currentPlayerCards)}")
    print()
    print(f"")
    print(f"PC Total hand: {CheckHandTotalValue(pcCards)}")
    print()
    MenuUI(userInputText= "What do you want to do: ", 
        options=[
            OptionMenu(title="ReMatch", action=InGame),
            OptionMenu(title="Exit", action=ExitGame),
        ])

def PlayerTurn(playerCards, pcCards):
    currentPlayerCards: list[Card] = playerCards
    isPlayerTurn: bool = True
    
        
    def oneMoreCard():
        currentPlayerCards.append(deck.pop())
    
    def NoMoreCard():
        isPlayerTurn: bool = False
        return CheckHandTotalValue(currentPlayerCards)
        
    
    while isPlayerTurn:
    
        value = CheckHandTotalValue(currentPlayerCards)
    
        if(value > 21):
            EndMessageOfTheGame(
                message="The game is over, your total value is too hight", 
                currentPlayerCards=currentPlayerCards, 
                pcCards=pcCards
            )
        
        elif value == 21:
            EndMessageOfTheGame(
                message="Congratulacion you wont this match", 
                currentPlayerCards=currentPlayerCards, 
                pcCards=pcCards
            )
        else:
            PrintBoard(currentPlayerCards, pcCards)
         
            MenuUI(userInputText= "Select a number: ", 
                options=[
                    OptionMenu(title="One more card", action=oneMoreCard),
                    OptionMenu(title="No more card", action=NoMoreCard),
                ])
             



currentPlayerCards: list[Card] = []
currentPcCards: list[Card] = []


def InGame()-> None:
    global isGameRunning
    global deck
    global currentPcCards
    print("-----------------")
    print("")
    print("**The Game is On**")
    
    #* Preparing inital hand
    ShuffleTheDecks()
    initialPlayerCards = [deck.pop(), deck.pop()]
    initialPcCards = [deck.pop()]
    currentPcCards = initialPcCards
    
    while isGameRunning:
        pcTotalHand = PlayerTurn(initialPlayerCards, initialPcCards)
        
        
        while True:
            value = CheckHandTotalValue(currentPcCards)
    
            if(value > 21):
                EndMessageOfTheGame(
                    message="Congratulations you have won the game, the pc's total value is too hight.", 
                    currentPlayerCards=currentPlayerCards, 
                    pcCards=currentPcCards
                )
    
            elif value == 21:
                EndMessageOfTheGame(
                message="Sorry, the PC was very lucky and won this match.", 
                currentPlayerCards=currentPlayerCards, 
                pcCards=currentPcCards
            )
         
                
      
    
        







def StartGame() -> None:

    
    
    while isGameRunning:
        print("")
        print("")
        print("**Welcome to 21 Games**")
        print("**I hope you know the rules if you dont please select rules and will see them**")
        
        print("---In this interface you have to select a number to do something!---")
        
        MenuUI(userInputText="Select a number: ",
            options=[
            OptionMenu(title="Start Game", action=InGame),
            OptionMenu(title="See Rules", action=PrintRules),
            OptionMenu(title="Exit the Game", action=ExitGame),
        ])
              
        
        

        
     
    
    