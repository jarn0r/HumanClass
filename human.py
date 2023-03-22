import os
#Erstellung der MEnschen Klasse
class Mensch():
    def __init__(self,name, gewicht=50,IQ=50,groesse=20):
        self.__name = name
        self.__gewicht = gewicht
        self.__iq = IQ
        self.__groesse = groesse
        self.alive = True
        self.__wille = 100
    
    #Essen zum zunehmen
    def essen(self, menge):
        self.__gewicht += menge
    
    #Laufen zum abnehmen  
    def laufen(self, menge):
        print("\t It ran {}".format(menge))
        self.__gewicht -= menge
        
    def stats(self):
        return self.__name, self.__gewicht, self.__groesse, self.__iq, self.__wille
    
    def die(self, alive):
        self.alive = False
        del self
        print("\t Your human died")
    
    def saveData(self):
        with open("charData.txt","w") as f:
            all = [self.__name, self.__gewicht, self.__groesse, self.__iq, self.__wille]
            print(len(all))
            i = 0
            while i<len(all):
                f.write("{}\n".format(str(all[i])))
                i += 1
            f.close()
            


    def readData():
        with open("charData.txt","r") as f:
            #a = f.readlines()
            count = 0
            i = 0
            for line in enumerate(f):
                count +=1
            #while i < count:
            #    a = f.readline().strip()
            #    print(a)
            #    i += 1
            #a = f.readline().strip()
            print(str(f.read()))
            print(count)
            f.close()
            #return Mensch()

p1 = Mensch("ye")
Mensch.readData()