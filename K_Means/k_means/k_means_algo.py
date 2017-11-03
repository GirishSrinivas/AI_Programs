from k_means import crimeEntity as c
from k_means import centroid as cdt
import random as rand
import math
import time
import csv


def readData():
    """

    :return:
    """
    cnt = 0
    data = []

    with open("hw3-crime_data.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if cnt > 0:
                crime = c.Crime()
                crime.setState(row[0])
                crime.setMurder(float(row[2]))
                crime.setAssult(int(row[3]))
                crime.setPop(int(row[4]))
                crime.setRape(float(row[5]))

                data.append(crime)
            cnt += 1

    return data


def printData(data):
    for obj in data:
        # print("%s, %f, %d, %d, %f " % (obj.getState(), obj.getMurder(), obj.getAssult(), obj.getPop(), obj.getRape()))
        print("%s, %f" % (obj.getState(), obj.getDist()))


def printCentroid(centroid):
    for obj in centroid:
        print("%f, %d, %d, %f" % (obj.getA(), obj.getB(), obj.getC(), obj.getD()))


def printDistanceMatrix(distmat):
    for obj in distmat:
        lst = distmat[obj][:-1]
        print(obj, lst)
        # print(len(distmat[obj]))
        print("Min dist is %f in index %d" % (min(lst), lst.index(min(lst))))


def getDistortion(data):
    dist = 0

    for obj in data:
        dist += obj.getDist()
    return dist / len(data)


def cmp(obj1, obj2):

    size = len(obj1)
    result = True

    for i in range(size):
        if obj1[i] != obj2[i]:
            result = False

    return result


def kmeans(data, centroid):
    """

    :param data:
    :param centroid:
    :return:
    """
    cnt = 1
    while(True):
        distmat = calculateDist(data, centroid)
        cent = calculateCentroid(distmat, centroid)

        oldcent = centroid
        centroid = cent
        newcent = cent
        
        res = cmp(oldcent, newcent)

        if res:
            # print("\nOld Centroid values are:")
            # printCentroid(oldcent)

            # print("\nNew Centroid values are: ")
            # printCentroid(newcent)
            break
        cnt += 1
    print("Total iteration: %d" % cnt)


def calculateDist(data, centroid):
    """

    :param data:
    :param centroid:
    :return:
    """
    distmat = {}

    for dataobj in data:

        totaldist = list()

        for centobj in centroid:
            dist = math.sqrt(math.pow((centobj.getA() - dataobj.getMurder()), 2) +
                             math.pow((centobj.getB() - dataobj.getAssult()), 2) +
                             math.pow((centobj.getC() - dataobj.getPop()), 2) +
                             math.pow((centobj.getD() - dataobj.getRape()), 2))

            totaldist.append(round(dist, 2))
        totaldist.append(dataobj)
        distmat[dataobj.getState()] = totaldist

    # printDistanceMatrix(distmat)
    return distmat


def calculateCentroid(distmat, centroid):
    """

    :param distmat:
    :param centroid:
    :return:
    """
    csize = len(centroid)

    newcentroid = []

    cent = [list() for _ in range(csize)]

    for obj in distmat:
        lst = distmat[obj][:-1]
        ob = distmat[obj][-1]
        mindist = min(lst)
        index = lst.index(mindist)
        ob.setDist(mindist)
        cent[index].append(ob)

    for i in range(len(cent)):
        # print("Length of centroid %d: %d" % (i, len(cent[i])))
        a = 0
        b = 0
        c = 0
        d = 0

        for j in range(len(cent[i])):
            a += cent[i][j].getMurder()
            b += cent[i][j].getAssult()
            c += cent[i][j].getPop()
            d += cent[i][j].getRape()

        newcent = cdt.Centroid()

        newcent.setA(round(a / len(cent[i]), 2))
        newcent.setB(round(b / len(cent[i]), 2))
        newcent.setC(round(c / len(cent[i]), 2))
        newcent.setD(round(d / len(cent[i]), 2))

        newcentroid.append(newcent)

    return newcentroid


def driver():
    """

    :return:
    """
    data = readData()
    size = len(data)

    # print("Length of data %d" % len(data))

    k = int(input("Enter the value of K: "))
    sample = rand.sample(range(0, size), k)
    # print(sample)

    rand_centroid = []
    centroid = []

    for i in range(len(sample)):
        obj = data[sample[i]]
        rand_centroid.append(obj)
        midpoint = cdt.Centroid()
        midpoint.setA(obj.getMurder())
        midpoint.setB(obj.getAssult())
        midpoint.setC(obj.getPop())
        midpoint.setD(obj.getRape())

        centroid.append(midpoint)

    start = time.time()

    kmeans(data, centroid)
    end = time.time()

    total = end - start

    distortion = getDistortion(data)

    print("Total execution time: %f" % total)

    print("Distortion: %f" % distortion)
