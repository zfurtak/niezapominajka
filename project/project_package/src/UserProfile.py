from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList


class TestScreen(Screen):
    pass


class ContentNavigationDrawer(MDBoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    pass


class UserProfileApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"    # ogarnąc kolory (biale napisy)
        return TestScreen()

    def on_start(self):
        icons_item = {
            "calendar-blank": "Start",
            "face": "Your profile",
            "flower-tulip": "My plants",
            "flower-tulip-outline": "Plant catalog",
            "tools": "Settings",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )


UserProfileApp().run()
