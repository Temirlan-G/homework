class Factorial:

    def factorial(self, num):
        if num == 1:
            return num
        else:
            return self.factorial(num - 1) * num


fct = Factorial()
print(fct.factorial(4))
