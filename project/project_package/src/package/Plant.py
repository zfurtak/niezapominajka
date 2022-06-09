from datetime import datetime, timedelta
from unittest import case
import os


def load_plant(plant_data, species):
    sp = species[0]
    for s in species:
        name = plant_data[2]
        if s.name == name:
            sp = s

    first_water = datetime.strptime(plant_data[3][:2] + '/' + plant_data[3][3:5] + '/' + plant_data[3][6:8], '%d/%m/%y')
    last_water = datetime.strptime(plant_data[6][:2] + '/' + plant_data[6][3:5] + '/' + plant_data[6][6:8], '%d/%m/%y')
    return Plant(plant_data[1], sp, first_water, plant_data[4], plant_data[5], last_water, plant_data[7])


def get_plant(name, plant_list):
    for p in plant_list:
        if p.name == name:
            return p


def plants_to_water_daily(day, plant_list):
    plants_to_water = []
    for p in plant_list:
        if should_water(p, day):
            plants_to_water.append([p, choose_icon(p)])
    sort_by_water_time(plants_to_water)
    return plants_to_water


def should_water(plant, day):
    p_day = plant.tillNextWater()
    if p_day % plant.species.days_between_watering == day % plant.species.days_between_watering:
        if day != 0 or datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) != plant.last_water:
            return True
    if p_day < 0 and day == 0:
        return True
    return False


def choose_icon(plant):
    days = plant.tillNextWater()
    if days >= 0:
        return ""
    if abs(days // plant.species.days_between_watering) == 1:
        return "water-alert"
    else:
        return "skull"


def sort_by_water_time(plant_list):
    td = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    plant_list.sort(key=lambda x: td - x[0].last_water)
    return plant_list


def delete_plant_from_list(plant_list, plant_name):
    for p in range(len(plant_list)):
        if plant_list[p].name == plant_name:
            file = os.path.split(plant_list[p].picture)
            if "species" != file[0][-7:]:
                os.remove(plant_list[p].relative_path)
            plant_list.remove(plant_list[p])
            return


class Plant:
    def __init__(self, name, species, first_water=datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
                 room=None, notes="Brak",
                 last_water=datetime.today().replace(hour=0, minute=0, second=0, microsecond=0), picture=None):
        self.name = name
        self.species = species
        self.first_water = first_water
        self.room = room
        self.notes = notes
        self.last_water = last_water
        self.picture = picture
        self.relative_path = picture


    def days_endured(self):
        return (datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - self.first_water).days

    def water_now(self):
        self.last_water = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    def actualize_last_water(self, lastWater: datetime):
        self.last_water = datetime.strptime(lastWater, "%Y-%m-%d")

    def change_name(self, name: str):
        self.name = name

    def change_room(self, room):
        self.room = room

    def next_watering(self):
        return self.last_water + timedelta(days=self.species.getDaysBetweenWatering())

    def changePicture(self, picture):
        self.picture = picture

    def stringFirstWater(self):
        return self.first_water.strftime('%Y-%m-%d')

    def stringLastWater(self):
        return self.last_water.strftime('%Y-%m-%d')

    def tillNextWater(self):
        nextW = self.next_watering()
        return (nextW - datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)).days
