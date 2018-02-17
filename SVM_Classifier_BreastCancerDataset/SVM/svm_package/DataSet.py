import csv
import numpy as np


class DataSet:
    """

    """
    def __init__(self, dataset_name):
        self.name = dataset_name
        self.attrsize = 0
        self.datasize = 0
        self.data = []
        self.target = []
        self.sample = []
        self.target_names = []

    def setName(self, name):
        self.name = name

    def setAttrSize(self, asize):
        self.attrsize = asize

    def setDataSize(self, dsize):
        self.datasize = dsize

    def getAttrSize(self):
        return self.attrsize

    def getDataSize(self):
        return self.datasize

    def __readData(self):
        """

        :return:
        """
        filename = self.name

        rawdata = open(filename, 'rt')
        reader = csv.reader(rawdata, delimiter=",")
        x = list(reader)
        self.setAttrSize(len(x))

        # print(len(x))

        for i in range(1, self.getAttrSize()):
            key = x[i][0]
            svalue = x[i][1:]
            fvalue = np.array(svalue)
            value = fvalue.astype(np.float)
            self.data.append(value)
            self.sample.append(key)

            if '11A' in key:
                self.target.append(0)
            else:
                self.target.append(1)

        self.target_names.append('Normal')
        self.target_names.append('Cancer')

    def load_data(self, size=None):
        """

        :param size:
        :return:
        """
        self.__readData()
        dataset = dict()
        samples = []

        if size is None:
            dataset['data'] = np.array(self.data)
        else:
            for i in range(len(self.data)):
                samples.append(self.data[i][:size])

            dataset['data'] = np.array(samples)

        dataset['samples'] = np.array(self.sample)
        dataset['targets'] = np.array(self.target)

        return dataset
