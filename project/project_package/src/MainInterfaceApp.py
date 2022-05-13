from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, CardTransition
from kivymd.app import MDApp
from kivy.properties import  StringProperty, ListProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem, OneLineListItem
from kivymd.uix.picker import MDTimePicker
from project.project_package.src.package.User import User
from project.project_package.src.package.Species import Species
from project.project_package.src.package.Plant import Plant
from project.project_package.src.database.database import Database

db = Database()
Window.size = (340, 630)


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # tutaj mozna podpiąć baze
        self.species = None
        self.user = User("Ala")

        self.ids.user_screen.ids.user_photo.source = self.user.photo
        self.ids.user_screen.ids.user_name.text = self.user.nickname
        self.ids.user_screen.ids.lvl.text = "Your level:"+str(self.user.level.value)
        # self.ids.user_screen.ids.plants_no.text = "You have: "+str(len(self.user.list_of_plants))+" plants"
        self.ids.user_screen.ids.time_from_kill.text = str(self.user.days_without_dead_plant)\
                                                       +" days without killing plants"


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DayScreen(Screen):
    pass


class SpeciesScreen(Screen):
    pass


class SpeciesCatalogScreen(Screen):
    pass


class PlantScreen(Screen):
    pass


class MyPlantsScreen(Screen):
    pass


class AddPlantScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class UserScreen(Screen):
    pass
    # def __init__(self, **kwargs):
    #     self.ids.

class SettingsScreen(Screen):
    pass


class LoginDialog(FloatLayout):
    pass


class SignUpDialog(FloatLayout):
    pass


class SpeciesProfileDialog(FloatLayout):
    def __init__(self, species_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.species_name.text = species_name


class AddPlantDialog(FloatLayout):
    def __init__(self, species_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.species_name.text = species_name


class PlantProfileDialog(FloatLayout):
    def __init__(self, plant_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.plant_name.text = f'Jestem {plant_name}'
        plant = db.get_plant(plant_name, "zuz")
        self.ids.species.text = f'Gatunek: {plant[1]}'
        self.ids.room.text = f'Moje lokum: {plant[5]}'
        self.ids.notes.text = f'Coś o mine: {plant[6]}'
        self.ids.last_water.text = f'Nie piję od: {plant[7]}'
        self.ids.plant_photo.source = plant[8]


class SingleSpecies(OneLineListItem):
    pass


class SinglePlant(OneLineListItem):
    pass


class MainApp(MDApp):
    dialog = None
    add_plant_dialog = None


    def __init__(self, **kwargs):
        super().__init__()
        rose = Species("rose", "rositina", 3, "Dużo wody, słońca i miłości <3",
                                "GUI/images/grootspecies.jpg", True)
        tulip = Species("tulip", "tulipina", 7, "Dużo miłości <3",
                                "GUI/images/groot.jpg", True)
        groot = Species("GROOT species", "NO SOY LATINA!", 3, "Dużo wody, słońca i miłości <3",
                                "GUI/images/grootspecies.jpg", True)

        species_ = [tulip, rose, groot]
        self.species = species_
        plants_ = db.get_plants()
        self.plants = []
        for x in plants_:
            self.plants.append(Plant(x[1], x[2]))


        # self.user = User("Stokrotka")


    def build(self):
        self.theme_cls.primary_palette = 'LightGreen'
        Builder.load_file("KV/MainInterface.kv")

        return MyScreenManager()

    def on_start(self):
        plantstext = "You have: " + str(len(self.plants)) + " plant"
        if len(self.plants) > 1:
            plantstext += "s"
        self.root.ids.user_screen.ids.plants_no.text = plantstext
        for s in self.species:
            self.root.ids.species_catalog_screen.ids.species_list.add_widget(
                SingleSpecies(
                    text=s.name,
                )
            )

        for p in self.plants:
            self.root.ids.my_plants_screen.ids.plants_list.add_widget(
                SinglePlant(
                    text=p.name,
                )
            )

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        User.set_reminder_time(self.user, time)

    def show_alert_dialog(self, text_):
        if not self.dialog:
            self.dialog = MDDialog(
                text=text_
            )
            self.dialog.open()
            self.dialog = None

    def show_login_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=LoginDialog())
        self.dialog.open()
        self.dialog = None

    def show_sign_up_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=SignUpDialog())
        self.dialog.open()
        self.dialog = None

    def show_species_profile_dialog(self, species_name):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=SpeciesProfileDialog(species_name))

        self.dialog.open()

    def show_plant_profile_dialog(self, plant_name):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=PlantProfileDialog(plant_name))
        self.dialog.open()
        self.dialog = None

    def show_add_plant_dialog(self, species_name):
        self.add_plant_dialog = MDDialog(
            type="custom",
            content_cls=AddPlantDialog(species_name))
        self.add_plant_dialog.open()

    def close_dialog(self):
        self.dialog.dismiss()

    def close_add_plant_dialog(self):
        self.add_plant_dialog.dismiss()

    def add_plant(self, plant_name, species_name):
        db.create_plant("zuz", plant_name, species_name, "06-07-2001", "pink", "kitchen", "hello", "06-05-2022", "GUI/images/test.jpg")
        self.root.ids.my_plants_screen.ids.plants_list.add_widget(SinglePlant(text=plant_name))

    def db_insert_user(self, user_name, password, photo):
        db.create_user(user_name, password, photo)

    def change_screen(self, screen_name, title, direction='None', mode=""):
        screen_manager = self.root.ids.screen_manager
        self.root.ids.toolbar.title = title

        if direction == 'None':
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name


if __name__ == '__main__':

    # db.create_plant("zuz", "Zuzia", "tulip", "01-01-2020", "pink", "bedroom", "lubi ciepelko", "10-05-2022", "GUI/images/basic.png")
    # db.delete_plants(3)
    print(db.get_plants())

    MainApp().run()

