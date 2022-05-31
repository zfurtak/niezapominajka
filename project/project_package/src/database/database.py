import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('main_data_base.db')
        self.cursor = self.con.cursor()
        self.create_users_table()
        self.create_plants_table()

    def close_db_connection(self):
        self.con.close()

    # all functionality for users

    def create_users_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, username varchar(15) NOT NULL, password varchar(50), last_dead_plant varchar(50), dead_plants_cnt integer, dark_mode integer, photo_source varchar(50))")
        self.con.commit()

    def create_user(self, username, password, photo_source, last_dead_plant, dead_plants_cnt=0, dark_mode=0):
        self.cursor.execute(
            "INSERT INTO users(username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source) VALUES(?, ?, ?, ?, ?, ?)",
            (username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source))
        self.con.commit()

        created_user = self.cursor.execute(
            "SELECT id, username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source FROM users WHERE username = ? and password = ? and last_dead_plant = ? and dead_plants_cnt = ? and dark_mode = ? and photo_source=?",
            (username, password, last_dead_plant, dead_plants_cnt, dark_mode, photo_source)).fetchall()
        return created_user[-1]

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

    def delete_user(self, userid):
        self.cursor.execute("DELETE FROM users WHERE id=?", (userid,))
        self.con.commit()

    # all functionality for plants

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

    def delete_plants(self, id):
        self.cursor.execute("DELETE FROM plants WHERE id=?", (id,))
        self.con.commit()

    def water_plant(self, plant_name, newData):
        update = self.cursor.execute("UPDATE plants SET last_water = ? WHERE plant_name = ?", (newData, plant_name))
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
