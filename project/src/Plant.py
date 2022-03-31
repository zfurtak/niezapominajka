from datetime import datetime

class Plant:
    colours = ['r', 'b', 'w']
    def __init__(self, name, species, firstwater = datetime.today().strftime('%Y-%m-%d'), colour = 'red', room = None, notes = "Brak", lastwater = datetime.today().strftime('%Y-%m-%d'), picture = "Basic picture"):
        self.name = name
        self.species = species
        self.firstwater = firstwater
        self.colour = colour
        self.room = room
        self.notes = notes
        self.lastwater = lastwater
        self.picture = picture

    def daysEndured(self):
        return (datetime.today().strftime('%Y-%m-%d') - self.firstwater).days

    def waterNow(self):
        self.lastwater = datetime.today().strftime('%Y-%m-%d')

    def actualizeLastWater(self, lastwater: datetime):
        self.lastwater = datetime.strptime(lastwater, "%Y-%m-%d")

    def changeName(self, name: str):
        self.name = name

    def changeRoom(self, room):
        self.room = room

    def nextWatering(self):
        return None
# """        tutaj coś z gatunku - podlewanie zależne od gatunku rośliny  """

    def changeColour(self, colour):
        self.colour = colour


    def changePicture(self, picture):
        self.picture = picture


