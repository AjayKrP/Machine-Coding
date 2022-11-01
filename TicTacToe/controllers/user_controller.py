from TicTacToe.services.user_service import UserService


class UserController:
    def __init__(self):
        self.userService = UserService()

    def enrollUser(self, name):
        return self.userService.createUser(name)

    