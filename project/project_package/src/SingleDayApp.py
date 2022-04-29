from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList, TwoLineListItem, ThreeLineListItem


class DayScreen(Screen):
    pass



class ContentNavigationDrawer(MDBoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    pass

class WindowManager(ScreenManager):
    def build(self):
        return DayScreen()


class SingleDayApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (340, 630)

    def build(self):
        return WindowManager()


if __name__ == '__main__':
    SingleDayApp().run()


