import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('main_data_base.db')
        self.cursor = self.con.cursor()
        self.create_users_table()
        self.create_plants_table()
        self.create_species_table()
        self.create_users_notification_table()

    def close_db_connection(self):
        self.con.close()

    # all functionality for users

    def create_users_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, username varchar(15) NOT NULL, password varchar(50), last_dead_plant varchar(50), dead_plants_cnt integer, dark_mode integer, photo_source varchar(50), join_date varchar(50))")
        self.con.commit()

    def create_user(self, username, password, photo_source, last_dead_plant, join_date, dead_plants_cnt=0, dark_mode=0):
        self.cursor.execute(
            "INSERT INTO users(username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source, join_date) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source, join_date))
        self.con.commit()

        created_user = self.cursor.execute(
            "SELECT id, username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source, join_date FROM users WHERE username = ? and password = ? and last_dead_plant = ? and dead_plants_cnt = ? and dark_mode = ? and photo_source=? and join_date=?",
            (username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source, join_date)).fetchall()
        return created_user[-1]

    def get_user(self, username):
        created_user = self.cursor.execute(
            "SELECT id, username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source, join_date FROM users WHERE username = ?",
            (username, )).fetchall()
        if len(created_user) == 0:
            return None
        return created_user[-1]

    def change_username(self, id, username):
        self.cursor.execute("UPDATE users SET username = ? WHERE id=?", (username, id))
        self.con.commit()

    def get_users(self):
        users = self.cursor.execute("SELECT id, username, password FROM users").fetchall()
        return users

    def get_usernames(self):
        usernames = self.cursor.execute("SELECT username FROM users").fetchall()
        return usernames

    def get_users_password(self, username):
        password = self.cursor.execute("SELECT password FROM users where username = ?", (username,)).fetchall()
        if not password:
            return None
        return password[-1]

    def killed_plant(self, new_data, name):
        update = self.cursor.execute("UPDATE users SET last_dead_plant = ? WHERE username=?", (new_data, name))
        self.con.commit()

    def change_image(self, photo, name):
        update = self.cursor.execute("UPDATE users SET photo_source = ? WHERE username=?", (photo, name))
        self.con.commit()

    def delete_user(self, userid):
        self.cursor.execute("DELETE FROM users WHERE id=?", (userid,))
        self.con.commit()

    def change_dark_mode(self, name, dark_mode_value):
        update = self.cursor.execute("UPDATE users SET dark_mode = ? WHERE username=?", (dark_mode_value, name))
        self.con.commit()

    #notifications

    def create_users_notification_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS notifications(id integer PRIMARY KEY AUTOINCREMENT, username varchar(50), notification varchar(12) NOT NULL)")
        self.con.commit()

    def get_users_notification(self, username):
        password = self.cursor.execute("SELECT notification FROM notifications where username = ?", (username,)).fetchall()
        if not password:
            return None
        return password[-1]

    def create_user_notification(self, username, notification):
        self.cursor.execute(
            "INSERT INTO notifications(username, notification) VALUES(?, ?)", (username, notification))
        self.con.commit()

    def set_users_notification(self, username, notification):
        if self.get_users_notification(username) is None:
            self.create_user_notification(username, notification)
        else:
            update = self.cursor.execute("UPDATE notifications SET notification = ? WHERE username=?", (notification, username))
            self.con.commit()


    # all functionalities for plants

    def create_plants_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS plants(id integer PRIMARY KEY AUTOINCREMENT, email varchar(50), plant_name varchar(12) NOT NULL, species varchar(50), first_water varchar(50), room varchar (50), notes varchar(50), last_water varchar(50), picture varchar(50))")
        self.con.commit()

    def create_plant(self, email, plant_name, species, first_water, room, notes, last_water, picture):
        self.cursor.execute(
            "INSERT INTO plants(email, plant_name, species, first_water, room, notes, last_water, picture) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
            (email, plant_name, species, first_water, room, notes, last_water, picture))
        self.con.commit()

        created_plant = self.cursor.execute(
            "SELECT id, email, plant_name, species, first_water, room, notes, last_water, picture FROM plants WHERE email = ? AND plant_name = ? and species = ? and first_water=? and room=? and notes=? and last_water=? and picture=?",
            (email, plant_name, species, first_water, room, notes, last_water, picture)).fetchall()
        return created_plant[-1]

    def get_plant(self, name_, email):
        plant = self.cursor.execute(
            "SELECT id, plant_name, species, first_water, room, notes, last_water, picture FROM plants WHERE plant_name=? AND email=?",
            (name_, email)).fetchall()
        if len(plant) == 0:
            return None
        return plant[-1]

    def get_plants(self):
        plant = self.cursor.execute(
            "SELECT id, plant_name, species, first_water, room, notes, last_water, picture FROM plants").fetchall()
        return plant

    def get_users_plants(self, email):
        plants = self.cursor.execute(
            "SELECT id, plant_name, species, first_water, room, notes, last_water, picture FROM plants WHERE email=?",
            (email,)).fetchall()
        return plants

    def get_unique_rooms(self, email):
        rooms = self.cursor.execute("SELECT DISTINCT room FROM plants WHERE email=?", (email,)).fetchall()
        return rooms

    def delete_plants(self, plant_name, email):
        self.cursor.execute("DELETE FROM plants WHERE plant_name = ? AND email=?", (plant_name, email))
        self.con.commit()

    def water_plant(self, plant_name, new_data, email):
        update = self.cursor.execute("UPDATE plants SET last_water = ? WHERE plant_name = ? AND email=?", (new_data, plant_name, email))
        self.con.commit()

    def change_plant_image(self, plant_name, picture, email):
        self.cursor.execute("UPDATE plants SET picture = ? WHERE plant_name = ? AND email=?",
                            (picture, plant_name, email))
        self.con.commit()

    # all functionality for species

    def create_species_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS species(id integer PRIMARY KEY AUTOINCREMENT, species_name varchar(50) NOT NULL, latin_name varchar(50), days_between_water integer, sun_pref varchar(50), care_tips varchar(50), notes varchar(50), picture varchar(50))")
        self.con.commit()

    def create_species(self, species_name, latin_name, days_between_water, sun_pref, care_tips, notes, picture):
        self.cursor.execute(
            "INSERT INTO species(species_name, latin_name, days_between_water, sun_pref, care_tips, notes, picture) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (species_name, latin_name, days_between_water, sun_pref, care_tips, notes, picture))
        self.con.commit()

        created_species = self.cursor.execute(
            "SELECT id, species_name, latin_name, days_between_water, sun_pref, care_tips, notes, picture FROM species WHERE species_name = ? AND latin_name = ? and days_between_water = ? and sun_pref=? and care_tips=? and notes=? and picture=?",
            (species_name, latin_name, days_between_water, sun_pref, care_tips, notes, picture)).fetchall()
        return created_species[-1]

    def get_species(self, name_):
        species = self.cursor.execute(
            "SELECT id, species_name, latin_name, days_between_water, sun_pref, care_tips, notes, picture FROM species WHERE species_name=?",
            (name_,)).fetchall()
        if len(species) == 0:
            return None
        return species[-1]

    def get_all_species(self):
        species = self.cursor.execute(
            "SELECT id, species_name, latin_name, days_between_water, sun_pref, care_tips, notes, picture FROM species").fetchall()
        return species
