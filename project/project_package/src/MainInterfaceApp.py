from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, CardTransition
from kivymd.app import MDApp
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem
from datetime import datetime, timedelta
from kivymd.uix.picker import MDTimePicker
from project.project_package.src.package.Screens import SinglePlant, SinglePlantToWater, SingleSpecies
from project.project_package.src.package.User import User
from project.project_package.src.package.Species import load_all_species
from project.project_package.src.package.Plant import load_plant, plantsToWater, plants_to_water_daily
from project.project_package.src.database.database import Database
from project.project_package.src.package.Dialogs import SpeciesProfileDialog, PlantProfileDialog, AddPlantDialog, DeletePlantDialog
from project.project_package.src.package.Screens import PlantScreen, MyPlantsScreen, AddPlantScreen, \
    MainScreen, UserScreen, SettingsScreen, SpeciesCatalogScreen, SingleSpecies, SinglePlant, SinglePlantToWater
from project.project_package.src.package.AccountScreens import WelcomeScreen, CreateAccountScreen

db = Database()
Window.size = (340, 630)


class MyScreenManager(ScreenManager):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class MainApp(MDApp):
    dialog = None
    add_plant_dialog = None
    delete_plant_dialog = None

    def __init__(self, **kwargs):
        super().__init__()
        self.day = 0
        self.species = load_all_species(db.get_all_species())
        self.plants = []
        self.user = None

    def build(self):
        self.theme_cls.primary_palette = 'LightGreen'
        Builder.load_file("KV/MainInterface.kv")

        return MyScreenManager()

    def on_start(self):
        for s in self.species:
            self.root.ids.species_catalog_screen.ids.species_list.add_widget(
                SingleSpecies(
                    text=s.name,
                )
            )

    def setup_profile(self):
        self.root.ids.user_screen.ids.user_photo.source = self.user.photo
        self.root.ids.user_screen.ids.user_name.text = self.user.nickname
        self.root.ids.user_screen.ids.lvl.text = "Twój poziom:" + str(self.user.level.value)
        self.root.ids.user_screen.ids.time_from_kill.text = str(self.user.days_without_dead_plant) + " dni bez zabicia roślinki"
        self.root.ids.user_screen.ids.plants_no.text = "Tyle masz roślinek: " + str(len(self.plants))

    def prepare_app_for_user(self):
        plants_ = db.get_users_plants(self.user.nickname)
        self.plants = []
        for x in plants_:
            self.plants.append(load_plant(x, self.species))

        if len(self.plants) > 1:
            plantsToWater(self.plants)

        self.root.ids.my_plants_screen.ids.plants_list.clear_widgets()

        for p in self.plants:
            self.root.ids.my_plants_screen.ids.plants_list.add_widget(
                SinglePlant(
                    text=p.name,
                )
            )

        self.prepare_list_of_plants_to_water(self.day)

    def prepare_list_of_plants_to_water(self, days):
        if days < 0:
            days = 0
        data = (datetime.today() + timedelta(days=days)).strftime('%d/%m/%y')
        self.root.ids.main_screen.ids.main_screen_toolbar.title = f'{data}'
        plants_to_water = []
        if len(self.plants) > 0:
            plants_to_water = plants_to_water_daily(days, self.plants)
        self.root.ids.main_screen.ids.plants_to_water.clear_widgets()
        for p in plants_to_water:
            self.root.ids.main_screen.ids.plants_to_water.add_widget(
                SinglePlantToWater(
                    text=p.name
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

    def show_species_profile_dialog(self, species_name):
        if self.dialog:
            self.close_dialog()
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=SpeciesProfileDialog(species_name))
        self.dialog.open()

    def show_plant_profile_dialog(self, plant_name):
        if self.dialog:
            self.close_dialog()
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=PlantProfileDialog(plant_name, self.user.nickname))
        self.dialog.open()

    def show_delete_plant_dialog(self, plant_name):
        self.delete_plant_dialog = MDDialog(
            type="custom",
            content_cls=DeletePlantDialog())
        self.delete_plant_dialog.open()

    def show_add_plant_dialog(self, species_name):
        self.add_plant_dialog = MDDialog(
            type="custom",
            content_cls=AddPlantDialog(species_name))
        self.add_plant_dialog.open()

    def close_dialog(self):
        self.dialog.dismiss(force=True)
        self.dialog = None

    def close_add_plant_dialog(self):
        self.add_plant_dialog.dismiss()

#TODO dokonczyc usuwanie
    def delete_plant(self):
        pass

    def add_plant(self, plant_name, species_name, room, about_me):
        if self.user.nickname == "":
            return

        if db.get_plant(plant_name, self.user.nickname) is None and plant_name != '' and len(plant_name) <= 15 and len(
                room) <= 15:
            if room == '':
                room = 'no room'
            data = datetime.today().strftime('%d/%m/%y')
            db.create_plant(self.user.nickname, plant_name, species_name[9:], data, room, about_me, data, "GUI/images/test.jpg")
            plant_data = db.get_plant(plant_name, self.user.nickname)
            p = load_plant(plant_data, self.species)
            self.plants.append(p)
            self.root.ids.my_plants_screen.ids.plants_list.add_widget(SinglePlant(text=plant_name))
            self.close_add_plant_dialog()

    def water_plant(self, plant_name):
        plant_name = plant_name[7:]
        for p in self.plants:
            if p.name == plant_name:
                p.water_now()
                data = datetime.today().strftime('%d/%m/%y')
                db.water_plant(plant_name, data)
                self.prepare_list_of_plants_to_water(self.day)
                return

    def other_day(self, way):
        self.day += way
        self.day = min(max(self.day, 0), 25)

        self.prepare_list_of_plants_to_water(self.day)

    def db_insert_user(self, user_name, password, photo):
        db.create_user(user_name, password, photo)

    def login(self, username, password):
        print(db.get_users())
        if self.root.ids.welcome_screen.login(username, password):
            self.root.ids.nav_drawer.swipe_edge_width = 1
            #TODO jakos tak tworzyc mądrze tego uzytkownika
            self.user = User(username)
            self.user.nickname = username
            self.turn_on_proper_mode()
            self.setup_profile()
            self.prepare_app_for_user()
            self.change_screen("MainScreen", "Start")

    def logout(self):
        self.plants = []
        self.day = 0
        self.root.ids.welcome_screen.clean()
        self.root.ids.nav_drawer.swipe_edge_width = 0
        self.user.nickname = ""
        self.prepare_app_for_user()
        self.theme_cls.theme_style = "Light"
        self.change_screen("WelcomeScreen", "Start")

    def create_account(self, username, password, confirm_password):
        if self.root.ids.create_account_screen.create_account(username, password, confirm_password):
            print("zmiana")
            # self.change_screen("WelcomeScreen", "Start")
            self.login(username, password)

    def change_screen(self, screen_name, title, direction='None', mode=""):
        screen_manager = self.root.ids.screen_manager
        self.root.ids.toolbar.title = title

        if screen_name == 'MainScreen':
            self.day = 0
            self.prepare_list_of_plants_to_water(0)

        if direction == 'None':
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name

    def change_mode(self, instance, value):
        if value:
            self.theme_cls.theme_style = "Dark"
            self.user.dark_mode = 1
        else:
            self.theme_cls.theme_style = "Light"
            self.user.dark_mode = 0

    def turn_on_proper_mode(self):
        if self.user.dark_mode:
            self.theme_cls.theme_style = "Dark"


if __name__ == '__main__':
    MainApp().run()
