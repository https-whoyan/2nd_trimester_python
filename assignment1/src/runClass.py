import sys
from customException import CustomException


class Run:
    numberOfTask: int = None


    def run(self, msvFunctions):
        try:
            if self.numberOfTask == None:
                numberOfTask: int = int(input("Введите номер задачи: "))
                if numberOfTask < 0 or numberOfTask > 25  and (numberOfTask != 32) and (numberOfTask != 33):
                    raise CustomException("Номер задачи от 1 до 25 (или 32, или 33)...")
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
        except Exception:
            print("Чет походу я внатуре неправильно одно из заданий написал...")
            sys.exit(0)
