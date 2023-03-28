import os
#Erstellung der MEnschen Klasse
class Mensch():
    def __init__(self,name,energy=100, hunger=50,IQ=50, wille=100, form="Normal"):
        self.__name = name
        self.__hunger = hunger
        self.__iq = IQ
        self.__energy = energy
        self.alive = True
        self.__wille = wille
        self.__form = form
    
    def __repr__(self) -> str:
        pass
        
    def __str__(self) -> str:
        return '\t Name: {} Hunger: {} Energy: {} Intelligence: {} Will: {} Form:{}'.format(self.__name,self.__hunger,self.__energy, self.__iq, self.__wille, self.__form)
        pass
    
    #Sends attribute values
    def stats(self):
        return self.__name, self.__hunger, self.__energy, self.__iq, self.__wille
    
    #sends attribute values as a dictionary for easier parameter use
    def dictStat(self):
        return {"name":self.__name,"hunger": self.__hunger,"energy": self.__energy,"IQ": self.__iq,"wille": self.__wille}
    
    #To kill it
    def die(self, alive):
        self.alive = False
        del self
        print("\t Your human died")
    
    #Save function 
    def saveData(self):
        with open("charData.txt","w") as f:
            all = [self.__name, self.__hunger, self.__energy, self.__iq, self.__wille, self.__form]
            print(len(all))
            i = 0
            while i<len(all):
                f.write("{}\n".format(str(all[i])))
                i += 1
            f.close()
    
    #read saved data and create object
    @classmethod
    def readData(cls):
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
            return Mensch(name=data[0], hunger=int(data[1]),energy=int(data[2]),IQ=int(data[3]), wille=int(data[4]), form=data[5])
        

#Threading add