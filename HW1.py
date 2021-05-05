class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, addfraction):
        a1 = self.a * addfraction.b + self.b * addfraction.a
        b1 = self.b * addfraction.b
        return Fraction(a1, b1)

    def __sub__(self, subfraction):
        a2 = self.a * subfraction.b - self.b * subfraction.a
        b2 = self.b * subfraction.b
        return Fraction(a2, b2)

    def __mul__(self, mulfraction):
        a3 = self.a * mulfraction.a
        b3 = self.b * mulfraction.b
        return Fraction(a3, b3)

    def __truediv__(self, divfraction):
        a4 = self.a * divfraction.b
        b4 = self.b * divfraction.a
        return Fraction(a4, b4)

    def __str__(self):
        return str(self.a) + '\n' + '-\n' + str(self.b)



f = Fraction(2, 5)
f1 = Fraction(1, 4)

f_add = f + f1
f_sub = f - f1
f_mul = f * f1
f_div = f / f1

print(f_add)
print(f_sub)
print(f_mul)
print(f_div)


