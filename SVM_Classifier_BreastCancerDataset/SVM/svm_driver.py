from svm_package import DataSet as ds
from svm_package import cancer_svm as cs


trainingset = "TrainingData1.csv"
testset = "TestData1.csv"


def main():
    dataobj = ds.DataSet(trainingset)
    testobj = ds.DataSet(testset)

    size = int(input("Enter the size of the features used for classification (5 - 70): "))
    print(size, type(size))

    if size > 0:
        data = dataobj.load_data(size)
        test = testobj.load_data(size)
    else:
        data = dataobj.load_data()
        test = testobj.load_data()

    Xpredicate = data['data']
    targets = data['targets']

    testPerdictor = test['data']
    test_targets = test['targets']

    cs.visualize_data(testPerdictor, test_targets, 'Test Set')
    # cs.visualize_data(Xpredicate, targets, 'Training set')
    cs.svm_trainer(Xpredicate, targets, testPerdictor, test_targets)
    cs.Polysvm_trainer(Xpredicate, targets, testPerdictor, test_targets)
    cs.neural_network(Xpredicate, targets, testPerdictor, test_targets)


if __name__ == "__main__":
    main()
