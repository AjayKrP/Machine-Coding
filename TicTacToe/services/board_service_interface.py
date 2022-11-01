from abc import ABC, abstractmethod


class BoardServiceInterface(ABC):
    def createBoard(self):
        pass

    def resetBoard(self, board):
        pass
