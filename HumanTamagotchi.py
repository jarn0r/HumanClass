from human import Mensch
from interface import Interface

p1 = Interface.startGame()
if p1==1:
    p1 = Mensch.readData()
else:
    p1 = Interface.creatingPlayer()
print(p1)
while p1.alive == True:
    Interface.mainGame(p1)
    pass