import random as rand
from maxMinFunc import MaxMinClass as mmc


def generateChromosome(obj):
    """

    :return:
    """
    chromosome = rand.sample(range(-abs(obj.getConstant() - 1), abs(obj.getConstant() - 1)), len(obj.getCoefficients()))
    return chromosome


def generatePopulation(obj):
    """

    :return:
    """
    population = [mmc.MaxMinObj() for i in range(obj.getPopulationSize())]

    for i in range(obj.getPopulationSize()):
        population[i].setSequence(generateChromosome(obj))
        population[i].setFitness(generateFitness(obj, population[i].getSequence()))
    return population


def generateFitness(obj, this):
    """

    :param obj:
    :param this:
    :return:
    """
    if obj.getChoice() == 1:
        fitness = maxFitness(obj, this)
    else:
        fitness = minFitness(obj, this)
    return fitness


def maxFitness(obj, this):
    """
    max = -|6a + 4b + 3c +5d| + 50

    :param this:
    :param obj:
    :return:
    """
    c = obj.getCoefficients()
    # print(this)
    # print(c)
    val = 0

    for i in range(len(c)):
        val += (c[i] * this[i])

    mx = -abs(val) + obj.getConstant()
    return mx


def minFitness(obj, this):
    """
    min = |6a + 4b + 3c +5d| - 50

    :param this:
    :param obj:
    :return:
    """
    c = obj.getCoefficients()

    val = 0
    for i in range(len(c)):
        val += (c[i] * this[i])

    mn = abs(val) - obj.getConstant()
    return mn


def asort(lst):
    """

    :param lst:
    :return:
    """
    lst.sort(key=lambda x: x[1])
    return lst


def dsort(lst):
    """

    :param lst:
    :return:
    """
    lst.sort(key=lambda x: x[1])
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst


def singlePointCrossover(obj, parent1, parent2):
    """

    :param obj:
    :param parent1:
    :param parent2:
    :return:
    """
    child = mmc.MaxMinObj()

    size = len(parent1)
    splice = int(rand.uniform(0, size))

    sequence = parent1[0: splice]
    sequence += parent2[splice:]

    new_sequenc = mutation(obj, sequence)

    child.setSequence(new_sequenc)
    child.setFitness((generateFitness(obj, new_sequenc)))
    return child


def mutation(obj, sequence):
    """

    :param obj:
    :param sequence:
    :return:
    """
    child_rand = rand.uniform(0, 1)
    if obj.getMutationRate() >= child_rand:
        c = int(rand.uniform(0, len(sequence)))
        mutate = int(rand.uniform(-abs(obj.getConstant() - 1), abs(obj.getConstant() - 1)))
        sequence[int(c)] = int(mutate)
    return sequence


def maxmin(obj):
    """

    :return:
    """
    print("\nOUTPUT")
    print("coefficients: ", obj.getCoefficients())
    print("constant: %d" % obj.getConstant())
    print("Population size: %d" % obj.getPopulationSize())
    print("sample size: %d" % obj.getSampleSize())
    print("mutation: %.1f" % obj.getMutationRate())
    print("Iteration: %d" % obj.getIteration())
    # print("choice: ", obj.getChoice())
    if obj.getChoice() == 1:
        print("choice: Maximize Function")
    else:
        print("choice: Minimize Function")

    total_population = generatePopulation(obj)

    new_population = []

    for i in range(len(total_population)):
        new_population.append((total_population[i].getSequence(), total_population[i].getFitness()))

    res = None
    itern = 0

    if obj.getIteration() < 0:
        upperlimit = 10000
    else:
        upperlimit = obj.getIteration()

    while itern < upperlimit:
        if obj.getChoice() == 1:
            sortedList = dsort(new_population)
        else:
            sortedList = asort(new_population)

        sample_list = sortedList[:obj.getSampleSize()]

        result, chromosome = isSolved(obj, sortedList)

        if result:
            return chromosome, itern

        rand.shuffle(sample_list)

        for parent1, parent2 in pairwise(sample_list):
            child = singlePointCrossover(obj, list(parent1[0]), list(parent2[0]))
            new_population.append((child.getSequence(), child.getFitness()))
        itern += 1
        res = sortedList[0]

    return res, itern


def isSolved(o, lst):
    """

    :return:
    """
    soln = []
    choice = o.getChoice()

    if choice == 1:
        goal = o.getConstant()
    else:
        goal = -o.getConstant()
    for i in range(len(lst)):
        obj = lst[i]
        if obj[1] == goal:
            soln.append(obj)

    if len(soln) > 0:
        return True, soln
    else:
        return False, soln


def pairwise(lstitm):
    a = iter(lstitm)
    return zip(a, a)
