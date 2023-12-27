import sys
from customException import CustomException


class Run:
    numberOfTask: int = None


    def run(self, msvFunctions):
        try:
            if self.numberOfTask == None:
                numberOfTask: int = int(input("Введите номер задачи (для сетов номера задач от 11 до 20): "))
                if numberOfTask < 0 or numberOfTask > 20:
                    raise CustomException("Номер задачи от 1 до 20...")
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
            print("Чет походу я внатуре неправильно одно из заданий написал...")
            print(e.__class__.__name__)
            sys.exit(0)
