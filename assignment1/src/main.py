from customException import CustomException
from tasks import customInput
import importlib
import sys


class Run:
    numberOfTask: int = None


    def run(self, msvFunctions):
        try:
            if self.numberOfTask == None:
                numberOfTask: int = int(input("Введите номер задачи: "))
                if (numberOfTask < 0 or numberOfTask > 25) and numberOfTask != 32 and numberOfTask != 33:
                    raise CustomException("Номер задачи от 1 до 25 (или 32/33) ...")
                if numberOfTask == 32 or numberOfTask == 33: numberOfTask -= 6
                self.numberOfTask = numberOfTask
            func = msvFunctions[ self.numberOfTask - 1]
            func()
            isException = False
        except ValueError:
            raise CustomException("Номер задачи - это номер, а не число.")
        except CustomException as e:
            raise e
        except ZeroDivisionError:
            CustomException("Другалек на ноль делит")
        except Exception as e:
            print("Чет походу я внатуре неправильно одно из заданий написал ;(...")
            print(e.__class__.__name__)
            sys.exit(0)


def returnMsvOfFunction():
    file_name = "tasks"
    module = importlib.import_module(file_name)
    function_list = [getattr(module, f"task{i}") for i in range(1, 26)]
    task32_33 = [getattr(module, f"task{i}") for i in range(32,34)]
    return  function_list + task32_33


if __name__ == '__main__':
    msvFunctions = returnMsvOfFunction()
    countOfCheckedTasks: int = 0
    try:
        print("Сколько задач хочешь проверить? Число вводи", end=" ")
        countOfCheckedTasks = customInput.customInput(1, int)[0]
    except CustomException as err:
        err.printErr()
    except KeyboardInterrupt:
        print("Добил бы выполнение программы...")
    for _ in range(countOfCheckedTasks):
        isException: bool = True
        runObj = Run()
        while isException:
            try:
                runObj.run(msvFunctions)
                isException = False
            except CustomException as err:
                err.printErr()
            except KeyboardInterrupt:
                print("Добил бы выполнение программы...")
                isException = False