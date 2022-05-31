class Achievement:

    def __init__(self, name, points, description):
        self.name = name
        self.points = points
        self.description = description

    def change_name(self, name):
        self.name = name

    def change_points(self, points):
        self.points = points

    def change_description(self, description):
        self.description = description
