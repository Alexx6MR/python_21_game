import pyinputplus as pyip


class GameUI:
    def __init__(self) -> None:
        pass
    
    class OptionMenu:
        def __init__(self, title: str, action:any) -> None:
            self.title= title
            self.action = action

        def run(self):
            self.action()

    
    def MenuUI(self, menuOptions:list[OptionMenu]=[], userInputText: str = "")->None:
        optionLength = len(menuOptions)
    
        print()
        print("_______Menu_____")
        print()
    
        #* Loop to print all the options we have
        for item in range(optionLength):
            print(f"{item +1}. {menuOptions[item].title}")

        #* Input to validate and select the option
        print("_________________")
        print()
        res = pyip.inputNum(userInputText, max=optionLength, min=1)    
        print()
        print()
        #* Loop to select and run the action in the selected object
        for item in range(optionLength):
            if(res == item+1):
                menuOptions[item].run()  

    
   
    def EndMessageOfTheGame(self,currentPlayerCards, pcCards, message)->None:
        print("_______")
        print(message)
        print("--------")
        # print(f"Player Total hand: {CheckHandTotalValue(currentPlayerCards)}")
        print()
        print(f"")
        # print(f"PC Total hand: {CheckHandTotalValue(pcCards)}")
        print()
        self.MenuUI(userInputText= "What do you want to do: ", 
        menuOptions=[
            self.OptionMenu(title="ReMatch", action=self.InGame),
            self.OptionMenu(title="Exit", action=self.ExitGame),
        ])

