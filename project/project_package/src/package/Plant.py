from datetime import datetime, timedelta
from unittest import case


def load_plant(plant_data, species):
    sp = species[0]
    print(plant_data)
    for s in species:
        name = plant_data[2]
        if "Gatunek: " in plant_data[2]:
            name = name[9:]
        if s.name == name:
            sp = s

    first_water = datetime.strptime(plant_data[3][:2] + '/' + plant_data[3][3:5] + '/' + plant_data[3][6:8], '%d/%m/%y')
    last_water = datetime.strptime(plant_data[6][:2] + '/' + plant_data[6][3:5] + '/' + plant_data[6][6:8], '%d/%m/%y')
    return Plant(plant_data[1], sp, first_water, plant_data[4], plant_data[5], last_water, plant_data[7])


def plants_to_water_daily(day, plant_list):
    plants_to_water = []
    for p in plant_list:
        if p.tillNextWater() == day % p.species.days_between_watering:
            plants_to_water.append(p)
    return plants_to_water


def plantsToWater(plant_list):
    td = datetime.today()
    plant_list.sort(key=lambda x: td - x.last_water)
    return plant_list


class Plant:
    def __init__(self, name, species, first_water=datetime.today(), room=None,
                 notes="Brak", last_water=datetime.today(), picture=None):
        self.name = name
        self.species = species
        self.first_water = first_water
        self.room = room
        self.notes = notes
        self.last_water = last_water
        self.picture = picture
        # if picture is not None:
        #     self.picture = picture
        # else:
        #     self.picture = self.species.getPicture()

    def days_endured(self):
        return (datetime.today() - self.first_water).days

    def water_now(self):
        self.last_water = datetime.today()

    def actualize_last_water(self, lastWater: datetime):
        self.last_water = datetime.strptime(lastWater, "%Y-%m-%d")

    def change_name(self, name: str):
        self.name = name

    def change_room(self, room):
        self.room = room

    def next_watering(self):  # dałam tu str bo nie dzialalo inaczej
        return self.last_water + timedelta(days=self.species.getDaysBetweenWatering())


    def changePicture(self, picture):
        self.picture = picture

    def stringFirstWater(self):
        return self.first_water.strftime('%Y-%m-%d')

    def stringLastWater(self):
        return self.last_water.strftime('%Y-%m-%d')

    def tillNextWater(self):
        nextW = self.next_watering()
        return (nextW - datetime.today()).days
