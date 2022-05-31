
class Species:

    def __init__(self, name, latinName, days_between_watering, care_tips, picture, sun_preference,
                 origin="Unknown", notes="Brak"):
        self.name = name
        self.latin_name = latinName
        self.days_between_watering = days_between_watering
        self.care_tips = care_tips
        self.picture = picture
        self.origin = origin
        self.sun_pref = sun_preference
        self.notes = notes

    def getDaysBetweenWatering(self):
        return self.days_between_watering

    def getPicture(self):
        return self.picture

    def add_notes(self, new_notes):
        self.notes += new_notes

    def set_new_notes(self, newNotes):
        self.notes = newNotes
