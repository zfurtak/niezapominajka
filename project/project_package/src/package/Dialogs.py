from kivy.uix.floatlayout import FloatLayout
from project.project_package.src.database.database import Database

db = Database()


class SpeciesProfileDialog(FloatLayout):
    def __init__(self, species_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.species_name.text = species_name
        species = db.get_species(species_name)
        self.ids.latin_species_name.text = f'Moje łacińskie imię:\n{species[2]}'
        self.ids.watering_days.text = "Podlewaj mnie co: "+str(species[3])+" dni"
        self.ids.sun.text = f'Preferencje słoneczne:\n{species[4]}'
        self.ids.care_tips.text = f'Rady pielęgnacyjne:\n{species[5]}'
        self.ids.notes.text = f'Dodatkowe notatki:\n{species[6]}'
        self.ids.species_photo.source = species[7]


class AddPlantDialog(FloatLayout):
    def __init__(self, species_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.species_name.text = f'Gatunek: {species_name}'


class DeletePlantDialog(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PlantProfileDialog(FloatLayout):
    def __init__(self, plant_name, username, **kwargs):
        super().__init__(**kwargs)
        self.ids.plant_name.text = f'Jestem {plant_name}'
        plant = db.get_plant(plant_name, username)
        if 'Gatunek: ' in plant[2]:
            self.ids.species.text = f'{plant[2]}'
        else:
            self.ids.species.text = f'Gatunek: {plant[2]}'
        print(plant)
        self.ids.room.text = f'Moje lokum: {plant[4]}'
        self.ids.notes.text = f'Coś o mine: {plant[5]}'
        self.ids.last_water.text = f'Nie piję od: {plant[6]}'
        self.ids.plant_photo.source = plant[7]
