from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

#kod z tutoriala ale nie na mobilne

class UserInterface(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

#widgets
        self.window.add_widget(Image(source="images/test.jpg"))
        self.greetings = Label(
                            text="Welcome in user's interface",
                            font_size=20,
                            color='##90ee90'
                            )
        self.window.add_widget(self.greetings)
        self.user = TextInput(
                    multiline=False,
                    padding_y=(20, 20),
                    size_hint=(1, 0.5)
                    )
        self.window.add_widget(self.user)
        self.button = Button(
                        text="Push me",
                        size_hint=(1, 0.5),
                        bold=True,
                        background_color='##90ee90'
                        #background_normal=""
                        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, event):
        self.greetings.text = "Hello " + self.user.text + "!"


if __name__ == "__main__":
    UserInterface().run()