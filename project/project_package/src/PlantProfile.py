from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class PlantProfile(MDApp):
    def flip(self):
        print("working...")

    def water(self, args):
        print("Thank YOU!!!")

    def build(self):
        screen = MDScreen()

        self.toolbar = MDToolbar(title = "Profil rośliny")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["format-list-bulleted", lambda x: self.flip()]]
        self.toolbar.left_action_items = [
            ["keyboard-backspace", lambda x: self.flip()]]

        screen.add_widget(self.toolbar)
        screen.add_widget(Image(
            source="images/groot.jpg",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint=(0.3, 0.3)
            ))

        self.label = MDLabel(
            text="Name:",
            halign="center",
            pos_hint = {"center_x": 0.3, "center_y": 0.5},
            theme_text_color = "Secondary"
        )

        self.myname = MDLabel(
            text="I AM GROOT!",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            theme_text_color = "Primary",
            font_style = "H5"
        )

        screen.add_widget(self.label)
        screen.add_widget(self.myname)

        screen.add_widget(MDFillRoundFlatButton(
            text="Podlej mnie!",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y": 0.15},
            on_press = self.water
        ))

        self.species = MDLabel(
            text="Gatunek:",
            halign="center",
            pos_hint={"center_x": 0.3, "center_y": 0.45},
            theme_text_color="Secondary"
        )

        self.myspecies = MDLabel(
            text="Groot to Groot!",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.species)
        screen.add_widget(self.myspecies)

        self.firstwater = MDLabel(
            text="Pierwsze podlewanie:",
            halign="center",
            pos_hint={"center_x": 0.3, "center_y": 0.4},
            theme_text_color="Secondary"
        )

        self.myfirstwater = MDLabel(
            text="1.04.2022",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.firstwater)
        screen.add_widget(self.myfirstwater)

        self.colour = MDLabel(
            text="Mój kolor:",
            halign="center",
            pos_hint={"center_x": 0.3, "center_y": 0.35},
            theme_text_color="Secondary"
        )

        self.mycolour = MDLabel(
            text="ZIELONY!!!",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.colour)
        screen.add_widget(self.mycolour)

        self.room = MDLabel(
            text="Pokój:",
            halign="center",
            pos_hint={"center_x": 0.3, "center_y": 0.3},
            theme_text_color="Secondary"
        )

        self.myroom = MDLabel(
            text="Doniczka",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.room)
        screen.add_widget(self.myroom)


        self.nextwater = MDLabel(
            text="Następne podlewane:",
            halign="center",
            pos_hint={"center_x": 0.3, "center_y": 0.25},
            theme_text_color="Secondary"
        )

        self.mynextwater = MDLabel(
            text="Teraz?",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.25},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.nextwater)
        screen.add_widget(self.mynextwater)

        # screen.add_widget()

        return screen



if __name__ == '__main__':
    PlantProfile().run()