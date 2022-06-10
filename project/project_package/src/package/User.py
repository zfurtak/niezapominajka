#!/usr/bin/env python3
from datetime import datetime
from .Level import Level
from .Achievement import Achievement
from .Plant import Plant
from project.project_package.src.database.database import Database

db = Database()


def load_user(user_data, notification):
    last_dead_plant = datetime.strptime(user_data[3][:10], '%Y-%m-%d')
    join_date = datetime.strptime(user_data[7][:10], '%Y-%m-%d')
    print(notification)
    if notification is None:
        notification = ('12:00', )
        db.create_user_notification(user_data[1], '12:00')
    user = User(id=user_data[0], nickname=user_data[1], dark_mode=user_data[5], last_dead_plant=last_dead_plant,
                photo=user_data[6],
                dead_plants=user_data[4], join_date=join_date, points=user_data[8])
    user.set_reminder_db_time(notification)
    return user


class User:
    def __init__(self, id, nickname, join_date=datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
                 dark_mode=0, list_of_achievements=None,
                 last_dead_plant=datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
                 photo="images/users/default_avatar.png", points=0, dead_plants=0):
        if list_of_achievements is None:
            list_of_achievements = []
        self.id = id
        self.nickname = nickname
        self.join_date = join_date
        self.level = Level(points)
        self.dark_mode = dark_mode
        self.list_of_achievements = list_of_achievements
        self.last_dead_plant = last_dead_plant
        self.dead_plants = dead_plants
        self.reminder_time = None
        self.photo = photo

    def set_reminder_db_time(self, time):
        d_time = datetime.strptime(time[0], '%H:%M').time()
        self.reminder_time = d_time

    def set_reminder_time(self, time):
        self.reminder_time = time

    def add_achievement(self, achievement):
        self.level.add_achievement(achievement)
        self.list_of_achievements.append(achievement.name)

    def upgrade_last_dead_plant_date(self):
        data = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        self.last_dead_plant = data
        db.killed_plant(data.strftime('%Y-%m-%d'), self.nickname)

    def get_days_without_dead_plant(self):
        return (datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - self.last_dead_plant).days

    def earn_xp(self, plants_no):
        #wzór na level
        points_earned = max(1, self.get_days_without_dead_plant()) * max(1, plants_no)
        print(points_earned)
        self.level.earn_points(points_earned)
        db.upgrade_points(self.nickname, self.level.current_points)
        self.level.check_points()
