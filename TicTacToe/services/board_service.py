from .board_service_interface import BoardServiceInterface
from ..models.board import Board


class BoardService(BoardServiceInterface):
    def createBoard(self):
        return Board()

    def resetBoard(self, board):
        for i in range(3):
            for j in range(3):
                board[i][j] = None

    def hasEmptyCell(self, board):
        empty = False
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    empty = True
                    break
        return empty
    