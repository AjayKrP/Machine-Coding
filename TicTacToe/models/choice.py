class Choice:
    def __init__(self, choice, user):
        self.choice = choice
        self.user = user

    def getUser(self):
        return self.user

    def setUser(self, user):
        self.user = user

    def getChoice(self):
        return self.choice

    def setName(self, choice):
        self.choice = choice
