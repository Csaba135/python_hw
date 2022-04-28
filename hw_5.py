class Fraction:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor
    def __str__(self):
        return "numarator/numitor"
    def __add__(self):
        return self.numitor+self.numarator
    def __sub__(self):
        return self.numarator-self.numitor
    def invert(self):
        return f'{self.numitor} {self.numarator}'

a=Fraction(5,6)
print(a.__add__())
print(a.__sub__())
print(a.invert())
