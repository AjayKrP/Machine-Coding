from abc import ABC, abstractmethod


class UserServiceInterface(ABC):
    def createUser(self, name):
        pass

    def removeUser(self, name):
        pass
    