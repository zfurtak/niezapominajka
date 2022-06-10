from .Achievement import Achievement


class Level:
    lvl_points = [10, 20, 30, 40, 50, 60]
    names = ["Nieklasyfikowany", "Amator zieleni", "Początkujący podlewacz", "Roślinny zapaleniec",
             "Użytkownik konewki", "Dawca deszczu"]

    def __init__(self, points_value=0):
        self.current_points = points_value
        self.value = self.count_lvl()
        self.name = self.names[0]

    def count_lvl(self):
        return self.current_points // 10

    def update_level(self):
        if self.value < 5:
            self.value += 1
            self.name = self.names[self.value]

    def earn_points(self, value):
        self.current_points += value

    def check_points(self):
        if self.current_points >= self.lvl_points[self.value]:
            # self.current_points -= self.lvl_points[self.value]
            self.update_level()

    def add_achievement(self, achievement):
        self.current_points += achievement.points
        self.check_points()

    def get_progress(self):
        return (self.current_points % 10) * 10
