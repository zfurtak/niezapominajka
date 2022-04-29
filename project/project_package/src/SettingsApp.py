from kivymd.uix.picker import MDTimePicker
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList


class SettingsScreen(Screen):
    pass


class ContentNavigationDrawer(MDBoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    pass


class SettingsApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (340, 630)

    def build(self):
        return SettingsScreen()

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        print(time)
        return time

    def on_start(self):
        icons_item = {
            "calendar-blank": "Start",
            "face": "Your profile",
            "flower-tulip": "My plants",
            "flower-tulip-outline": "Plant catalog"
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )


if __name__ == '__main__':
    SettingsApp().run()
