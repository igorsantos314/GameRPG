from Personagens import *

class Batalha:

    def __init__(self, P1, P2, manaP1, manaP2):
        self.P1 = P1
        self.P2 = P2
        self.manaP1 = manaP1
        self.manaP2 = manaP2

    def getP1(self):
        return self.P1

    def getP2(self):
        return self.P2
    
    def getManaP1(self):
        return self.manaP1
    
    def getManaP2(self):
        return self.manaP2

    def viewP1(self):
        print("\n-------------------------------")
        print("----  PERSONAGENS PLAYER 1  -----")
        print("---------------------------------\n")

        for i in self.getP1():
            i.printData()
        
        print("\n-------------------------------\n")

    def viewP2(self):
        print("\n-------------------------------")
        print("----  PERSONAGENS PLAYER 1  -----")
        print("---------------------------------\n")

        for i in self.getP2():
            i.printData()
        
        print("\n-------------------------------\n")

    def startBattle(self):
        pass
