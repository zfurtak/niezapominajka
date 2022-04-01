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

    def more(self, args):
        print("NOWY GROOT!")

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
            source="images/grootspecies.jpg",
            pos_hint={"center_x": 0.75, "center_y": 0.65},
            size_hint=(0.4, 0.4)
            ))

        self.label = MDLabel(
            text="Nazwa:",
            halign="center",
            pos_hint={"center_x": 0.1, "center_y": 0.8},
            theme_text_color="Secondary"
        )

        self.myname = MDLabel(
            text="I AM GROOT SPECIES!",
            halign="center",
            pos_hint = {"center_x": 0.4, "center_y": 0.8},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.myname)

        self.daysbetweenwaters = MDLabel(
            text="Częstość podlewania:",
            halign="center",
            pos_hint={"center_x": 0.1, "center_y": 0.75},
            theme_text_color="Secondary"
        )

        self.mydays = MDLabel(
            text="X dni",
            halign="center",
            pos_hint={"center_x": 0.4, "center_y": 0.75},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.daysbetweenwaters)
        screen.add_widget(self.mydays)

        screen.add_widget(MDFillRoundFlatButton(
            text="DODAJ!",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.more
        ))

        self.myinfo = MDLabel(
            text="Lubię pić umiarkowaną ilość wody.",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"
        )

        self.info = MDLabel(
            text="Informacje:",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.info)
        screen.add_widget(self.myinfo)





        return screen



if __name__ == '__main__':
    PlantProfile().run()