from typing import List, Tuple, Any, Set

from customInput import CustomInput
from customException import CustomException

customInput = CustomInput()

def task1():
    fruits: Tuple[str] = tuple(customInput.customInput(5, str))
    print("Кортеж: {}".format(fruits))


def task2():
    msv: List[int] = range(1, 11)
    mid: int = len(msv) // 2
    ans: List[int] = [int(x) for x in msv[mid - 3: mid + 2]]
    print("Числа: {}".format(ans))


def task3():
    ans: Tuple[float] = tuple(customInput.customInput(3, float))
    print("Числа {}".format(ans))


def task4():
    msv: List[int] = [1, 5, 4, 7, 8, 2]
    print("Изначатальный массив: {}".format(msv))
    elToAdd: int = 4
    msv.append(elToAdd)
    print("Массив после изменений: {}, добавленный элемент: {}".format(msv, elToAdd))
    deletedEl: int = msv.pop(0)
    print("Массив после изменений: {}, удаленный элемент: {}".format(msv, deletedEl))
    msv.sort()
    print("Массив после сортировки: {}".format(msv))


def task5():
    msv: List[int] = [1, 5, 4, 7, 8, 2]
    print("Число, которое чекается на наличие в массиве {}: ".format(msv), end="")
    num: int = customInput.customInput(1, int)[0]
    exists: bool = num in set(msv)
    if exists: print("Число есть в массиве")
    else: print("Число нет в массиве")


def task6():
    msv: List[int] = [1, 5, 4, 7, 8, 2]
    reversedMsv: List[int] = msv.copy()
    reversedMsv.reverse()
    print("Изначальный массив: {}, перевернутый массив: {}".format(msv, reversedMsv))


def task7():
    myTuple: Tuple[Any] = ('abf', 5, True, -34.7)
    el1, el2, el3, el4 = list(myTuple)
    print(f"Кортеж: {myTuple}, а элементы: {el1}, {el2}, {el3}, {el4}")


def task8():
    print("Количество чисел в массиве: ", end="")
    n: int = customInput.customInput(1, int)[0]
    msv: List[float] = customInput.customInput(n, float)
    maxEl, minEl = max(msv), min(msv)
    print(f"Максимум и минимум в массиве {msv} соответсвенно: {maxEl}, {minEl}")


def task9():
    print("Количество чисел в массиве 1: ", end="")
    n: int = customInput.customInput(1, int)[0]
    msv1: List[float] = customInput.customInput(n, float)
    print("Количество чисел в массиве 2: ", end="")
    m: int = customInput.customInput(1, int)[0]
    msv2: List[float] = customInput.customInput(m, float)
    ansMsv: List[float] = msv1 + msv2
    print(f"Конкетированный массивы {msv1} и {msv2}: {ansMsv}")


def task10():
    print("Количество чисел в массиве: ", end="")
    n: int = customInput.customInput(1, int)[0]
    myTuple: Tuple[float] = tuple(customInput.customInput(n, float))
    print(f"Кортеж: {myTuple}")


def task11():
    print("Количество неуникальных чиел в сете: ", end="")
    n: int = customInput.customInput(1, int)[0]
    mySet: Set[float] = set(customInput.customInput(n, float))
    print(f"Сет: {mySet}")


def task12():
    set1: Set[int] = {1, 4, -3, -12, 132}
    set2: Set[int] = {0, 1, -12, 3, 205, -2}
    unionSets: Set[int] = set1 | set2
    inserSets: Set[int] = set1 & set2
    diffSet1: Set[int] = set1.difference(set2)
    simmDiff: Set[int] = set1 ^ set2
    print(f"Сеты: {set1}, {set2}")
    print(f"Обьединение: {unionSets}, пересечение: {inserSets}, разница: {diffSet1}, симметричная разница: {simmDiff}")


def task13():
    print("Введи 3 записи типа key value")
    print("Пример: 5 1")
    msv: List[str] = customInput.customInput(6, str)
    ansDict = dict()
    for i in range(0, 6, 2):
        ansDict[msv[i]] = msv[i + 1]
    print(f"Словарь: {ansDict}")


def task14():
    testDict = {
        "a": 5,
        "b": "asmas",
        "and4": True,
        "53ns": [1, 6],
    }
    print(f"Ключ, наличие которого нужно проверерить в словаре {testDict}: ", end="")
    key: str = customInput.customInput(1, str)[0]
    exists: bool = key in testDict.keys()
    if exists: print("Ключ есть в словаре")
    else: print("Ключа нету в словаре")


def task15():
    print("Введи слово, для которого нужно чекнуть втречаемостьб каждого символа: ", end="")
    word: str = customInput.customInput(1, str)[0].lower()
    dictLetters = dict()
    for letter in set(word):
        dictLetters[letter] = word.count(letter)
    for uniqueLetter in dictLetters.keys():
        print(f"Частота буквы {uniqueLetter}: {dictLetters[uniqueLetter]}")


def task16():
    testSet: Set[Any] = {"5", "abc", "5", "8", "SKew"}
    print(f"Ключ, наличие которого нужно проверерить в сете {testSet}: ", end="")
    key: str = customInput.customInput(1, str)[0]
    exists: bool = key in testSet
    if exists:
        print("Ключ есть в сете")
    else:
        print("Ключа нету в сету")


def task17():
    testDict = {
        "a": 5,
        "b": "asmas",
        "and4": True,
        "53ns": [1, 6],
    }
    print(f"Значение в словаре {testDict}: {testDict.values()}")


def task18():
    dict1 = {
        "a": 5,
        "b": "asmas",
        "and4": True,
        "53ns": [1, 6],
    }
    dict2 = {
        "a": 6,
        "с": False,
        "18": "testValue",
    }
    unionDict = dict1 | dict2
    print(f"Обьединенный словарь из словарей \n{dict1} ::: {dict2}\n{unionDict}")


def task19():
    testDict = {
        "a": 5,
        "b": "asmas",
        "and4": True,
        "53ns": [1, 6],
    }
    print(f"Ключ, который нужно удалить из словаря {testDict}: ", end="")
    key: str = customInput.customInput(1, str)[0]
    if not (key in testDict.keys()): print("Ключа нет в словаре")
    else:
        testDict.pop(key)
        print(f"Измененный словарь: {testDict}")


def task20():
    print("Количество чисел в массиве: ", end="")
    n: int = customInput.customInput(1, int)[0]
    msv: List[int] = customInput.customInput(n, int)
    setMsv: Set[int] = set(msv)
    print(f"Уникальные значения из массива {msv}: {setMsv}")


def task21():
    mySet: Set[float] = set((1.5, -4.8, 17))
    print(mySet)
    mySet2: Set[float] = set(customInput.customInput(5, float))
    interSets: Set[float] = mySet & mySet2
    print(f"Перечесение: {interSets}")
    diffSet1: Set[float] = mySet.difference(mySet2)
    print(f"Разница сета1 к сету2: {diffSet1}")
    isSet1Subset2: bool = mySet.issubset(mySet2)
    if isSet1Subset2: print(f"Да, {mySet} это сабсет {mySet2}")
    else: print(f"Нет, {mySet} не является сабсетом {mySet2}")
    
    for commonEl in interSets: mySet2.remove(commonEl)
    print(f"set2 после удаления общих элементов {interSets}: {mySet2}")