#!/usr/bin/env python3
from datetime import datetime
from .Level import Level
from .Achievement import Achievement
from .Plant import Plant


class User:

    def __init__(self, nickname):
        self.nickname = nickname
        self.join_date = datetime.today()
        self.level = Level()
        self.list_of_achievements = []
        self.list_of_plants = []
        self.days_with_app = 0
        self.days_without_dead_plant = 0
        self.reminder_time = None
        self.photo = "GUI/images/test.jpg"

    def set_reminder_time(self, time):
        self.reminder_time = time

    def addAchievement(self, achievement):
        self.level.addAchievement(achievement)
        self.list_of_achievements.append(achievement.name)

    def addPlant(self, plant):
        self.list_of_plants.append(plant)

    def updateDays(self):
        self.days_with_app += 1

    def deadPlant(self):
        self.days_without_dead_plant = 0

    def updateDaysWithoutDeadPlant(self):
        self.days_without_dead_plant += 1


