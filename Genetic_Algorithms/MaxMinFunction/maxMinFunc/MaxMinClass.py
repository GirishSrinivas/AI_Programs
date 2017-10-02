class MaxMinObj:
    def __init__(self):
        self.sequence = []
        self.fitness = 0
        self.coefficients = []
        self.constant = 0
        self.population_size = 0
        self.sample_size = 0
        self.total_population = []
        self.mutation_rate = 0.0
        self.iteration = 0
        self.choice = 0

    # setter methods
    def setSequence(self, val):
        self.sequence = val

    def setFitness(self, val):
        self.fitness = val

    def setCoefficients(self, val):
        self.coefficients = val

    def setConstant(self, val):
        self.constant = val

    def setPopulationSize(self, val):
        self.population_size = val

    def setSampleSize(self, val):
        self.sample_size = val

    def setTotalPopulation(self, val):
        self.total_population = val

    def setMutationRate(self, val):
        self.mutation_rate = val

    def setIteration(self, val):
        self.iteration = val

    def setChoice(self, val):
        self.choice = val

    # getter methods
    def getSequence(self):
        return self.sequence

    def getFitness(self):
        return self.fitness

    def getCoefficients(self):
        return self.coefficients

    def getConstant(self):
        return self.constant

    def getPopulationSize(self):
        return self.population_size

    def getSampleSize(self):
        return self.sample_size

    def getTotalPopulation(self):
        return self.total_population

    def getMutationRate(self):
        return self.mutation_rate

    def getIteration(self):
        return self.iteration

    def getChoice(self):
        return self.choice
