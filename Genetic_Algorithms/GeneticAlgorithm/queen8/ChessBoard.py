class Chromosome:
    def __init__(self):
        self.sequence = None
        self.fitness = None

    def setSequence(self, val):
        self.sequence = val

    def setFitness(self, fitness):
        self.fitness = fitness

    def getSequence(self):
        return self.sequence

    def getFittness(self):
        return self.fitness

