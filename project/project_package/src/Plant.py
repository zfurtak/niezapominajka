from datetime import datetime, timedelta
import project_package


class Plant:
    colours = ['r', 'b', 'w']

    def __init__(self, name, species, firstWater=datetime.today().strftime('%Y-%m-%d'), colour='red', room=None,
                 notes="Brak", lastWater=datetime.today().strftime('%Y-%m-%d'), picture=None):
        self.name = name
        self.species = species
        self.firstWater = firstWater
        self.colour = colour
        self.room = room
        self.notes = notes
        self.lastWater = lastWater
        if(picture is not None):
            self.picture = picture
        else:
            self.picture = self.species.getPicture()

    def daysEndured(self):
        return (datetime.today().strftime('%Y-%m-%d') - self.firstWater).days

    def waterNow(self):
        self.lastWater = datetime.today().strftime('%Y-%m-%d')

    def actualizeLastWater(self, lastWater: datetime):
        self.lastWater = datetime.strptime(lastWater, "%Y-%m-%d")

    def changeName(self, name: str):
        self.name = name

    def changeRoom(self, room):
        self.room = room

    def nextWatering(self): #dałam tu str bo nie dzialalo inaczej
        return self.lastWater + str(timedelta(days=self.species.getDaysBetweenWatering()))

    def changeColour(self, colour):
        self.colour = colour

    def changePicture(self, picture):
        self.picture = picture
