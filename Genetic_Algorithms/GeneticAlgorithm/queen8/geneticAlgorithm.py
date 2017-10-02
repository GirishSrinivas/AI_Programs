"""
@author: Girish Srinivas
@email: gsrinivas@unomaha.edu
@description: Genetic Algorithm for solving 8 - Queen problem
"""
from queen8 import ChessBoard as cb
import random as rand

N_QUEEN = 8
# MAT = np.zeros((8, 8))


class GeneticAlgorithm:
    def __init__(self, pop_size, sample_size, tot_pop, mutation, itern):
        """
        Constructor for GeneticAlgorithm class with class variables
        :param pop_size:
        :param sample_size:
        :param tot_pop:
        :param mutation:
        :param itern:
        """
        self.population_size = 0
        self.sample_size = 0
        self.total_population = []
        self.mutation_rate = 0.0
        self.iteration = 0

        self.setPopulationSize(pop_size)
        self.setSampleSize(sample_size)
        self.setTotalPopulation(tot_pop)
        self.setMutationRate(mutation)
        self.setIteration(itern)

    def setPopulationSize(self, val):
        """
        This Method sets the class variable population_size
        :param val:
        :return: none
        """
        self.population_size = val

    def setSampleSize(self, val):
        """
        This Method sets the class variable sample_size
        :param val:
        :return: none
        """
        self.sample_size = val

    def setTotalPopulation(self, val):
        """
        This Method sets the class variable total_population
        :param val:
        :return:
        """
        self.total_population = val

    def setMutationRate(self, val):
        """
        This Method sets the class variable mutation_rate
        :param val:
        :return:
        """
        self.mutation_rate = val

    def setIteration(self, val):
        """
        This Method sets the class variable iteration
        :param val:
        :return:
        """
        self.iteration = val

    def getPopulationSize(self):
        """

        :return:
        """
        return self.population_size

    def getSampleSize(self):
        """

        :return:
        """
        return self.sample_size

    def getTotalPopulation(self):
        """

        :return:
        """
        return self.total_population

    def getMutationRate(self):
        """

        :return:
        """
        return self.mutation_rate

    def getIteration(self):
        """

        :return:
        """
        return self.iteration


def generateChromosome():
    """
    This method generates random boards
    :return:
    """

    rand_board = rand.sample(range(0, N_QUEEN), N_QUEEN)
    return rand_board


def fitness(chromosome):
    """
    returns 28 - <number of conflicts>
    to test for conflicts, we check for
     -> row conflicts
     -> diagonal conflicts

    The ideal case can yield upton 28 arrangements of non attacking pairs.
    for iteration 0 -> there are 7 non attacking queens
    for iteration 1 -> there are 6 no attacking queens ..... and so on
    Therefore max fitness = 7 + 6+ 5+4 +3 +2 +1 = 28
    hence fitness val returned will be 28 - <number of clashes>
    """

    # calculate row and column clashes
    # just subtract the unique length of array from total length of array
    # [1,1,1,2,2,2] - [1,2] => 4 clashes
    clashes = 0
    row_col_clashes = abs(len(chromosome) - len(set(chromosome)))
    clashes += row_col_clashes

    # calculate diagonal clashes
    for i in range(len(chromosome)):
        for j in range(len(chromosome)):
            if i != j:
                dx = abs(i - j)
                dy = abs(chromosome[i] - chromosome[j])
                if dx == dy:
                    clashes += 1

    return 28 - clashes


def generatePopulation(population_size=500):
    """

    :param population_size:
    :return:
    """
    population = [cb.Chromosome() for i in range(population_size)]

    for i in range(population_size):
        population[i].setSequence(generateChromosome())
        population[i].setFitness(fitness(population[i].sequence))

    return population


def singlePointCrossover(self, parent1, parent2):
    """
    This method cuts the chromosome at a single random point and
    :return:
    """
    child1 = cb.Chromosome()
    child2 = cb.Chromosome()

    splice = int(rand.uniform(1, 7))

    seq1 = parent1[0: splice] + parent2[splice:]
    seq2 = parent2[0: splice] + parent1[splice:]

    ch_seq1 = mutation(self, seq1)
    ch_seq2 = mutation(self, seq2)

    child1.setSequence(ch_seq1)
    child1.setFitness(fitness(ch_seq1))

    child2.setSequence(ch_seq2)
    child2.setFitness(fitness(ch_seq2))

    return child1, child2


def twoPointCrossover(self, parent1, parent2):
    """

    :param self:
    :param parent1:
    :param parent2:
    :return:
    """
    child1 = cb.Chromosome()
    child2 = cb.Chromosome()

    split1 = int(rand.uniform(1, 4))
    split2 = int(rand.uniform(4, 7))

    seq1 = parent1[0:split1] + parent2[split1:split2] + parent1[split2:]
    seq2 = parent2[0:split1] + parent1[split1:split2] + parent2[split2:]

    ch_seq1 = mutation(self, seq1)
    ch_seq2 = mutation(self, seq2)

    child1.setSequence(ch_seq1)
    child1.setFitness(fitness(ch_seq1))

    child2.setSequence(ch_seq2)
    child2.setFitness(fitness(ch_seq2))

    return child1, child2


