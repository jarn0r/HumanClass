import threading

class Ressources():
    def __init__(self,menge) -> None:
        self.__menge = menge
        pass
    
    def changeAmount(self,amount):
        self.__menge += amount
        
        
    def __repr__(self) -> str:
        pass
    
    def __str__(self) -> str:
        return '{}'.format(self.__menge)
    
class Food(Ressources):
    def __init__(self, menge) -> None:
        super().__init__(menge)
        
    
    pass

class Money(Ressources):
    def __init__(self, menge) -> None:
        super().__init__(menge)
    pass


#Save MEthod and read method add