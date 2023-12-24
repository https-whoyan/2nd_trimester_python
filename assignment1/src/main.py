from customException import CustomException
from tasks import customInput
from runClass import Run
import importlib

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