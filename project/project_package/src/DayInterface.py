from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import TwoLineListItem


KV = '''
Screen:
    MDBoxLayout:
        orientation: "vertical"
        
        MDToolbar:
            title: "Dzień: 01-04-2022        Oto twoje roślinki do podlania"
            md_bg_color: app.theme_cls.accent_color
            right_action_items: [["menu"]]
            left_action_items: [["keyboard-backspace"]]


        ScrollView:
            MDList:
                id: container
  
    
'''


class DayInterface(MDApp):
    def flip(self):
        print("working...")

    def build(self):
        screen = MDScreen()

        self.toolbar = MDToolbar(title="Dzień: 01-04-2022")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["format-list-bulleted", lambda x: self.flip()]]
        self.toolbar.left_action_items = [
            ["keyboard-backspace", lambda x: self.flip()]]

        screen.add_widget(self.toolbar)

        self.titleLabel = MDLabel(
            text="Roślinki do podlania:",
            halign="center",
            # pos_hint={"center_x": 0.1, "center_y": 0.85}
        )

        return Builder.load_string(KV)

    def on_start(self):

        # self.root.ids.container.add_widget(self.titleLabel)
        for i in range(1, 20):
            self.root.ids.container.add_widget(
                TwoLineListItem(text=f"Roślina nr: {i}",
                                secondary_text="Gatunek: xxx"))


if __name__ == '__main__':
    DayInterface().run()


