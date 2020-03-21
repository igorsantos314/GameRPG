class Personagem:

    name = ''
    power = 300
    force = 200
    xp = 300

    def __init__(self, name, power=0, force=0, xp=0):
        self.name = name
        self.power = power
        self.force = force
        self.xp = xp

    def getName(self):
        return self.name

    def getPower(self):
        return self.power

    def getForce(self):
        return self.force

    def getXp(self):
        return self.xp 

    def getType(self):
        return ''

    def printData(self):
        print("             -------------------------")
        print("             --- Type:  ", self.getType())
        print("             --- Nome:  ", self.name)
        print("             --- Power: ", self.power)
        print("             --- Force: ", self.force)
        print("             --- XP:    ", self.xp)
        print("             -------------------------")

class Arqueiro(Personagem):

    def __init__(self, name, power=300, force=200, xp=300):
        self.name = name
        self.power = power
        self.force = force
        self.xp = xp

    def getType(self):
        return '|ARQUEIRO|'


class Guerreiro(Personagem):

    def __init__(self, name, power=250, force=450, xp=225):
        self.name = name
        self.power = power
        self.force = force
        self.xp = xp

    def getType(self):
        return '|GUERREIRO|'

listPersonagens = []

for i in range(2):

    nomeArq = input("Arqueiro Nome: ")
    nomeGue = input("Guerreiro Nome: ")

    a = Arqueiro(nomeArq)
    b = Guerreiro(nomeGue)

    listPersonagens.append(a)
    listPersonagens.append(b)

for i in listPersonagens:
    i.printData()