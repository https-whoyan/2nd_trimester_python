import os
import csv
from utils import getUsersList

from utils import getUsersList

class Auth:
    isLogined: bool = False

    def login(self, username: str, password: str) -> bool:
        registeredUsers: List[Dict] = getUsersList()

        for user in registeredUsers:
            if user['Name'] == username and user['Password'] == password:
                isLogined = True
                return True
        return False

