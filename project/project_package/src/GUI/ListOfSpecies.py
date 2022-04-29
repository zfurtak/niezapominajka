from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField

KV = '''
Screen:
    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Katalog roślin"
            md_bg_color: app.theme_cls.accent_color
            right_action_items: [["menu"]]
            left_action_items: [["keyboard-backspace"]]


        ScrollView:
            MDList:
                id: box


'''


class DayInterface(MDApp):

    def build(self):
        screen = Builder.load_string(KV)

        return screen

    def on_start(self):
        self.input = MDTextField(
            text="Szukaj po nazwie",
            halign="center"
        )

        self.root.ids.box.add_widget(self.input)
        for i in range(1, 20):
            self.root.ids.box.add_widget(
                OneLineListItem(
                    text=f"Gatunek nr: {i}"))


if __name__ == '__main__':
    DayInterface().run()


