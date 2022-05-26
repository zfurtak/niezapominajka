from datetime import datetime, timedelta
from unittest import case

def loadPlant(plantData, species):
    sp = species[0]

    for s in species:
        if s.name == plantData[2]:
            sp = s
    firstWater = datetime.strptime(plantData[3][:2] + '/' + plantData[3][3:5] + '/' + plantData[3][6:8], '%d/%m/%y')
    lastWater = datetime.strptime(plantData[7][:2] + '/' + plantData[7][3:5] + '/' + plantData[7][6:8], '%d/%m/%y')
    return Plant(plantData[1], sp, firstWater, plantData[4], plantData[5], plantData[6], lastWater, plantData[8])


class Plant:
    def __init__(self, name, species, firstWater=datetime.today(), color='red', room=None,
                 notes="Brak", lastWater=datetime.today(), picture=None):
        self.name = name
        self.species = species
        self.firstWater = firstWater
        self.color = color
        self.room = room
        self.notes = notes
        self.lastWater = lastWater
        self.picture = picture
        # if picture is not None:
        #     self.picture = picture
        # else:
        #     self.picture = self.species.getPicture()


    def daysEndured(self):
        return (datetime.today() - self.firstWater).days

    def waterNow(self):
        self.lastWater = datetime.today()

    def actualizeLastWater(self, lastWater: datetime):
        self.lastWater = datetime.strptime(lastWater, "%Y-%m-%d")

    def changeName(self, name: str):
        self.name = name

    def changeRoom(self, room):
        self.room = room

    def nextWatering(self): #dałam tu str bo nie dzialalo inaczej
        print(self.lastWater, "+", timedelta(days=self.species.getDaysBetweenWatering()))
        return self.lastWater + timedelta(days=self.species.getDaysBetweenWatering())

    def changeColour(self, colour):
        self.colour = colour

    def changePicture(self, picture):
        self.picture = picture

    def stringFirstWater(self):
        return self.firstWater.strftime('%Y-%m-%d')

    def stringLastWater(self):
        return self.lastWater.strftime('%Y-%m-%d')

    def tillNextWater(self):
        print("sth")
        nextW = self.nextWatering()
        print("->", nextW, "-", datetime.today())
        return (nextW - datetime.today()).days

    def plantsToWater(self, plantlist):
        # plantlist = sorted(plantlist, key=lambda x: x.tillNextWater)
        td = datetime.today()
        plantlist.sort(key=lambda x: td - x.lastWater)
        return plantlist

    def plantsToWaterOnDay(self, day, plant_list):
        print("START")
        plantsTowater = []
        for p in plant_list:
            print("*", p.tillNextWater())
            if p.tillNextWater() == day:
                plantsTowater.append(p)
        return plantsTowater

