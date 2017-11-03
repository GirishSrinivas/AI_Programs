class Crime:
    def __init__(self):
        self.state = None
        self.murder = 0.0
        self.assult = 0.0
        self.pop = 0.0
        self.rape = 0.0
        self.dist = 0.0

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def setMurder(self, murder):
        self.murder = murder

    def getMurder(self):
        return self.murder

    def setAssult(self, assult):
        self.assult = assult

    def getAssult(self):
        return self.assult

    def setPop(self, pop):
        self.pop = pop

    def getPop(self):
        return self.pop

    def setRape(self, rape):
        self.rape = rape

    def getRape(self):
        return self.rape

    def setDist(self, dist):
        self.dist = dist

    def getDist(self):
        return self.dist

