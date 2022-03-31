from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class UserInterface(MDApp):
    def flip(self):
        print("working...")

    def build(self):
        screen = MDScreen()

        self.toolbar = MDToolbar(title="Profil użytkownika")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["format-list-bulleted", lambda x: self.flip()]]
        self.toolbar.left_action_items = [
            ["keyboard-backspace", lambda x: self.flip()]]

        screen.add_widget(self.toolbar)

        #logo
        screen.add_widget(Image(
            source="images/test.jpg",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint=(0.3, 0.3)
        ))

        self.nickname = MDLabel(
                        text="Twoje imię: Pjeseł",
                        halign="center",
                        pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.lvl = MDLabel(
            text="Twój lvl: 10",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.4}
        )
        self.plant_counter = MDLabel(
            text="Masz: 18 roślin",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3}
        )
        self.killer_counter = MDLabel(
            text="Nie zabiłes roślinki od: 100 dni",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.2}
        )
        screen.add_widget(self.nickname)
        screen.add_widget(self.lvl)
        screen.add_widget(self.plant_counter)
        screen.add_widget(self.killer_counter)

        return screen


if __name__ == '__main__':
    UserInterface().run()