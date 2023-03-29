from human import Mensch
from interface import Interface


if __name__ == "__main__":
    p1 = Interface.startGame()
    if p1==1:
        p1 = Mensch.readData()
    else:
        p1 = Interface.creatingPlayer()
    print(p1)
    p1.saveData()
    while p1.alive == True:
        Interface.mainGame(p1)
        pass