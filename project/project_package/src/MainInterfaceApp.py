from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList, ThreeLineListItem


class DayScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class ContentNavigationDrawer(MDBoxLayout):
    def switch_screen(self, name):
        MainInterfaceApp().switch_screen(name)


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    pass


class MainInterfaceApp(MDApp):
    # sim = ScreenManager()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (340, 630)

    def build(self, sm=None):
        # sm.add_widget(DayScreen(name="single_day"))
        # sm.add_widget(MainScreen(name="start"))
        #
        # return sm
        return DayScreen()

    def switch_screen(self, name, sm=None):
        sm.current = name


if __name__ == '__main__':
    MainInterfaceApp().run()
