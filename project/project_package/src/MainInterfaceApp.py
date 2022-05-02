from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.picker import MDTimePicker

Window.size = (340, 630)


class MyScreenManager(ScreenManager):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DayScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class UserScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class Content(BoxLayout):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()


class MainApp(MDApp):
    def build(self):
        Builder.load_file("KV/MainInterface.kv")
        return MyScreenManager()

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        return time


if __name__ == '__main__':
    MainApp().run()
