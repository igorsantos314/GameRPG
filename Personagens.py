class Personagem:

    def __init__(self, name, power=0, force=0, xp=0, life=0):
        self.name = name
        self.power = power
        self.force = force
        self.xp = xp
        self.life = life

    def getName(self):
        return self.name

    def getPower(self):
        return self.power

    def getForce(self):
        return self.force

    def getXp(self):
        return self.xp 

    def getLife(self):
        return self.life

    def getType(self):
        return ''

    def printData(self):
        print("             -------------------------")
        print("             --- Type:  ", self.getType())
        print("             --- Nome:  ", self.getName())
        print("             --- Vida:  ", self.getLife())
        print("             --- Power: ", self.getPower())
        print("             --- Force: ", self.getForce())
        print("             --- XP:    ", self.getXp())
        print("             -------------------------")

class Arqueiro(Personagem):

    def __init__(self, name, power=300, force=200, xp=300, life=1000):
        self.name = name
        self.power = power
        self.force = force
        self.xp = xp
        self.life = life

    def getType(self):
        return '|ARQUEIRO|'


class Guerreiro(Personagem):

    def __init__(self, name, power=250, force=450, xp=225, life=1000):
        self.name = name
        self.power = power
        self.force = force
        self.xp = xp
        self.life = life

    def getType(self):
        return '|GUERREIRO|'