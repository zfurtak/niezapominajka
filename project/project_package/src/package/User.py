#!/usr/bin/env python3
from datetime import datetime
from .Level import Level
from .Achievement import Achievement
from .Plant import Plant
# id, username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source, join_date,
#TODO trzeba dodać join_date, baza dla lvl
# id, username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source

def load_user(user_data):
    last_dead_plant = datetime.strptime(user_data[3], '%d/%m/%y')
    user = User(user_data[0], user_data[1], dark_mode=user_data[5], last_dead_plant=last_dead_plant, photo=user_data[6],
                dead_plants=user_data[4])
    print(user_data[6])
    return user

class User:

    def __init__(self, id, nickname, join_date=datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
                 level=Level(), dark_mode=0, list_of_achievements=None,
                 last_dead_plant=datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
                 photo="GUI/images/test.jpg", points=0, dead_plants=0):
        if list_of_achievements is None:
            list_of_achievements = []
        self.id = id
        self.nickname = nickname
        self.join_date = join_date
        self.level = level
        self.dark_mode = dark_mode
        self.list_of_achievements = list_of_achievements
        self.list_of_plants = []  # to chyba możemy sobie darować???
        self.days_with_app = 0  # to chyba można policzyć w zależności od daty, chyba że to licznik dni w które się logował
        self.last_dead_plant = last_dead_plant
        self.points = points
        self.dead_plants = dead_plants
        # self.days_without_dead_plant = 0  # data chyba lepsza

        self.reminder_time = None
        self.photo = photo

    def set_reminder_time(self, time):
        self.reminder_time = time

    def add_achievement(self, achievement):
        self.level.addAchievement(achievement)
        self.list_of_achievements.append(achievement.name)

    def add_plant(self, plant):
        self.list_of_plants.append(plant)

    def update_days(self):
        self.days_with_app += 1

    def dead_plant(self):
        self.last_dead_plant = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    def get_days_without_dead_plant(self):
         return (datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - self.last_dead_plant).days

    # def update_days_without_dead_plant(self):
    #     self.days_without_dead_plant += 1