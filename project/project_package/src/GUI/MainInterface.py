from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.picker import MDDatePicker

KV = '''
Screen:
    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Strona główna"
            md_bg_color: app.theme_cls.accent_color
            right_action_items: [["menu"]]
            


'''


class MainInterface(MDApp):
    def flip(self):
        print("working...")

    def build(self):
        dialog = MDDatePicker()
        dialog.open()




        return Builder.load_string(KV)


if __name__ == '__main__':
    MainInterface().run()


