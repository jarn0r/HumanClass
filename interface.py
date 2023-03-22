import human


def startScreen():
    print("\t Welcome to your own Human Generator")
    print("\t ****************************************************")
    print("\t Lets start by creating one")

def header(name, Gewicht, IQ, Groesse,wille):
    clear()
    print("\t Welcome to your own Human Generator")
    print("\t ****************************************************")
    print("\t Your current Human is:")
    print("\t Name: ", name," Weight: ", Gewicht," Intelligence: ", IQ," Height: ", Groesse, " Wille: ", wille, "%")
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
    name, wheight, height, iq, wille = p1.stats()
    header(name=name, Gewicht=wheight, IQ=iq, Groesse=height)
    mainScreen()