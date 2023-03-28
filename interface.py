from human import Mensch
import os
class Interface():
    def startScreen():
        print("\t Welcome to your own Human Generator")
        print("\t ****************************************************")
        print("\t Lets start by creating one")
        print("\t Do you already have a saved one or do you want to restart ?")
        print("1: To load from save File")
        print("2: To start a new one")
        wert = int(input("Insert Number:"))
        if  wert == 1:
            return 1
        else:
            return 2

    def header(obj):
        Interface.clear()
        print("\t Welcome to your own Human Generator")
        print("\t ****************************************************")
        print("\t Your current Human is:")
        #print("\t Name: ", name," Weight: ", Gewicht," Intelligence: ", IQ," Height: ", Groesse, " Wille: ", wille, "%")
        print(obj)
        pass

    def clear():
        os.system('cls')
        
    def mainScreen(obj):
        Interface.header(obj)
        print("1: Eat")
        print("2: Run")
        print("3: Weigh")
        print("4: Study")
        print("5: Play League")
        print("6: Take weird IQ Test")
        print("7: Lose will to live")
        user = int(input("\n \t Whats its task?"))

    def startGame():
        Interface.clear()
        return Interface.startScreen()
        
    def mainGame(obj):
        Interface.clear()
        Interface.mainScreen(obj)
        
    def creatingPlayer():
        name = input("Its name?")
        return Mensch(name=name)