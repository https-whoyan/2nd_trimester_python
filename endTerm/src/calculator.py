class Arithmetic:
    def __init__(self): pass


    def add(self, a: float, b: float):
        return a + b


    def subtract(self, a: float, b: float):
        return a - b


    def multiply(self, a: float, b: float):
        return a * b


    def divide(self, a: float, b: float):
        if b == 0:
            raise Exception("Cannot Divine By Zero")
        return a / b


class Double(Arithmetic):
    def __init__(self):
        super().__init__()


    def twox(self, digit):
        return self.multiply(digit, 2)


class Even(Arithmetic):
    def __init__(self):
        super().__init__()

    def isEven(self, digit):
        return digit % 2 == 0