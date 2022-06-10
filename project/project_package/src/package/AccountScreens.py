from kivy.uix.screenmanager import Screen
from datetime import datetime, timedelta
from project.project_package.src.database.database import Database
from project.project_package.src.package.functions import without_whitespace

db = Database()


class WelcomeScreen(Screen):
    def login(self, username, password):
        if (username,) in db.get_usernames():
            if db.get_users_password(username) == (password,):
                self.warning("")
                return True
            else:
                self.warning("Nieprawidłowe hasło")
        else:
            self.warning("Brak użytkownika " + username)
        return None

    def warning(self, text):
        self.ids.welcome_screen_warning.text = text

    def clean(self):
        self.ids.user_name_text_field.text = ""
        self.ids.password_field.text = ""


class CreateAccountScreen(Screen):
    def create_account(self, username, password, confirm_password):
        if (username,) not in db.get_usernames():
            if without_whitespace(username) and without_whitespace(password):
                if password == confirm_password:
                    db.create_user(username, password, "images/users/default_avatar.png", str(datetime.today()), str(datetime.today()))
                    self.warning("")
                    return True
                else:
                    self.warning("Hasła nie są takie same")
            else:
                self.warning("Pozbądź się białych znaków")
        else:
            self.warning("Użytkownik " + username + " istnieje")
        return False

    def warning(self, text):
        self.ids.create_account_screen_warning.text = text


class UserScreen(Screen):
    def setup_profile(self, user, plants):
        self.ids.user_photo.source = user.photo
        self.ids.user_name.text = user.nickname
        self.ids.lvl.text = "Twój poziom:\n" + str(user.level.name)
        self.ids.lvl_progress.value = user.level.get_progress()
        self.ids.time_from_kill.text = str(user.get_days_without_dead_plant()) + " dni bez zabicia roślinki"
        self.ids.plants_no.text = "Tyle masz roślinek: " + str(len(plants))

    def update_after_delete(self, user, plants):
        self.ids.lvl.text = "Twój poziom: " + str(user.level.value)
        self.ids.time_from_kill.text = str(user.get_days_without_dead_plant()) + " dni bez zabicia roślinki"
        self.ids.plants_no.text = "Tyle masz roślinek: " + str(len(plants))

    def update_after_add(self, user, plants):
        self.ids.lvl.text = "Twój poziom: " + str(user.level.value)
        self.ids.plants_no.text = "Tyle masz roślinek: " + str(len(plants))