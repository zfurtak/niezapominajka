#!/usr/bin/env python3
from datetime import datetime
from .Level import Level
from .Achievement import Achievement
from .Plant import Plant


class User:

    def __init__(self, nickname):
        self.nickname = nickname
        self.joinDate = datetime.today()
        self.level = Level()
        self.listOfAchievements = []
        self.listOfPlants = []
        self.daysWithApp = 0
        self.daysWithoutDeadPlant = 0

    def addAchievement(self, achievement):
        self.level.addAchievement(achievement)
        self.listOfAchievements.append(achievement.name)

    def addPlant(self, plant):
        self.listOfPlants.append(plant)

    def updateDays(self):
        self.daysWithApp += 1

    def deadPlant(self):
        self.daysWithoutDeadPlant = 0

    def updateDaysWithoutDeadPlant(self):
        self.daysWithoutDeadPlant += 1


