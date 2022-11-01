from TicTacToe.models.choice import Choice


class ChoiceService:
    def createChoice(self, choice, user):
        return Choice(choice, user)
