from .user_service_interface import UserServiceInterface
from ..models.user import User


class UserService(UserServiceInterface):
    userList = {}
    userCounter = 0

    def createUser(self, name):
        if self.userCounter > 2:
            raise ValueError("User should not be more than 2.")
        if name in self.userList:
            raise ValueError("Name already exist.")
        self.userList[name] = User(name)
        self.userCounter += 1

        return self.userList[name]

    def removeUser(self, name):
        if name not in self.userList:
            raise ValueError("Name does not exist.")
        del self.userList[name]
        self.userList -= 1

    def getUserCounter(self):
        return self.userCounter
