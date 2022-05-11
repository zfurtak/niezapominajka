from .Achievement import Achievement


class Level:
    lvlPoints = [0, 10, 20, 30]
    names = ["brak", "Początkujący podlewacz", "Użytkownik konewki", "Dawca deszczu"]

    def __init__(self):
        self.value = 1
        self.currentPoints = 0
        self.name = self.names[1]

    def updateLevel(self):
        self.value += 1
        self.name = self.names[self.value]

    def checkPoints(self):
        if self.currentPoints >= self.lvlPoints[self.value]:
            self.currentPoints -= self.lvlPoints[self.value]
            self.updateLevel()

    def addAchievement(self, achievement):
        self.currentPoints += achievement.points
        self.checkPoints()