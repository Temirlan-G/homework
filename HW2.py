class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, mnim):
        z1 = self.a + mnim.a
        z2 = self.b + mnim.b
        return print(z1,'+', z2,'i')

    def __sub__(self, mnim):
        z1 = self.a - mnim.a
        z2 = self.b - mnim.b
        return print(z1,'+', z2,'i')

    def __mul__(self, mnim):
        z1 = self.a * mnim.a - self.b * mnim.b
        z2 = self.a * mnim.b + mnim.a * self.b
        return print(z1, '+', z2, 'i')

    def __truediv__(self, mnim):
        z1 = (self.a * self.b + mnim.a * mnim.b) / (self.b**2 + mnim.b**2)
        z2 = (mnim.a * self.b - self.a * mnim.b) / (self.b**2 + mnim.b**2)
        return print(z1, '+', z2, 'i')

# self.a = a
# mnim.a = b
# self.b = c
# mnim.b = d

cmpls = Complex(5, 3)
cmpls1 = Complex(8, 2)

cmplx = Complex(-5, -1)
cmplx1 = Complex(-1, 1)

add = cmpls + cmpls1
sub = cmpls - cmpls1
mul = cmpls * cmpls1
div = cmplx / cmplx1


