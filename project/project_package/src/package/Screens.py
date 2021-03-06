from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem, OneLineIconListItem


class MyPlantsScreen(Screen):
    pass


class AddPlantScreen(Screen):
    pass


class MainScreen(Screen):
    def change_day(self, day):
        if day == 0:
            self.ids.water_all_button.opacity = 1
            self.ids.water_all_button.disabled = False

            return
        self.ids.water_all_button.opacity = 0
        self.ids.water_all_button.disabled = True


class SettingsScreen(Screen):
    pass


class SpeciesCatalogScreen(Screen):
    pass


class SingleSpecies(OneLineListItem):
    pass


class SinglePlant(OneLineListItem):
    pass


class SinglePlantToWater(OneLineIconListItem):
    icon = StringProperty()
