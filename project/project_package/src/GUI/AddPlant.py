from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDToolbar

class SpeciesProfile(MDApp):
    def flip(self):
        print("working...")

    def add(self, args):
        print("Plant saved")

    def change(self, args):
        print("Change from basic to basic")

    def build(self):
        screen = MDScreen()

        self.toolbar = MDToolbar(title = "Profil gatunku")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["format-list-bulleted", lambda x: self.flip()]]
        self.toolbar.left_action_items = [
            ["keyboard-backspace", lambda x: self.flip()]]

        screen.add_widget(self.toolbar)
        screen.add_widget(Image(
            source="images/basic.png",
            pos_hint={"center_x": 0.75, "center_y": 0.65},
            size_hint=(0.4, 0.4)
            ))

        # screen.add_widget(MDFillRoundFlatButton(
        #     text="Zmień zdjęcie",
        #     font_size=17,
        #     pos_hint={"center_x": 0.75, "center_y": 0.4},
        #     on_press=self.change()
        # ))
        iconBtn = MDIconButton(icon="camera", pos_hint={"center_x": 0.75, "center_y": 0.4}, on_press=self.change)

        screen.add_widget(iconBtn)

        self.label = MDLabel(
            text="Imie:",
            halign="center",
            pos_hint={"center_x": 0.1, "center_y": 0.8},
            theme_text_color="Secondary"
        )

        self.myname = MDTextField(
            text="Roślinka nr x",
            halign="center",
            pos_hint={"center_x": 0.4, "center_y": 0.8},
            size_hint = (0.3, 1)
        )


        screen.add_widget(self.label)
        screen.add_widget(self.myname)

        self.species = MDLabel(
            text="Gatunek:",
            halign="center",
            pos_hint={"center_x": 0.1, "center_y": 0.75},
            theme_text_color="Secondary"
        )

        self.myspecies = MDLabel(
            text="Gatunek Y",
            halign="center",
            pos_hint={"center_x": 0.4, "center_y": 0.75},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.species)
        screen.add_widget(self.myspecies)

        screen.add_widget(MDFillRoundFlatButton(
            text="Zatwierdź",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.add
        ))

        self.firstwater = MDLabel(
            text="Pierwsze podlewanie:",
            halign="center",
            pos_hint={"center_x": 0.1, "center_y": 0.7},
            theme_text_color="Secondary"
        )

        self.myfirstwater = MDLabel(
            text="1.04.2022",
            halign="center",
            pos_hint={"center_x": 0.4, "center_y": 0.7},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.firstwater)
        screen.add_widget(self.myfirstwater)

        self.colour = MDLabel(
            text="Mój kolor:",
            halign="center",
            pos_hint={"center_x": 0.1, "center_y": 0.65},
            theme_text_color="Secondary"
        )

        self.mycolour = MDLabel(
            text="ZIELONY!!!",
            halign="center",
            pos_hint={"center_x": 0.4, "center_y": 0.65},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.colour)
        screen.add_widget(self.mycolour)

        self.room = MDLabel(
            text="Pokój:",
            halign="center",
            pos_hint={"center_x": 0.1, "center_y": 0.6},
            theme_text_color="Secondary"
        )

        self.myroom = MDTextField(
            text="pokój x",
            halign="center",
            pos_hint={"center_x": 0.4, "center_y": 0.6},
            size_hint = (0.3, 1)
        )

        screen.add_widget(self.room)
        screen.add_widget(self.myroom)


        return screen



if __name__ == '__main__':
    SpeciesProfile().run()