class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, mnim):
        z1 = self.a + mnim.a
        z2 = self.b + mnim.b
        return Complex(z1, z2)

    def __sub__(self, mnim):
        z1 = self.a - mnim.a
        z2 = self.b - mnim.b
        return Complex(z1, z2)

    def __mul__(self, mnim):
        z1 = self.a * mnim.a - self.b * mnim.b
        z2 = self.a * mnim.b + mnim.a * self.b
        return Complex(z1, z2)

    def __truediv__(self, mnim):
        z1 = (self.a * mnim.a + self.b * mnim.b) / (mnim.a**2 + mnim.b**2)
        z2 = (self.b * mnim.a - self.a * mnim.b) / (mnim.a**2 + mnim.b**2)
        return Complex(z1, z2)

    def __str__(self):
        return str(self.a) + ' + ' + str(self.b) + 'i'


cmplx = Complex(5, 3)
cmplx1 = Complex(8, 2)
cmplx2 = Complex(7, 3)
cmplx3 = Complex(6, 2)


add = cmplx + cmplx1
print(add, '  add z1=5+3, z2=8+2')
sub = cmplx - cmplx1
print(sub, ' subtract z1=5+3, z2=8+2')
mul = cmplx * cmplx1
print(mul, ' multiply z1=5+3, z2=8+2')
div = cmplx2 / cmplx3
print(div, ' divide z1=7+3, z2=6+2')

print('--------------------------------------------------')

add1 = cmplx + cmplx1 + cmplx3 + cmplx3
print(add1)
sub1 = cmplx - cmplx1 - cmplx2 - cmplx3
print(sub1)
mul1 = cmplx * cmplx1 * cmplx2 * cmplx3
print(mul1)
div1 = cmplx / cmplx1 / cmplx2 / cmplx3
print(div1)
