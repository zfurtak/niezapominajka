from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class SettingsApp(MDApp):
    def flip(self):
        print("working...")

    def build(self):
        screen = MDScreen()

        self.toolbar = MDToolbar(title="Ustawienia")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["format-list-bulleted", lambda x: self.flip()]]
        self.toolbar.left_action_items = [
            ["keyboard-backspace", lambda x: self.flip()]]

        screen.add_widget(self.toolbar)


        self.reminderTime = MDLabel(
                        text="Godzina przypominajki: ",
                        halign="center",
                        pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        self.sound = MDLabel(
            text="Dźwięk: ",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.6}
        )
        self.silentMode = MDLabel(
            text="Tryb cichy: OFF",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.tips = MDFillRoundFlatIconButton(
            icon="more",
            text="Tips",
            pos_hint={"center_x": 0.5, "center_y": 0.4}
        )
        self.support = MDFillRoundFlatIconButton(
            icon="help-circle",
            text="Support",
            pos_hint={"center_x": 0.5, "center_y": 0.3}
        )
        self.zero = MDFillRoundFlatIconButton(
            icon="trash-can-outline",
            text="Clear the app",
            pos_hint={"center_x": 0.5, "center_y": 0.2}
        )
        screen.add_widget(self.reminderTime)
        screen.add_widget(self.sound)
        screen.add_widget(self.silentMode)
        screen.add_widget(self.support)
        screen.add_widget(self.tips)
        screen.add_widget(self.zero)

        return screen


if __name__ == '__main__':
    SettingsApp().run()