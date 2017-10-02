import random as rand
from maxMinFunc import MaxMinClass as mmc
from maxMinFunc import maxMin as mm


def main():
    """
    This is the starting point of execution for maxMin program
    :return:
    """
    while True:
        obj = mmc.MaxMinObj()
        inp = [int(x) for x in input("Enter the values with space: ").split()]
        obj.setPopulationSize(int(input("Population size: ")))
        obj.setSampleSize(int(input("Number of chromosomes to be selected: ")))
        obj.setMutationRate(float(input("Mutation rate (between 0 - 1): ")))
        obj.setIteration(int(input("Number of Iterations (-1 for infinite): ")))

        obj.setConstant(inp[- 1])
        obj.setCoefficients(inp[:- 1])

        print("Press 1. to Maximize the function")
        print("Press 0. to Minimize the function")
        obj.setChoice(int(input("Enter choice: ")))
        res, i = mm.maxmin(obj)
        print("result: ", res)
        # print("Sequence: ", res[0])
        print("Iteration: %d" % i)
        brk = input("Enter 'y' to continue or press any key to exit: ")
        if brk == 'y':
            continue
        else:
            break

    print("Bye... ")


if __name__ == "__main__":
    main()
