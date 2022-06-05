from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem, OneLineIconListItem


class PlantScreen(Screen):
    pass


class MyPlantsScreen(Screen):
    pass


class AddPlantScreen(Screen):
    pass


class MainScreen(Screen):
    def change_day(self, day):
        if day == 0:
            self.ids.water_all_button.opacity = 1
            self.ids.water_all_button.disabled = False
            print("a teraz widać!")

            return
        self.ids.water_all_button.opacity = 0
        self.ids.water_all_button.disabled = True
        print("nie widać mnie!")


class UserScreen(Screen):
    def setup_profile(self, user, plants):
        self.ids.user_photo.source = user.photo
        self.ids.user_name.text = user.nickname
        self.ids.lvl.text = "Twój poziom:" + str(user.level.value)
        self.ids.time_from_kill.text = str(user.get_days_without_dead_plant()) + " dni bez zabicia roślinki"
        print(len(plants))
        self.ids.plants_no.text = "Tyle masz roślinek: " + str(len(plants))
        # user.days_with_app =


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