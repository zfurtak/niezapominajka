from datetime import datetime, timedelta



class Plant:
    def __init__(self, name, species, firstWater=datetime.today(), colour='red', room=None,
                 notes="Brak", lastWater=datetime.today(), picture=None):
        self.name = name
        self.species = species
        self.firstWater = firstWater
        self.colour = colour
        self.room = room
        self.notes = notes
        self.lastWater = lastWater
        if picture is not None:
            self.picture = picture
        else:
            self.picture = self.species.getPicture()


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
        return self.lastWater + timedelta(days=self.species.getDaysBetweenWatering())

    def changeColour(self, colour):
        self.colour = colour

    def changePicture(self, picture):
        self.picture = picture

    def stringFirstWater(self):
        return self.firstWater.strftime('%Y-%m-%d')

    def stringLastWater(self):
        return self.lastWater.strftime('%Y-%m-%d')