
def load_single_species(data):
    return Species(data[1], data[2], data[3], data[4], data[5], data[6], data[7])


def load_all_species(array):
    species_array = []
    for i in array:
        species_array.append(load_single_species(i))
    return species_array


class Species:
    def __init__(self, name, latinName,  days_between_watering, sun_preference,care_tips,  notes, picture):
        self.name = name
        self.latin_name = latinName
        self.days_between_watering = days_between_watering
        self.care_tips = care_tips
        self.picture = picture
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
