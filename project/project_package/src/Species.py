import project_package


class Species:

    def __init__(self, name, latinName, daysBetweenWatering, careTips, picture, sunPref, origin="Unknown", notes="Brak"):
        self.name = name
        self.latinName = latinName
        self.daysBetweenWatering = daysBetweenWatering
        self.careTips = careTips
        self.picture = picture
        self.origin = origin
        self.sunPref = sunPref
        self.notes = notes

    def getDaysBetweenWatering(self):
        return self.daysBetweenWatering

    def getPicture(self):
        return self.picture

    def addNotes(self, newNotes):
        self.notes += newNotes

    def setNewNotes(self, newNotes):
        self.notes = newNotes
        