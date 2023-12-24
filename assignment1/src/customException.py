class CustomException(Exception):
    message: str
    def __init__(self, message: str):
        self.message = message

    def printErr(self):
        print(self.message, ". Попробуй еше раз, другалек", sep="")