class Math(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, a, b):
        print(a + b)

    def substraction(self, a, b):
        print(a - b)

    def division(self, a, b):
        print(a / b)

    def multiplication(self, a, b):
        print(a * b)


def main():
    math = Math(3, 5)

    math.addition(math.a, math.b)
    math.substraction(math.a, math.b)
    math.division(math.a, math.b)
    math.multiplication(math.a, math.b)


main()