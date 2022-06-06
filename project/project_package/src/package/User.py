#!/usr/bin/env python3
from datetime import datetime
from .Level import Level
from .Achievement import Achievement
from .Plant import Plant
from project.project_package.src.database.database import Database

db = Database()
# id, username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source, join_date

#id, username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source, join_date

def load_user(user_data):
    last_dead_plant = datetime.strptime(user_data[3][:10], '%Y-%m-%d')
    join_date = datetime.strptime(user_data[7][:10], '%Y-%m-%d')
    user = User(id=user_data[0], nickname=user_data[1], dark_mode=user_data[5], last_dead_plant=last_dead_plant,
                photo=user_data[6],
                dead_plants=user_data[4], join_date=join_date)

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
        self.last_dead_plant = last_dead_plant
        self.points = points
        self.dead_plants = dead_plants
        self.reminder_time = None
        self.photo = photo

    def set_reminder_time(self, time):
        self.reminder_time = time

    def add_achievement(self, achievement):
        self.level.addAchievement(achievement)
        self.list_of_achievements.append(achievement.name)

    def upgrade_last_dead_plant_date(self):
        data = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        self.last_dead_plant = data
        db.killed_plant(data.strftime('%Y-%m-%d'), self.nickname)

    def get_days_without_dead_plant(self):
        return (datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - self.last_dead_plant).days
