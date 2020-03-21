class Arqueiro:

    name = ''
    power = 300
    force = 200
    xp = 300

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getPower(self):
        return self.power

    def getForce(self):
        return self.force

    def getXp(self):
        return self.xp

    def printArq(self):
        print("             -------------------------")
        print("             --- Nome:  ", self.name)
        print("             --- Power: ", self.power)
        print("             --- Force: ", self.force)
        print("             --- XP:    ", self.xp)
        print("             -------------------------")

igor = Arqueiro('Igor')
igor.printArq()