import os
#Erstellung der MEnschen Klasse
class Mensch():
    
    def __init__(self,name, gewicht=50,IQ=50,groesse=20):
        self.__name = name
        self.__gewicht = gewicht
        self.__iq = IQ
        self.__groesse = groesse
        self.alive = True
    
    #Essen zum zunehmen
    def essen(self, menge):
        self.__gewicht += menge
        
    #Ausgabe der Daten
    def wiegen(self):
        print("Ich wiege {}".format(self.__gewicht))
    
    #Laufen zum abnehmen  
    def laufen(self, menge):
        print("\t It ran {}".format(menge))
        self.__gewicht -= menge
        
    def stats(self):
        return self.__name, self.__gewicht, self.__groesse, self.__iq
    
    def die(self, alive):
        self.alive = False
        del self
        print("\t Your human died")


def startScreen():
    print("\t Welcome to your own Human Generator")
    print("\t ****************************************************")
    print("\t Lets start by creating one")

def header(name, Gewicht, IQ, Groesse):
    clear()
    print("\t Welcome to your own Human Generator")
    print("\t ****************************************************")
    print("\t Your current Human is:")
    print("\t Name: ", name," Weight: ", Gewicht," Intelligence: ", IQ," Height: ", Groesse)
    pass

def clear():
    os.system('cls')
    
def mainScreen():
    print("1: Eat")
    print("2: Run")
    print("3: Weigh")
    print("4: Study")
    print("5: Play League")
    print("6: Take weird IQ Test")
    print("7: Lose will to live")
    user = int(input("\n \t Whats its task?"))

startScreen()
name = input("Its name?")
gewicht = int(input("How much does it weight?"))
iq = int(input("How smart is it?"))
grosse = int(input("How big is it?"))
p1 = Mensch(gewicht=gewicht,IQ=iq,groesse=grosse, name=name)

while(p1.alive):
    name, wheight, height, iq = p1.stats()
    header(name=name, Gewicht=wheight, IQ=iq, Groesse=height)
    mainScreen()