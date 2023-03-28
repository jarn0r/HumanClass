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
        gewicht = int(input("How much does it weight?"))
        iq = int(input("How smart is it?"))
        grosse = int(input("How big is it?"))
        return Mensch(gewicht=gewicht,IQ=iq,groesse=grosse, name=name)
        



"""
startScreen()
name = input("Its name?")
gewicht = int(input("How much does it weight?"))
iq = int(input("How smart is it?"))
grosse = int(input("How big is it?"))
p1 = Mensch(gewicht=gewicht,IQ=iq,groesse=grosse, name=name)

while(p1.alive):
    name, wheight, height, iq, wille = p1.stats()
    header(name=name, Gewicht=wheight, IQ=iq, Groesse=height)
    mainScreen()
"""