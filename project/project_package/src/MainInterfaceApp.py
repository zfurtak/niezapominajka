from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem, MDList, TwoLineIconListItem, OneLineListItem
from kivymd.uix.picker import MDTimePicker
from project.project_package.src.package.User import User
from project.project_package.src.package.Species import Species

Window.size = (340, 630)


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # tutaj mozna podpiąć baze
        contacts = ["Paula", "John", "Kate", "Vlad"]
        for c in contacts:
            self.ids.species_catalog_screen.ids.species_list.add_widget(
                OneLineListItem(
                    text=c
                )
            )

        my_plants = ["stokrotka basia", "tulipan staszek", "róża rozalia", "kaktus kajtek"]
        for plant in my_plants:
            self.ids.my_plants_screen.ids.plants_list.add_widget(
                OneLineListItem(
                    text=plant

                )
            )




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


class SettingsScreen(Screen):
    pass


# class Content(BoxLayout):
#     manager = ObjectProperty()
#     nav_drawer = ObjectProperty()
#     toolbar = ObjectProperty()


class MainApp(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__()
        self.user = User("Stokrotka")
        self.species = [Species("GROOT species", "NO SOY LATINA!", 3, "Dużo wody, słońca i miłości <3",
                                "GUI/images/grootspecies.jpg", True)]

    def build(self):
        self.theme_cls.primary_palette = 'LightGreen'
        Builder.load_file("KV/MainInterface.kv")

        return MyScreenManager()

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


if __name__ == '__main__':
    MainApp().run()
