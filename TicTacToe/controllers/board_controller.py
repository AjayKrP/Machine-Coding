from TicTacToe.services.board_service import BoardService

import sys


class BoardController:
    def __init__(self):
        self.boardService = BoardService()

    def generateBoard(self):
        return self.boardService.createBoard().board

    def fillBoard(self, board, x, y, choice):
        if x < 0 or y < 0 or x >= 3 or y >= 3:
            print("Please enter correct cordinate.")
            return

        if board[x][y] is not None:
            curr = board[x][y]
            print(f"Current choice is filled by user {curr.user.name}")
        board[x][y] = choice.choice

        if self.isWinner(board, x, y):
            print(f"winner is {choice.user.name}")
            sys.exit(0)

    def isWinner(self, board, x, y):

        # check rows
        if (board[x][0] and board[x][1] and board[x][2]) and board[x][0] == board[x][1] == board[x][2]:
            return True

        # check cols
        if (board[0][y] and board[1][y] and board[2][y]) and board[0][y] == board[1][y] == board[2][y]:
            return True

        # check diagonals
        if (board[0][0] and board[1][1] and board[2][2]) and board[0][0] == board[1][1] == board[2][2]:
            return True

        if (board[2][0] and board[1][1] and board[0][2]) and board[2][0] == board[1][1] == board[0][2]:
            return True

        if not self.boardService.hasEmptyCell(board):
            print(f"Draw Game!")
            sys.exit(0)

        return False
