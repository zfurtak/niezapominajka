from .Achievement import Achievement


class Level:
    lvl_points = [0, 10, 20, 30]
    names = ["brak", "Początkujący podlewacz", "Użytkownik konewki", "Dawca deszczu"]

    def __init__(self):
        self.value = 1
        self.current_points = 0
        self.name = self.names[1]

    def update_level(self):
        self.value += 1
        self.name = self.names[self.value]

    def check_points(self):
        if self.current_points >= self.lvl_points[self.value]:
            self.current_points -= self.lvl_points[self.value]
            self.update_level()

    def addAchievement(self, achievement):
        self.current_points += achievement.points
        self.check_points()
