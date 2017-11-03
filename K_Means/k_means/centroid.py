class Centroid:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.d = 0.0

    def setA(self, a):
        self.a = a

    def getA(self):
        return self.a

    def setB(self, b):
        self.b = b

    def getB(self):
        return self.b

    def setC(self, c):
        self.c = c

    def getC(self):
        return self.c

    def setD(self, d):
        self.d = d

    def getD(self):
        return self.d

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

    def __ne__(self, other):
        return self.a != other.a and self.b != other.b and self.c != other.c and self.d != other.d
