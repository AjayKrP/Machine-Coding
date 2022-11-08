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

        if self.isWinner(board, x, y, choice.choice):
            print(f"winner is {choice.user.getName()}")
            sys.exit(0)

    def isWinner(self, board, x, y, choice):
        # check rows
        rows = True
        for i in range(3):
            if board[x][i] != choice:
                rows = False
                break
        if rows:
            return True

        cols = True
        # check cols
        for j in range(3):
            if board[j][y] != choice:
                cols = False
                break
        if cols:
            return True

        d1 = True
        i = j = 0
        # check diagonals
        while i < 3 and j < 3:
            if board[i][j] != choice:
                d1 = False
                break
            i += 1
            j += 1
        if d1:
            return True

        # second diagonal
        d2 = True
        i = 3 - 1
        j = 0
        while i >= 0 and j < 3:
            if board[i][j] != choice:
                d2 = False
                break
            i -= 1
            j += 1
        if d2:
            return True

        if not self.boardService.hasEmptyCell(board):
            print(f"Draw Game!")
            sys.exit(0)

        return False
