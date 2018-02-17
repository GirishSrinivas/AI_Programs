from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import math


def visualize_data(X, y, label):
    """

    :param X:
    :param y:
    :param label:
    :return:
    """
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
    plt.xlabel('Attribute-1')
    plt.ylabel('Attribute-1')
    plt.title(label)
    plt.show()


def svm_trainer(X, y, test, test_ids):
    """

    :param X:
    :param y:
    :param test:
    :param test_ids:
    :return:
    """
    shp = test.shape
    print("shape: ", shp)

    print("\n\nUsing Linear Kernel")
    clf = SVC(kernel='linear', C=1, gamma=0.7)
    clf.fit(X, y)
    test_true, test_predict = test_ids, clf.predict(test)

    print("True Classes: ", test_true)
    print("Predicted Classes: ", test_predict)

    report = classification_report(test_true, test_predict)
    cmatrix = confusion_matrix(test_true, test_predict)

    print('\nConfusion matrix:')
    print(cmatrix)

    print('\nClassification Report:')
    print(report)

    mcc = correlation_coefficient(cmatrix)
    print("\nCorrelation Coefficient: ", mcc)

    plot_predection(test, test_predict, 'SVM - Linear Kernel')
    # plot_confusion_matrix(cmatrix)


def neural_network(X, y, test, test_ids):
    """

    :param X:
    :param y:
    :param test:
    :param test_ids:
    :return:
    """
    print("\n\nusing Multi-layer Perceptron")

    scaler = StandardScaler()
    scaler.fit(X)
    scaler.fit(test)
    X_train = scaler.transform(X)
    X_test = scaler.transform(test)

    mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30), max_iter=500)

    mlp.fit(X_train, y)

    test_true, test_predict = test_ids, mlp.predict(X_test)

    print("True Classes: ", test_true)
    print("Predicted Classes: ", test_predict)

    report = classification_report(test_true, test_predict)
    cmatrix = confusion_matrix(test_true, test_predict)

    print('\nConfusion matrix:')
    print(cmatrix)

    print('\nClassification Report:')
    print(report)

    mcc = correlation_coefficient(cmatrix)
    print("\nCorrelation Coefficient: ", mcc)

    plot_predection(test, test_predict, 'Multi-layer Perceptron')

    # plot_confusion_matrix(cmatrix)


def Polysvm_trainer(X, y, test, test_ids):
    """

    :param X:
    :param y:
    :param test:
    :param test_ids:
    :return:
    """
    shp = test.shape
    print("shape: ", shp)

    print("\n\nUsing Poly Kernel")
    clf = SVC(kernel='poly', degree=3, C=1)
    clf.fit(X, y)
    test_true, test_predict = test_ids, clf.predict(test)

    print("True Classes: ", test_true)
    print("Predicted Classes: ", test_predict)

    report = classification_report(test_true, test_predict)
    cmatrix = confusion_matrix(test_true, test_predict)

    print('\nConfusion matrix:')
    print(cmatrix)

    print('\nClassification Report:')
    print(report)

    mcc = correlation_coefficient(cmatrix)
    print("\nCorrelation Coefficient: ", mcc)

    plot_predection(test, test_predict, 'SVM - Poly Kernel')

    # plot_confusion_matrix(cmatrix)


def plot_confusion_matrix(cmatrix):
    """

    :param cmatrix:
    :return:
    """
    plt.matshow(cmatrix)
    plt.title('Confusion matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


def correlation_coefficient(cmatrix):
    """

    :param cmatrix:
    :return:
    """
    tp = cmatrix[0][0]
    tn = cmatrix[1][1]
    fp = cmatrix[0][1]
    fn = cmatrix[1][0]

    mcc = ((tp * tn) - (fp * fn)) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

    return mcc


def plot_predection(test, y, label):
    """

    :param test:
    :param y:
    :param label:
    :return:
    """
    features = test[:, :2]
    xf = features[:, 0].reshape(14, 14)
    yf = features[:, 1].reshape(14, 14)

    z = y.reshape(xf.shape)

    plt.subplot(1, 1, 1)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.contourf(xf, yf, z, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.xlabel('Attribute - 1')
    plt.ylabel('Attribute - 2')
    plt.scatter(features[:, 0], features[:, 1], c=y, cmap=plt.cm.coolwarm)
    plt.title(label)
    plt.show()