def cutAndSpliceCrossover(self, parent1, parent2):
    """

    :param self:
    :param parent1:
    :param parent2:
    :return:
    """
    child1 = cb.Chromosome()
    child2 = cb.Chromosome()

    split1 = int(rand.uniform(1, 4))
    split2 = int(rand.uniform(4, 7))

    seq1 = parent1[:split1] + parent2[split2:]
    seq2 = parent2[:split2] + parent1[split1:]

    if len(seq1) > 8:
        seq1 = seq1[:8]
    else:
        rem = 8 - len(seq1)
        seq1 = seq1 + rand.sample(range(0, 8), rem)

    if len(seq2) > 8:
        seq2 = seq2[:8]
    else:
        rem = 8 - len(seq2)
        seq2 = seq2 + rand.sample(range(0, 8), rem)

    ch_seq1 = mutation(self, seq1)
    ch_seq2 = mutation(self, seq2)

    child1.setSequence(ch_seq1)
    child1.setFitness(fitness(ch_seq1))

    child2.setSequence(ch_seq2)
    child2.setFitness(fitness(ch_seq2))

    return child1, child2


def uniformCrossover(self, parent1, parent2):
    """

    :param self:
    :param parent1:
    :param parent2:
    :return:
    """
    child1 = cb.Chromosome()
    child2 = cb.Chromosome()

    probability = 0.5

    seq1 = []
    seq2 = []

    for i in range(8):
        chrnd = rand.uniform(0, 1)

        if probability < chrnd:
            seq1.append(parent1[i])
            seq2.append(parent2[i])
        else:
            seq1.append(parent2[i])
            seq2.append(parent1[i])

    ch_seq1 = mutation(self, seq1)
    ch_seq2 = mutation(self, seq2)

    child1.setSequence(ch_seq1)
    child1.setFitness(fitness(ch_seq1))

    child2.setSequence(ch_seq2)
    child2.setFitness(fitness(ch_seq2))

    return child1, child2


def mutation(self, sequence):
    """

    :param self:
    :param sequence:
    :return:
    """
    child_rand = rand.uniform(0, 1)
    if self.getMutationRate() < child_rand:
        c = int(rand.uniform(0, len(sequence)))
        mutate = int(rand.uniform(0, len(sequence)))
        sequence[int(c)] = int(mutate)
    return sequence


def GA(self, choice):
    """

    :param self:
    :param choice:
    :return:
    """
    res = None
    itern = 0

    if choice < 1 or choice > 4:
        return res, itern

    samplesize = self.getSampleSize()

    total_population = self.getTotalPopulation()
    new_population = []

    for i in range(len(self.getTotalPopulation())):
        new_population.append((total_population[i].getFittness(), total_population[i].getSequence()))

    # print(self.getIteration())

    if self.getIteration() < 0:
        upperlimit = 10000
    else:
        upperlimit = self.getIteration()

    while itern < upperlimit:
        sortedlist = sort(new_population)
        sample_list = sortedlist[:samplesize]

        result, chromosome = isSolved(sortedlist)

        if result:
            return chromosome, itern

        rand.shuffle(sample_list)

        for parent1, parent2 in pairwise(sample_list):
            if choice == 1:
                child1, child2 = singlePointCrossover(self, list(parent1[1]), list(parent2[1]))
                new_population.append((child1.getFittness(), child1.getSequence()))
                new_population.append((child2.getFittness(), child2.getSequence()))
            elif choice == 2:
                child1, child2 = twoPointCrossover(self, list(parent1[1]), list(parent2[1]))
                new_population.append((child1.getFittness(), child1.getSequence()))
                new_population.append((child2.getFittness(), child2.getSequence()))
            elif choice == 3:
                child1, child2 = cutAndSpliceCrossover(self, list(parent1[1]), list(parent2[1]))
                new_population.append((child1.getFittness(), child1.getSequence()))
                new_population.append((child2.getFittness(), child2.getSequence()))
            elif choice == 4:
                child1, child2 = uniformCrossover(self, list(parent1[1]), list(parent2[1]))
                new_population.append((child1.getFittness(), child1.getSequence()))
                new_population.append((child2.getFittness(), child2.getSequence()))

        itern += 1
        res = sortedlist[0]
        # print(res)
    return res, itern


def sort(lst):
    """

    :param lst:
    :return:
    """
    lst.sort(key=lambda x: x[0])
    lst.sort(key=lambda x: x[0], reverse=True)
    return lst


def isSolved(lst):
    """

    :param lst:
    :return:
    """
    soln = []
    for i in range(len(lst)):
        obj = lst[i]
        if obj[0] == 28:
            soln.append(obj)

    if len(soln) > 0:
        return True, soln
    else:
        return False, soln


def pairwise(lstitm):
    """

    :param lstitm:
    :return:
    """
    a = iter(lstitm)
    return zip(a, a)


# def printChessBoard(self, chessboard):
#     """
#     Prints the chess board with 8 queens
#     :return:
#     """
#
#     # places the 8 - Queen on the board
#     for i in range(len(chessboard)):
#         MAT[chessboard[i] - 1][i] = chessboard[i]
#
#     string = ""
#     for row in range(len(MAT)):
#         for col in range(len(MAT)):
#             if MAT[row][col] == 0:
#                 string += str(" |_| ")
#             else:
#                 string += str(" ") + str(MAT[row][col]) + str(" ")
#         string += "\n"
#
#     print(string)




