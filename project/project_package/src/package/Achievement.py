
class Achievement:

    def __init__(self, name, points, description):
        self.name = name
        self.points = points
        self.description = description

    def changeName(self, name):
        self.name = name

    def changePoints(self, points):
        self.points = points

    def changeDescription(self, description):
        self.description = description