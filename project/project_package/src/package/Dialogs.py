from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivymd.toast import toast
from kivy.app import App
from kivymd.uix.filemanager import MDFileManager
from project.project_package.src.package.Plant import load_plant
from project.project_package.src.database.database import Database
from datetime import datetime
import os
from pathlib import Path


db = Database()


class SpeciesProfileDialog(FloatLayout):
    def __init__(self, species_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.species_name.text = species_name
        species = db.get_species(species_name)
        self.ids.latin_species_name.text = f'My latin name:\n{species[2]}'
        self.ids.watering_days.text = "Water me every: "+str(species[3])+" days"
        self.ids.sun.text = f'Sun prefers:\n{species[4]}'
        self.ids.care_tips.text = f'Tips:\n{species[5]}'
        self.ids.notes.text = f'Notes:\n{species[6]}'
        self.ids.species_photo.source = species[7]


class AddPlantDialog(FloatLayout):
    def __init__(self, species_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.species_name.text = f'Species: {species_name}'


class DeletePlantDialog(FloatLayout):
    def __init__(self, species_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.plant_name.text = f'O no!!\nWhat happened to {species_name}?'

    def message(self):
        self.ids.plant_name.theme_text_color = "Error"
        self.ids.plant_name.text = "Not funny"
        self.ids.plant_name.pos_hint = {"center_x": .5, "center_y": .7}
        self.ids.delete1.opacity = 0
        self.ids.delete1.disabled = True
        self.ids.delete2.opacity = 0
        self.ids.delete2.disabled = True
        self.ids.delete3.opacity = 0
        self.ids.delete3.disabled = True


class PlantProfileDialog(FloatLayout):
    def __init__(self, plant_name, username, **kwargs):
        super().__init__(**kwargs)
        self.ids.plant_name.text = f'I am {plant_name}'
        plant = db.get_plant(plant_name, username)
        # plant = load_plant(db.get_plant(plant_name, username)[1], self.species)

        if 'Species: ' in plant[2]:
            self.ids.species.text = f'{plant[2]}'
        else:
            self.ids.species.text = f'Species: {plant[2]}'
        print(plant)
        self.ids.room.text = f'My place: {plant[4]}'
        self.ids.notes.text = f'Something about me: {plant[5]}'
        self.ids.last_water.text = f"I've not drunk since: {plant[6]}"
        self.ids.plant_photo.source = plant[7]


class SpeciesReportDialog(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ChangeImageDialog(FloatLayout):
    def __init__(self, object_type, name, **kwargs):
        super().__init__(**kwargs)
        self.type = object_type
        self.name = name
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True
        )

    def file_manager_open(self):
        self.file_manager.show('/')  # for computer
        # self.file_manager.show(primary_ext_storage)  # for mobile phone
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        toast(path)
        App.get_running_app().change_photo(self.type, self.name, path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
