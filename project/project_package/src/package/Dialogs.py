from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.toast import toast
from kivy.app import App
from kivymd.uix.filemanager import MDFileManager

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
    def __init__(self, species_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.plant_name.text = f'O nie!!\nCo się stało z {species_name}?'

    def message(self):
        self.ids.plant_name.theme_text_color = "Error"
        self.ids.plant_name.text = "Nie śmieszne"
        self.ids.delete1.opacity = 0
        self.ids.delete1.disabled = True
        self.ids.delete2.opacity = 0
        self.ids.delete2.disabled = True
        self.ids.delete3.opacity = 0
        self.ids.delete3.disabled = True


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
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)
        App.get_running_app().change_photo(self.type, self.name, path)
        print(path)


    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()


    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
