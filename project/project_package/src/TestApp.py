from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class HomeScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class TestApp(MDApp):
    Window.size = (340, 630)



if __name__ == '__main__':
    TestApp().run()