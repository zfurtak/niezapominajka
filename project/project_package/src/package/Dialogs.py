from kivy.uix.floatlayout import FloatLayout
from project.project_package.src.database.database import Database

db = Database()


class SpeciesProfileDialog(FloatLayout):
    def __init__(self, species_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.species_name.text = species_name


class AddPlantDialog(FloatLayout):
    def __init__(self, species_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.species_name.text = f'Gatunek: {species_name}'


class PlantProfileDialog(FloatLayout):
    def __init__(self, plant_name, username, **kwargs):
        super().__init__(**kwargs)
        self.ids.plant_name.text = f'Jestem {plant_name}'
        plant = db.get_plant(plant_name, username)
        if 'Gatunek: ' in plant[2]:
            self.ids.species.text = f'{plant[2]}'
        else:
            self.ids.species.text = f'Gatunek: {plant[1]}'
        print(plant)
        self.ids.room.text = f'Moje lokum: {plant[5]}'
        self.ids.notes.text = f'Coś o mine: {plant[6]}'
        self.ids.last_water.text = f'Nie piję od: {plant[7]}'
        self.ids.plant_photo.source = plant[8]