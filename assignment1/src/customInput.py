from typing import List, Any, TypeVar
from customException import CustomException

class CustomInput:
    def valudateToInt(self, arr: List[str]) -> List[int]:
        try:
            return [int(num) for num in arr]
        except Exception as e:
            raise CustomException('В вводе есть значение не типа int')

    def validateToDouble(self, arr: List[str]) -> List[float]:
        try:
            return [float(num) for num in arr]
        except Exception as e:
            raise CustomException('В вводе есть значение не типа double')

    def customInput(self, n: int, neededTypeVar: TypeVar) -> List[Any]:
        inputedMsv: List[Str] = []
        while len(inputedMsv) < n:
            inputedMsv = inputedMsv + input().split()
        inputedMsv  = inputedMsv[:n]
        if neededTypeVar == int:
            return  self.valudateToInt(inputedMsv)
        elif neededTypeVar == float:
            return self.validateToDouble(inputedMsv)
        else: return inputedMsv
