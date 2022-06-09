import webbrowser
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, CardTransition
from kivymd.app import MDApp
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem
from datetime import datetime, timedelta
from kivymd.uix.picker import MDTimePicker
from project.project_package.src.package.User import User, load_user
from project.project_package.src.package.Species import load_all_species
from project.project_package.src.package.Plant import load_plant, plants_to_water_daily, \
    delete_plant_from_list, get_plant
from project.project_package.src.database.database import Database
from project.project_package.src.package.Dialogs import SpeciesProfileDialog, PlantProfileDialog, AddPlantDialog, \
    DeletePlantDialog, ChangeImageDialog, SpeciesReportDialog
from project.project_package.src.package.Screens import SingleSpecies, SinglePlant, SinglePlantToWater
import os
from pathlib import Path
from project.project_package.src.package.functions import save_image
from project.project_package.src.package.AccountScreens import WelcomeScreen, CreateAccountScreen

db = Database()
Window.size = (340, 630)
PLANTS_MAX = 25


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
        # self.file_manager = MDFileManager(
        #     exit_manager=self.exit_manager,
        #     select_path=self.select_path,
        #     ext=[".jpg", ".png", ".jpeg"]
        # )

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
        self.root.ids.user_screen.setup_profile(self.user, self.plants)

    def prepare_app_for_user(self):
        plants_ = db.get_users_plants(self.user.nickname)
        self.plants = []
        for x in plants_:
            self.plants.append(load_plant(x, self.species))

        self.load_plants_catalog()
        self.prepare_list_of_plants_to_water(self.day)
        self.setup_profile()

    def load_plants_catalog(self):
        self.root.ids.my_plants_screen.ids.plants_list.clear_widgets()

        for p in self.plants:
            self.root.ids.my_plants_screen.ids.plants_list.add_widget(
                SinglePlant(
                    text=p.name,
                )
            )

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
                    text=p[0].name,
                    icon=p[1]
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
            content_cls=DeletePlantDialog(plant_name[7:]))
        self.delete_plant_dialog.open()

    def show_add_plant_dialog(self, species_name):
        self.add_plant_dialog = MDDialog(
            type="custom",
            content_cls=AddPlantDialog(species_name))
        self.add_plant_dialog.open()

    def show_change_image_dialog(self, object_type, name):
        if self.dialog:
            self.close_dialog()
        self.dialog = MDDialog(
            type="custom",
            content_cls=ChangeImageDialog(object_type, name))
        self.dialog.open()

    def show_report_dialog(self):
        if self.dialog:
            self.close_dialog()
        self.dialog = MDDialog(
            type="custom",
            content_cls=SpeciesReportDialog())
        self.dialog.open()

    def send_report(self, new_species):
        filename = "./reports/" + self.user.nickname + "_" + \
                   datetime.today().strftime('%Y_%m_%d') + ".txt"
        file = Path(filename)
        file.touch(exist_ok=True)
        file = open(filename, "w")
        file.write(f'Noticed lack of species named: {new_species} by user: {self.user.nickname}')
        file.close()

    def close_dialog(self):
        self.dialog.dismiss(force=True)
        self.dialog = None

    def close_add_plant_dialog(self):
        self.add_plant_dialog.dismiss()

    def delete_plant(self, text, type):
        if type == "joke":
            self.delete_plant_dialog.content_cls.message()
            return
        plant_name = text[23:-1]
        delete_plant_from_list(self.plants, plant_name)
        if type == "dead":
            self.user.upgrade_last_dead_plant_date()

        db.delete_plants(plant_name, self.user.nickname)
        self.load_plants_catalog()
        self.root.ids.user_screen.update_after_delete(self.user, self.plants)
        self.prepare_list_of_plants_to_water(0)

    def add_plant(self, plant_name, species_name, room, about_me):
        if self.user.nickname == "":
            return
        if len(self.plants) >= PLANTS_MAX:
            return
        if db.get_plant(plant_name, self.user.nickname) is None and plant_name != '' and len(plant_name) <= 15 \
                and len(room) <= 15:
            if room == '':
                room = 'Brak'
            data = datetime.today().strftime('%d/%m/%y')

            species_name = species_name[9:]
            actual_species = None
            for s in self.species:
                if s.name == species_name:
                    actual_species = s
            db.create_plant(self.user.nickname, plant_name, species_name, data, room, about_me, data,
                            actual_species.picture)
            plant_data = db.get_plant(plant_name, self.user.nickname)
            p = load_plant(plant_data, self.species)
            self.plants.append(p)
            self.root.ids.my_plants_screen.ids.plants_list.add_widget(SinglePlant(text=plant_name))
            self.close_add_plant_dialog()
            self.show_plant_profile_dialog(plant_name)
            self.root.ids.user_screen.update_after_add(self.user, self.plants)

    def water_plant(self, plant_name):
        plant_name = plant_name[7:]
        for p in self.plants:
            if p.name == plant_name:
                self.water(p)
                return

    def water(self, plant):
        plant.water_now()
        data = datetime.today().strftime('%d/%m/%y')
        db.water_plant(plant.name, data, self.user.nickname)
        self.prepare_list_of_plants_to_water(self.day)

    def water_all(self):
        if self.day != 0:
            return
        plants_list = plants_to_water_daily(self.day, self.plants)
        for p in plants_list:
            self.water(p[0])

    def other_day(self, way):
        self.day += way
        self.day = min(max(self.day, 0), 25)
        self.root.ids.main_screen.change_day(self.day)
        self.prepare_list_of_plants_to_water(self.day)

    def db_insert_user(self, user_name, password, photo):
        db.create_user(user_name, password, photo, datetime.today().strftime('%d/%m/%y'))

    def login(self, username, password):
        if self.root.ids.welcome_screen.login(username, password):
            self.root.ids.nav_drawer.swipe_edge_width = 1
            self.user = load_user(db.get_user(username))
            self.turn_on_proper_mode()
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
            self.login(username, password)

    def support_event(self):
        webbrowser.open('https://images.app.goo.gl/AAaDeaJZJWewHmVA9')

    def change_photo(self, object_type, name, path):
        if object_type == "user":
            dir_path = os.getcwd() + rf"/images/users/{self.user.nickname}.jpg"
            save_image(path, dir_path)
            db.change_image(rf"images/users/{self.user.nickname}.jpg", self.user.nickname)
            self.user.photo = path
            self.root.ids.user_screen.setup_profile(self.user, self.plants)
        if object_type == "plant":
            dir_path = os.getcwd() + rf"/images/plants/{self.user.nickname}_{name}.jpg"
            save_image(path, dir_path)
            db.change_plant_image(name, rf"images/plants/{self.user.nickname}_{name}.jpg", self.user.nickname)
            plant = get_plant(name, self.plants)
            plant.picture = path
            plant.relative_path = dir_path

    def change_screen(self, screen_name, title):
        screen_manager = self.root.ids.screen_manager
        self.root.ids.toolbar.title = title

        if screen_name == 'MainScreen':
            self.day = 0
            self.prepare_list_of_plants_to_water(0)

        screen_manager.transition = NoTransition()
        screen_manager.current = screen_name

    def change_mode(self, instance, value):
        if value:
            self.theme_cls.theme_style = "Dark"
            self.user.dark_mode = 1
            db.change_dark_mode(self.user.nickname, 1)
        else:
            self.theme_cls.theme_style = "Light"
            self.user.dark_mode = 0
            db.change_dark_mode(self.user.nickname, 0)

    def turn_on_proper_mode(self):
        if self.user.dark_mode:
            self.theme_cls.theme_style = "Dark"
            self.root.ids.settings_screen.ids.dark_mode_switch.active = True
        else:
            self.theme_cls.theme_style = "Light"
            self.root.ids.settings_screen.ids.dark_mode_switch.active = False


if __name__ == '__main__':
    MainApp().run()
