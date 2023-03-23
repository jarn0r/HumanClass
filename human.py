import os
#Erstellung der MEnschen Klasse
class Mensch():
    def __init__(self,name, gewicht=50,groesse=20,IQ=50, wille=100):
        self.__name = name
        self.__gewicht = gewicht
        self.__iq = IQ
        self.__groesse = groesse
        self.alive = True
        self.__wille = wille
    
    #Essen zum zunehmen
    def essen(self, menge):
        self.__gewicht += menge
    
    #Laufen zum abnehmen  
    def laufen(self, menge):
        print("\t It ran {}".format(menge))
        self.__gewicht -= menge
        print("Gewicht liegt bei {}".format(self.__gewicht))
    
    #Sends attribute values
    def stats(self):
        return self.__name, self.__gewicht, self.__groesse, self.__iq, self.__wille
    
    #sends attribute values as a dictionary for easier parameter use
    def dictStat(self):
        return {"name":self.__name,"Gewicht": self.__gewicht,"Groesse": self.__groesse,"IQ": self.__iq,"wille": self.__wille}
    
    #To kill it
    def die(self, alive):
        self.alive = False
        del self
        print("\t Your human died")
    
    #Save function 
    def saveData(self):
        with open("charData.txt","w") as f:
            all = [self.__name, self.__gewicht, self.__groesse, self.__iq, self.__wille]
            print(len(all))
            i = 0
            while i<len(all):
                f.write("{}\n".format(str(all[i])))
                i += 1
            f.close()
    
    #read saved data and create object
    def readData():
        with open("charData.txt","r") as f:
            a = f.readlines()
            data = []
            print(a)
            print(a[1])
            for i in a:
                print(i)
                i.split()
                print(i)
                data.append(i)
            print(data)
            f.close()
            return Mensch(name=data[0], gewicht=int(data[1]),groesse=int(data[2]),IQ=int(data[3]), wille=int(data[4]))