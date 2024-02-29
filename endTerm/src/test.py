from calculator import Arithmetic, Double, Even


# Арифметика
arithmeticClass: Arithmetic = Arithmetic()
print("Добавление: ", arithmeticClass.add(7, 3))
print("Разница: ", arithmeticClass.subtract(7, 3))
print("Умножение: ", arithmeticClass.multiply(7, 3))
print("Деленгие: ", arithmeticClass.divide(7, 3))


# Double Арифметика
doubleArifm: Double = Double()
print("Double 5'ки:  ", doubleArifm.twox(5))

# Even класс
EvenAriаfm: Even = Even()
print("45 это четное: ", EvenAriаfm.isEven(45))
print("128 это честное: ", EvenAriаfm.isEven(128))