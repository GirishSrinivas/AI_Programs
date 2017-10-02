from queen8 import geneticAlgorithm as ga


def main():
    """
    This is the main method where the execution begins
    :return:
    """

    population_size = int(input("Population size: "))
    chromosome_size = int(input("Number of chromosomes to be selected: "))
    mutation_rate = float(input("Mutation rate (between 0 - 1): "))
    iteration = int(input("Number of Iterations (-1 for infinite): "))

    population = ga.generatePopulation(population_size)

    g = ga.GeneticAlgorithm(population_size, chromosome_size, population, mutation_rate, iteration)
    # result, itrn = ga.GA(g)

    while True:
        print("Press 1. Single Point Crossover")
        print("Press 2. Two Point Crossover")
        print("Press 3. Cut and Splice Crossover")
        print("Press 4. Uniform Crossover")
        choice = int(input("choice: "))
        result, itrn = ga.GA(g, choice)
        if result is not None:
            print("result: ")
            print(result)
            print("Iterations: %d" % itrn)
        else:
            print("Bad choice")

        brk = input("Enter 'y' to continue or press any key to exit: ")
        if brk == 'y':
            continue
        else:
            break


if __name__ == "__main__":
    main()
