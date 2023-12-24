from customInput import CustomInput
from customException import CustomException
import math

customInput = CustomInput()

def task1():
    a: int = customInput.customInput(1, float)[0]
    print("Периметр: {}, площадь: {}".format(4 * a, a  * a))


def task2():
    a, b = customInput.customInput(2, float)
    print("Периметр: {}, площадь: {}".format(2 * a + 2 * b, a * b))

def task3():
    a, b, c = customInput.customInput(3, float)
    v: float = a * b * c
    print("Обьем: {}".format(v))


def task4():
        a, b = customInput.customInput(2, float)
        sqrtAB: float = (a * b) ** 0.5
        print("Корень: {}".format(sqrtAB))


def task5():
    a, b = customInput.customInput(2, float)
    c: float = (a ** 2 + b ** 2) ** 0.5
    p: float = a  + b + c
    print("Сторона с: {}, перимерт: {}".format(c, p))


def task6():
    a, b, c = customInput.customInput(3, float)
    a, b, c = b, c, a
    print("Числа: {}, {}, {}".format(a, b, c))


def task7():
    a, b, c = customInput.customInput(3, float)
    a, b, c = c, a, b
    print("Числа: {}, {}, {}".format(a, b, c))


def task8():
    x: float = customInput.customInput(1, float)[0]
    y: float = 3 * (x ** 6) - 6 * (x ** 2) + 7
    print("y: {}".format(y))


def task9():
    x: float = customInput.customInput(1, float)[0]
    y1: float = 4 * ((x - 3) ** 6)
    y2: float = 7 * ((x - 2) ** 3)
    y: float = y1 - y2 + 2
    print("y: {}".format(y))


def task10():
    name: str = " ".join(customInput.customInput(2, str))
    print("Асыл лох, а имя: {}".format(name))


def task11():
    num: int = customInput.customInput(1, str)[0]
    try:
        testIntNum = int(num)
    except ValueError:
        raise CustomException("Тебя просят число ввести, а не строку")
    if len(num) != 4 or num[0] == "0":
        raise CustomException("Ты плохое число ввел. Либо не 4-х значное, либо в начале 0))")
    sumOfDigits: int = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
    print("Сумма цифр: {}".format(sumOfDigits))


def task12():
    n: int = customInput.customInput(1,int)[0]
    D: int = n // 86400
    n %= 86400
    HH: int = n // 3600
    n %= 3600
    MM: int = n // 60
    n %= 60
    print(f"Вот твое число {D}:{HH:02}:{MM:02}:{n:02}")


def task13():
    k: int = customInput.customInput(1, int)[0]
    if k < 1 or k > 365: raise CustomException("Рэнж 1...365")
    print("Номер дня в неделе: {}".format(n % 7 + 1))


def task14():
    a, b, c = customInput.customInput(3, int)
    a, b, c = sorted([a, b, c])
    print("Числа: {}, {}, {}".format(a, b, c))


def task15():
    a, b, c, d = customInput.customInput(4, float)
    summaRotEbal : float = a + b + c + d
    diff: float = max([a, b, c, d]) - min([a, b, c, d])
    proiz: float = a * b * c * d
    print("Cумма, разница, и произведение: {}, {}, {}".format(summaRotEbal, diff, proiz))


def task16():
    x, y = customInput.customInput(2, float)
    absX, absY = math.fabs(x), math.fabs(y)
    proizXY: float = math.fabs(x * y)
    ans: float = (absX + absY) / (1 + proizXY)
    print("Ответ: {}".format(ans))


def task17():
    a = customInput.customInput(1, float)
    v: float = a * a * a
    summaBokovoiRotIbal: float = a * e
    print("Обьем: {}, площадь боковой: {}".format(v, summaBokovoiRotIbal))


def task18():
    a, b = customInput.customInput(2, float)
    arifm: float = (a + b) / 2
    geom: float = (a * b) ** 0.5
    print("Арифметическое: {}, геометрическое: {}".format(arifm, geom))


def task19():
    x, y = customInput.customInput(2, float)
    sverhuRotIbal: float = (math.fabs(x - 1)  ** 0.5) - math.fabs(y) ** (1 /3)
    snizy: float = 1.0 + (x * x) / 2 + (y * y) / 4
    ans: float = sverhuRotIbal / snizy
    print("Ответ: {}".format(ans))


def task20():
    x, y = customInput.customInput(2, float)
    sverhuRotIbal: float = (math.fabs(x - 1)  ** 0.5) - math.fabs(y) ** (1 /3)
    snizy: float = 1.0 + (x * x) / 2 + (y * y) / 4
    a: float = sverhuRotIbal / snizy
    b = x * (math.atan(z) + math.e ** (-(x + 3)))
    print("Ответы: {}, {}".format(a, b))


def task21():
    x, y, z = customInput.customInput(3, float)
    a: float = ( (3+math.e**(y-1))/(1+x**2*abs(y-tan(z))))
    b: float = (1 + math.fabs(y-x) + (y-x)**2/2 + math.fabs(y-x)**3/3)
    print("Ответы: {}, {}".format(a, b))


def task22():
    x, y, z = customInput.customInput(3, float)
    a: float =  (1+y)*((x+y/(x**2+4))/(math.e**(-x-2)+1/(x**2+4)))
    b: float = (1 + math.fabs(y-x) + (y-x)**2/2 + math.fabs(y-x)**3/3)
    print("Ответы: {}, {}".format(a, b))


def task23():
    x, y, z = customInput.customInput(3, float)
    a: float = ((2 * math.cos(x - math.pi / 6)) / (0.5 + math.sin(y) ** 2))
    b: float = 1 + (x ** 2 / (3 + z ** 2 / 5))
    print("Ответы: {}, {}".format(a, b))


def task24():
    x, y, z = customInput.customInput(3, float)
    a: float = ((1 + math.sin(x + y) ** 2) / (2 + math.fabs(x - 2 * x / (1 + x ** 2 * y ** 2)))) + x
    b: float = math.cos(math.atan(1 / z)) ** 2
    print("Ответы: {}, {}".format(a, b))


def task25():
    x, y, z = customInput.customInput(3, float)
    a: float = math.log(math.fabs((y - x ** 0.5) * (x - (y  / (z + x * x + 4)))), math.e)
    b: float = x - (x**2/math.factorial(3) + x**5/math.factorial(5))
    print("Ответы: {}, {}".format(a, b))


def task32():
    x1, y1, x2, y2 = customInput.customInput(4, float)
    ans: float = ((x2 - x1) ** 2  + (y2 - y1) ** 2) ** 0.5
    print("Ответ: {}".format(ans))


def task33():
    x1, y1, x2, y2, x3, y3 = customInput.customInput(6, float)
    st1: float =  ((x2 - x1) ** 2  + (y2 - y1) ** 2) ** 0.5
    st2: float = ((x3 - x2) ** 2  + (y3 - y2) ** 2) ** 0.5
    st3: float =  ((x3 - x1) ** 2  + (y3 - y1) ** 2) ** 0.5
    p: float = st1 + st2 + st3
    print("Ответ: {}".format(p))