import TicTacToe.services.choice_service as cc

class ChoiceController:
    def __init__(self):
        self.choiceService = cc.ChoiceService()

    def getChoicePerUser(self, choice, user):
        return self.choiceService.createChoice(choice, user)
