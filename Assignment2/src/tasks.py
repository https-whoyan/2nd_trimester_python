from typing import List

from customInput import CustomInput
from customException import CustomException
import math

customInput = CustomInput()

def task1():
    a: int = customInput.customInput(1, float)[0]
    if a > 0: a += 1
    else: a -=2
    print("Ответ: {}".format(a))


def task2():
    msv: List[float] = customInput.customInput(3, float)
    counterPol, counterOtr = 0, 0
    for num in msv:
        if num < 0: counterOtr += 1
        elif num > 0: counterPol += 1
    print("Положительные: {}, отрицательные: {}".format(counterPol, counterOtr))
def task3():
    msv: List[int] = customInput.customInput(3, float)
    msv.sort()
    print("Сумма максимальных {}".format(msv[-1] + msv[-2]))

def task4():
        a = customInput.customInput(2, int)[0]
        message: str
        if a % 2 == 0: message = "Число четное"
        else: message = "Число нечетное"
        print(message)


def task5():
    x, y = customInput.customInput(2, float)
    message: str
    if x > 0 and y > 0: message = "Первая четверть"
    if x < 0 and y > 0: message = "Вторая четверть"
    if x < 0 and y < 0: message = "Третья четверть"
    if x > 0 and y < 0: message = "Четвертая четверть"
    print(message)


def task6():
    a, b = customInput.customInput(2, int)
    print("Сумма чисел: {}".format(sum(range(a, b + 1))))


def task7():
    a, b = customInput.customInput(2, int)
    msv: List[int] = range(a, b + 1)
    proiz: int = 1
    for num in msv: proiz *= num
    print("Произведение: {}".format(proiz))


def task8():
    n: int = customInput.customInput(1,int)[0]
    summa: int = sum([i ** 2 for i in range(n, 2 * n + 1)])
    print("Сумма: {}".format(summa))


def task9():
    n: int = customInput.customInput(1,int)[0]
    a: float = customInput.customInput(1, float)[0]
    ans: str = " ".join([str(a  ** x) for x in range(1, n + 1)])
    print("Степени числа {} от 1 до {}: {}".format(a, n, ans))


def task10():
    n: int = customInput.customInput(1, int)[0]
    summa: int = 0
    fact: int = 1
    for i in range(1, n + 1):
        fact  *= i
        summa += fact
    print("Сумма факторивалов: {}".format(summa))
