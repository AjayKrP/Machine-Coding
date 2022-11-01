#!/usr/bin/env python3

from controllers.choice_controller import ChoiceController
from controllers.board_controller import BoardController
from controllers.user_controller import UserController

if __name__ == "__main__":
    userController = UserController()
    choiceController = ChoiceController()
    boardController = BoardController()

    user1 = userController.enrollUser("ajay")
    user2 = userController.enrollUser("deepak")
    userMapping = {0: user1, 1: user2}
    board = boardController.generateBoard()
    idx = 0
    while True:
        x = int(input('Enter x'))
        y = int(input("Enter y"))
        choice = input("Enter choice")
        while choice not in ["0", "x"]:
            choice = input("Enter Correct choice(0/x)")
        if idx % 2 == 0:
            boardController.fillBoard(board, x, y, choiceController.getChoicePerUser(choice, user1))
        else:
            boardController.fillBoard(board, x, y, choiceController.getChoicePerUser(choice, user2))
        
        idx += 1
    


        