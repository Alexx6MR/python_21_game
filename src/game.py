import pyinputplus as pyip

isGameRunning: bool = True

class OptionMenu:
    def __init__(self, title: str, action:any) -> None:
        self.title= title
        self.action = action

    def run(self):
        self.action()


def MenuUI(options:list[OptionMenu])->None:
    optionLength = len(options)
    

    print()
    print("_______Menu_____")
    print()
    
    #* Loop to print all the options we have
    for item in range(optionLength):
        print(f"{item +1}. {options[item].title}")


    #* Input to validate and select the option
    print("_________________")
    res = pyip.inputNum("select a number: ", max=optionLength, min=1);    
    
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
    # MenuUI(OptionMenu(title="Exit", action=print("Game is Starting")))

def StartGame() -> None:
    global isGameRunning
    
    
    while isGameRunning:
        print("**Welcome to 21 Games**")
        print("**I hope you know the rules if you dont please select rules and will see them**")
        
        print("---In this interface you have to select a number to do something!---")
        
        
        def ExitGame()->None:
            isGameRunning = False
        
        MenuUI([
            OptionMenu(title="Start Game", action=PrintRules),
            OptionMenu(title="See Rules", action=PrintRules),
            OptionMenu(title="Exit the Game", action=PrintRules),
        ])
      
        # match res:
        #     case 1: print("respuesta 1")
        #     case 2: PrintRules()
        #     case 3: isGameRunning = False
            
        
        
        
        
        isGameRunning = False
        
     
    
    